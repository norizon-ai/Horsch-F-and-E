"""Transcription provider factory."""

from app.config import settings
from app.providers.base import TranscriptionProvider


def get_provider() -> TranscriptionProvider:
    """Return the configured transcription provider."""
    provider = settings.transcription_provider.lower()

    if provider == "whisper_local":
        from app.providers.whisper_local import WhisperLocalProvider
        return WhisperLocalProvider()
    elif provider == "azure_speech":
        from app.providers.azure_speech import AzureSpeechProvider
        return AzureSpeechProvider()
    else:
        raise ValueError(f"Unknown transcription provider: {provider}")
