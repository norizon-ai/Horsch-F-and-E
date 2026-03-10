import uuid
from datetime import datetime
from typing import Dict, Optional
from app.models import Session, SessionState, DocumentType


class SessionManager:
	"""In-memory session storage (for simplicity - can be replaced with Redis/DB later)"""

	_sessions: Dict[str, Session] = {}

	@classmethod
	def create_session(cls, author_name: str, document_type: DocumentType) -> Session:
		"""Create a new documentation session"""
		session_id = str(uuid.uuid4())
		now = datetime.utcnow().isoformat()

		session = Session(
			session_id=session_id,
			author_name=author_name,
			document_type=document_type,
			state=SessionState.RECORDING,
			created_at=now,
			updated_at=now
		)

		cls._sessions[session_id] = session
		return session

	@classmethod
	def get_session(cls, session_id: str) -> Optional[Session]:
		"""Get session by ID"""
		return cls._sessions.get(session_id)

	@classmethod
	def update_session(cls, session_id: str, **kwargs) -> Session:
		"""Update session fields"""
		session = cls.get_session(session_id)
		if not session:
			raise ValueError(f"Session {session_id} not found")

		# Update fields
		for key, value in kwargs.items():
			if hasattr(session, key):
				setattr(session, key, value)

		# Update timestamp
		session.updated_at = datetime.utcnow().isoformat()

		cls._sessions[session_id] = session
		return session

	@classmethod
	def delete_session(cls, session_id: str):
		"""Delete a session"""
		if session_id in cls._sessions:
			del cls._sessions[session_id]

	@classmethod
	def get_all_sessions(cls) -> Dict[str, Session]:
		"""Get all sessions (for debugging)"""
		return cls._sessions
