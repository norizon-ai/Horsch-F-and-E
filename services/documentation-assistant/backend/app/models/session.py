from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from datetime import datetime


class DocumentType(str, Enum):
	WORK_INSTRUCTION = "work-instruction"
	ADR = "adr"
	CUSTOM = "custom"


class SessionState(str, Enum):
	TYPE_SELECTION = "type-selection"
	RECORDING = "recording"
	TRANSCRIPT_REVIEW = "transcript-review"
	AI_INTERVIEW = "ai-interview"
	DOCUMENT_REVIEW = "document-review"
	COMPLETED = "completed"


class Session(BaseModel):
	session_id: str
	author_name: str
	document_type: Optional[DocumentType] = None
	state: SessionState = SessionState.TYPE_SELECTION

	# Recording data
	audio_file_path: Optional[str] = None
	recording_duration: int = 0

	# Transcript data
	transcript: Optional[str] = None
	transcript_edited: bool = False

	# Interview data
	interview_qa: List[dict] = []
	questions_remaining: int = 0
	current_question: Optional[str] = None

	# Document data
	generated_document: Optional[dict] = None

	# Metadata
	created_at: str
	updated_at: str

	class Config:
		use_enum_values = True


class StartSessionRequest(BaseModel):
	author_name: str
	document_type: DocumentType


class ApproveTranscriptRequest(BaseModel):
	session_id: str
	edited_transcript: str


class InterviewResponseRequest(BaseModel):
	session_id: str
	answer: str


class GenerateDocumentRequest(BaseModel):
	session_id: str


class PublishDocumentRequest(BaseModel):
	session_id: str
	final_document: dict
