import json
import redis
from typing import Dict, List, Any, Optional
from src.config import settings

class RedisManager:
    """Handles all Redis operations for job processing."""

    def __init__(self):
        self.client = redis.from_url(settings.redis_url, decode_responses=True)
        self.ttl_seconds = settings.redis_ttl_days * 86400 # days -> seconds

    @property
    def redis(self):
        """Alias for backward compatibility."""
        return self.client
    
    def publish_event(self, job_id: str, event: Dict[str, Any]) -> None:
        """Publish event to job's PubSub channel."""

        channel = f"jobs:{job_id}:events"
        self.client.publish(channel, json.dumps(event))
    
    def save_speakers(self, job_id: str, speakers: List[Dict[str, Any]]) -> None:
        """Save speakers list to Redis with TTL."""

        key = f"jobs:{job_id}:speakers"
        self.client.setex(key, self.ttl_seconds, json.dumps(speakers))
    
    def save_transcript(self, job_id: str, transcript: Dict[str, Any]) -> None:
        """Save transcript to Redis with TTL."""

        key = f"jobs:{job_id}:transcript"
        self.client.setex(key, self.ttl_seconds, json.dumps(transcript))
    
    def get_speakers(self, job_id: str) -> Optional[List[Dict[str, Any]]]:
        """Retrieve speakers list from Redis and extend TTL."""

        key = f"jobs:{job_id}:speakers"
        data = self.client.get(key)
        if data:
            self.client.expire(key, self.ttl_seconds)
            return json.loads(data)
        return None

    def get_transcript(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve transcript from Redis and extend TTL."""

        key = f"jobs:{job_id}:transcript"
        data = self.client.get(key)
        if data:
            self.client.expire(key, self.ttl_seconds)
            return json.loads(data)
        return None

    def set_job_status(self, job_id: str, status: str, metadata: Optional[Dict] = None) -> None:
        """Set job status with TTL."""

        key = f"jobs:{job_id}:status"
        value = {"status": status, "metadata": metadata or {}}
        self.client.setex(key, self.ttl_seconds, json.dumps(value))

    def get_job_status(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get job status and extend TTL."""

        key = f"jobs:{job_id}:status"
        data = self.client.get(key)
        if data:
            self.client.expire(key, self.ttl_seconds)
            return json.loads(data)
        return None

    def subscribe(self, channel: str):
        """Create PubSub subscription."""

        pubsub = self.client.pubsub()
        pubsub.subscribe(channel)
        return pubsub
    
    def close(self):
        """Close Redis connection."""
        self.client.close()