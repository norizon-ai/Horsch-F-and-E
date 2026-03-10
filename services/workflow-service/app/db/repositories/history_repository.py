"""
Repository for workflow history database operations.
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.db.models import WorkflowHistory, Workflow


class HistoryRepository:
    """Repository for workflow history CRUD operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_history(
        self,
        user_id: UUID,
        workflow_id: UUID,
        title: str,
        payload: dict
    ) -> WorkflowHistory:
        """
        Create a new workflow history record.

        Args:
            user_id: UUID of the user
            workflow_id: UUID of the workflow type
            title: Title of the workflow session
            payload: JSONB payload containing workflow data

        Returns:
            Created WorkflowHistory object
        """
        history = WorkflowHistory(
            user_id=user_id,
            workflow_id=workflow_id,
            title=title,
            payload=payload,
            is_deleted=False
        )

        self.db.add(history)
        await self.db.commit()
        await self.db.refresh(history)

        return history

    async def get_user_history(
        self,
        user_id: UUID,
        include_deleted: bool = False
    ) -> List[WorkflowHistory]:
        """
        Get all workflow history for a user.

        Args:
            user_id: UUID of the user
            include_deleted: Whether to include soft-deleted records

        Returns:
            List of WorkflowHistory objects, ordered by created_at DESC
        """
        query = (
            select(WorkflowHistory)
            .options(joinedload(WorkflowHistory.workflow))
            .where(WorkflowHistory.user_id == user_id)
        )

        if not include_deleted:
            query = query.where(WorkflowHistory.is_deleted == False)

        query = query.order_by(WorkflowHistory.created_at.desc())

        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_history_by_id(
        self,
        history_id: UUID,
        user_id: UUID
    ) -> Optional[WorkflowHistory]:
        """
        Get a specific workflow history record by ID.

        Ensures the record belongs to the specified user to prevent data leaks.

        Args:
            history_id: UUID of the history record
            user_id: UUID of the user (for access control)

        Returns:
            WorkflowHistory object or None if not found or user doesn't match
        """
        query = (
            select(WorkflowHistory)
            .options(joinedload(WorkflowHistory.workflow))
            .where(
                and_(
                    WorkflowHistory.id == history_id,
                    WorkflowHistory.user_id == user_id,
                    WorkflowHistory.is_deleted == False
                )
            )
        )

        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def soft_delete_history(
        self,
        history_id: UUID,
        user_id: UUID
    ) -> bool:
        """
        Soft delete a workflow history record.

        Sets is_deleted=True instead of actually deleting the record.

        Args:
            history_id: UUID of the history record
            user_id: UUID of the user (for access control)

        Returns:
            True if deleted, False if not found or user doesn't match
        """
        query = (
            select(WorkflowHistory)
            .where(
                and_(
                    WorkflowHistory.id == history_id,
                    WorkflowHistory.user_id == user_id,
                    WorkflowHistory.is_deleted == False
                )
            )
        )

        result = await self.db.execute(query)
        history = result.scalar_one_or_none()

        if not history:
            return False

        history.is_deleted = True
        await self.db.commit()

        return True

    async def update_history_payload(
        self,
        history_id: UUID,
        user_id: UUID,
        payload: dict
    ) -> Optional[WorkflowHistory]:
        """
        Update the payload of an existing history record.

        Useful for updating chat history or workflow state.

        Args:
            history_id: UUID of the history record
            user_id: UUID of the user (for access control)
            payload: New JSONB payload

        Returns:
            Updated WorkflowHistory object or None if not found
        """
        query = (
            select(WorkflowHistory)
            .options(joinedload(WorkflowHistory.workflow))
            .where(
                and_(
                    WorkflowHistory.id == history_id,
                    WorkflowHistory.user_id == user_id,
                    WorkflowHistory.is_deleted == False
                )
            )
        )

        result = await self.db.execute(query)
        history = result.scalar_one_or_none()

        if not history:
            return None

        history.payload = payload
        await self.db.commit()
        await self.db.refresh(history)

        return history

    async def update_history_title(
        self,
        history_id: UUID,
        user_id: UUID,
        title: str
    ) -> Optional[WorkflowHistory]:
        """
        Update the title of an existing history record.

        Args:
            history_id: UUID of the history record
            user_id: UUID of the user (for access control)
            title: New title

        Returns:
            Updated WorkflowHistory object or None if not found
        """
        query = (
            select(WorkflowHistory)
            .options(joinedload(WorkflowHistory.workflow))
            .where(
                and_(
                    WorkflowHistory.id == history_id,
                    WorkflowHistory.user_id == user_id,
                    WorkflowHistory.is_deleted == False
                )
            )
        )

        result = await self.db.execute(query)
        history = result.scalar_one_or_none()

        if not history:
            return None

        history.title = title
        await self.db.commit()
        await self.db.refresh(history)

        return history

    async def get_workflow_by_name(self, name: str) -> Optional[Workflow]:
        """
        Get a workflow type by name.

        Args:
            name: Name of the workflow (e.g., "Search", "Meeting Documentation")

        Returns:
            Workflow object or None if not found
        """
        query = select(Workflow).where(Workflow.name == name)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_all_workflows(self) -> List[Workflow]:
        """
        Get all available workflow types.

        Returns:
            List of Workflow objects
        """
        query = select(Workflow).order_by(Workflow.name)
        result = await self.db.execute(query)
        return list(result.scalars().all())
