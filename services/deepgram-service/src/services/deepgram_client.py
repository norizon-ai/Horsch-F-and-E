import logging
import httpx
import os
from typing import List, Optional, Dict, Any
from deepgram import DeepgramClient
from src.config import settings

logger = logging.getLogger(__name__)


class DeepgramService:
    """Handles Deepgram API interactions."""
    
    def __init__(self):
        if not settings.deepgram_api_key:
            raise ValueError("DEEPGRAM_API_KEY environment variable is required")
        
        self.client = DeepgramClient(settings.deepgram_api_key)
    
    async def transcribe_file(self, file_path: str, glossary: Optional[List[str]] = None, language: str = "en") -> Dict[str, Any]:
        """Transcribe audio file using Deepgram API."""

        options: dict = {
            "model": settings.deepgram_model,
            "smart_format": True,
            "diarize": True,
            "utterances": True,
            "punctuate": True,
            "language": language if language in ["de", "en"] else "en"
        }

        if glossary:
            options["keywords"] = [
                f"{term}:{settings.keyword_boost}" for term in glossary
            ]
            logger.info(f"Using {len(glossary)} glossary terms as keywords")
        
        try:
            file_size = os.path.getsize(file_path)
            logger.info(f"Starting Deepgram transcription for: {file_path} ({file_size} bytes)")
            with open(file_path, "rb") as audio:
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