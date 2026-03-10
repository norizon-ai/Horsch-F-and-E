import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.api import health, transcribe, jobs
from fastapi.staticfiles import StaticFiles
import os

logging.basicConfig(
    level=logging.INFO if not settings.debug else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="Deepgram-based transcription with speaker diarization and audio snippets",
    version="1.0.0",
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])

# Internal API endpoints (called by workflow-service)

app.include_router(
    transcribe.router,
    prefix="/internal/transcribe",
    tags=["transcription"]
)
app.include_router(
    jobs.router,
    prefix="/internal/jobs",
    tags=["jobs"]
)

os.makedirs(settings.data_dir, exist_ok=True)

# Mount static files for data directory
app.mount(
    "/data",
    StaticFiles(directory=settings.data_dir),
    name="data"
)

@app.on_event("startup")
async def startup_event():
    """Application startup handler."""
    logger.info(
        f"Application starting: {settings.app_name}",
        extra={
            "debug": settings.debug,
            "deepgram_model": settings.deepgram_model,
        }
    )

@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown handler."""
    logger.info("Application shutting down")

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "service": settings.app_name,
        "status": "running",
        "version": "1.0.0",
        "engine": "deepgram"
    }