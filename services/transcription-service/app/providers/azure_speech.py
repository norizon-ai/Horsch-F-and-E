"""Azure Speech Services transcription provider (stub)."""

from typing import Optional

from app.models import UnifiedTranscript
from app.providers.base import TranscriptionProvider, ProgressCallback


class AzureSpeechProvider(TranscriptionProvider):
    """Placeholder for future Azure Speech integration."""

    async def transcribe(
        self,
        file_path: str,
        language: str = "de",
        on_progress: Optional[ProgressCallback] = None,
    ) -> UnifiedTranscript:
        raise NotImplementedError(
            "Azure Speech provider is not yet implemented. "
            "Set TRANSCRIPTION_PROVIDER=whisper_local to use local Whisper."
        )
