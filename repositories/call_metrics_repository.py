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

    @staticmethod
    def delete_call_by_call_id(call_id):
        call = CallMetrics.query.filter_by(call_id=call_id).first()
        if not call:
            return False

        db.session.delete(call)
        db.session.commit()
        return True
