"""
Microsoft Teams authentication and meeting import endpoints.

Provides OAuth2 Authorization Code flow for delegated Microsoft Graph
permissions, meeting listing, and recording download/import.
"""

import os
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.config import get_settings, ensure_upload_dir
from app.services.microsoft_teams import teams_service
from app.services.job_manager import JobManager

router = APIRouter(tags=["microsoft"])

SESSION_COOKIE = "ms_session"


def _get_session_id(request: Request) -> str | None:
    return request.cookies.get(SESSION_COOKIE)


def _is_configured() -> bool:
    settings = get_settings()
    return bool(settings.ms_client_id and settings.ms_tenant_id)


# ------------------------------------------------------------------
# OAuth2 flow
# ------------------------------------------------------------------


@router.get("/auth/microsoft/login")
async def microsoft_login():
    """Return the Microsoft authorization URL for the frontend to open in a popup."""
    if not _is_configured():
        raise HTTPException(status_code=501, detail="Microsoft integration not configured")

    auth_url, _state = teams_service.build_auth_url()
    return {"auth_url": auth_url}


@router.get("/auth/microsoft/callback", response_class=HTMLResponse)
async def microsoft_callback(request: Request, code: str, state: str):
    """OAuth2 callback. Exchanges code for tokens and closes the popup."""
    session_id = await teams_service.handle_callback(code, state)

    if not session_id:
        return HTMLResponse(
            content=_popup_html(success=False),
            status_code=200,
        )

    response = HTMLResponse(content=_popup_html(success=True))
    response.set_cookie(
        key=SESSION_COOKIE,
        value=session_id,
        httponly=True,
        samesite="lax",
        max_age=3600,
    )
    return response


@router.get("/auth/microsoft/status")
async def microsoft_status(request: Request):
    """Check if the current session has valid Microsoft tokens."""
    if not _is_configured():
        return {"connected": False, "configured": False}

    session_id = _get_session_id(request)
    if not session_id:
        return {"connected": False, "configured": True}

    token = teams_service.get_session(session_id)
    if not token:
        return {"connected": False, "configured": True}

    return {
        "connected": True,
        "configured": True,
        "userName": token.user_name,
        "expiresAt": token.expires_at,
    }


@router.delete("/auth/microsoft/logout")
async def microsoft_logout(request: Request, response: Response):
    """Clear stored tokens for the current session."""
    session_id = _get_session_id(request)
    if session_id:
        teams_service.remove_session(session_id)
    response.delete_cookie(SESSION_COOKIE)
    return {"success": True}


# ------------------------------------------------------------------
# Teams meetings
# ------------------------------------------------------------------


@router.get("/teams/meetings")
async def list_meetings(request: Request, include_photos: bool = False):
    """
    List recent Teams meetings with recording info.

    Args:
        include_photos: If True, fetch profile photos for attendees (slower)

    Returns last 5 meetings with:
    - Meeting title, date/time, participants
    - Recording availability and IDs
    - Organizer information
    - Optional: Attendee profile photos (base64 encoded)
    """
    session_id = _get_session_id(request)
    if not session_id:
        raise HTTPException(status_code=401, detail="Not authenticated with Microsoft")

    token = teams_service.get_session(session_id)
    if not token:
        raise HTTPException(status_code=401, detail="Session expired")

    meetings = await teams_service.list_meetings(session_id)

    # Optionally enrich with profile photos
    if include_photos:
        for meeting in meetings:
            attendees = meeting.get("attendees", [])
            if attendees:
                enriched_attendees = await teams_service.get_attendee_details(
                    session_id, attendees
                )
                meeting["attendees"] = enriched_attendees

    return {"meetings": meetings, "connected": True}


# ------------------------------------------------------------------
# Recording import
# ------------------------------------------------------------------


class ImportRecordingRequest(BaseModel):
    meeting_id: str
    recording_id: str
    meeting_subject: str = ""
    meeting_start: str = ""
    attendees: list[dict] = []  # List of {name, email, profilePhotoUrl} from Teams


@router.post("/jobs/{job_id}/import-teams-recording")
async def import_teams_recording(job_id: str, body: ImportRecordingRequest, request: Request):
    """Download a Teams recording and attach it to the job.

    Re-uses the existing JobManager.set_file_info() and KStudio trigger
    logic from the upload endpoint.
    """
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    session_id = _get_session_id(request)
    if not session_id:
        raise HTTPException(status_code=401, detail="Not authenticated with Microsoft")

    settings = get_settings()
    ensure_upload_dir()

    # Teams recordings are typically mp4
    file_ext = ".mp4"
    file_path = os.path.join(settings.upload_dir, f"{job_id}{file_ext}")

    success = await teams_service.download_recording(
        session_id=session_id,
        meeting_id=body.meeting_id,
        recording_id=body.recording_id,
        dest_path=file_path,
        meeting_subject=body.meeting_subject,
    )

    if not success:
        raise HTTPException(
            status_code=403,
            detail="Sorry, recording download denied. Only the meeting organizer can download recordings. Ask the organizer to export and share the file.",
        )

    file_size = os.path.getsize(file_path)
    file_name = f"{body.meeting_subject or 'Teams Recording'}.mp4"

    # Estimate duration (rough: ~1MB per minute for video)
    duration_seconds = max(60, int(file_size / 1_000_000 * 60))

    # Parse recording date from meeting_start (ISO 8601 format: 2024-02-14T10:00:00)
    recording_date = body.meeting_start or datetime.utcnow().isoformat()

    JobManager.set_file_info(
        job_id=job_id,
        file_path=file_path,
        file_name=file_name,
        file_size=file_size,
        duration_seconds=duration_seconds,
    )

    # Store Teams import metadata (attendees, recording date)
    JobManager.update_job(
        job_id=job_id,
        teams_import=True,
        recording_date=recording_date,
        teams_attendees=body.attendees,
    )

    # Processing is triggered separately by the user clicking "Start Processing"

    return {
        "success": True,
        "file_id": f"file-{job_id}",
        "file_size": file_size,
        "duration_seconds": duration_seconds,
        "skip_speaker_verification": True,  # Teams provides speaker identities
        "recording_date": recording_date,
        "attendees": body.attendees,
    }


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def _popup_html(success: bool) -> str:
    """HTML page that notifies the opener window and closes the popup."""
    status = "success" if success else "error"
    return f"""<!DOCTYPE html>
<html>
<head><title>Microsoft Login</title></head>
<body>
<script>
  if (window.opener) {{
    window.opener.postMessage({{ type: 'ms-auth', status: '{status}' }}, '*');
  }}
  window.close();
</script>
<p>{"Sign-in successful. This window will close." if success else "Sign-in failed. Please close this window and try again."}</p>
</body>
</html>"""
