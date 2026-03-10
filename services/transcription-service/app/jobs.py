"""In-memory job state store with asyncio.Queue-based SSE delivery."""

import asyncio
import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class JobState:
    """State for a single transcription job."""
    job_id: str
    status: JobStatus = JobStatus.PENDING
    tenant_id: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    speakers: Optional[List[Dict[str, Any]]] = None
    transcript: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    # SSE subscribers — each gets their own Queue
    _subscribers: List[asyncio.Queue] = field(default_factory=list)

    def subscribe(self) -> asyncio.Queue:
        """Create a new SSE subscriber queue."""
        queue: asyncio.Queue = asyncio.Queue()
        self._subscribers.append(queue)
        return queue

    def unsubscribe(self, queue: asyncio.Queue) -> None:
        """Remove an SSE subscriber queue."""
        try:
            self._subscribers.remove(queue)
        except ValueError:
            pass

    async def publish(self, event: Dict[str, Any]) -> None:
        """Publish an event to all subscribers."""
        for queue in self._subscribers:
            await queue.put(event)


class JobStore:
    """Thread-safe in-memory job store."""

    def __init__(self):
        self._jobs: Dict[str, JobState] = {}
        self._lock = asyncio.Lock()

    async def get_or_create(
        self,
        job_id: str,
        tenant_id: Optional[str] = None,
    ) -> tuple[JobState, bool]:
        """
        Get existing job or create a new one.
        Returns (job, created) tuple. Provides idempotency — if a job
        is already processing or completed, returns it without creating
        a duplicate.
        """
        async with self._lock:
            if job_id in self._jobs:
                return self._jobs[job_id], False
            job = JobState(job_id=job_id, tenant_id=tenant_id)
            self._jobs[job_id] = job
            return job, True

    async def get(self, job_id: str) -> Optional[JobState]:
        """Get a job by ID."""
        return self._jobs.get(job_id)

    async def set_status(self, job_id: str, status: JobStatus) -> None:
        """Update job status."""
        job = self._jobs.get(job_id)
        if job:
            job.status = status
            if status == JobStatus.COMPLETED:
                job.completed_at = datetime.utcnow()

    async def save_results(
        self,
        job_id: str,
        speakers: List[Dict[str, Any]],
        transcript: Dict[str, Any],
    ) -> None:
        """Save transcription results (in-memory + disk)."""
        from app.config import settings

        job = self._jobs.get(job_id)
        if job:
            job.speakers = speakers
            job.transcript = transcript

        # Persist to disk for retrieval after restart
        results_dir = os.path.join(settings.data_dir, "jobs", job_id)
        os.makedirs(results_dir, exist_ok=True)
        results_path = os.path.join(results_dir, "results.json")
        with open(results_path, "w") as f:
            json.dump({"speakers": speakers, "transcript": transcript}, f, ensure_ascii=False)
        logger.info(f"[{job_id}] Results persisted to {results_path}")


# Singleton
job_store = JobStore()
