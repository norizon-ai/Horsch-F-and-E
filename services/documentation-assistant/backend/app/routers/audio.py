from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from app.storage.session_manager import SessionManager
from app.storage.file_storage import FileStorage
from app.services.transcription import TranscriptionService
from app.services.document_processor import DocumentProcessor
from app.models import SessionState

router = APIRouter(prefix="/api/audio", tags=["audio"])

# Initialize services
transcription_service = TranscriptionService()
document_processor = DocumentProcessor()


@router.post("/upload")
async def upload_audio(session_id: str, audio: UploadFile = File(...)):
	"""Upload audio recording"""
	session = SessionManager.get_session(session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	# Read audio file
	audio_data = await audio.read()

	# Save to disk
	file_path = await FileStorage.save_audio(
		session_id=session_id,
		audio_data=audio_data,
		filename=audio.filename or "recording.webm"
	)

	# Update session
	SessionManager.update_session(
		session_id,
		audio_file_path=file_path,
		state=SessionState.TRANSCRIPT_REVIEW
	)

	return {
		"status": "uploaded",
		"file_path": file_path
	}


@router.get("/transcribe/{session_id}")
async def transcribe_audio(session_id: str):
	"""Transcribe audio file"""
	session = SessionManager.get_session(session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	if not session.audio_file_path:
		raise HTTPException(status_code=400, detail="No audio file found for this session")

	# Transcribe
	result = await transcription_service.transcribe(
		audio_file_path=session.audio_file_path,
		doc_type=session.document_type
	)

	# Update session with transcript
	SessionManager.update_session(
		session_id,
		transcript=result["transcript"]
	)

	return result


@router.post("/upload-documents")
async def upload_documents(session_id: str, files: List[UploadFile] = File(...)):
	"""Upload reference documents for context"""
	session = SessionManager.get_session(session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	uploaded_file_paths = []

	for file in files:
		# Read file data
		file_data = await file.read()

		# Save to disk
		file_path = await FileStorage.save_document(
			session_id=session_id,
			file_data=file_data,
			filename=file.filename or "document"
		)

		uploaded_file_paths.append(file_path)

	# Process documents and extract text
	combined_content = await document_processor.process_multiple_files(uploaded_file_paths)

	# Store in session metadata
	SessionManager.update_session(
		session_id,
		uploaded_files=uploaded_file_paths,
		reference_content=combined_content
	)

	return {
		"status": "uploaded",
		"files_count": len(uploaded_file_paths),
		"file_paths": uploaded_file_paths
	}
