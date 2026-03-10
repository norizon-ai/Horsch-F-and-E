"""Dead Letter Queue task for permanently failed jobs."""

import logging
import json
from datetime import datetime
from src.celery_app import celery_app
from src.services.redis_manager import RedisManager

logger = logging.getLogger(__name__)


@celery_app.task(name='store_failed_task', queue='dead_letter')
def store_failed_task(failed_task_data: dict) -> dict:
    """
    Store permanently failed task in Dead Letter Queue.

    This task is called when a job fails after all retries.
    Failed jobs are stored in Redis with a 30-day TTL for manual inspection.

    Args:
        failed_task_data: Dict with job_id, error, retries, failed_at, etc.

    Returns:
        dict: Storage confirmation
    """
    job_id = failed_task_data.get('job_id')

    try:
        logger.error(
            f"[DLQ] Storing permanently failed job {job_id} in Dead Letter Queue"
        )

        # Store in Redis with 30-day TTL
        redis = RedisManager()
        dlq_key = f"dlq:failed_jobs:{job_id}"

        redis.redis.setex(
            dlq_key,
            30 * 86400,  # 30 days
            json.dumps(failed_task_data, indent=2)
        )

        # Add to DLQ index (sorted set by timestamp)
        dlq_index_key = "dlq:failed_jobs_index"
        timestamp = datetime.utcnow().timestamp()
        redis.redis.zadd(
            dlq_index_key,
            {job_id: timestamp}
        )

        # Set TTL on index as well
        redis.redis.expire(dlq_index_key, 30 * 86400)

        logger.info(
            f"[DLQ] Job {job_id} stored in DLQ. "
            f"Error: {failed_task_data.get('error')[:100]}..."
        )

        redis.close()

        return {
            'status': 'stored',
            'dlq_key': dlq_key,
            'job_id': job_id
        }

    except Exception as e:
        logger.error(f"[DLQ] Failed to store job {job_id} in DLQ: {e}")
        raise
