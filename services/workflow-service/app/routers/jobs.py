"""
Jobs router - CRUD operations for workflow jobs.
"""

from fastapi import APIRouter, HTTPException, UploadFile, File, Request
from typing import List
import os
import aiofiles

from app.models import (
    CreateJobResponse,
    JobStatus,
    UploadResponse,
    SpeakersResponse,
    UpdateSpeakersRequest,
    Speaker,
)
from app.services.job_manager import JobManager
from app.services.file_metadata import extract_recording_date, extract_file_duration
from app.config import get_settings, ensure_upload_dir

router = APIRouter(tags=["jobs"])


@router.post("/jobs", response_model=CreateJobResponse)
async def create_job():
    """Create a new workflow job."""
    job = JobManager.create_job()
    return CreateJobResponse(
        job_id=job.id,
        status="pending",
        created_at=job.created_at,
    )


@router.get("/jobs/{job_id}", response_model=JobStatus)
async def get_job(job_id: str):
    """Get the current status of a job."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    return JobStatus(
        id=job.id,
        status=job.status,
        currentStep=job.current_step,
        createdAt=job.created_at,
        updatedAt=job.updated_at,
        fileUploaded=job.file_path is not None,
        hasSpeakers=len(job.speakers) > 0,
        hasProtocol=job.protocol is not None,
        recordingDate=job.recording_date,
        skipSpeakerVerification=job.teams_import,
        teamsAttendees=job.teams_attendees if job.teams_import else None,
    )


@router.delete("/jobs/{job_id}")
async def delete_job(job_id: str):
    """Cancel and cleanup a job."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    # Clean up any uploaded files
    if job.file_path and os.path.exists(job.file_path):
        try:
            os.remove(job.file_path)
        except OSError:
            pass  # Best effort cleanup

    JobManager.delete_job(job_id)
    return {"success": True, "message": f"Job {job_id} deleted"}

@router.get("/jobs/debug/files")
async def debug_files(path: str):
    """Debug endpoint to check files"""
    from app.config import get_settings
    settings = get_settings()
    full_path = os.path.join(settings.upload_dir, path.lstrip('/'))
    return {
        "upload_dir": settings.upload_dir,
        "requested_path": path,
        "resolved_path": full_path,
        "exists": os.path.exists(full_path),
        "is_file": os.path.isfile(full_path) if os.path.exists(full_path) else False,
        "size": os.path.getsize(full_path) if os.path.exists(full_path) else -1
    }


@router.post("/jobs/{job_id}/upload", response_model=UploadResponse)
async def upload_file(job_id: str, file: UploadFile = File(...), request: Request = None):
    """Upload an audio file for transcription."""
    job = JobManager.get_job(job_id)
    if job is None:
        # Auto-create job if it doesn't exist (frontend-initiated workflow)
        job = JobManager.create_job(job_id=job_id)

    # Validate file type
    valid_extensions = {".mp3", ".mp4", ".m4a", ".wav", ".webm"}
    file_ext = os.path.splitext(file.filename or "")[1].lower()
    if file_ext not in valid_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Supported: {', '.join(valid_extensions)}"
        )

    settings = get_settings()
    ensure_upload_dir()

    # Save file
    file_path = os.path.join(settings.upload_dir, f"{job_id}{file_ext}")

    # Read file content and get size
    content = await file.read()
    file_size = len(content)

    # Check file size
    max_size = settings.max_upload_size_mb * 1024 * 1024
    if file_size > max_size:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size: {settings.max_upload_size_mb}MB"
        )

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)

    # Extract actual duration from file metadata (more accurate than estimation)
    duration_seconds = extract_file_duration(file_path)
    if duration_seconds is None:
        # Fallback: estimate duration (rough: ~1MB per minute for audio)
        duration_seconds = max(60, int(file_size / 1_000_000 * 60))

    # Extract recording date from file metadata
    recording_date = extract_recording_date(file_path)

    # Update job state
    JobManager.set_file_info(
        job_id=job_id,
        file_path=file_path,
        file_name=file.filename or "unknown",
        file_size=file_size,
        duration_seconds=duration_seconds,
    )

    # Store recording date
    JobManager.update_job(
        job_id=job_id,
        recording_date=recording_date,
    )

    # Trigger KStudio processing (if not in mock mode)
    if not settings.use_mocks:
        import httpx
        # Get language from request header (de/en)
        language = request.headers.get("X-Language", "de") if request else "de"
        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    f"{settings.kstudio_url}/internal/transcribe/{job_id}/process",
                    json={
                        "file_path": file_path,
                        "glossary": [],  # TODO: Load from user settings/job config
                        "language": language
                    },
                    timeout=30.0
                )
        except Exception as e:
            # Log error but don't fail the upload
            # Processing will be tracked via SSE stream
            print(f"Warning: Failed to trigger KStudio processing: {e}")

    return UploadResponse(
        success=True,
        file_id=f"file-{job_id}",
        duration_seconds=duration_seconds,
    )


@router.post("/jobs/{job_id}/process")
async def trigger_processing(job_id: str, request: Request):
    """Trigger transcription processing for an already-uploaded file (e.g. Teams import)."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    file_path = getattr(job, "file_path", None)
    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="No file found for this job. Upload a file first.")

    settings = get_settings()
    if not settings.use_mocks:
        import httpx
        language = request.headers.get("X-Language", "de") if request else "de"
        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    f"{settings.kstudio_url}/internal/transcribe/{job_id}/process",
                    json={
                        "file_path": file_path,
                        "glossary": [],
                        "language": language,
                    },
                    timeout=30.0,
                )
        except Exception as e:
            print(f"Warning: Failed to trigger processing: {e}")

    return {"success": True, "job_id": job_id}


@router.get("/jobs/{job_id}/speakers", response_model=SpeakersResponse)
async def get_speakers(job_id: str):
    """Get detected speakers for a job."""
    import logging
    logger = logging.getLogger(__name__)

    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    # If speakers are already set, return them
    if job.speakers:
        # DEBUG: Log speakers being returned to frontend
        logger.info(f"GET /jobs/{job_id}/speakers - Returning {len(job.speakers)} speakers:")
        for i, s in enumerate(job.speakers):
            logger.info(f"  Speaker {i}: detected='{s.detected_name}', confirmed='{s.confirmed_name}'")
        return SpeakersResponse(speakers=job.speakers)

    # No speakers yet (speakers are populated by transcription service)
    logger.info(f"GET /jobs/{job_id}/speakers - No speakers available yet")
    return SpeakersResponse(speakers=[])


@router.put("/jobs/{job_id}/speakers")
async def update_speakers(job_id: str, request: UpdateSpeakersRequest):
    """Update speaker names (confirmations from user)."""
    import logging
    logger = logging.getLogger(__name__)

    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    # DEBUG: Log what we're receiving from frontend
    logger.info(f"=== UPDATE SPEAKERS REQUEST ===")
    logger.info(f"Job ID: {job_id}")
    logger.info(f"Received {len(request.speakers)} speakers from frontend:")
    for i, speaker in enumerate(request.speakers):
        logger.info(f"  Speaker {i}: id={speaker.id}")
        logger.info(f"    detectedName: '{speaker.detected_name}'")
        logger.info(f"    confirmedName: '{speaker.confirmed_name}'")
        logger.info(f"    confirmedName empty? {speaker.confirmed_name == ''}")
        logger.info(f"    confirmedName truthy? {bool(speaker.confirmed_name)}")
    logger.info(f"=== END UPDATE SPEAKERS ===")

    JobManager.set_speakers(job_id, request.speakers)

    return {"success": True, "message": "Speakers updated"}
