import os
import aiofiles
from pathlib import Path
from app.config import settings


class FileStorage:
	"""Handle file storage for audio and other uploads"""

	@staticmethod
	async def save_document(session_id: str, file_data: bytes, filename: str) -> str:
		"""Save uploaded document file"""
		docs_dir = Path(settings.audio_storage_path).parent / "documents" / session_id
		docs_dir.mkdir(parents=True, exist_ok=True)

		file_path = docs_dir / filename

		async with aiofiles.open(file_path, 'wb') as f:
			await f.write(file_data)

		return str(file_path)

	@staticmethod
	async def save_audio(session_id: str, audio_data: bytes, filename: str = "recording.webm") -> str:
		"""Save audio file to disk"""
		# Create directory if it doesn't exist
		audio_dir = Path(settings.audio_storage_path) / session_id
		audio_dir.mkdir(parents=True, exist_ok=True)

		file_path = audio_dir / filename

		async with aiofiles.open(file_path, 'wb') as f:
			await f.write(audio_data)

		return str(file_path)

	@staticmethod
	async def read_audio(file_path: str) -> bytes:
		"""Read audio file from disk"""
		async with aiofiles.open(file_path, 'rb') as f:
			return await f.read()

	@staticmethod
	def get_audio_path(session_id: str, filename: str = "recording.webm") -> str:
		"""Get audio file path"""
		return str(Path(settings.audio_storage_path) / session_id / filename)
