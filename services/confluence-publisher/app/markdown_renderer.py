"""
Confluence Publisher - Markdown Renderer.

Converts a Protocol dict (from the workflow service) into a clean
markdown string suitable for Confluence page creation.
"""

from datetime import datetime
from typing import Any, Dict, List


def render_protocol_to_markdown(protocol: Dict[str, Any]) -> str:
    """
    Render a meeting protocol dict to a markdown string.

    Args:
        protocol: Protocol data with keys like title, date, attendees,
                  executiveSummary, actionItems, decisions, nextSteps, etc.

    Returns:
        Formatted markdown string
    """
    sections: List[str] = []

    # Title
    title = protocol.get("title", "Meeting Protocol")
    sections.append(f"# {title}")

    # Metadata line
    date = protocol.get("date", datetime.now().strftime("%Y-%m-%d"))
    attendees = protocol.get("attendees", [])
    meta_parts = [f"**Date:** {date}"]
    if attendees:
        meta_parts.append(f"**Attendees:** {', '.join(attendees)}")
    sections.append(" | ".join(meta_parts))

    # Executive Summary
    if summary := protocol.get("executiveSummary"):
        sections.append("## Executive Summary")
        sections.append(summary)

    # Action Items
    action_items = protocol.get("actionItems", [])
    if action_items:
        sections.append("## Action Items")
        sections.append(_render_action_items_table(action_items))

    # Decisions
    decisions = protocol.get("decisions", [])
    if decisions:
        sections.append("## Decisions")
        for i, decision in enumerate(decisions, 1):
            sections.append(f"{i}. {decision}")

    # Next Steps
    next_steps = protocol.get("nextSteps", [])
    if next_steps:
        sections.append("## Next Steps")
        for i, step in enumerate(next_steps, 1):
            sections.append(f"{i}. {step}")

    # Custom sections (template-specific)
    custom_sections = protocol.get("customSections", protocol.get("sections", []))
    if isinstance(custom_sections, list):
        for section in custom_sections:
            if isinstance(section, dict):
                section_title = section.get("title", "Section")
                section_content = section.get("content", "")
                sections.append(f"## {section_title}")
                sections.append(section_content)

    # Transcript (collapsible)
    transcript = protocol.get("transcript", protocol.get("fullTranscript"))
    if transcript:
        sections.append("---")
        sections.append("<details><summary>Full Transcript</summary>")
        sections.append("")
        sections.append(transcript)
        sections.append("")
        sections.append("</details>")

    return "\n\n".join(sections)


def _render_action_items_table(action_items: List[Any]) -> str:
    """Render action items as a markdown table."""
    rows = ["| Task | Assignee | Due Date |", "|------|----------|----------|"]

    for item in action_items:
        if isinstance(item, dict):
            task = item.get("text", item.get("task", str(item)))
            assignee = item.get("assignee", "")
            due_date = item.get("dueDate", item.get("due_date", ""))
        else:
            task = str(item)
            assignee = ""
            due_date = ""

        # Escape pipe characters in content
        task = task.replace("|", "\\|")
        assignee = assignee.replace("|", "\\|") if assignee else ""
        due_date = due_date.replace("|", "\\|") if due_date else ""

        rows.append(f"| {task} | {assignee} | {due_date} |")

    return "\n".join(rows)
