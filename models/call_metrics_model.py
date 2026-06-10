from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CallMetrics(db.Model):
    __tablename__ = "call_metrics"

    id = db.Column(db.String, primary_key=True)

    call_id = db.Column(db.BigInteger)
    clinic_name = db.Column(db.String)
    call_timestamp = db.Column(db.String)

    primary_intent = db.Column(db.String)
    secondary_intents = db.Column(db.Text)

    detected_intents = db.Column(db.Text)
    workflow_events = db.Column(db.Text)
    workflow_summary = db.Column(db.Text)

    completion_data = db.Column(db.Text)
    blocker_data = db.Column(db.Text)

    final_output = db.Column(db.Text)

    created_at = db.Column(db.String)

    transcript = db.Column(db.Text)