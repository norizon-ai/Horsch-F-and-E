"""
Template loader service - loads meeting templates from YAML configuration.

This module provides functions to load and parse the meeting_templates.yaml file,
converting the YAML definitions into MeetingTemplate Pydantic models.
"""

import yaml
from pathlib import Path
from typing import List, Optional, Dict, Any
from functools import lru_cache

from app.models import MeetingTemplate, TemplateStructure, TemplateSection, TemplateSuggestion

# Path to the templates YAML file
YAML_PATH = Path(__file__).parent.parent.parent / "meeting_templates.yaml"


@lru_cache(maxsize=1)
def load_yaml_templates() -> Dict[str, Any]:
    """Load and cache YAML templates."""
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _determine_category(template_id: str) -> str:
    """Map template ID to category based on meeting type."""
    external = [
        "CLIENT_UPDATE",
        "CLIENT_TECHNICAL",
        "PROSPECT_SALES",
        "PARTNER",
        "NETWORKING",
    ]
    return "external" if template_id in external else "internal"


def _map_icon(template_id: str) -> str:
    """Map template ID to an icon name."""
    icons = {
        "CLIENT_UPDATE": "briefcase",
        "CLIENT_TECHNICAL": "code",
        "PROSPECT_SALES": "trending-up",
        "PARTNER": "handshake",
        "COACH_MENTOR": "graduation-cap",
        "NETWORKING": "users",
        "TEAM_SYNC": "refresh-cw",
        "TEAM_DESIGN": "layout",
    }
    return icons.get(template_id, "file-text")


def _generate_description(template_data: Dict[str, Any]) -> str:
    """Generate a template description from YAML data."""
    signals = template_data.get("classification_signals", [])
    if signals:
        return f"Keywords: {', '.join(signals[:3])}"
    return template_data.get("name", "Meeting template")


def _extract_custom_sections(schema: Dict[str, Any]) -> List[TemplateSection]:
    """Extract custom sections from the YAML schema."""
    custom_sections = []
    section_id = 0

    # Define which schema fields map to custom sections
    section_mappings = {
        "status_updates": ("Status Updates", "textarea"),
        "key_insights": ("Key Insights", "textarea"),
        "watchouts": ("Watchouts", "list"),
        "client_sentiment": ("Client Sentiment", "textarea"),
        "open_questions": ("Open Questions", "list"),
        "technical_requirements": ("Technical Requirements", "list"),
        "system_landscape": ("System Landscape", "textarea"),
        "technical_decisions": ("Technical Decisions", "list"),
        "constraints_limitations": ("Constraints & Limitations", "list"),
        "data_integration_points": ("Data Integration Points", "list"),
        "company_context": ("Company Context", "textarea"),
        "pain_points": ("Pain Points", "list"),
        "interest_level": ("Interest Level", "textarea"),
        "questions_asked": ("Questions Asked", "list"),
        "objections_concerns": ("Objections & Concerns", "list"),
        "discussion_topics": ("Discussion Topics", "list"),
        "potential_value": ("Potential Value", "textarea"),
        "concerns_blockers": ("Concerns & Blockers", "list"),
        "topics_discussed": ("Topics Discussed", "list"),
        "feedback_received": ("Feedback Received", "list"),
        "recommendations": ("Recommendations", "list"),
        "their_background": ("Their Background", "textarea"),
        "what_theyre_working_on": ("What They're Working On", "textarea"),
        "updates_by_person": ("Updates by Person", "textarea"),
        "blockers": ("Blockers", "list"),
        "problem_statement": ("Problem Statement", "textarea"),
        "user_flow": ("User Flow", "list"),
        "design_decisions": ("Design Decisions", "list"),
        "open_questions_tbd": ("Open Questions / TBD", "list"),
        "edge_cases": ("Edge Cases", "list"),
    }

    for field_name, (label, field_type) in section_mappings.items():
        if field_name in schema:
            field_data = schema[field_name]
            placeholder = None

            if isinstance(field_data, dict):
                placeholder = field_data.get("extraction_prompt")

            custom_sections.append(TemplateSection(
                id=field_name,
                label=label,
                type=field_type,
                placeholder=placeholder[:100] if placeholder else None,
            ))
            section_id += 1

    return custom_sections[:5]  # Limit to 5 custom sections for UI


