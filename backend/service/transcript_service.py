import logging
import re
from typing import Any, Dict, List
from sqlalchemy.orm import Session
from repository.analysis_repository import AnalysisRepository
from repository.models import CallIntent, CallTranscript
from repository.transcript_repository import TranscriptRepository
from service.clinic_name_utils import normalize_clinic_name
from service.classifier_service import ClassifierService

logger = logging.getLogger(__name__)

class TranscriptService:
    
    def __init__(self):
        self.classifier = ClassifierService()
 
    def analyze(self, db: Session, call_record_id: int) -> Dict[str, Any]:
        repo = TranscriptRepository(db)
        analysis_repo = AnalysisRepository(db)

        transcript = repo.get_by_call_record_id(call_record_id)
        if not transcript:
            raise ValueError(f"Transcript with call_record_id {call_record_id} not found")

        conversation = self._normalize_conversation(transcript.transcript)
        if not conversation:
            raise ValueError("Empty conversation")

        clinic_name = self._extract_clinic_name(conversation)

        intent_data = self.classifier.classify(conversation)
        analysis_repo.save_intent(
            call_record_id=call_record_id,
            primary_intent=intent_data["primary_intent"],
            secondary_intents=intent_data["secondary_intents"],
            confidence=intent_data["confidence"],
            needs_human_review=intent_data["needs_human_review"],
            reasoning=intent_data["reasoning"],
            call_transcript=transcript.transcript,
            clinic_name=clinic_name,
        )

        db.commit()
        return {
            "call_record_id": call_record_id,
            "clinic": clinic_name,
            "call_transcript": transcript.transcript,
            "intent": intent_data,
        }

    def analyze_all(self, db: Session) -> Dict[str, Any]:
        repo = TranscriptRepository(db)
        transcripts = repo.get_all(limit=10000)
        success = 0
        failed = 0
        for t in transcripts:
            try:
                self.analyze(db, t.call_record_id)
                success += 1
            except Exception as e:
                failed += 1
                logger.error(f"Failed call_record_id {t.call_record_id}: {e}")
        return {"processed": success + failed, "success": success, "failed": failed}

    def get_results(self, db: Session, call_record_id: int) -> Dict[str, Any]:
        transcript = db.query(CallTranscript).filter(
            CallTranscript.call_record_id == call_record_id
        ).first()
        if not transcript:
            return {
                "call_record_id": call_record_id,
                "clinic": None,
                "call_transcript": None,
                "intent": {
                    "primary_intent": None,
                    "secondary_intents": [],
                    "confidence": 0,
                    "needs_human_review": False,
                    "reasoning": "",
                },
            }

        intent = db.query(CallIntent ).filter(
            CallIntent.transcript_id == transcript.id
        ).first()
        return {
            "call_record_id": call_record_id,
            "clinic": intent.clinic_name if intent else None,
            "call_transcript": intent.call_transcript if intent else transcript.transcript,
            "intent": {
                "primary_intent": intent.primary_intent if intent else None,
                "secondary_intents": intent.secondary_intents if intent else [],
                "confidence": intent.confidence if intent else 0,
                "needs_human_review": intent.needs_human_review if intent else False,
                "reasoning": intent.reasoning if intent else "",
            },
        }

    def _normalize_conversation(self, transcript_data: Any) -> List[Dict[str, str]]:
        if isinstance(transcript_data, dict):
            transcript_data = (
                transcript_data.get("conversation")
                or transcript_data.get("transcript")
                or transcript_data.get("messages")
                or []
            )

        if not isinstance(transcript_data, list):
            return []

        normalized: List[Dict[str, str]] = []
        for message in transcript_data:
            if not isinstance(message, dict):
                continue

            role = (message.get("role") or message.get("speaker") or "").strip().lower()
            content = message.get("content")
            
            if content is None:
                content = message.get("message")
            if content is None:
                content = message.get("text")

            if not isinstance(content, str):
                content = "" if content is None else str(content)

            content = content.strip()
            if role and content:
                normalized.append({"role": role, "content": content})

        return normalized

    def _extract_clinic_name(self, conversation: List[Dict[str, str]]) -> str:
        first_agent_message = next(
            (message.get("content", "") for message in conversation if message.get("role") == "agent"),
            "",
        )

        clinic_name = normalize_clinic_name(first_agent_message)
        if clinic_name != "Unknown Clinic":
            return clinic_name

        return "Unknown Clinic"
