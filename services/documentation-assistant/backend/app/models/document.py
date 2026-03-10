from pydantic import BaseModel
from typing import List, Optional
from .session import DocumentType


class DocumentMetadata(BaseModel):
	author: str
	doc_type: DocumentType
	created_at: str
	status: str = "draft"


class GeneratedDocument(BaseModel):
	id: str
	title: str
	content: str
	metadata: DocumentMetadata
	sections: Optional[List[dict]] = None
	safety_warnings: Optional[List[str]] = None
	prerequisites: Optional[List[str]] = None
	steps: Optional[List[dict]] = None
	troubleshooting: Optional[List[dict]] = None
