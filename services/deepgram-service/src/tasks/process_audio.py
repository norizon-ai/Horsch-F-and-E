import logging
import asyncio
from typing import List
from celery import Task
from src.celery_app import celery_app
from src.services.processor import AudioProcessor

logger = logging.getLogger(__name__)

class ProcessAudioTask(Task):
    """Custom task class with retry logic for external API failures."""

    autoretry_for = (
        Exception,
    )
    retry_kwargs = {'max_retries': 3}
    retry_backoff = True
    retry_backoff_max = 600
    retry_jitter = True


@celery_app.task(
    bind=True,
    base=ProcessAudioTask,
    name='process_audio_task',
    max_retries=3
)
def process_audio_task(self, job_id: str, file_path: str, glossary: List[str], language: str = "en") -> dict:
    """
    Process audio file through full ML pipeline.

    This is the main Celery task that orchestrates:
    1. Deepgram transcription + diarization
    2. Ghost speaker filtering
    3. OpenAI name inference
    4. FFmpeg snippet generation
    5. Redis storage
    """
    try:
        logger.info(f"[Celery] Starting audio processing for job {job_id}, language={language}")

        # Create processor instance
        processor = AudioProcessor()

        asyncio.run(processor.process(job_id, file_path, glossary, language))

        logger.info(f"[Celery] Completed audio processing for job {job_id}")

        return {
            "status": "completed",
            "job_id": job_id
        }

    except Exception as exc:
        logger.error(
            f"[Celery] Task failed for job {job_id}: {exc}",
            exc_info=True
        )

        # Retry logic for transient errors
        retryable_errors = (
            "timeout",
            "rate limit",
            "503",
            "429",
            "connection",
            "temporary"
        )

        error_msg = str(exc).lower()
        should_retry = any(err in error_msg for err in retryable_errors)

        if should_retry and self.request.retries < self.max_retries:
            countdown = 60 * (2 ** self.request.retries)
            logger.warning(
                f"[Celery] Retrying job {job_id} in {countdown}s "
                f"(attempt {self.request.retries + 1}/{self.max_retries})"
            )
            raise self.retry(exc=exc, countdown=countdown)

        logger.error(
            f"[Celery] Job {job_id} permanently failed after "
            f"{self.request.retries} retries"
        )

        # Publish error to Redis so frontend can show it
        from src.services.redis_manager import RedisManager
        redis = RedisManager()
        redis.publish_event(job_id, {
            "type": "error",
            "message": f"Processing failed: {str(exc)}"
        })

        # Send to Dead Letter Queue for manual inspection
        from src.celery_app import celery_app
        dlq_task_id = f"dlq_{job_id}"
        celery_app.send_task(
            'store_failed_task',
            args=[{
                'original_task_id': self.request.id,
                'job_id': job_id,
                'file_path': file_path,
                'glossary': glossary,
                'error': str(exc),
                'retries': self.request.retries,
                'failed_at': __import__('datetime').datetime.utcnow().isoformat()
            }],
            queue='dead_letter',
            task_id=dlq_task_id
        )
        logger.info(f"[Celery] Sent job {job_id} to Dead Letter Queue (task_id={dlq_task_id})")

        raise