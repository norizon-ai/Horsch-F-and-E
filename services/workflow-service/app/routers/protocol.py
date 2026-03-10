"""
Protocol router - Generate and manage meeting protocols.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import Any, Optional
import logging

from openai import AsyncOpenAI, BadRequestError as OpenAIBadRequestError
import httpx

from app.models import Protocol, ProtocolResponse, UpdateProtocolRequest, ActionItem
from app.services.job_manager import JobManager
from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter(tags=["protocol"])

# Module-level LLM client -- reused across requests to avoid
# connection-pool leaks and repeated TLS handshakes.
_llm_client: Optional[AsyncOpenAI] = None


def _get_llm_client() -> AsyncOpenAI:
    """Get or create the shared AsyncOpenAI client."""
    global _llm_client
    if _llm_client is None:
        settings = get_settings()
        kwargs = {"api_key": settings.llm_api_key}
        if settings.llm_base_url:
            kwargs["base_url"] = settings.llm_base_url
        _llm_client = AsyncOpenAI(
            **kwargs,
            timeout=httpx.Timeout(300.0, connect=10.0, read=300.0, write=30.0, pool=30.0),
        )
    return _llm_client


class GenerateProtocolRequest(BaseModel):
    """Request body for protocol generation."""
    template_id: Optional[str] = Field(None, alias="templateId", description="Template to apply to the protocol")
    two_pass: Optional[bool] = Field(None, alias="twoPass", description="Use two-pass generation (structure then extract). Defaults to WORKFLOW_LLM_TWO_PASS env var or False.")

    model_config = {"populate_by_name": True}


@router.get("/jobs/{job_id}/protocol", response_model=ProtocolResponse)
async def get_protocol(job_id: str):
    """Get the generated protocol for a job."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    if job.protocol is None:
        raise HTTPException(
            status_code=404,
            detail="Protocol not yet generated. Call POST /jobs/{job_id}/protocol first."
        )

    return ProtocolResponse(protocol=job.protocol)


@router.post("/jobs/{job_id}/protocol", response_model=ProtocolResponse)
async def generate_protocol(job_id: str, request: Optional[GenerateProtocolRequest] = None):
    """
    Generate a protocol from the transcription.

    The protocol combines:
    - Transcript from the transcription service
    - Template structure (if template_id provided)
    - Speaker names (confirmed by user)

    Into a structured meeting protocol with:
    - Executive summary
    - Action items with assignees
    - Decisions made
    - Next steps
    """
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    template_id = request.template_id if request else None

    # Determine whether to use two-pass generation.
    # Priority: explicit request param > env var > default (False)
    settings = get_settings()
    use_two_pass = (
        request.two_pass
        if request and request.two_pass is not None
        else settings.llm_two_pass
    )

    try:
        if use_two_pass:
            logger.info(f"Using TWO-PASS protocol generation for job {job_id}")
            protocol = await _generate_protocol_two_pass(
                transcript=job.transcript,
                speakers=job.speakers,
                template_id=template_id,
            )
        else:
            protocol = await _generate_protocol_with_llm(
                transcript=job.transcript,
                speakers=job.speakers,
                template_id=template_id,
            )

        # Post-process: replace any remaining detected speaker names
        # (e.g. "Sprecher 1") the LLM may have echoed from the transcript
        if job.speakers:
            protocol = _apply_speaker_name_replacements(protocol, job.speakers)

        JobManager.set_protocol(job_id, protocol)
        return ProtocolResponse(protocol=protocol)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"LLM protocol generation failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=502,
            detail=f"Protocol generation failed: {str(e)}. The LLM service may be temporarily unavailable."
        )


