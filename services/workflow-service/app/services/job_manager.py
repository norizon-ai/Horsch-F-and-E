"""
Redis-backed job state manager for workflow processing.
Ensures state is shared across multiple service replicas.
"""

import json
import secrets
from typing import Dict, Optional, List, Any
from datetime import datetime
from dataclasses import dataclass, field, asdict

import redis
from app.models import Speaker, Protocol
from app.config import get_settings

@dataclass
class JobState:
    """State of a workflow job."""
    id: str
    status: str = "pending"
    current_step: int = 1
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    # File info
    file_path: Optional[str] = None
    file_name: Optional[str] = None
    file_size: Optional[int] = None
    duration_seconds: Optional[int] = None
    recording_date: Optional[str] = None  # Actual recording date from file metadata or Teams

    # Teams import metadata
    teams_import: bool = False  # True if imported from Teams
    teams_attendees: List[dict] = field(default_factory=list)  # Attendees with names/photos from Teams

    # Transcription results
    speakers: List[Speaker] = field(default_factory=list)
    transcript: Optional[str] = None

    # Protocol
    protocol: Optional[Protocol] = None

    # Publishing
    confluence_url: Optional[str] = None
    pdf_url: Optional[str] = None

    def touch(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.utcnow().isoformat()


class JobManager:
    """
    Manages workflow job state in Redis.
    Ensures state is shared across multiple service replicas.
    """

    _redis_client: Optional[redis.Redis] = None

    @classmethod
    def _get_client(cls) -> redis.Redis:
        """Get or create the Redis client."""
        if cls._redis_client is None:
            settings = get_settings()
            # The REDIS_URL from main.bicep already includes the DB index (e.g. /1)
            cls._redis_client = redis.from_url(
                settings.redis_url,
                decode_responses=True
            )
        return cls._redis_client

    @classmethod
    def _get_key(cls, job_id: str) -> str:
        """Get the Redis key for a job."""
        return f"workflow:job:{job_id}"

    @classmethod
    def create_job(cls, job_id: Optional[str] = None) -> JobState:
        """Create a new workflow job with a unique ID or a specified ID."""
        if job_id is None:
            timestamp = int(datetime.utcnow().timestamp() * 1000)
            random_suffix = secrets.token_hex(4)
            job_id = f"job-{timestamp}-{random_suffix}"

        job = JobState(id=job_id)
        cls._save_job(job)
        return job

    @classmethod
    def _save_job(cls, job: JobState):
        """Save a job state to Redis with 24h expiration."""
        client = cls._get_client()
        key = cls._get_key(job.id)
        
        # Convert dataclass to dict. asdict is recursive and handles nested dataclasses.
        # Speaker and Protocol are Pydantic models, so they need special handling.
        data = asdict(job)
        
        # Ensure deep nesting of Pydantic models is converted to dicts for JSON
        def convert_pydantic(obj):
            if isinstance(obj, list):
                return [convert_pydantic(i) for i in obj]
            if isinstance(obj, dict):
                return {k: convert_pydantic(v) for k, v in obj.items()}
            # If it has a .dict() or .model_dump() (Pydantic v1/v2)
            if hasattr(obj, "model_dump"):
                return obj.model_dump()
            if hasattr(obj, "dict"):
                return obj.dict()
            return obj

        # Convert Pydantic models to dicts recursively
        data = convert_pydantic(data)

        client.setex(key, 86400, json.dumps(data))

    @classmethod
    def get_job(cls, job_id: str) -> Optional[JobState]:
        """Get a job by ID."""
        client = cls._get_client()
        key = cls._get_key(job_id)
        data = client.get(key)
        
        if not data:
            return None
        
        try:
            job_dict = json.loads(data)
            
            # Reconstruct Speaker and Protocol objects if present
            if job_dict.get("speakers"):
                job_dict["speakers"] = [Speaker(**s) if isinstance(s, dict) else s for s in job_dict["speakers"]]
            
            if job_dict.get("protocol") and isinstance(job_dict["protocol"], dict):
                job_dict["protocol"] = Protocol(**job_dict["protocol"])
                
            return JobState(**job_dict)
        except Exception:
            # Fallback or log error
            return None

    @classmethod
    def update_job(cls, job_id: str, **kwargs) -> Optional[JobState]:
        """Update job fields."""
        job = cls.get_job(job_id)
        if job is None:
            return None

        for key, value in kwargs.items():
            if hasattr(job, key):
                setattr(job, key, value)

        job.touch()
        cls._save_job(job)
        return job

    @classmethod
    def delete_job(cls, job_id: str) -> bool:
        """Delete a job."""
        client = cls._get_client()
        return bool(client.delete(cls._get_key(job_id)))

    @classmethod
    def set_speakers(cls, job_id: str, speakers: List[Speaker]) -> Optional[JobState]:
        """Set the speakers for a job."""
        return cls.update_job(job_id, speakers=speakers)

    @classmethod
    def set_protocol(cls, job_id: str, protocol: Protocol) -> Optional[JobState]:
        """Set the protocol for a job."""
        return cls.update_job(job_id, protocol=protocol, current_step=4)

    @classmethod
    def set_file_info(
        cls,
        job_id: str,
        file_path: str,
        file_name: str,
        file_size: int,
        duration_seconds: int
    ) -> Optional[JobState]:
        """Set file information after upload."""
        return cls.update_job(
            job_id,
            file_path=file_path,
            file_name=file_name,
            file_size=file_size,
            duration_seconds=duration_seconds,
            status="processing",
            current_step=2
        )

    @classmethod
    def list_jobs(cls) -> List[JobState]:
        """List all jobs (for debugging)."""
        client = cls._get_client()
        keys = client.keys("workflow:job:*")
        jobs = []
        for key in keys:
            job_id = key.split(":")[-1]
            job = cls.get_job(job_id)
            if job:
                jobs.append(job)
        return jobs

    @classmethod
    def clear_all(cls):
        """Clear all jobs (for testing)."""
        client = cls._get_client()
        keys = client.keys("workflow:job:*")
        if keys:
            client.delete(*keys)
