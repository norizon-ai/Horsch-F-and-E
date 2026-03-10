"""Transcription endpoints — process trigger and SSE stream."""

import asyncio
import json
import logging
from typing import AsyncGenerator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.jobs import JobStatus, job_store
from app.models import ProcessRequest
from app.services.transcriber import TranscriptionPipeline

router = APIRouter(prefix="/internal/transcribe")
logger = logging.getLogger(__name__)

# Track running background tasks to prevent garbage collection
_background_tasks: set[asyncio.Task] = set()


@router.post("/{job_id}/process")
async def process_audio(job_id: str, request: ProcessRequest):
    """
    Trigger async audio processing.

    Idempotency guard: if job is already processing or completed,
    returns existing status instead of starting a duplicate pipeline.
    """
    job, created = await job_store.get_or_create(
        job_id, tenant_id=request.tenant_id
    )

    # Idempotency guard
    if not created:
        if job.status in (JobStatus.PROCESSING, JobStatus.COMPLETED):
            logger.info(
                f"[{job_id}] Idempotency guard: job already {job.status.value}, "
                f"skipping duplicate pipeline"
            )
            return {"job_id": job_id, "status": job.status.value}

    # Start pipeline as background task
    pipeline = TranscriptionPipeline()
    task = asyncio.create_task(
        pipeline.process(
            job_id,
            request.file_path,
            request.glossary,
            request.language,
            request.tenant_id,
        )
    )
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)

    logger.info(f"[{job_id}] Background pipeline started")

    return {"job_id": job_id, "status": "processing"}


@router.get("/{job_id}/stream")
async def stream_progress(job_id: str):
    """SSE stream of processing progress via asyncio.Queue."""
    logger.info(f"[{job_id}] SSE stream requested")

    async def event_generator() -> AsyncGenerator[str, None]:
        job = await job_store.get(job_id)

        # Fast path: job already completed
        if job and job.status == JobStatus.COMPLETED and job.speakers:
            logger.info(f"[{job_id}] Already complete, sending immediate event")
            transcript_text = ""
            if job.transcript:
                transcript_text = job.transcript.get("text", "")
            complete_event = {
                "type": "complete",
                "percent": 100,
                "message": "Transkription abgeschlossen",
                "speakers": job.speakers,
                "transcript": transcript_text,
            }
            yield f"data: {json.dumps(complete_event)}\n\n"
            return

        # Fast path: job failed
        if job and job.status == JobStatus.FAILED:
            yield f"data: {json.dumps({'type': 'error', 'error': job.error or 'Processing failed'})}\n\n"
            return

        if not job:
            # Job doesn't exist yet — create a pending one so we can subscribe
            job, _ = await job_store.get_or_create(job_id)

        queue = job.subscribe()

        try:
            while True:
                try:
                    # Wait for events with timeout for heartbeat
                    event = await asyncio.wait_for(queue.get(), timeout=30.0)
                    yield f"data: {json.dumps(event)}\n\n"

                    if event.get("type") in ("complete", "error"):
                        logger.info(
                            f"[{job_id}] SSE stream ended: {event.get('type')}"
                        )
                        break

                except asyncio.TimeoutError:
                    # Send heartbeat to keep connection alive
                    yield ": heartbeat\n\n"

        finally:
            job.unsubscribe(queue)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