def _apply_speaker_name_replacements(protocol: Protocol, speakers: list) -> Protocol:
    """
    Apply speaker name replacements to a protocol.

    Replaces detected speaker names (Sprecher 1, Speaker 0, etc.) with confirmed names
    throughout all text fields in the protocol.

    Args:
        protocol: The protocol to update
        speakers: List of speakers with detected and confirmed names

    Returns:
        Updated protocol with speaker names replaced
    """
    import re

    # Build speaker name mapping
    speaker_name_map = {}
    for i, s in enumerate(speakers):
        # Handle both dict and Speaker object formats
        if isinstance(s, dict):
            detected_name = s.get("detectedName", f"Speaker {i}")
            confirmed_name = s.get("confirmedName", "")
        else:
            detected_name = s.detected_name or f"Speaker {i}"
            confirmed_name = s.confirmed_name or ""

        # DEFENSIVE: Strip whitespace from names
        confirmed_name = confirmed_name.strip() if confirmed_name else ""
        detected_name = detected_name.strip() if detected_name else f"Speaker {i}"

        logger.info(f"Speaker {i}: detected='{detected_name}', confirmed='{confirmed_name}'")

        # Only create mapping if name was actually changed
        if confirmed_name and confirmed_name != detected_name:
            # Map the exact detected name (this is the ground truth)
            speaker_name_map[detected_name] = confirmed_name
            logger.info(f"  → Mapping '{detected_name}' to '{confirmed_name}'")
        elif not confirmed_name:
            logger.info(f"  → No confirmed name provided (will use detected name)")
        else:
            logger.info(f"  → Confirmed name same as detected (no replacement needed)")

    if not speaker_name_map:
        logger.info("No speaker name replacements needed (no confirmed names differ from detected)")
        return protocol  # No replacements needed

    logger.info(f"Applying speaker name replacements: {speaker_name_map}")

    def replace_in_text(text: str) -> str:
        """Replace speaker names in text, avoiding double-replacements.

        Guards against "René" → "René Richter" also matching the "René"
        inside an already-correct "René Richter".
        """
        if not text:
            return text
        result = text
        # Sort by length (longest first) to avoid partial replacements
        for detected_name in sorted(speaker_name_map.keys(), key=len, reverse=True):
            confirmed_name = speaker_name_map[detected_name]

            # Build a pattern that matches the detected name but NOT when
            # it's already part of the confirmed name.
            # E.g. detected="René", confirmed="René Richter"
            #   → match "René" only when NOT followed by " Richter"
            pattern = rf'\b{re.escape(detected_name)}\b'
            if confirmed_name.startswith(detected_name) and len(confirmed_name) > len(detected_name):
                suffix = confirmed_name[len(detected_name):]
                pattern = rf'\b{re.escape(detected_name)}\b(?!{re.escape(suffix)})'
            elif confirmed_name.endswith(detected_name) and len(confirmed_name) > len(detected_name):
                prefix = confirmed_name[:-len(detected_name)]
                pattern = rf'(?<!{re.escape(prefix)})\b{re.escape(detected_name)}\b'

            result = re.sub(pattern, confirmed_name, result, flags=re.IGNORECASE)
        return result

    # Create a copy to avoid mutating the original
    protocol_dict = protocol.model_dump(by_alias=True)

    # CRITICAL FIX: Replace speaker names in attendees list
    if protocol_dict.get("attendees"):
        original_attendees = protocol_dict["attendees"].copy()
        logger.info(f"BEFORE attendee replacement: {original_attendees}")
        logger.info(f"Speaker mapping to apply: {speaker_name_map}")
        protocol_dict["attendees"] = [replace_in_text(name) for name in protocol_dict["attendees"]]
        logger.info(f"AFTER attendee replacement: {protocol_dict['attendees']}")

        # Verify replacement actually happened
        if original_attendees == protocol_dict["attendees"]:
            logger.warning(f"WARNING: Attendees were NOT changed during replacement!")
            logger.warning(f"  This means either:")
            logger.warning(f"  1. Attendees already had confirmed names (good)")
            logger.warning(f"  2. The regex pattern didn't match (bug!)")
        else:
            logger.info(f"SUCCESS: Attendees were updated from {original_attendees} to {protocol_dict['attendees']}")

    # Replace in all text fields
    if protocol_dict.get("executiveSummary"):
        protocol_dict["executiveSummary"] = replace_in_text(protocol_dict["executiveSummary"])

    if protocol_dict.get("fullTranscript"):
        protocol_dict["fullTranscript"] = replace_in_text(protocol_dict["fullTranscript"])

    if protocol_dict.get("decisions"):
        protocol_dict["decisions"] = [replace_in_text(d) for d in protocol_dict["decisions"]]

    if protocol_dict.get("nextSteps"):
        protocol_dict["nextSteps"] = [replace_in_text(s) for s in protocol_dict["nextSteps"]]

    if protocol_dict.get("actionItems"):
        for item in protocol_dict["actionItems"]:
            if item.get("text"):
                item["text"] = replace_in_text(item["text"])
            if item.get("assignee"):
                item["assignee"] = replace_in_text(item["assignee"])

    if protocol_dict.get("customSections"):
        for section in protocol_dict["customSections"]:
            if section.get("content"):
                if isinstance(section["content"], str):
                    section["content"] = replace_in_text(section["content"])
                elif isinstance(section["content"], list):
                    section["content"] = [replace_in_text(c) if isinstance(c, str) else c for c in section["content"]]

    # Reconstruct Protocol object from updated dict
    return Protocol(**protocol_dict)