def get_all_templates() -> List[MeetingTemplate]:
    """Convert YAML templates to MeetingTemplate models."""
    try:
        data = load_yaml_templates()
    except FileNotFoundError:
        # Fall back to empty list if YAML not found
        return []

    templates = []
    templates_data = data.get("meeting_templates", {}).get("templates", {})

    for template_id, template_data in templates_data.items():
        category = _determine_category(template_id)
        schema = template_data.get("schema", {})
        custom_sections = _extract_custom_sections(schema)

        # Get suggested title from metadata if available
        suggested_title = None
        metadata = schema.get("metadata", {})
        if "client" in metadata:
            suggested_title = "[Client] - [Topic]"
        elif "company" in metadata:
            suggested_title = "[Company] - [Meeting Type]"
        elif "partner" in metadata:
            suggested_title = "[Partner] - [Topic]"
        elif "feature_topic" in metadata:
            suggested_title = "[Feature] - Design Session"
        elif "coach_mentor" in metadata:
            suggested_title = "[Coach/Mentor] - Session"
        elif "person" in metadata:
            suggested_title = "[Person] - Networking"

        templates.append(MeetingTemplate(
            id=template_id,
            name=template_data.get("name", template_id),
            description=_generate_description(template_data),
            icon=_map_icon(template_id),
            category=category,
            structure=TemplateStructure(
                suggestedTitle=suggested_title,
                customSections=custom_sections if custom_sections else None,
            ),
        ))

    return templates


def get_template_by_id(template_id: str) -> Optional[MeetingTemplate]:
    """Get a specific template by ID."""
    templates = get_all_templates()
    for template in templates:
        if template.id == template_id:
            return template
    return None


def get_classification_signals(template_id: str) -> List[str]:
    """Get classification signals for a template."""
    try:
        data = load_yaml_templates()
        templates = data.get("meeting_templates", {}).get("templates", {})
        template_data = templates.get(template_id, {})
        return template_data.get("classification_signals", [])
    except (FileNotFoundError, KeyError):
        return []


def get_raw_template_schema(template_id: str) -> Optional[Dict[str, Any]]:
    """
    Return the raw YAML schema block for a template (not the Pydantic model).

    This gives access to extraction_prompts, extraction_patterns,
    nested type definitions, and validation rules that are lost during
    Pydantic conversion.
    """
    try:
        data = load_yaml_templates()
        templates = data.get("meeting_templates", {}).get("templates", {})
        template_data = templates.get(template_id)
        if template_data:
            return template_data.get("schema")
        return None
    except FileNotFoundError:
        return None


def get_validation_rules() -> Dict[str, Any]:
    """Return the validation rules section from the YAML."""
    try:
        data = load_yaml_templates()
        return data.get("meeting_templates", {}).get("validation", {})
    except FileNotFoundError:
        return {}


def get_all_classification_signals() -> Dict[str, List[str]]:
    """Get classification signals for all templates."""
    try:
        data = load_yaml_templates()
        templates = data.get("meeting_templates", {}).get("templates", {})
        return {
            template_id: template_data.get("classification_signals", [])
            for template_id, template_data in templates.items()
        }
    except FileNotFoundError:
        return {}


# ---------------------------------------------------------------------------
# Production template API (moved from mock_generator.py)
# ---------------------------------------------------------------------------

def _get_fallback_templates() -> List[MeetingTemplate]:
    """Fallback templates if YAML loading fails."""
    return [
        MeetingTemplate(
            id="team-meeting",
            name="Team Meeting",
            description="Internal team syncs and status updates",
            icon="users",
            category="internal",
            structure=TemplateStructure(
                suggestedTitle="Team Meeting - [Date]",
                customSections=[
                    TemplateSection(
                        id="blockers",
                        label="Blockers",
                        type="list",
                        placeholder="Current blockers and impediments..."
                    ),
                ],
            ),
        ),
        MeetingTemplate(
            id="customer-meeting",
            name="Customer Meeting",
            description="External client discussions, demos, and follow-ups",
            icon="briefcase",
            category="external",
            structure=TemplateStructure(
                suggestedTitle="[Customer] - [Topic]",
            ),
        ),
        MeetingTemplate(
            id="general",
            name="General Meeting",
            description="Standard meeting protocol without specific structure",
            icon="file-text",
            category="internal",
            structure=TemplateStructure(),
        ),
    ]


def get_templates() -> List[MeetingTemplate]:
    """Get all available meeting templates from YAML with fallback."""
    templates = get_all_templates()
    if templates:
        return templates
    return _get_fallback_templates()


def suggest_template(transcript: Optional[str] = None) -> TemplateSuggestion:
    """
    Suggest a template based on transcript content.

    Uses classification_signals from YAML templates for matching.
    """
    if not transcript:
        return TemplateSuggestion(
            templateId="TEAM_SYNC",
            confidence=0.5,
            reason="Kein Transkript verfügbar - Standard-Template vorgeschlagen"
        )

    transcript_lower = transcript.lower()
    all_signals = get_all_classification_signals()

    best_match = ("TEAM_SYNC", 0, "Team Sync")
    templates = get_all_templates()
    template_names = {t.id: t.name for t in templates}

    for template_id, signals in all_signals.items():
        matches = sum(1 for s in signals if s.lower() in transcript_lower)
        if matches > best_match[1]:
            template_name = template_names.get(template_id, template_id)
            best_match = (template_id, matches, template_name)

    confidence = min(0.95, 0.5 + (best_match[1] * 0.1))

    return TemplateSuggestion(
        templateId=best_match[0],
        confidence=confidence,
        reason=f"Erkannt als {best_match[2]} basierend auf {best_match[1]} Schlüsselwörtern"
    )
