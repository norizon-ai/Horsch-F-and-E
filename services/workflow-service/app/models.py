"""
Pydantic models for the Workflow Service API.
These models match the frontend TypeScript types in src/lib/types/index.ts
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any
from datetime import datetime


# ============================================================================
# Speaker Models
# ============================================================================

class Speaker(BaseModel):
    """Detected speaker from audio transcription."""
    id: str
    detected_name: str = Field(alias="detectedName")
    confirmed_name: str = Field(default="", alias="confirmedName")
    sample_audio_url: Optional[str] = Field(None, alias="sampleAudioUrl")
    speaking_time: Optional[int] = Field(None, alias="speakingTime")
    transcript_snippet: Optional[str] = Field(None, alias="transcriptSnippet")
    confidence: Optional[float] = None
    is_external: Optional[bool] = Field(None, alias="isExternal")
    waveform_data: Optional[List[float]] = Field(None, alias="waveformData")

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "id": "speaker-1",
                "detectedName": "Sprecher 1",
                "confirmedName": "Max Mustermann",
                "speakingTime": 245
            }
        }
    }


class SpeakersResponse(BaseModel):
    """Response containing list of detected speakers."""
    speakers: List[Speaker]


class UpdateSpeakersRequest(BaseModel):
    """Request to update speaker names."""
    speakers: List[Speaker]


# ============================================================================
# Action Item & Protocol Models
# ============================================================================

class ActionItem(BaseModel):
    """Action item from meeting protocol."""
    id: str
    text: str
    assignee: Optional[str] = None
    due_date: Optional[str] = Field(None, alias="dueDate")
    completed: bool = False

    model_config = {"populate_by_name": True}


class TranscriptSegment(BaseModel):
    """Individual segment of the transcript with speaker attribution."""
    id: str
    speaker_id: str = Field(alias="speakerId")
    speaker_name: str = Field(alias="speakerName")
    start_time: float = Field(alias="startTime")
    end_time: float = Field(alias="endTime")
    text: str

    model_config = {"populate_by_name": True}


class CustomSection(BaseModel):
    """Template-specific custom section with content."""
    id: str
    label: str
    type: Literal["text", "list"] = "text"
    content: Any  # string for text, List[str] for list

    model_config = {"populate_by_name": True}


class Protocol(BaseModel):
    """Generated meeting protocol."""
    title: str
    date: str
    attendees: List[str]
    executive_summary: str = Field(alias="executiveSummary")
    action_items: List[ActionItem] = Field(alias="actionItems")
    full_transcript: str = Field(alias="fullTranscript")
    transcript_segments: Optional[List[TranscriptSegment]] = Field(None, alias="transcriptSegments")
    decisions: Optional[List[str]] = None
    next_steps: Optional[List[str]] = Field(None, alias="nextSteps")
    template_id: Optional[str] = Field(None, alias="templateId")
    custom_sections: Optional[List[CustomSection]] = Field(None, alias="customSections")

    model_config = {"populate_by_name": True}


class ProtocolResponse(BaseModel):
    """Response containing generated protocol."""
    protocol: Protocol


class UpdateProtocolRequest(BaseModel):
    """Request to update an existing protocol."""
    protocol: Protocol


# ============================================================================
# Template Models
# ============================================================================

class TemplateSection(BaseModel):
    """Custom section in a meeting template."""
    id: str
    label: str
    type: Literal["textarea", "list", "text"]
    placeholder: Optional[str] = None
    default_value: Optional[str] = Field(None, alias="defaultValue")

    model_config = {"populate_by_name": True}


class TemplateStructure(BaseModel):
    """Structure modifications for a template."""
    suggested_title: Optional[str] = Field(None, alias="suggestedTitle")
    custom_sections: Optional[List[TemplateSection]] = Field(None, alias="customSections")
    action_item_defaults: Optional[List[Dict[str, Any]]] = Field(None, alias="actionItemDefaults")

    model_config = {"populate_by_name": True}


class MeetingTemplate(BaseModel):
    """Meeting template definition."""
    id: str
    name: str
    description: str
    icon: str
    category: Literal["internal", "external", "project"]
    structure: TemplateStructure

    model_config = {"populate_by_name": True}


class TemplateSuggestion(BaseModel):
    """AI-suggested template based on transcript analysis."""
    template_id: str = Field(alias="templateId")
    confidence: float
    reason: str

    model_config = {"populate_by_name": True}


class TemplatesResponse(BaseModel):
    """Response containing templates and optional AI suggestion."""
    templates: List[MeetingTemplate]
    suggestion: Optional[TemplateSuggestion] = None


# ============================================================================
# Job Models
# ============================================================================

class CreateJobResponse(BaseModel):
    """Response when creating a new workflow job."""
    job_id: str
    status: Literal["pending"] = "pending"
    created_at: str


class JobStatus(BaseModel):
    """Current status of a workflow job."""
    id: str
    status: Literal["pending", "processing", "completed", "failed"]
    current_step: int = Field(alias="currentStep")
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    file_uploaded: bool = Field(default=False, alias="fileUploaded")
    has_speakers: bool = Field(default=False, alias="hasSpeakers")
    has_protocol: bool = Field(default=False, alias="hasProtocol")
    recording_date: Optional[str] = Field(None, alias="recordingDate")
    skip_speaker_verification: bool = Field(default=False, alias="skipSpeakerVerification")
    teams_attendees: Optional[List[Dict]] = Field(None, alias="teamsAttendees")

    model_config = {"populate_by_name": True}


class UploadResponse(BaseModel):
    """Response after file upload."""
    success: bool
    file_id: str
    duration_seconds: int


# ============================================================================
# Transcription Models
# ============================================================================

class TranscriptionEvent(BaseModel):
    """SSE event during transcription processing."""
    type: Literal["progress", "complete", "error"]
    stage: Optional[str] = None
    percent: Optional[int] = None
    message: Optional[str] = None
    speakers: Optional[List[Speaker]] = None
    transcript: Optional[str] = None
    error: Optional[str] = None


# ============================================================================
# Publish Models
# ============================================================================

class PublishRequest(BaseModel):
    """Request to publish protocol to Confluence."""
    protocol: Protocol
    space_key: Optional[str] = Field(None, alias="spaceKey")

    model_config = {"populate_by_name": True}


class PublishResponse(BaseModel):
    """Response after publishing to Confluence."""
    success: bool
    confluence_url: str
    page_id: str


class ExportPdfRequest(BaseModel):
    """Request to export protocol as PDF."""
    protocol: Protocol


class ExportPdfResponse(BaseModel):
    """Response containing PDF download URL."""
    url: str


# ============================================================================
# User Models
# ============================================================================

class UserSuggestion(BaseModel):
    """User suggestion from LDAP/AD search."""
    id: str
    name: str
    email: str
    department: Optional[str] = None


class UsersSearchResponse(BaseModel):
    """Response containing user search results."""
    users: List[UserSuggestion]
