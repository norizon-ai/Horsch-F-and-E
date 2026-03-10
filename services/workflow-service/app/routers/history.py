"""
Workflow History API endpoints.

Provides endpoints for creating, retrieving, and managing workflow history records.
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User, WorkflowHistory, Workflow
from app.db.repositories.history_repository import HistoryRepository
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/history", tags=["Workflow History"])


# =============================================================================
# Pydantic Schemas
# =============================================================================

class CreateHistoryRequest(BaseModel):
    """Request schema for creating new workflow history."""
    workflow_name: str = Field(..., description="Name of the workflow type (e.g., 'Search', 'Meeting Documentation')")
    title: str = Field(..., min_length=1, max_length=500, description="Title of the workflow session")
    payload: dict = Field(default_factory=dict, description="JSONB payload containing workflow data")


class HistoryListItem(BaseModel):
    """Schema for history list items (lightweight, no payload)."""
    id: UUID
    workflow_id: UUID
    workflow_name: str
    title: str
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True


class HistoryDetail(BaseModel):
    """Schema for full history record (includes payload)."""
    id: UUID
    user_id: UUID
    workflow_id: UUID
    workflow_name: str
    title: str
    payload: dict
    is_deleted: bool
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True


class UpdateHistoryPayloadRequest(BaseModel):
    """Request schema for updating history payload."""
    payload: dict = Field(..., description="New JSONB payload")


class UpdateHistoryTitleRequest(BaseModel):
    """Request schema for updating history title."""
    title: str = Field(..., min_length=1, max_length=500, description="New title for the history record")


class WorkflowTypeResponse(BaseModel):
    """Schema for workflow type."""
    id: UUID
    name: str
    description: str | None

    class Config:
        from_attributes = True


# =============================================================================
# Endpoints
# =============================================================================

@router.post("", response_model=HistoryDetail, status_code=status.HTTP_201_CREATED)
async def create_history(
    request: CreateHistoryRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new workflow history record.

    Protected endpoint - requires authentication.

    Args:
        request: CreateHistoryRequest with workflow_name, title, and payload
        user: Currently authenticated user
        db: Database session

    Returns:
        Created history record with full details

    Raises:
        404: If workflow type not found
    """
    repo = HistoryRepository(db)

    # Get workflow by name
    workflow = await repo.get_workflow_by_name(request.workflow_name)
    if not workflow:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workflow type '{request.workflow_name}' not found"
        )

    # Create history record
    history = await repo.create_history(
        user_id=user.id,
        workflow_id=workflow.id,
        title=request.title,
        payload=request.payload
    )

    return HistoryDetail(
        id=history.id,
        user_id=history.user_id,
        workflow_id=history.workflow_id,
        workflow_name=workflow.name,
        title=history.title,
        payload=history.payload,
        is_deleted=history.is_deleted,
        created_at=history.created_at,
        updated_at=history.updated_at
    )


@router.get("", response_model=List[HistoryListItem])
async def get_user_history(
    include_deleted: bool = False,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all workflow history for the current user.

    Returns lightweight list items (id, title, created_at) for sidebar display.
    Ordered by newest first.

    Protected endpoint - requires authentication.

    Args:
        include_deleted: Whether to include soft-deleted records (default: False)
        user: Currently authenticated user
        db: Database session

    Returns:
        List of history records (without payload for performance)
    """
    repo = HistoryRepository(db)
    histories = await repo.get_user_history(user.id, include_deleted=include_deleted)

    return [
        HistoryListItem(
            id=h.id,
            workflow_id=h.workflow_id,
            workflow_name=h.workflow.name,
            title=h.title,
            created_at=h.created_at,
            updated_at=h.updated_at
        )
        for h in histories
    ]


@router.get("/{history_id}", response_model=HistoryDetail)
async def get_history_by_id(
    history_id: str,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific workflow history record by ID.

    Returns full record including JSONB payload.

    Protected endpoint - requires authentication.
    User can only access their own history records.

    Args:
        history_id: UUID of the history record
        user: Currently authenticated user
        db: Database session

    Returns:
        Full history record with payload

    Raises:
        404: If history not found or doesn't belong to user
    """
    repo = HistoryRepository(db)
    history = await repo.get_history_by_id(history_id, user.id)

    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="History record not found or access denied"
        )

    return HistoryDetail(
        id=history.id,
        user_id=history.user_id,
        workflow_id=history.workflow_id,
        workflow_name=history.workflow.name,
        title=history.title,
        payload=history.payload,
        is_deleted=history.is_deleted,
        created_at=history.created_at,
        updated_at=history.updated_at
    )


@router.delete("/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_history(
    history_id: str,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Soft delete a workflow history record.

    Sets is_deleted=True instead of actually deleting the record.

    Protected endpoint - requires authentication.
    User can only delete their own history records.

    Args:
        history_id: UUID of the history record
        user: Currently authenticated user
        db: Database session

    Raises:
        404: If history not found or doesn't belong to user
    """
    repo = HistoryRepository(db)
    deleted = await repo.soft_delete_history(history_id, user.id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="History record not found or access denied"
        )

    return None


@router.patch("/{history_id}/payload", response_model=HistoryDetail)
async def update_history_payload(
    history_id: str,
    request: UpdateHistoryPayloadRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update the payload of an existing history record.

    Useful for updating chat history or workflow state.

    Protected endpoint - requires authentication.
    User can only update their own history records.

    Args:
        history_id: UUID of the history record
        request: New payload data
        user: Currently authenticated user
        db: Database session

    Returns:
        Updated history record

    Raises:
        404: If history not found or doesn't belong to user
    """
    repo = HistoryRepository(db)
    history = await repo.update_history_payload(history_id, user.id, request.payload)

    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="History record not found or access denied"
        )

    return HistoryDetail(
        id=history.id,
        user_id=history.user_id,
        workflow_id=history.workflow_id,
        workflow_name=history.workflow.name,
        title=history.title,
        payload=history.payload,
        is_deleted=history.is_deleted,
        created_at=history.created_at,
        updated_at=history.updated_at
    )


@router.patch("/{history_id}/title", response_model=HistoryDetail)
async def update_history_title(
    history_id: str,
    request: UpdateHistoryTitleRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update the title of an existing history record.

    Protected endpoint - requires authentication.
    User can only update their own history records.

    Args:
        history_id: UUID of the history record
        request: New title
        user: Currently authenticated user
        db: Database session

    Returns:
        Updated history record

    Raises:
        404: If history not found or doesn't belong to user
    """
    repo = HistoryRepository(db)
    history = await repo.update_history_title(history_id, user.id, request.title)

    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="History record not found or access denied"
        )

    return HistoryDetail(
        id=history.id,
        user_id=history.user_id,
        workflow_id=history.workflow_id,
        workflow_name=history.workflow.name,
        title=history.title,
        payload=history.payload,
        is_deleted=history.is_deleted,
        created_at=history.created_at,
        updated_at=history.updated_at
    )


@router.get("/workflows/types", response_model=List[WorkflowTypeResponse])
async def get_workflow_types(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all available workflow types.

    Protected endpoint - requires authentication.

    Args:
        user: Currently authenticated user
        db: Database session

    Returns:
        List of available workflow types
    """
    repo = HistoryRepository(db)
    workflows = await repo.get_all_workflows()

    return [
        WorkflowTypeResponse(
            id=w.id,
            name=w.name,
            description=w.description
        )
        for w in workflows
    ]
