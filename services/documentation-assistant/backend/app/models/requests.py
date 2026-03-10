from pydantic import BaseModel
from typing import Optional, Dict, Any


class StartSessionRequest(BaseModel):
	"""Request to start a new documentation session"""
	author_name: str
	document_type: str


class ApproveTranscriptRequest(BaseModel):
	"""Request to approve/edit transcript and start AI interview"""
	session_id: str
	edited_transcript: str


class InterviewResponseRequest(BaseModel):
	"""Request to submit answer to interview question"""
	session_id: str
	answer: str


class GenerateDocumentRequest(BaseModel):
	"""Request to generate final document"""
	session_id: str


class PublishDocumentRequest(BaseModel):
	"""Request to publish document to knowledge base"""
	session_id: str
	final_document: Dict[str, Any]
