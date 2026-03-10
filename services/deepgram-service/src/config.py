"""Application configuration using Pydantic Settings."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Deepgram API
    deepgram_api_key: str
    deepgram_model: str = "nova-2"
    
    # OpenAI API (for speaker inference)
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.2
    openai_max_tokens: int = 500

    # Inference tuning
    inference_max_chars: int = 50000      # transcript chars sent to LLM (whole-context mode)

    # Deepgram options
    keyword_boost: float = 2.0
    deepgram_timeout: float = 300.0
    deepgram_connect_timeout: float = 10.0

    # Snippet generation
    snippet_duration_secs: float = 5.0
    snippet_max_utterances: int = 10      # only consider first N utterances per speaker
    snippet_text_max_chars: int = 100
    ffmpeg_timeout_secs: int = 30

    # Prompts
    prompts_dir: str = "/app/prompts"

    # Redis
    redis_url: str = "redis://localhost:6379/0"
    redis_ttl_days: int = 7  # Auto-delete job data after N days

    # Storage paths (local fallback if S3 is not configured)
    upload_dir: str = "/app/uploads"
    data_dir: str = "/app/data"

    # S3/MinIO Object Storage
    s3_endpoint: Optional[str] = None          # MinIO: http://minio:9000, AWS: leave blank
    s3_access_key: Optional[str] = None
    s3_secret_key: Optional[str] = None
    s3_bucket: str = "nora-meeting-data"
    s3_region: Optional[str] = None            # AWS only: us-east-1, eu-central-1, etc.
    s3_public_url: str = "http://localhost:9000"  # CDN URL in production

    # Application
    app_name: str = "Nora Deepgram Service"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
