from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
from src.models.schemas import ProcessRequest
from src.services.redis_manager import RedisManager
from src.tasks.process_audio import process_audio_task
import logging
import json
import asyncio

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/{job_id}/process")
async def process_audio(job_id: str, request: ProcessRequest):
    """ Trigger asynchronous audio processing via Celery. Called by workflow-service after file upload."""

    logger.info(
        f"Processing request received for job {job_id}: "
        f"file={request.file_path}, glossary_size={len(request.glossary)}"
    )

    # Submit task to Celery queue
    task = process_audio_task.apply_async(
        args=[job_id, request.file_path, request.glossary, request.language],
        task_id=job_id
    )

    logger.info(
        f"Celery task submitted for job {job_id}, "
        f"task_id={task.id}, state={task.state}"
    )

    return {
        "job_id": job_id,
        "task_id": task.id,
        "status": "queued"
    }


@router.get("/{job_id}/stream")
async def stream_progress(job_id: str):
    """SSE stream of processing progress. Subscribes to Redis PubSub channel: jobs:{job_id}:events"""

    logger.info(f"SSE stream requested for job {job_id}")

    async def event_generator() -> AsyncGenerator[str, None]:
        """Generate SSE events from Redis PubSub."""
        redis_manager = RedisManager()

        existing_speakers = redis_manager.get_speakers(job_id)
        if existing_speakers:
            logger.info(f"Job {job_id} already complete, sending immediate completion event")
            existing_transcript = redis_manager.get_transcript(job_id)
            complete_event = {
                "type": "complete",
                "percent": 100,
                "message": "Transcription complete",
                "speakers": existing_speakers,
                "transcript": existing_transcript.get("text", "") if existing_transcript else ""
            }
            yield f"data: {json.dumps(complete_event)}\n\n"
            redis_manager.close()
            return

        pubsub = redis_manager.subscribe(f"jobs:{job_id}:events")
        
        try:
            last_ping = asyncio.get_event_loop().time()
            while True:
                message = pubsub.get_message(ignore_subscribe_messages=True)
                if message and message['type'] == 'message':
                    event_data = message['data']
                    yield f"data: {event_data}\n\n"
                    last_ping = asyncio.get_event_loop().time()
                    
                    event = json.loads(event_data)
                    if event['type'] in ['complete', 'error']:
                        logger.info(
                            f"SSE stream completed for job {job_id}, "
                            f"event_type={event['type']}"
                        )
                        break
                else:
                    current_time = asyncio.get_event_loop().time()
                    if current_time - last_ping > 15:
                        yield ": keepalive\n\n"
                        last_ping = current_time
                
                await asyncio.sleep(0.5)
        finally:
            pubsub.unsubscribe()
            pubsub.close()
            redis_manager.close()

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )