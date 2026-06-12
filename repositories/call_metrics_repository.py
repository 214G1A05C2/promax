from models.call_metrics_model import CallMetrics
from models.call_metrics_model import db

class CallMetricsRepository:

    @staticmethod
    def get_all_calls():
        data = CallMetrics.query.all()
        return data

    @staticmethod
    def create_call(payload):
        call = CallMetrics(**payload)
        db.session.add(call)
        db.session.commit()
        return call
