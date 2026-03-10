"""
Configuration settings for the Workflow Service.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Mock mode - set to False when real services are ready
    use_mocks: bool = False  # PDF export now fully implemented

    # Database (reads from DATABASE_URL, not WORKFLOW_DATABASE_URL)
    database_url: str = Field(
        default="postgresql+asyncpg://norizon:norizon@localhost:5432/workflows",
        validation_alias="DATABASE_URL"
    )

    # Auth0 Configuration (reads from AUTH0_*, not WORKFLOW_AUTH0_*)
    auth0_enabled: bool = Field(default=True, validation_alias="AUTH0_ENABLED")
    auth0_domain: str = Field(default="", validation_alias="AUTH0_DOMAIN")
    auth0_audience: str = Field(default="", validation_alias="AUTH0_AUDIENCE")

    # Internal service URLs
    kstudio_url: str = "http://localhost:8002"  # KStudio ML Pipeline
    transcription_service_url: str = "http://localhost:8002"  # DEPRECATED - use kstudio_url
    deepsearch_url: str = "http://localhost:8000"  # Custom DeepResearch service
    confluence_publisher_url: str = "http://localhost:8003"

    # LLM provider settings (protocol generation)
    # Reads WORKFLOW_LLM_API_KEY, falls back to OPENAI_API_KEY
    llm_api_key: str = Field(default_factory=lambda: os.environ.get("OPENAI_API_KEY", ""))
    llm_base_url: Optional[str] = None  # None = OpenAI default; set to IONOS endpoint for EU hosting
    llm_model: str = "gpt-4o-mini"
    llm_temperature: float = 0.3
    llm_max_tokens: int = 8000
    llm_two_pass: bool = False  # Enable two-pass protocol generation (structure then extract)

    # File storage
    upload_dir: str = "/tmp/workflow-uploads"
    max_upload_size_mb: int = 500

    # Microsoft Teams / Azure AD (OAuth2 delegated permissions)
    ms_tenant_id: str = ""
    ms_client_id: str = ""
    ms_client_secret: str = ""
    ms_redirect_uri: str = "http://localhost:8001/auth/microsoft/callback"

    # CORS origins - configurable via WORKFLOW_CORS_ORIGINS env var (comma-separated)
    # Defaults to localhost for development
    cors_origins: str = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"

    # Redis configuration (reads from REDIS_URL, not WORKFLOW_REDIS_URL)
    redis_url: str = Field(
        default="redis://localhost:6379/0",
        validation_alias="REDIS_URL"
    )

    model_config = {
        "env_prefix": "WORKFLOW_",
        "case_sensitive": False,
    }

    @property
    def cors_origins_list(self) -> list[str]:
        """Parse CORS origins from comma-separated string to list."""
        if isinstance(self.cors_origins, str):
            return [origin.strip() for origin in self.cors_origins.split(',')]
        return self.cors_origins


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Ensure upload directory exists
def ensure_upload_dir():
    """Create upload directory if it doesn't exist."""
    settings = get_settings()
    os.makedirs(settings.upload_dir, exist_ok=True)
