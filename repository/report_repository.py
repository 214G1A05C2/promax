from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import literal
from repository.models import CallIntent , CallTranscript
from service.clinic_name_utils import normalize_clinic_name

class ReportRepository:
    def __init__(self, session: Session):
        self.session = session

    def intent_analysis_data(self) -> List[Dict[str, Any]]:
        results = (
            self.session.query(
                CallIntent.call_record_id.label("Call ID"),
                CallTranscript.created_at.label("Date"),
                CallIntent.clinic_name,
                CallIntent.call_transcript,
                CallIntent.primary_intent,
                CallIntent.secondary_intents,
            )
            .join(
                CallTranscript,
                CallIntent.transcript_id == CallTranscript.id
            )
            .order_by(CallIntent.call_record_id)
            .all()
        )

        rows = []
        for row in results:
            item = row._asdict()
            # item["clinic_name"] = normalize_clinic_name(item.get("clinic_name"))
            rows.append(item)

        return rows
































"""
def intent_analysis_data(self) -> List[Dict[str, Any]]:
        results = (
            self.session.query(
                CallIntent.call_record_id.label("Call ID"),
                literal(None).label("Date"),
                CallIntent.clinic_name,
                CallIntent.call_transcript,
                CallIntent.primary_intent,
                CallIntent.secondary_intents,
                # CallIntent.confidence,
                # CallIntent.needs_human_review,
                # CallIntent.reasoning,
            )
            .order_by(CallIntent.call_record_id)
            .all()
        )
        rows = []
        for row in results:
            item = row._asdict()
            item["clinic_name"] = normalize_clinic_name(item.get("clinic_name"))
            rows.append(item)
        return rows
"""