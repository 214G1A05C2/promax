from pathlib import Path

from sqlalchemy import create_engine, inspect, text   #Creates database connection engine , Used to inspect database structure
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

_engine_kwargs = {"pool_pre_ping": True}
if settings.DATABASE_URL.startswith("sqlite"):
    _engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, **_engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    if settings.DATABASE_URL.startswith("sqlite:///"):
        db_path = Path(settings.DATABASE_URL[len("sqlite:///"):])
        db_path.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
    _ensure_denormalized_call_intents_columns()


def _ensure_denormalized_call_intents_columns():
    if engine.dialect.name == "sqlite":
        return

    inspector = inspect(engine)
    table_names = set(inspector.get_table_names())
    if "call_intents" not in table_names:
        return

    existing_columns = {column["name"] for column in inspector.get_columns("call_intents")}
    statements = []

    if "call_record_id" not in existing_columns:
        statements.append("ALTER TABLE call_intents ADD COLUMN call_record_id BIGINT")
    if "call_transcript" not in existing_columns:
        statements.append("ALTER TABLE call_intents ADD COLUMN call_transcript JSON")
    if "clinic_name" not in existing_columns:
        statements.append("ALTER TABLE call_intents ADD COLUMN clinic_name VARCHAR(255)")

    if not statements:
        return

    with engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))

        if "call_transcripts" not in table_names:
            return

        if "clinics" in table_names:
            connection.execute(text(
                """
                UPDATE call_intents AS ci
                SET call_record_id = COALESCE(ci.call_record_id, ct.call_record_id),
                    call_transcript = COALESCE(ci.call_transcript, ct.transcript),
                    clinic_name = COALESCE(ci.clinic_name, cl.clinic_name, 'Unknown Clinic')
                FROM call_transcripts AS ct
                LEFT JOIN clinics AS cl ON cl.transcript_id = ct.id
                WHERE ci.transcript_id = ct.id
                """
            ))
        else:
            connection.execute(text(
                """
                UPDATE call_intents AS ci
                SET call_record_id = COALESCE(ci.call_record_id, ct.call_record_id),
                    call_transcript = COALESCE(ci.call_transcript, ct.transcript),
                    clinic_name = COALESCE(ci.clinic_name, 'Unknown Clinic')
                FROM call_transcripts AS ct
                WHERE ci.transcript_id = ct.id
                """
            ))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
