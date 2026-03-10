"""Transcription Service — FastAPI application."""

# --- CPU thread limit (must be set BEFORE any native library import) ---
import os as _os

_cpu_threads = _os.environ.get("CPU_THREADS", str(max(1, (_os.cpu_count() or 8) // 2)))
if _cpu_threads != "0":
    for _var in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                 "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        _os.environ[_var] = _cpu_threads

import logging
import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings

# --- Structured JSON logging ---
try:
    from pythonjsonlogger import json as jsonlogger

    handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s %(message)s",
        rename_fields={"asctime": "timestamp", "levelname": "level"},
    )
    handler.setFormatter(formatter)
    logging.root.handlers = [handler]
    logging.root.setLevel(logging.DEBUG if settings.debug else logging.INFO)
except ImportError:
    logging.basicConfig(
        level=logging.DEBUG if settings.debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

logger = logging.getLogger(__name__)

# --- FastAPI app ---
app = FastAPI(
    title=settings.app_name,
    description="Local speech-to-text with speaker diarization",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
from app.api.health import router as health_router  # noqa: E402
from app.api.jobs import router as jobs_router  # noqa: E402
from app.api.transcribe import router as transcribe_router  # noqa: E402

app.include_router(health_router)
app.include_router(jobs_router)
app.include_router(transcribe_router)

# --- Static files for snippets ---
data_dir = settings.data_dir
os.makedirs(data_dir, exist_ok=True)
app.mount("/data", StaticFiles(directory=data_dir), name="data")


@app.on_event("startup")
async def startup():
    logger.info(
        "Transcription service starting",
        extra={
            "provider": settings.transcription_provider,
            "whisper_model": settings.whisper_model,
            "whisper_device": settings.whisper_device,
            "default_language": settings.default_language,
            "cpu_threads": settings.cpu_threads,
            "debug": settings.debug,
        },
    )
