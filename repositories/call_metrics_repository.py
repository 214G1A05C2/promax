from models.call_metrics_model import CallMetrics

class CallMetricsRepository:

    @staticmethod
    def get_all_calls():

        data = CallMetrics.query.all()

        print("TOTAL RECORDS:", len(data))

        return data