async def _generate_protocol_with_llm(
    transcript: Optional[str],
    speakers: list,
    template_id: Optional[str] = None,
) -> Protocol:
    """
    Generate a meeting protocol using an LLM.

    Supports OpenAI, IONOS (vLLM), or any OpenAI-compatible API.
    Uses template-aware prompts that include per-field extraction instructions
    from the YAML template schemas.

    Args:
        transcript: The full meeting transcript
        speakers: List of speakers with confirmed names
        template_id: Optional template to apply

    Returns:
        Generated Protocol object
    """
    from datetime import datetime
    from app.services.json_parser import extract_json_from_response
    from app.services.prompt_builder import build_template_aware_prompt

    if not transcript:
        raise HTTPException(
            status_code=400,
            detail="No transcript available. Complete transcription first."
        )

    settings = get_settings()
    if not settings.llm_api_key:
        raise HTTPException(
            status_code=500,
            detail="LLM API key not configured (set WORKFLOW_LLM_API_KEY)"
        )

    # Build speaker name list from speakers
    speaker_names = []
    if speakers:
        for i, s in enumerate(speakers):
            if isinstance(s, dict):
                detected_name = s.get("detectedName", f"Speaker {i}")
                confirmed_name = s.get("confirmedName") or detected_name
            else:
                detected_name = s.detected_name or f"Speaker {i}"
                confirmed_name = s.confirmed_name or detected_name
            speaker_names.append(confirmed_name)

    # Build template-aware prompt
    prompt = build_template_aware_prompt(
        transcript=transcript,
        template_id=template_id,
        speaker_names=speaker_names,
        model_name=settings.llm_model,
    )

    # Reuse module-level client (connection pooling, no FD leaks)
    client = _get_llm_client()

    # Make the API call with response_format fallback
    call_kwargs = {
        "model": settings.llm_model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": settings.llm_temperature,
        "max_tokens": settings.llm_max_tokens,
    }

    content = None
    try:
        # Try with JSON mode first
        try:
            response = await client.chat.completions.create(
                **call_kwargs,
                response_format={"type": "json_object"},
            )
        except OpenAIBadRequestError as e:
            error_msg = str(e).lower()
            if "response_format" in error_msg or "json" in error_msg:
                logger.info("response_format not supported, retrying without it")
                response = await client.chat.completions.create(**call_kwargs)
            else:
                raise

        if not response.choices:
            raise HTTPException(status_code=502, detail="LLM returned empty response (no choices)")

        content = response.choices[0].message.content
        if not content:
            raise HTTPException(status_code=502, detail="LLM returned empty content")
        protocol_data = extract_json_from_response(content)

        logger.info(f"LLM returned {len(protocol_data)} fields: {list(protocol_data.keys())}")

        # Map LLM output to Protocol model
        return _map_llm_output_to_protocol(
            data=protocol_data,
            transcript=transcript,
            speaker_names=speaker_names,
            template_id=template_id,
        )

    except ValueError as e:
        # JSON extraction failed -- try text parsing as last resort
        logger.warning(f"JSON extraction failed: {e}")
        if content:
            protocol_data = _parse_text_protocol(content, speaker_names)
            return Protocol(
                title=protocol_data.get("title", "Meeting Protocol"),
                date=datetime.now().strftime("%Y-%m-%d"),
                attendees=speaker_names,
                executiveSummary=protocol_data.get("executive_summary", ""),
                actionItems=[
                    ActionItem(id=f"action-{i}", text=item.get("text", ""))
                    for i, item in enumerate(protocol_data.get("action_items", []))
                ],
                fullTranscript=transcript or "",
                decisions=protocol_data.get("decisions"),
                nextSteps=protocol_data.get("next_steps"),
                templateId=template_id,
            )
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Protocol generation failed: {str(e)}"
        )


