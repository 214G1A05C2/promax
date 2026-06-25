from typing import Optional, List
from sqlalchemy.orm import Session
from repository.models import CallTranscript

class TranscriptRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_call_record_id(self, call_record_id: int) -> Optional[CallTranscript]:
        return self.session.query(CallTranscript).filter(
            CallTranscript.call_record_id == call_record_id
        ).first()

    def get_all(self, limit: int = 100, offset: int = 0) -> List[CallTranscript]: 
        return self.session.query(CallTranscript).order_by(
            CallTranscript.call_record_id
        ).offset(offset).limit(limit).all()
        
