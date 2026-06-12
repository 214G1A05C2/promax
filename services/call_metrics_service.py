from repositories.call_metrics_repository import (
    CallMetricsRepository
)
import uuid


class CallMetricsService:

    @staticmethod
    def fetch_all_calls():
        data = CallMetricsRepository.get_all_calls()
        result = []
        for row in data:
            primary_intent = (row.primary_intent or "").strip()

            result.append({
                "id": row.id,
                "call_id": row.call_id,
                "clinic_name": row.clinic_name,
                "call_timestamp": row.call_timestamp,
                "primary_intent": primary_intent,
                "secondary_intents": row.secondary_intents,
                "detected_intents": row.detected_intents,
                "workflow_events": row.workflow_events,
                "workflow_summary": row.workflow_summary,
                "completion_data": row.completion_data,
                "blocker_data": row.blocker_data,
                "final_output": row.final_output,
                "created_at": row.created_at,
                "transcript": row.transcript,
            })

        return result

    @staticmethod
    def create_call_metric(payload):
        data = {
            "id": payload.get("id") or str(uuid.uuid4()),
            "call_id": payload.get("call_id"),
            "clinic_name": payload.get("clinic_name"),
            "call_timestamp": payload.get("call_timestamp"),
            "primary_intent": payload.get("primary_intent"),
            "secondary_intents": payload.get("secondary_intents"),
            "detected_intents": payload.get("detected_intents"),
            "workflow_events": payload.get("workflow_events"),
            "workflow_summary": payload.get("workflow_summary"),
            "completion_data": payload.get("completion_data"),
            "blocker_data": payload.get("blocker_data"),
            "final_output": payload.get("final_output"),
            "created_at": payload.get("created_at"),
            "transcript": payload.get("transcript"),
        }

        call = CallMetricsRepository.create_call(data)

        return {
            "id": call.id,
            "message": "Call metric saved successfully",
        }
