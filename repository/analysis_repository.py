import json
from typing import Any, List
from sqlalchemy.orm import Session
from repository.models import CallIntent, CallTranscript
# from service.clinic_name_utils import normalize_clinic_name

class AnalysisRepository:
    def __init__(self, session: Session):
        self.session = session

    def _get_transcript(self, call_record_id: int) -> CallTranscript:
        transcript = self.session.query(CallTranscript).filter(
            CallTranscript.call_record_id == call_record_id
        ).first()
        if not transcript:
            raise ValueError(f"Transcript with call_record_id {call_record_id} not found")
        return transcript

    def save_intent(
        self,
        call_record_id,
        primary_intent,
        secondary_intents,
        confidence,
        needs_human_review,
        reasoning,
        call_transcript,
        clinic_name):
        
        transcript = self._get_transcript(call_record_id)
        reasoning_value = reasoning if isinstance(reasoning, str) else json.dumps(reasoning)
        clinic_value = clinic_name
        # clinic_value = normalize_clinic_name(clinic_name)

        record = (
            self.session.query(CallIntent)
            .filter(
                CallIntent.transcript_id == transcript.id
            ) 
            .first()
             
        )

        if record:

            record.call_record_id = transcript.call_record_id
            record.call_transcript = call_transcript
            record.clinic_name = clinic_value
            record.primary_intent = primary_intent
            record.secondary_intents = secondary_intents
            record.confidence = confidence
            record.needs_human_review = needs_human_review
            record.reasoning = reasoning_value

        else:

            record = CallIntent(
                transcript_id=transcript.id,
                call_record_id=transcript.call_record_id,
                call_transcript=call_transcript,
                clinic_name=clinic_value,
                primary_intent=primary_intent,
                secondary_intents=secondary_intents,
                confidence=confidence,
                needs_human_review=needs_human_review,
                reasoning=reasoning_value
            )

            self.session.add(record)

        self.session.commit()

        return record