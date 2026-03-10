"""
Database models for user authentication and workflow history.
"""

from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from app.db.database import Base


class User(Base):
    """User model for authentication."""

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auth0_subject = Column(String(255), unique=True, nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    name = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, auth0_subject={self.auth0_subject})>"


class Workflow(Base):
    """Workflow types (Search, Meeting Documentation, Offboarding, etc.)."""

    __tablename__ = "workflows"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # Relationship to workflow history
    histories = relationship("WorkflowHistory", back_populates="workflow")

    def __repr__(self):
        return f"<Workflow(id={self.id}, name={self.name})>"


class WorkflowHistory(Base):
    """Workflow history records for each user."""

    __tablename__ = "workflow_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    workflow_id = Column(UUID(as_uuid=True), ForeignKey("workflows.id"), nullable=False, index=True)
    title = Column(String(500), nullable=False)
    payload = Column(JSONB, nullable=False, default={})
    is_deleted = Column(Boolean, nullable=False, default=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())

    # Relationships
    user = relationship("User")
    workflow = relationship("Workflow", back_populates="histories")

    def __repr__(self):
        return f"<WorkflowHistory(id={self.id}, user_id={self.user_id}, workflow={self.workflow.name if self.workflow else 'None'}, title={self.title})>"