async def _generate_protocol_two_pass(
    transcript: Optional[str],
    speakers: list,
    template_id: Optional[str] = None,
) -> Protocol:
    """
    Generate a meeting protocol using a two-pass LLM approach.

    Pass 1 (Structure): Analyze the transcript and produce a detailed
    topic-level outline -- what was discussed, by whom, key statements,
    decisions, and action items per topic.

    Pass 2 (Extract): Feed the outline + original transcript to produce
    the final structured protocol JSON matching the template schema.

    This approach yields better results on long transcripts (>30 min)
    because it separates comprehension from formatting.  The model can
    focus on understanding the meeting in Pass 1, then focus on precise
    field extraction in Pass 2.

    Design note for future chunking integration:
        Pass 1 can be run independently on transcript chunks (e.g. 15-min
        segments).  The per-chunk outlines would be merged into a single
        combined outline, which then feeds into Pass 2 unchanged.  This
        function's interface would not need to change -- only the internal
        Pass 1 logic would iterate over chunks.

    Args:
        transcript: The full meeting transcript
        speakers: List of speakers with confirmed names
        template_id: Optional template to apply

    Returns:
        Generated Protocol object
    """
    from datetime import datetime
    from app.services.json_parser import extract_json_from_response
    from app.services.prompt_builder import (
        build_structure_pass_prompt,
        build_extraction_pass_prompt,
    )

    if not transcript:
        raise HTTPException(
            status_code=400,
            detail="No transcript available. Complete transcription first."
        )

    settings = get_settings()
    if not settings.llm_api_key:
        raise HTTPException(
            status_code=500,
            detail="LLM API key not configured (set WORKFLOW_LLM_API_KEY)"
        )

    # Build speaker name list
    speaker_names = []
    if speakers:
        for i, s in enumerate(speakers):
            if isinstance(s, dict):
                detected_name = s.get("detectedName", f"Speaker {i}")
                confirmed_name = s.get("confirmedName") or detected_name
            else:
                detected_name = s.detected_name or f"Speaker {i}"
                confirmed_name = s.confirmed_name or detected_name
            speaker_names.append(confirmed_name)

    client = _get_llm_client()

    # ------------------------------------------------------------------
    # Pass 1: Structure analysis
    # ------------------------------------------------------------------
    logger.info("Two-pass generation: starting Pass 1 (structure analysis)")

    structure_prompt = build_structure_pass_prompt(
        transcript=transcript,
        speaker_names=speaker_names,
        model_name=settings.llm_model,
    )

    call_kwargs_p1 = {
        "model": settings.llm_model,
        "messages": [{"role": "user", "content": structure_prompt}],
        "temperature": settings.llm_temperature,
        "max_tokens": settings.llm_max_tokens,
    }

    try:
        try:
            response_p1 = await client.chat.completions.create(
                **call_kwargs_p1,
                response_format={"type": "json_object"},
            )
        except OpenAIBadRequestError as e:
            error_msg = str(e).lower()
            if "response_format" in error_msg or "json" in error_msg:
                logger.info("Pass 1: response_format not supported, retrying without it")
                response_p1 = await client.chat.completions.create(**call_kwargs_p1)
            else:
                raise

        if not response_p1.choices:
            raise HTTPException(status_code=502, detail="Pass 1: LLM returned empty response")

        content_p1 = response_p1.choices[0].message.content
        if not content_p1:
            raise HTTPException(status_code=502, detail="Pass 1: LLM returned empty content")

        structure_data = extract_json_from_response(content_p1)
        topics_count = len(structure_data.get("topics", []))
        logger.info(
            f"Pass 1 complete: {topics_count} topics identified, "
            f"keys: {list(structure_data.keys())}"
        )

    except HTTPException:
        raise
    except ValueError as e:
        logger.warning(f"Pass 1 JSON extraction failed: {e}. Falling back to single-pass.")
        # If Pass 1 fails to produce valid JSON, fall back to single-pass
        return await _generate_protocol_with_llm(
            transcript=transcript,
            speakers=speakers,
            template_id=template_id,
        )

    # ------------------------------------------------------------------
    # Pass 2: Template-aware extraction using the structure
    # ------------------------------------------------------------------
    logger.info("Two-pass generation: starting Pass 2 (extraction)")

    extraction_prompt = build_extraction_pass_prompt(
        transcript=transcript,
        structure_json=structure_data,
        template_id=template_id,
        speaker_names=speaker_names,
        model_name=settings.llm_model,
    )

    call_kwargs_p2 = {
        "model": settings.llm_model,
        "messages": [{"role": "user", "content": extraction_prompt}],
        "temperature": settings.llm_temperature,
        "max_tokens": settings.llm_max_tokens,
    }

    content_p2 = None
    try:
        try:
            response_p2 = await client.chat.completions.create(
                **call_kwargs_p2,
                response_format={"type": "json_object"},
            )
        except OpenAIBadRequestError as e:
            error_msg = str(e).lower()
            if "response_format" in error_msg or "json" in error_msg:
                logger.info("Pass 2: response_format not supported, retrying without it")
                response_p2 = await client.chat.completions.create(**call_kwargs_p2)
            else:
                raise

        if not response_p2.choices:
            raise HTTPException(status_code=502, detail="Pass 2: LLM returned empty response")

        content_p2 = response_p2.choices[0].message.content
        if not content_p2:
            raise HTTPException(status_code=502, detail="Pass 2: LLM returned empty content")

        protocol_data = extract_json_from_response(content_p2)
        logger.info(f"Pass 2 complete: {len(protocol_data)} fields: {list(protocol_data.keys())}")

        return _map_llm_output_to_protocol(
            data=protocol_data,
            transcript=transcript,
            speaker_names=speaker_names,
            template_id=template_id,
        )

    except ValueError as e:
        logger.warning(f"Pass 2 JSON extraction failed: {e}")
        if content_p2:
            protocol_data = _parse_text_protocol(content_p2, speaker_names)
            return Protocol(
                title=protocol_data.get("title", "Meeting Protocol"),
                date=datetime.now().strftime("%Y-%m-%d"),
                attendees=speaker_names,
                executiveSummary=protocol_data.get("executive_summary", ""),
                actionItems=[
                    ActionItem(id=f"action-{i}", text=item.get("text", ""))
                    for i, item in enumerate(protocol_data.get("action_items", []))
                ],
                fullTranscript=transcript or "",
                decisions=protocol_data.get("decisions"),
                nextSteps=protocol_data.get("next_steps"),
                templateId=template_id,
            )
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Two-pass protocol generation failed in Pass 2: {str(e)}"
        )


