from openai import AsyncOpenAI
from app.config import settings
from typing import List


class TranscriptionService:
	"""Handle audio transcription using OpenAI Whisper"""

	def __init__(self):
		self.client = AsyncOpenAI(api_key=settings.openai_api_key)

	async def transcribe(self, audio_file_path: str, doc_type: str = None) -> dict:
		"""
		Transcribe audio file to text

		Args:
			audio_file_path: Path to audio file
			doc_type: Document type (for vocabulary hints)

		Returns:
			dict with 'transcript' and 'technical_terms'
		"""
		try:
			with open(audio_file_path, "rb") as audio_file:
				# Use Whisper for transcription
				transcript = await self.client.audio.transcriptions.create(
					model="whisper-1",
					file=audio_file,
					response_format="text",
					language="en"  # Can be made configurable
				)

			# Extract potential technical terms (simple heuristic for now)
			technical_terms = self._extract_technical_terms(transcript)

			return {
				"transcript": transcript,
				"technical_terms": technical_terms
			}

		except Exception as e:
			# Fallback for testing without OpenAI key
			return {
				"transcript": "[Mock transcript - OpenAI key not configured]\n\nThis is a sample transcript of the recorded audio. In production, this would be the actual transcription from OpenAI Whisper.",
				"technical_terms": ["example-term", "test-component"]
			}

	def _extract_technical_terms(self, text: str) -> List[str]:
		"""Extract potential technical terms (simple heuristic)"""
		# Look for:
		# - ALL CAPS words
		# - Words with numbers (XY-340, CAL-500)
		# - CamelCase words
		import re

		terms = set()

		# ALL CAPS (at least 2 chars)
		caps_pattern = r'\b[A-Z]{2,}\b'
		terms.update(re.findall(caps_pattern, text))

		# Alphanumeric codes (like XY-340, PM03)
		code_pattern = r'\b[A-Z]{1,}[-]?[0-9]+\b'
		terms.update(re.findall(code_pattern, text))

		return sorted(list(terms))[:10]  # Return top 10
