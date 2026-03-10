"""
Publish router - Confluence publishing and PDF export.
"""

from fastapi import APIRouter, HTTPException
import httpx
import asyncio
import logging
from datetime import datetime
from typing import Optional

from app.models import (
    PublishRequest,
    PublishResponse,
    ExportPdfRequest,
    ExportPdfResponse,
)
from app.services.job_manager import JobManager
from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter(tags=["publish"])


async def _publish_to_confluence(request: PublishRequest, job_id: Optional[str] = None) -> PublishResponse:
    """Internal publish logic shared by both endpoints."""
    settings = get_settings()

    if settings.use_mocks:
        await asyncio.sleep(1.0)
        page_id = f"page-{int(datetime.utcnow().timestamp() * 1000)}"
        confluence_url = f"https://confluence.example.com/pages/{page_id}"

        if job_id:
            job = JobManager.get_job(job_id)
            if job:
                job.confluence_url = confluence_url
                job.current_step = 5
                job.touch()

        return PublishResponse(
            success=True,
            confluence_url=confluence_url,
            page_id=page_id,
        )

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{settings.confluence_publisher_url}/internal/publish",
                json={
                    "protocol": request.protocol.model_dump(by_alias=True),
                    "space_key": request.space_key,
                },
                timeout=30.0,
            )
            response.raise_for_status()
            data = response.json()

            if job_id:
                job = JobManager.get_job(job_id)
                if job:
                    job.confluence_url = data.get("confluence_url")
                    job.current_step = 5
                    job.touch()

            return PublishResponse(**data)

        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Failed to publish to Confluence: {str(e)}"
            )


async def _export_pdf(request: ExportPdfRequest, job_id: Optional[str] = None):
    """Internal PDF export logic - returns PDF file directly."""
    from fastapi.responses import StreamingResponse

    settings = get_settings()

    if settings.use_mocks:
        # Mock mode: return a minimal PDF placeholder
        await asyncio.sleep(0.3)
        from io import BytesIO
        mock_pdf = BytesIO(b"%PDF-1.4\n%Mock PDF\n%%EOF")
        timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
        return StreamingResponse(
            mock_pdf,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="protocol-{timestamp}.pdf"'
            }
        )

    # Real mode: proxy the PDF from confluence-publisher
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{settings.confluence_publisher_url}/internal/export/pdf",
                json={"protocol": request.protocol.model_dump(by_alias=True)},
                timeout=30.0,
            )
            response.raise_for_status()

            # Get filename from Content-Disposition header if available
            content_disposition = response.headers.get("Content-Disposition", "")
            logger.info(f"Received Content-Disposition from confluence-publisher: {content_disposition}")

            if "filename=" in content_disposition:
                filename = content_disposition.split('filename="')[1].split('"')[0]
            else:
                timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
                filename = f"protocol-{timestamp}.pdf"

            logger.info(f"Using filename for PDF: {filename}")

            # Stream the PDF response directly to the client
            return StreamingResponse(
                response.iter_bytes(),
                media_type="application/pdf",
                headers={
                    "Content-Disposition": f'attachment; filename="{filename}"'
                }
            )

        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Failed to export PDF: {str(e)}"
            )


@router.post("/jobs/{job_id}/publish", response_model=PublishResponse)
async def publish_to_confluence_with_job(job_id: str, request: PublishRequest):
    """Publish the protocol to Confluence (job-scoped endpoint)."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    return await _publish_to_confluence(request, job_id)


@router.post("/publish", response_model=PublishResponse)
async def publish_to_confluence(request: PublishRequest):
    """Publish the protocol to Confluence."""
    return await _publish_to_confluence(request)


@router.post("/jobs/{job_id}/export/pdf")
async def export_to_pdf_with_job(job_id: str, request: ExportPdfRequest):
    """Export the protocol as a PDF (job-scoped endpoint). Returns PDF file directly."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
    return await _export_pdf(request, job_id)


@router.post("/export/pdf")
async def export_to_pdf(request: ExportPdfRequest):
    """Export the protocol as a PDF. Returns PDF file directly."""
    return await _export_pdf(request)