def _map_llm_output_to_protocol(
    data: dict,
    transcript: str,
    speaker_names: list[str],
    template_id: Optional[str],
) -> Protocol:
    """
    Map LLM JSON output to the Protocol model.

    Standard fields go to Protocol top-level attributes.
    All other fields become CustomSection entries.
    """
    from datetime import datetime
    from app.services.prompt_builder import SECTION_LABELS

    # --- Standard fields ---
    title = data.get("title", "Meeting Protocol")
    tldr = data.get("tldr", data.get("executiveSummary", data.get("executive_summary", "")))

    # Action items -- handle both camelCase and snake_case keys
    raw_actions = data.get("action_items", data.get("actionItems", []))
    action_items = []
    for i, item in enumerate(raw_actions):
        if isinstance(item, dict):
            text = item.get("task", item.get("text", str(item)))
            assignee = item.get("owner", item.get("assignee"))
            due = item.get("due", item.get("dueDate"))
            action_items.append(ActionItem(
                id=f"action-{i}",
                text=text,
                assignee=assignee,
                dueDate=due,
            ))
        elif isinstance(item, str):
            action_items.append(ActionItem(id=f"action-{i}", text=item))

    # Also handle follow_up_actions (NETWORKING template)
    raw_followups = data.get("follow_up_actions", [])
    for i, item in enumerate(raw_followups, start=len(action_items)):
        if isinstance(item, dict):
            action_items.append(ActionItem(
                id=f"action-{i}",
                text=item.get("task", item.get("text", str(item))),
                assignee=item.get("owner", item.get("assignee")),
                dueDate=item.get("due", item.get("dueDate")),
            ))

    decisions = data.get("decisions", [])
    if not isinstance(decisions, list):
        decisions = [str(decisions)] if decisions else []

    # next_steps can be string, list of strings, or list of objects
    raw_next = data.get("next_steps", data.get("nextSteps", []))
    if isinstance(raw_next, str):
        next_steps = [raw_next] if raw_next else []
    elif isinstance(raw_next, list):
        next_steps = []
        for item in raw_next:
            if isinstance(item, str):
                next_steps.append(item)
            elif isinstance(item, dict):
                # Format object: "owner: task (due: date)"
                parts = []
                if item.get("owner"):
                    parts.append(item["owner"])
                if item.get("task"):
                    parts.append(item["task"])
                due = item.get("due", "")
                text = ": ".join(parts) if parts else str(item)
                if due and due != "TBD":
                    text += f" (bis: {due})"
                next_steps.append(text)
    else:
        next_steps = []

    # --- Custom sections from template-specific fields ---
    # Fields that are NOT custom sections
    standard_keys = {
        "title", "tldr", "executiveSummary", "executive_summary",
        "decisions", "action_items", "actionItems",
        "next_steps", "nextSteps", "follow_up_actions",
        "full_transcript", "fullTranscript", "metadata",
    }

    custom_sections = []
    for field_key, value in data.items():
        if field_key in standard_keys:
            continue
        if value is None or value == "" or value == []:
            continue

        label_info = SECTION_LABELS.get(field_key)
        if label_info:
            label, section_type = label_info
        else:
            # Unknown field -- use the key as label
            label = field_key.replace("_", " ").title()
            section_type = "list" if isinstance(value, list) else "text"

        content = _format_section_content(value, section_type)
        custom_sections.append({
            "id": field_key,
            "label": label,
            "type": section_type,
            "content": content,
        })

    from app.models import CustomSection as CS
    custom_section_models = [
        CS(id=s["id"], label=s["label"], type=s["type"], content=s["content"])
        for s in custom_sections
    ] if custom_sections else None

    return Protocol(
        title=title,
        date=datetime.now().strftime("%Y-%m-%d"),
        attendees=speaker_names,
        executiveSummary=tldr,
        actionItems=action_items,
        fullTranscript=transcript,
        decisions=decisions if decisions else None,
        nextSteps=next_steps if next_steps else None,
        templateId=template_id,
        customSections=custom_section_models,
    )


