"""Data models matching kstudio/workflow-service API contract."""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Word(BaseModel):
    """Word-level timestamp."""
    word: str
    start: float
    end: float
    speaker: str


class Segment(BaseModel):
    """Utterance/segment with speaker attribution."""
    start: float
    end: float
    text: str
    speaker: str


class UnifiedTranscript(BaseModel):
    """
    Common Data Format (CDF) for transcription output.
    Must match kstudio schema for frontend compatibility.
    """
    text: str
    segments: List[Segment]
    word_timestamps: List[Word]
    engine_used: str


class Speaker(BaseModel):
    """Speaker model matching workflow-service expectations."""
    id: str
    detected_name: str = Field(alias="detectedName")
    confirmed_name: str = Field(default="", alias="confirmedName")
    sample_audio_url: Optional[str] = Field(None, alias="sampleAudioUrl")
    speaking_time: Optional[int] = Field(None, alias="speakingTime")
    transcript_snippet: Optional[str] = Field(None, alias="transcriptSnippet")
    confidence: Optional[float] = None
    is_external: Optional[bool] = Field(None, alias="isExternal")
    waveform_data: Optional[List[float]] = Field(None, alias="waveformData")
    hint: Optional[str] = None

    model_config = {"populate_by_name": True}


class ProcessRequest(BaseModel):
    """Request to process an audio file."""
    file_path: str
    glossary: List[str] = []
    language: str = "de"
    tenant_id: Optional[str] = None


class SpeakersResponse(BaseModel):
    """Response containing list of detected speakers."""
    speakers: List[Speaker]


class TranscriptionUsageEvent(BaseModel):
    """Structured usage event for billing/analytics pipeline."""
    tenant_id: Optional[str]
    job_id: str
    duration_seconds: float
    language: str
    provider: str
    speaker_count: int
    timestamp: datetime
