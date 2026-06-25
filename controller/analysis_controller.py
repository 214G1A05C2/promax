from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from service.transcript_service import TranscriptService

router = APIRouter(prefix="/api", tags=["analysis"])

@router.post("/analyze/{call_record_id}")
def analyze_single(call_record_id: int, db: Session = Depends(get_db)):
    service = TranscriptService()
    try:
        result = service.analyze(db, call_record_id)
        return {"status": "completed", "data": result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-all")
def analyze_all(db: Session = Depends(get_db)):
    service = TranscriptService()
    return service.analyze_all(db)