def _format_section_content(value: Any, section_type: str) -> Any:
    """
    Format a field value for display in a CustomSection.

    - Strings pass through
    - Lists of strings pass through
    - Objects are serialized to readable text
    - Lists of objects are converted to lists of formatted strings
    """
    if isinstance(value, str):
        return value

    if isinstance(value, dict):
        # Object -> readable text
        return _format_object_as_text(value)

    if isinstance(value, list):
        if not value:
            return []
        if all(isinstance(item, str) for item in value):
            return value
        # List of objects -> list of formatted strings
        formatted = []
        for item in value:
            if isinstance(item, str):
                formatted.append(item)
            elif isinstance(item, dict):
                formatted.append(_format_object_as_text(item))
            else:
                formatted.append(str(item))
        return formatted

    return str(value)


def _format_object_as_text(obj: dict) -> str:
    """
    Format a dict as readable text for display.

    Examples:
        {"owner": "Lisa", "task": "Send doc", "due": "TBD"}
        -> "Lisa: Send doc (due: TBD)"

        {"decision": "Use REST API", "rationale": "Simpler integration"}
        -> "Use REST API — Simpler integration"

        {"overall": "positive", "indicators": ["enthusiastic", "asked for pricing"]}
        -> "positive — enthusiastic, asked for pricing"
    """
    if not obj:
        return ""

    keys = list(obj.keys())

    # Pattern: owner + task + due (action-like)
    if "owner" in obj and "task" in obj:
        parts = [f"{obj['owner']}: {obj['task']}"]
        if obj.get("due") and obj["due"] != "TBD":
            parts[0] += f" (bis: {obj['due']})"
        return parts[0]

    # Pattern: decision/recommendation/blocker + rationale/priority
    for primary_key in ["decision", "recommendation", "blocker", "objection", "concern", "feedback", "constraint", "scenario"]:
        if primary_key in obj:
            primary = str(obj[primary_key])
            secondary_parts = []
            for k, v in obj.items():
                if k == primary_key:
                    continue
                if isinstance(v, list):
                    secondary_parts.append(", ".join(str(x) for x in v))
                elif v and str(v) not in ("", "None", "null"):
                    secondary_parts.append(f"{k}: {v}")
            if secondary_parts:
                return f"{primary} — {'; '.join(secondary_parts)}"
            return primary

    # Pattern: overall + indicators (sentiment-like)
    if "overall" in obj:
        overall = str(obj["overall"])
        extras = []
        for k, v in obj.items():
            if k == "overall":
                continue
            if isinstance(v, list):
                extras.extend(str(x) for x in v)
            elif v:
                extras.append(str(v))
        if extras:
            return f"{overall} — {', '.join(extras)}"
        return overall

    # Pattern: system + data_type + direction (data integration)
    if "system" in obj:
        parts = [str(obj["system"])]
        if obj.get("data_type"):
            parts.append(str(obj["data_type"]))
        if obj.get("direction"):
            parts.append(f"({obj['direction']})")
        if obj.get("notes"):
            parts.append(f"— {obj['notes']}")
        return " ".join(parts)

    # Pattern: step_number + actor + action (user flow)
    if "step_number" in obj and "action" in obj:
        actor = obj.get("actor", "")
        return f"{obj['step_number']}. [{actor}] {obj['action']}"

    # Pattern: requirement + type + priority
    if "requirement" in obj:
        req = str(obj["requirement"])
        extras = []
        if obj.get("type"):
            extras.append(str(obj["type"]))
        if obj.get("priority"):
            extras.append(str(obj["priority"]))
        if extras:
            return f"{req} ({', '.join(extras)})"
        return req

    # Fallback: key: value pairs
    parts = []
    for k, v in obj.items():
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        if v and str(v) not in ("", "None", "null"):
            parts.append(f"{k}: {v}")
    return "; ".join(parts)


