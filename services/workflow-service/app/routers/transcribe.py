"""
Transcribe router - SSE streaming for transcription progress.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
import httpx
import asyncio
import json
import logging
from typing import AsyncGenerator

from app.services.job_manager import JobManager
from app.config import get_settings

logger = logging.getLogger(__name__)

router = APIRouter(tags=["transcription"])


async def step_uploading(request: Request) -> AsyncGenerator[str, None]:
    """Step 1: Upload and encrypt file (0-25%)"""
    for i in range(10):
        if await request.is_disconnected():
            return
        percent = int(i * 2.5)  # 0, 2, 5, 7, 10, 12, 15, 17, 20, 22
        yield f'data: {{"type":"progress","stage":"uploading","percent":{percent},"message":"Datei wird hochgeladen..."}}\n\n'
        await asyncio.sleep(0.2)


async def step_transcribing(request: Request) -> AsyncGenerator[str, None]:
    """Step 2: Speech-to-text conversion (25-50%)"""
    for i in range(10):
        if await request.is_disconnected():
            return
        percent = 25 + int(i * 2.5)
        yield f'data: {{"type":"progress","stage":"transcribing","percent":{percent},"message":"Sprache wird erkannt..."}}\n\n'
        await asyncio.sleep(0.2)


async def step_diarizing(request: Request) -> AsyncGenerator[str, None]:
    """Step 3: Speaker identification (50-75%)"""
    for i in range(10):
        if await request.is_disconnected():
            return
        percent = 50 + int(i * 2.5)
        yield f'data: {{"type":"progress","stage":"diarizing","percent":{percent},"message":"Sprecher werden identifiziert..."}}\n\n'
        await asyncio.sleep(0.2)


async def step_correcting(request: Request) -> AsyncGenerator[str, None]:
    """Step 4: Apply custom vocabulary (75-100%)"""
    for i in range(10):
        if await request.is_disconnected():
            return
        percent = 75 + int(i * 2.5)
        yield f'data: {{"type":"progress","stage":"correcting","percent":{percent},"message":"Vokabular wird angewendet..."}}\n\n'
        await asyncio.sleep(0.2)


async def mock_transcription_stream(
    job_id: str,
    request: Request
) -> AsyncGenerator[str, None]:
    """
    Main stream: calls each step sequentially.
    Generates mock SSE events matching frontend expectations.
    """
    # Step 1: Uploading
    async for event in step_uploading(request):
        yield event

    # Step 2: Transcribing
    async for event in step_transcribing(request):
        yield event

    # Step 3: Diarizing
    async for event in step_diarizing(request):
        yield event

    # Step 4: Correcting
    async for event in step_correcting(request):
        yield event

    # Generate final mock data (lazy import -- only used in dev/mock mode)
    from app.services.mock_generator import MockGenerator
    mock_gen = MockGenerator()
    speakers = mock_gen.generate_speakers()
    protocol = mock_gen.generate_protocol(speakers=speakers)

    # Store in job state
    JobManager.set_speakers(job_id, speakers)
    job = JobManager.get_job(job_id)
    if job:
        job.transcript = protocol.full_transcript
        job.status = "completed"
        job.current_step = 3  # Speaker verification step
        job.touch()
        JobManager._save_job(job)  # Persist transcript to Redis

    # Final: Complete event with mock data
    complete_event = {
        "type": "complete",
        "speakers": [s.model_dump(by_alias=True) for s in speakers],
        "transcript": protocol.full_transcript,
    }
    yield f"data: {json.dumps(complete_event)}\n\n"


async def proxy_transcription_stream(
    job_id: str,
    settings
) -> AsyncGenerator[bytes, None]:
    """
    Proxy SSE stream from Deepgram service.
    Used when USE_MOCKS=false.
    Parses complete events to store transcript and speakers in JobState.
    """
    logger.info(f"[SSE Proxy] Starting proxy stream for job {job_id}")
    async with httpx.AsyncClient(timeout=None) as client:
        logger.info(f"[SSE Proxy] Connecting to {settings.kstudio_url}/internal/transcribe/{job_id}/stream")
        async with client.stream(
            "GET",
            f"{settings.kstudio_url}/internal/transcribe/{job_id}/stream"
        ) as response:
            logger.info(f"[SSE Proxy] Connected, status={response.status_code}, starting to iterate chunks")

            # Buffer for incomplete SSE events
            buffer = ""

            async for chunk in response.aiter_bytes():
                logger.debug(f"[SSE Proxy] Received chunk of {len(chunk)} bytes")

                # Add chunk to buffer
                buffer += chunk.decode('utf-8')

                # Process complete SSE events (ending with \n\n)
                while '\n\n' in buffer:
                    event_text, buffer = buffer.split('\n\n', 1)

                    # Try to parse the SSE event to extract complete data
                    try:
                        if event_text.startswith('data: '):
                            event_data = event_text[6:].strip()
                            if event_data:
                                event = json.loads(event_data)
                                if event.get('type') == 'complete':
                                    # Store transcript and speakers in JobState
                                    job = JobManager.get_job(job_id)
                                    if job:
                                        transcript_text = event.get('transcript', '')
                                        job.transcript = transcript_text
                                        job.status = "completed"
                                        job.current_step = 3  # Speaker verification step
                                        job.touch()
                                        JobManager._save_job(job)  # Persist transcript to Redis
                                        logger.info(f"[SSE Parser] Stored transcript for job {job_id}: {len(transcript_text) if transcript_text else 0} chars")
                                    # Store speakers
                                    speakers = event.get('speakers', [])
                                    if speakers:
                                        JobManager.set_speakers(job_id, speakers)
                                        logger.info(f"[SSE Parser] Stored {len(speakers)} speakers for job {job_id}")
                    except Exception as e:
                        # Log parsing errors
                        logger.error(f"[SSE Parser] Failed to parse SSE event for job {job_id}: {e}")

                yield chunk


@router.get("/transcribe/{job_id}/stream")
async def stream_transcription(job_id: str, request: Request):
    """
    Stream transcription progress via Server-Sent Events (SSE).

    The stream emits events of type:
    - progress: { type, stage, percent, message }
    - complete: { type, speakers, transcript }
    - error: { type, error }
    """
    settings = get_settings()
    logger.info(f"[Stream Endpoint] Received stream request for job {job_id}, use_mocks={settings.use_mocks}")

    job = JobManager.get_job(job_id)
    if job is None:
        # Auto-create job if it doesn't exist (matches upload endpoint behavior)
        job = JobManager.create_job(job_id)

    if settings.use_mocks:
        logger.info(f"[Stream Endpoint] Using mock stream for job {job_id}")
        return StreamingResponse(
            mock_transcription_stream(job_id, request),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",  # Disable nginx buffering
            },
        )

    # Proxy to real transcription service
    logger.info(f"[Stream Endpoint] Using proxy stream for job {job_id}")
    return StreamingResponse(
        proxy_transcription_stream(job_id, settings),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
