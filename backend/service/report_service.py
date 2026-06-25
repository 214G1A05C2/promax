from typing import List, Dict, Any
from sqlalchemy.orm import Session
from repository.report_repository import ReportRepository

class ReportService:
    def get_intent_analysis(self, db: Session) -> List[Dict[str, Any]]:
        return ReportRepository(db).intent_analysis_data()
    
    