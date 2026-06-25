import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from service.report_service import ReportService
from service.excel_service import ExcelService

router = APIRouter(prefix="/api/reports", tags=["Reports"])

@router.post("/generate")
def generate_reports(db: Session = Depends(get_db)):
    try:
        report_service = ReportService()
        excel_service = ExcelService()
        intent_data = report_service.get_intent_analysis(db)
        excel_service.generate_intent_report(intent_data)
        return {"status": "reports generated", "folder": "reports/"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
def list_reports():
    folder = "reports"
    if not os.path.exists(folder):
        return {"reports": []}
    files = [f for f in os.listdir(folder) if f.endswith(".xlsx")]
    return {"reports": files}