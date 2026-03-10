"""
Confluence Publisher - Configuration.

Settings loaded from environment variables with PUBLISHER_ prefix.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Publisher service configuration."""

    mcp_server_url: str = "http://localhost:8005"

    model_config = SettingsConfigDict(env_prefix="PUBLISHER_")


_settings: Settings | None = None


def get_settings() -> Settings:
    """Get cached settings instance."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
