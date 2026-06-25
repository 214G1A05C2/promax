from repositories.call_metrics_repository import (
    CallMetricsRepository
)
import ast
import json
import uuid


class CallMetricsService:
    LIST_FIELDS = {
        "secondary_intents",
        "workflow_events",
        "transcript",
    }
    OBJECT_FIELDS = {
        "detected_intents",
        "workflow_summary",
        "completion_data",
        "blocker_data",
    }
    JSON_FIELDS = LIST_FIELDS | OBJECT_FIELDS

    @staticmethod
    def _parse_json_value(value):
        if value is None or value == "":
            return None

        if isinstance(value, (dict, list, int, float, bool)):
            return value

        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return None

            try:
                return json.loads(stripped)
            except json.JSONDecodeError:
                try:
                    parsed = ast.literal_eval(stripped)
                except (ValueError, SyntaxError):
                    return value

                if isinstance(parsed, (dict, list)):
                    return parsed

                return value

        return value

    @staticmethod
    def _stringify_json_value(value):
        if value is None:
            return None

        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False)

        return value

    @classmethod
    def _normalize_db_row(cls, row):
        primary_intent = (row.primary_intent or "").strip()

        payload = {
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
        }

        for field in cls.JSON_FIELDS:
            value = cls._parse_json_value(payload[field])
            if value is None:
                value = [] if field in cls.LIST_FIELDS else {}
            payload[field] = value

        return payload

    @classmethod
    def _prepare_payload(cls, payload):
        prepared = {
            "id": str(payload.get("id") or uuid.uuid4()),
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

        for field in cls.JSON_FIELDS:
            prepared[field] = cls._stringify_json_value(prepared[field])

        if isinstance(prepared.get("primary_intent"), str):
            prepared["primary_intent"] = prepared["primary_intent"].strip() or None

        return prepared

    @staticmethod
    def fetch_all_calls():
        data = CallMetricsRepository.get_all_calls()
        result = [CallMetricsService._normalize_db_row(row) for row in data]

        return {
            "success": True,
            "count": len(result),
            "data": result,
        }

    @staticmethod
    def fetch_call_by_call_id(call_id):
        row = CallMetricsRepository.get_call_by_call_id(call_id)
        if not row:
            return {
                "success": False,
                "message": "Call metric not found",
                "data": None,
            }, 404

        return {
            "success": True,
            "data": CallMetricsService._normalize_db_row(row),
        }, 200

    @staticmethod
    def create_call_metric(payload):
        data = CallMetricsService._prepare_payload(payload)

        call = CallMetricsRepository.create_call(data)

        return {
            "success": True,
            "message": "Call metric saved successfully",
            "data": CallMetricsService._normalize_db_row(call),
        }

    @staticmethod
    def delete_call_metric(call_id):
        deleted = CallMetricsRepository.delete_call_by_call_id(call_id)
        if not deleted:
            return {
                "success": False,
                "message": "Call metric not found",
                "deleted": False,
            }

        return {
            "success": True,
            "message": "Call metric deleted successfully",
            "deleted": True,
        }
