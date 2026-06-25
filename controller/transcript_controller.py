from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from repository.transcript_repository import TranscriptRepository
from service.transcript_service import TranscriptService

router = APIRouter(prefix="/api", tags=["Transcripts"])  # Group related APIs

@router.get("/transcripts")
def list_transcripts(limit: int = Query(100, ge=1), offset: int = Query(0, ge=0),
                     db: Session = Depends(get_db)): # Used for Dependency Injection.
    repo = TranscriptRepository(db)
    transcripts = repo.get_all(limit=limit, offset=offset)
    return [{"id": t.id, "call_record_id": t.call_record_id} for t in transcripts]


@router.get("/results/{call_record_id}")
def get_results(call_record_id: int, db: Session = Depends(get_db)):
    service = TranscriptService()
    try: 
        results = service.get_results(db, call_record_id)
        return {"status": "analyzed", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/transcripts")
# def list_transcripts(
#     limit: int | None = Query(100, ge=1),
#     offset: int = Query(0, ge=0),
#     db: Session = Depends(get_db)
# ):
#     repo = TranscriptRepository(db)

#     if limit is None:
#         transcripts = repo.get_all()
#     else:
#         transcripts = repo.get_all(limit=limit, offset=offset)

#     return [
#         {"id": t.id, "call_record_id": t.call_record_id}
#         for t in transcripts
#     ]

# @router.get("/transcripts")
# def list_transcripts(db: Session = Depends(get_db)):
#     repo = TranscriptRepository(db)
#     transcripts = repo.get_all()  # no limit, no offset

#     return [
#         {"id": t.id, "call_record_id": t.call_record_id}
#         for t in transcripts
#     ]
