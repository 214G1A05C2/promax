from repositories.call_metrics_repository import (
    CallMetricsRepository
)


class CallMetricsService:

    @staticmethod
    def fetch_all_calls():

        data = CallMetricsRepository.get_all_calls()

        result = []

        for row in data:

            result.append({
                "id": row.id,
                "call_id": row.call_id,
                "clinic_name": row.clinic_name,
                "call_timestamp": row.call_timestamp,
                "primary_intent": row.primary_intent,
                "secondary_intents": row.secondary_intents,
                "created_at": row.created_at
            })

        return result