def _parse_text_protocol(text: str, speaker_names: list) -> dict:
    """
    Parse unstructured text protocol into structured data.

    This is a fallback when the LLM doesn't return JSON.
    """
    # Simple heuristic parser - split by sections
    lines = text.split("\n")

    protocol_data = {
        "title": "Meeting Protocol",
        "executive_summary": "",
        "action_items": [],
        "decisions": [],
        "next_steps": []
    }

    current_section = None
    current_content = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Detect section headers (various formats)
        lower = line.lower()
        if any(x in lower for x in ["titel:", "title:"]):
            if current_section:
                _save_section(protocol_data, current_section, current_content)
            current_section = "title"
            current_content = [line.split(":", 1)[-1].strip()]
        elif any(x in lower for x in ["zusammenfassung:", "summary:", "executive"]):
            if current_section:
                _save_section(protocol_data, current_section, current_content)
            current_section = "summary"
            current_content = []
        elif any(x in lower for x in ["aktionspunkte:", "action items:", "aufgaben:"]):
            if current_section:
                _save_section(protocol_data, current_section, current_content)
            current_section = "actions"
            current_content = []
        elif any(x in lower for x in ["entscheidungen:", "decisions:"]):
            if current_section:
                _save_section(protocol_data, current_section, current_content)
            current_section = "decisions"
            current_content = []
        elif any(x in lower for x in ["nächste schritte:", "next steps:"]):
            if current_section:
                _save_section(protocol_data, current_section, current_content)
            current_section = "next_steps"
            current_content = []
        else:
            # Add to current section content
            if current_section:
                current_content.append(line)

    # Save last section
    if current_section:
        _save_section(protocol_data, current_section, current_content)

    # If we didn't find any structure, put everything in summary
    if not protocol_data["executive_summary"] and text:
        protocol_data["executive_summary"] = text[:500] + "..." if len(text) > 500 else text

    return protocol_data


