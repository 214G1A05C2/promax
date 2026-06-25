import os
import logging
from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
from database import init_db
from contextlib import asynccontextmanager
from controller.transcript_controller import router as transcript_router
from controller.analysis_controller import router as analysis_router
from controller.report_controller import router as report_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__) #Configures application-wide logging.




@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing database...")
    init_db()
    logger.info("Startup complete.")

    yield  

    logger.info("Application shutting down...")
    
app = FastAPI(title="Healthcare Intent Analytics", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transcript_router)
app.include_router(analysis_router)
app.include_router(report_router)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

@app.get("/")
def root():
    return {"message": "Application is running."}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    reload_enabled = os.environ.get("UVICORN_RELOAD", "0") == "1"

    logger.info("Open http://127.0.0.1:%s/ in your browser.", port)
    uvicorn.run("app:app", host=host, port=port, reload=reload_enabled)
