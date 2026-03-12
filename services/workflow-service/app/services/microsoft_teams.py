"""
Microsoft Teams integration service.

Handles OAuth2 Authorization Code flow (delegated permissions) and
Microsoft Graph API calls to list meetings and download recordings.
"""

import secrets
import time
import logging
import json
from typing import Optional
from urllib.parse import urlencode

import httpx
import msal

from app.config import get_settings


class TokenInfo:
    """Stored OAuth2 token set for a user session."""

    __slots__ = ("access_token", "refresh_token", "expires_at", "user_name")

    def __init__(
        self,
        access_token: str,
        refresh_token: str,
        expires_at: float,
        user_name: str = "",
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_at = expires_at
        self.user_name = user_name

    @property
    def expired(self) -> bool:
        return time.time() >= self.expires_at - 60  # 60s buffer


# Graph API scopes required for Teams meeting access
GRAPH_SCOPES = [
    "User.Read",
    "OnlineMeetings.Read",
    "OnlineMeetingRecording.Read.All",
    "Calendars.Read",
    "Files.Read.All",
]

GRAPH_BASE = "https://graph.microsoft.com/v1.0"


logger = logging.getLogger(__name__)


class MicrosoftTeamsService:
    """Manages OAuth2 flow and Graph API calls for Teams meetings."""

    def __init__(self) -> None:
        self._tokens: dict[str, TokenInfo] = {}
        self._state_map: dict[str, str] = {}  # state -> session_id

    # ------------------------------------------------------------------
    # MSAL confidential client (lazy)
    # ------------------------------------------------------------------

    def _get_msal_app(self) -> msal.ConfidentialClientApplication:
        settings = get_settings()
        authority = f"https://login.microsoftonline.com/{settings.ms_tenant_id}"
        return msal.ConfidentialClientApplication(
            client_id=settings.ms_client_id,
            client_credential=settings.ms_client_secret,
            authority=authority,
        )

    # ------------------------------------------------------------------
    # OAuth2 Authorization Code flow
    # ------------------------------------------------------------------

    def build_auth_url(self) -> tuple[str, str]:
        """Build Microsoft login URL. Returns (auth_url, state)."""
        settings = get_settings()
        app = self._get_msal_app()
        state = secrets.token_urlsafe(32)
        session_id = secrets.token_urlsafe(32)
        self._state_map[state] = session_id

        flow = app.initiate_auth_code_flow(
            scopes=GRAPH_SCOPES,
            redirect_uri=settings.ms_redirect_uri,
            state=state,
        )
        # Store the flow so we can complete it in the callback
        self._state_map[f"flow:{state}"] = flow  # type: ignore[assignment]
        return flow["auth_uri"], state

    async def handle_callback(self, code: str, state: str) -> Optional[str]:
        """Exchange authorization code for tokens.

        Returns session_id on success, None on failure.
        """
        flow = self._state_map.pop(f"flow:{state}", None)
        session_id = self._state_map.pop(state, None)
        if not flow or not session_id:
            return None

        app = self._get_msal_app()
        result = app.acquire_token_by_auth_code_flow(
            auth_code_flow=flow,
            auth_response={"code": code, "state": state},
        )

        if "access_token" not in result:
            return None

        expires_in = result.get("expires_in", 3600)
        user_name = result.get("id_token_claims", {}).get("name", "")

        self._tokens[session_id] = TokenInfo(
            access_token=result["access_token"],
            refresh_token=result.get("refresh_token", ""),
            expires_at=time.time() + expires_in,
            user_name=user_name,
        )
        return session_id

    def get_session(self, session_id: str) -> Optional[TokenInfo]:
        """Return token info for a session, or None."""
        return self._tokens.get(session_id)

    def remove_session(self, session_id: str) -> None:
        """Remove stored tokens for a session."""
        self._tokens.pop(session_id, None)

    async def _get_access_token(self, session_id: str) -> Optional[str]:
        """Get a valid access token, refreshing if needed."""
        token = self._tokens.get(session_id)
        if not token:
            return None

        if not token.expired:
            return token.access_token

        # Attempt silent refresh via MSAL
        if token.refresh_token:
            app = self._get_msal_app()
            result = app.acquire_token_by_refresh_token(
                token.refresh_token,
                scopes=GRAPH_SCOPES,
            )
            if "access_token" in result:
                token.access_token = result["access_token"]
                token.refresh_token = result.get("refresh_token", token.refresh_token)
                token.expires_at = time.time() + result.get("expires_in", 3600)
                return token.access_token

        # Refresh failed — remove session
        self._tokens.pop(session_id, None)
        return None

    # ------------------------------------------------------------------
    # Graph API helpers
    # ------------------------------------------------------------------

    async def _graph_get(self, session_id: str, path: str, params: dict | None = None) -> dict | None:
        """Make an authenticated GET request to Microsoft Graph."""
        access_token = await self._get_access_token(session_id)
        if not access_token:
            return None

        url = f"{GRAPH_BASE}{path}"
        if params:
            url = f"{url}?{urlencode(params)}"

        async with httpx.AsyncClient() as client:
            resp = await client.get(
                url,
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=30.0,
            )
            if resp.status_code == 200:
                return resp.json()
            
            # Log error response for debugging
            try:
                error_data = resp.json()
                logger.error(f"Graph API Error ({resp.status_code}) on {path}: {json.dumps(error_data)}")
            except Exception:
                logger.error(f"Graph API Error ({resp.status_code}) on {path}: {resp.text}")
            
            return None

    async def get_attendee_details(self, session_id: str, attendees: list[dict]) -> list[dict]:
        """Enrich attendee list with profile photos from Microsoft Graph.

        Args:
            session_id: User session ID
            attendees: List of attendee dicts with 'email' field

        Returns:
            Enriched attendee list with profilePhotoUrl field
        """
        access_token = await self._get_access_token(session_id)
        if not access_token:
            return attendees

        enriched = []
        async with httpx.AsyncClient() as client:
            for attendee in attendees:
                email = attendee.get("email", "")
                enriched_attendee = attendee.copy()

                if email:
                    # Try to get user photo - this may fail if photo doesn't exist
                    try:
                        photo_url = f"{GRAPH_BASE}/users/{email}/photo/$value"
                        resp = await client.get(
                            photo_url,
                            headers={"Authorization": f"Bearer {access_token}"},
                            timeout=10.0,
                        )
                        if resp.status_code == 200:
                            # Convert photo to base64 data URL
                            import base64
                            photo_bytes = resp.content
                            photo_b64 = base64.b64encode(photo_bytes).decode('utf-8')
                            enriched_attendee["profilePhotoUrl"] = f"data:image/jpeg;base64,{photo_b64}"
                    except Exception:
                        # Photo fetch failed - that's okay, not all users have photos
                        pass

                enriched.append(enriched_attendee)

        return enriched

    # ------------------------------------------------------------------
    # Teams Meetings
    # ------------------------------------------------------------------

    async def list_meetings(self, session_id: str) -> list[dict]:
        """List recent Teams meetings with recording info.

        Uses calendar events as the primary source (better titles/dates),
        falling back to onlineMeetings endpoint.
        Returns the last 5 meetings with detailed attendee information.
        """
        meetings: list[dict] = []

        # Filter events to those that started in the last 30 days and up to now
        from datetime import datetime, timedelta, timezone
        start_date = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
        end_date = datetime.now(timezone.utc).isoformat()

        # Try calendar events with online meetings first
        events = await self._graph_get(
            session_id,
            "/me/events",
            {
                "$filter": f"start/dateTime ge '{start_date}' and start/dateTime le '{end_date}'",
                "$top": "30",
                "$orderby": "start/dateTime desc",
                "$select": "id,subject,start,end,attendees,onlineMeeting,organizer",
            },
        )

        # Also search for recordings directly in OneDrive as a fallback/supplement
        # Broaden the search to look for .mp4 files in the Recordings folder
        recordings_files = await self._graph_get(
            session_id,
            "/me/drive/root/search(q='.mp4')",
        )

        if recordings_files and "value" in recordings_files:
            for file in recordings_files["value"]:
                # Map file to a "meeting-like" object
                meetings.append({
                    "id": file.get("id"),
                    "meetingId": None,
                    "subject": file.get("name", "Recording"),
                    "startDateTime": file.get("createdDateTime", ""),
                    "endDateTime": file.get("lastModifiedDateTime", ""),
                    "attendees": [],
                    "attendeeCount": 0,
                    "hasRecording": True,
                    "recordingId": file.get("id"),
                    "recordingDuration": None,
                    "organizerName": "OneDrive",
                    "organizerEmail": "",
                    "isDirectFile": True
                })

        if events and "value" in events:
            for event in events["value"]:
                join_url = (event.get("onlineMeeting") or {}).get("joinUrl", "")
                meeting_id = await self._resolve_meeting_id(session_id, join_url)
                recording_info = None
                if meeting_id:
                    recording_info = await self._get_recording_info(session_id, meeting_id)

                # Parse attendees with detailed information
                attendees = []
                for attendee in event.get("attendees", []):
                    email_address = attendee.get("emailAddress", {})
                    attendees.append({
                        "name": email_address.get("name", "Unknown"),
                        "email": email_address.get("address", ""),
                        "type": attendee.get("type", "required"),  # required, optional, resource
                    })

                organizer = event.get("organizer", {}).get("emailAddress", {})

                meetings.append({
                    "id": meeting_id or event["id"],
                    "meetingId": meeting_id,  # Explicit meeting ID for API calls
                    "subject": event.get("subject", "Untitled Meeting"),
                    "startDateTime": event.get("start", {}).get("dateTime", ""),
                    "endDateTime": event.get("end", {}).get("dateTime", ""),
                    "attendees": attendees,
                    "attendeeCount": len(attendees),
                    "hasRecording": recording_info is not None,
                    "recordingId": recording_info.get("id") if recording_info else None,
                    "recordingDuration": recording_info.get("recordingDuration") if recording_info else None,
                    "organizerName": organizer.get("name", ""),
                    "organizerEmail": organizer.get("address", ""),
                })

                # Stop after collecting 5 meetings (to limit response size)
                if len(meetings) >= 5:
                    break

        return meetings

    async def _resolve_meeting_id(self, session_id: str, join_url: str) -> Optional[str]:
        """Resolve a join URL to an onlineMeeting ID."""
        if not join_url:
            return None

        result = await self._graph_get(
            session_id,
            "/me/onlineMeetings",
            {"$filter": f"joinWebUrl eq '{join_url}'"},
        )
        if result and result.get("value"):
            return result["value"][0].get("id")
        return None

    async def _get_recording_info(self, session_id: str, meeting_id: str) -> Optional[dict]:
        """Check if a meeting has recordings. Returns first recording info or None."""
        result = await self._graph_get(
            session_id,
            f"/me/onlineMeetings/{meeting_id}/recordings",
        )
        if result and result.get("value"):
            return result["value"][0]
        return None

    async def _find_recording_in_onedrive(self, session_id: str, meeting_subject: str) -> Optional[str]:
        """Search OneDrive for a Teams recording matching the meeting subject.

        Teams saves recordings to the organizer's OneDrive. Only returns a match
        if the filename clearly matches the meeting subject (no guessing).
        """
        if not meeting_subject:
            return None

        # Search for .mp4 files — Teams recordings are always mp4
        result = await self._graph_get(
            session_id,
            "/me/drive/root/search(q='.mp4')",
        )
        if not result or "value" not in result:
            return None

        # Only match if the meeting subject appears in the filename
        # Teams names recordings like "Meeting Subject-20240214_100000-Recording.mp4"
        for file in result["value"]:
            name = file.get("name", "")
            if meeting_subject.lower() in name.lower():
                logger.info(f"Found OneDrive recording match: {name}")
                return file["id"]

        logger.info(f"No OneDrive recording found matching subject: {meeting_subject}")
        return None

    async def download_recording(
        self,
        session_id: str,
        meeting_id: str,
        recording_id: str,
        dest_path: str,
        meeting_subject: str = "",
    ) -> bool:
        """Download a meeting recording to a local file.

        Tries the onlineMeetings recordings API first, falls back to
        OneDrive download if that returns 403 (common with delegated permissions).

        Returns True on success.
        """
        access_token = await self._get_access_token(session_id)
        if not access_token:
            return False

        if not meeting_id:
            # Direct OneDrive File (recording_id is the driveItem id)
            url = f"{GRAPH_BASE}/me/drive/items/{recording_id}/content"
            return await self._stream_download(access_token, url, dest_path)

        # Try the recordings API first
        url = f"{GRAPH_BASE}/me/onlineMeetings/{meeting_id}/recordings/{recording_id}/content"
        success = await self._stream_download(access_token, url, dest_path)

        if not success:
            # Fallback: download from OneDrive where Teams saves recordings
            logger.info("Recordings API failed, trying OneDrive fallback...")
            drive_item_id = await self._find_recording_in_onedrive(session_id, meeting_subject)
            if drive_item_id:
                url = f"{GRAPH_BASE}/me/drive/items/{drive_item_id}/content"
                success = await self._stream_download(access_token, url, dest_path)

        return success

    async def _stream_download(self, access_token: str, url: str, dest_path: str) -> bool:
        """Stream-download a file from a URL with Bearer auth."""
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "GET",
                url,
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=600.0,
                follow_redirects=True,
            ) as resp:
                if resp.status_code != 200:
                    error_body = await resp.aread()
                    logger.error(
                        f"Download failed ({resp.status_code}) for {url}: "
                        f"{error_body.decode('utf-8', errors='replace')[:1000]}"
                    )
                    return False
                with open(dest_path, "wb") as f:
                    async for chunk in resp.aiter_bytes(chunk_size=131072):
                        f.write(chunk)
        return True


# Module-level singleton
teams_service = MicrosoftTeamsService()
