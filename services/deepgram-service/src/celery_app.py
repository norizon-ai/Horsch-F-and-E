"""Celery application for async job processing."""

from celery import Celery
from src.config import settings

# Initialize Celery with Redis broker and backend
celery_app = Celery(
    "deepgram_service",
    broker=settings.redis_url,
    backend=settings.redis_url
)

# Configure Celery behavior
celery_app.conf.update(
    # Reliability
    task_acks_late=True,                    # Only ack after task completes (survive crashes)
    task_reject_on_worker_lost=True,        # Requeue if worker dies mid-task
    worker_prefetch_multiplier=1,           # Fetch 1 task at a time (fair distribution)

    # Retry behavior
    task_default_retry_delay=60,            # Wait 1 min before retry
    task_max_retries=3,                     # Retry failed tasks up to 3 times

    # Dead Letter Queue - Failed tasks go here after max retries
    task_publish_retry_policy={
        'max_retries': 3,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.2,
    },

    # Result backend
    result_expires=86400,                   # Keep results for 24 hours

    # Serialization
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,

    # Task routing - send failed tasks to DLQ
    task_default_queue='default',
    task_queues={
        'default': {
            'exchange': 'default',
            'routing_key': 'default',
        },
        'dead_letter': {
            'exchange': 'dead_letter',
            'routing_key': 'dead_letter',
        },
    },
)

# Auto-discover tasks
celery_app.autodiscover_tasks(['src.tasks'])
