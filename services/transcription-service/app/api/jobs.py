"""Job management endpoints — file upload and speaker retrieval."""

import logging
import os

import aiofiles
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import settings
from app.jobs import job_store
from app.models import SpeakersResponse

router = APIRouter(prefix="/internal/jobs")
logger = logging.getLogger(__name__)

VALID_EXTENSIONS = {".mp3", ".mp4", ".m4a", ".wav", ".webm", ".ogg", ".flac"}


@router.post("/{job_id}/upload")
async def upload_audio(job_id: str, file: UploadFile = File(...)):
    """Receive audio file from workflow-service."""
    file_ext = os.path.splitext(file.filename or "")[1].lower()

    if file_ext not in VALID_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Supported: {', '.join(sorted(VALID_EXTENSIONS))}",
        )

    os.makedirs(settings.upload_dir, exist_ok=True)
    file_path = os.path.join(settings.upload_dir, f"{job_id}{file_ext}")
    content = await file.read()

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)

    logger.info(f"[{job_id}] Uploaded {file.filename} ({len(content)} bytes)")

    return {
        "success": True,
        "file_id": f"file-{job_id}",
        "file_path": file_path,
        "size": len(content),
    }


@router.get("/{job_id}/speakers")
async def get_speakers(job_id: str):
    """Get detected speakers for a completed job."""
    job = await job_store.get(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if not job.speakers:
        raise HTTPException(status_code=404, detail="No speakers available yet")

    return SpeakersResponse(
        speakers=[
            {**s, "detectedName": s.get("detectedName", "")}
            for s in job.speakers
        ]
    )


@router.get("/{job_id}/transcript")
async def get_transcript(job_id: str):
    """Get the full transcript with segments and word timestamps."""
    job = await job_store.get(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if not job.transcript:
        raise HTTPException(status_code=404, detail="No transcript available yet")

    return job.transcript
