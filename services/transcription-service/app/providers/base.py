"""Abstract base class for transcription providers."""

from abc import ABC, abstractmethod
from typing import Callable, Awaitable, Optional

from app.models import UnifiedTranscript


# Progress callback type: (stage, percent, message) -> None
ProgressCallback = Callable[[str, int, str], Awaitable[None]]


class TranscriptionProvider(ABC):
    """
    Abstract transcription provider.

    Implementations must convert an audio file to a UnifiedTranscript
    with word-level timestamps and speaker diarization.
    """

    @abstractmethod
    async def transcribe(
        self,
        file_path: str,
        language: str = "de",
        on_progress: Optional[ProgressCallback] = None,
    ) -> UnifiedTranscript:
        """
        Transcribe an audio file with speaker diarization.

        Args:
            file_path: Path to the preprocessed WAV file.
            language: ISO 639-1 language code.
            on_progress: Async callback for progress updates.

        Returns:
            UnifiedTranscript with segments, words, and speaker labels.
        """
        ...
