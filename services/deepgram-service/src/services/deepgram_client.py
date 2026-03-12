import logging
import httpx
import os
import subprocess
import tempfile
from typing import List, Optional, Dict, Any
from deepgram import DeepgramClient
from src.config import settings

logger = logging.getLogger(__name__)

# Video extensions that should have audio extracted before transcription
_VIDEO_EXTENSIONS = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".m4v"}


class DeepgramService:
    """Handles Deepgram API interactions."""
    
    def __init__(self):
        if not settings.deepgram_api_key:
            raise ValueError("DEEPGRAM_API_KEY environment variable is required")
        
        self.client = DeepgramClient(settings.deepgram_api_key)
    
    def _extract_audio(self, video_path: str) -> Optional[str]:
        """
        Extract audio track from a video file using FFmpeg.

        Returns path to a temporary WAV file, or None if extraction fails.
        The caller is responsible for deleting the temp file.
        """
        ext = os.path.splitext(video_path)[1].lower()
        if ext not in _VIDEO_EXTENSIONS:
            return None

        original_size = os.path.getsize(video_path)
        logger.info(
            f"Video file detected ({ext}, {original_size / 1024 / 1024:.1f} MB) — "
            f"extracting audio track with FFmpeg before transcription"
        )

        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp.close()

        try:
            result = subprocess.run(
                [
                    "ffmpeg", "-y",
                    "-i", video_path,
                    "-vn",              # strip video
                    "-acodec", "pcm_s16le",  # 16-bit PCM WAV
                    "-ar", "16000",     # 16 kHz — optimal for Deepgram speech
                    "-ac", "1",         # mono (Deepgram diarizes from single channel)
                    tmp.name,
                ],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode != 0:
                logger.warning(f"FFmpeg audio extraction failed: {result.stderr[:500]}")
                os.unlink(tmp.name)
                return None

            audio_size = os.path.getsize(tmp.name)
            logger.info(
                f"Audio extracted: {audio_size / 1024 / 1024:.1f} MB "
                f"(was {original_size / 1024 / 1024:.1f} MB video)"
            )
            return tmp.name

        except subprocess.TimeoutExpired:
            logger.warning("FFmpeg audio extraction timed out (120s)")
            os.unlink(tmp.name)
            return None
        except Exception as e:
            logger.warning(f"FFmpeg audio extraction error: {e}")
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)
            return None

    async def transcribe_file(self, file_path: str, glossary: Optional[List[str]] = None, language: str = "en") -> Dict[str, Any]:
        """Transcribe audio file using Deepgram API."""

        options: dict = {
            "model": settings.deepgram_model,
            "smart_format": True,
            "diarize": True,
            "utterances": True,
            "punctuate": True,
            "detect_language": True,
        }

        if glossary:
            options["keywords"] = [
                f"{term}:{settings.keyword_boost}" for term in glossary
            ]
            logger.info(f"Using {len(glossary)} glossary terms as keywords")

        # For video files, extract audio first to improve diarization accuracy
        extracted_audio = self._extract_audio(file_path)
        transcribe_path = extracted_audio or file_path

        try:
            file_size = os.path.getsize(transcribe_path)
            logger.info(f"Starting Deepgram transcription for: {transcribe_path} ({file_size} bytes)")
            with open(transcribe_path, "rb") as audio:
                payload = {"buffer": audio}

                response = self.client.listen.prerecorded.v("1").transcribe_file(
                    payload,
                    options,
                    timeout=httpx.Timeout(settings.deepgram_timeout, connect=settings.deepgram_connect_timeout)
                )

            logger.info("Deepgram transcription completed successfully")
            return response.to_dict()

        except Exception as e:
            logger.error(f"Deepgram transcription failed: {str(e)}")
            raise
        finally:
            # Clean up extracted audio temp file
            if extracted_audio and os.path.exists(extracted_audio):
                os.unlink(extracted_audio)
                logger.debug(f"Cleaned up extracted audio: {extracted_audio}")