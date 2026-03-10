"""
Templates router - Meeting template management.
"""

from fastapi import APIRouter, HTTPException
import asyncio

from app.models import MeetingTemplate, TemplatesResponse
from app.services.job_manager import JobManager
from app.services.template_loader import get_templates, get_template_by_id, suggest_template
from app.config import get_settings

router = APIRouter(tags=["templates"])


@router.get("/jobs/{job_id}/templates", response_model=TemplatesResponse)
async def get_templates_for_job(job_id: str):
    """
    Get available templates with AI-suggested template for the job.
    The suggestion is based on transcript content analysis.
    """
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    settings = get_settings()

    if settings.use_mocks:
        # Simulate AI analysis delay
        await asyncio.sleep(0.3)

        templates = get_templates()
        suggestion = suggest_template(transcript=job.transcript)

        return TemplatesResponse(
            templates=templates,
            suggestion=suggestion,
        )

    # Real implementation would analyze the transcript
    # and suggest the most appropriate template
    templates = get_templates()
    return TemplatesResponse(templates=templates, suggestion=None)


@router.get("/templates/{template_id}", response_model=MeetingTemplate)
async def get_template(template_id: str):
    """Get a specific template by ID."""
    template = get_template_by_id(template_id)

    if template is None:
        raise HTTPException(
            status_code=404,
            detail=f"Template '{template_id}' not found"
        )

    return template


@router.get("/templates", response_model=TemplatesResponse)
async def list_templates():
    """List all available templates (without job-specific suggestion)."""
    templates = get_templates()
    return TemplatesResponse(templates=templates, suggestion=None)
