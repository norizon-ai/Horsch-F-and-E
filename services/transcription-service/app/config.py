"""Application configuration using Pydantic Settings."""

import os

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Settings loaded from environment variables."""

    # Transcription provider
    transcription_provider: str = "whisper_local"  # whisper_local | azure_speech

    # Whisper settings
    whisper_model: str = "large-v3"
    whisper_device: str = "auto"  # auto | cpu | cuda
    whisper_compute_type: str = "auto"  # auto | int8 | float16 | float32
    default_language: str = "de"

    # CPU thread limit — prevents freezing the machine during long transcriptions.
    # Default: half of available cores. Set to 0 for unlimited (all cores).
    cpu_threads: int = max(1, os.cpu_count() // 2) if os.cpu_count() else 4

    # Pyannote diarization
    hf_token: Optional[str] = None
    diarization_model: str = "pyannote/speaker-diarization-3.1"

    # OpenAI (speaker name inference — optional)
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"
    llm_base_url: Optional[str] = None  # None = OpenAI default; set to IONOS endpoint for EU hosting
    inference_max_chars: int = 50000

    # Snippet generation
    snippet_duration_secs: float = 5.0
    snippet_max_utterances: int = 10
    snippet_text_max_chars: int = 100
    ffmpeg_timeout_secs: int = 30

    # Storage paths
    upload_dir: str = "/tmp/transcription-uploads"
    data_dir: str = "/tmp/transcription-data"

    # Processing
    max_processing_timeout: int = 14400  # 4 hours

    # Application
    app_name: str = "Nora Transcription Service"
    debug: bool = False

    model_config = {"env_file": ".env", "case_sensitive": False}


settings = Settings()