def _save_section(protocol_data: dict, section: str, content: list):
    """Helper to save parsed section content."""
    if section == "title" and content:
        protocol_data["title"] = content[0]
    elif section == "summary":
        protocol_data["executive_summary"] = " ".join(content)
    elif section == "actions":
        # Parse action items (look for bullet points, numbered lists, etc.)
        for line in content:
            if line.startswith(("-", "*", "•")) or (line and line[0].isdigit()):
                text = line.lstrip("-*•0123456789. ").strip()
                if text:
                    protocol_data["action_items"].append({"text": text})
    elif section == "decisions":
        for line in content:
            if line.startswith(("-", "*", "•")) or (line and line[0].isdigit()):
                text = line.lstrip("-*•0123456789. ").strip()
                if text:
                    protocol_data["decisions"].append(text)
    elif section == "next_steps":
        for line in content:
            if line.startswith(("-", "*", "•")) or (line and line[0].isdigit()):
                text = line.lstrip("-*•0123456789. ").strip()
                if text:
                    protocol_data["next_steps"].append(text)


@router.put("/jobs/{job_id}/protocol", response_model=ProtocolResponse)
async def update_protocol(job_id: str, request: UpdateProtocolRequest):
    """Update an existing protocol after user edits."""
    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    # Store the updated protocol
    JobManager.set_protocol(job_id, request.protocol)

    return ProtocolResponse(protocol=request.protocol)


@router.get("/jobs/{job_id}/protocol/render")
async def render_protocol(job_id: str, format: str = "markdown"):
    """
    Render the protocol in the specified format.

    Args:
        job_id: The job ID whose protocol to render.
        format: Output format -- "markdown" (default) or "adf".

    Returns:
        Markdown as text/plain, or ADF as application/json.
    """
    from app.services.protocol_renderer import (
        render_protocol_to_adf,
        render_protocol_to_markdown,
    )

    job = JobManager.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    if job.protocol is None:
        raise HTTPException(
            status_code=404,
            detail="Protocol not yet generated. Call POST /jobs/{job_id}/protocol first.",
        )

    protocol_dict = job.protocol.model_dump(by_alias=True)

    if format == "adf":
        adf = render_protocol_to_adf(protocol_dict)
        return JSONResponse(content=adf)
    elif format == "markdown":
        md = render_protocol_to_markdown(protocol_dict)
        return PlainTextResponse(content=md, media_type="text/markdown")
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported format '{format}'. Use 'markdown' or 'adf'.",
        )
