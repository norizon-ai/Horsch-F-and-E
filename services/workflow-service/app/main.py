"""
Workflow Service - Main FastAPI application.

This service is the frontend gateway for the meeting documentation workflow.
It orchestrates calls to the transcription-service and confluence-publisher.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import jobs, protocol, templates, transcribe, publish, users, confluence, microsoft, history

# Create FastAPI app
app = FastAPI(
    title="Workflow Service",
    description="Knowledge Transfer workflow orchestration for Norizon",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

# Include routers
app.include_router(jobs.router)
app.include_router(protocol.router)
from fastapi.staticfiles import StaticFiles

app.include_router(templates.router)
app.include_router(transcribe.router)
app.include_router(publish.router)
app.include_router(users.router)
app.include_router(confluence.router)
app.include_router(microsoft.router)
app.include_router(history.router)

import os
import logging
logger = logging.getLogger(__name__)

# Fallback create dir just in case
os.makedirs(settings.upload_dir, exist_ok=True)

from fastapi import Response

from fastapi.responses import FileResponse
import mimetypes

@app.get("/data/{file_path:path}")
async def serve_data_files(file_path: str):
    import os
    full_path = os.path.join(settings.upload_dir, file_path)
    if not os.path.exists(full_path):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="File not found")
    
    mime, _ = mimetypes.guess_type(full_path)
    return FileResponse(
        full_path, 
        media_type=mime or "application/octet-stream",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Accept-Ranges": "bytes"
        }
    )


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "service": "workflow-service",
        "use_mocks": settings.use_mocks,
    }


@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "service": "workflow-service",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }
