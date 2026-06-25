from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    ForeignKey,
    Float,
    Boolean,
    Text,
    JSON
)
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship
from database import Base


class CallTranscript(Base):
    __tablename__ = "call_transcripts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    call_record_id = Column(Integer, unique=False, nullable=False)
    transcript = Column(JSON, nullable=False)
    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    

    intent = relationship(
        "CallIntent",
        back_populates="transcript",
        uselist=False
    )

class CallIntent(Base):
    __tablename__ = "call_intents"

    id = Column(Integer, primary_key=True)

    transcript_id = Column(
        Integer,
        ForeignKey("call_transcripts.id"),
        unique=True,
        nullable=False,
        index=True
    )

    call_record_id = Column(Integer, nullable=False, index=True)
    call_transcript = Column(JSON, nullable=False)
    clinic_name = Column(String(255), nullable=False, default="Unknown Clinic")

    primary_intent = Column(String(100), nullable=False)
    secondary_intents = Column(JSON, nullable=True, default=list)
    confidence = Column(Float, default=0)
    needs_human_review = Column(Boolean, default=False)
    reasoning = Column(Text)
    

    transcript = relationship(
        "CallTranscript",
        back_populates="intent"
    )
