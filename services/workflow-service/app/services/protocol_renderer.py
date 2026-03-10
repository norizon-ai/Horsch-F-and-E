"""
Protocol Renderer -- Markdown and Confluence ADF output.

Converts a Protocol dict (from the two-pass LLM pipeline) into:
  1. Professional, table-heavy Markdown
  2. Confluence ADF (Atlassian Document Format) JSON

Design constraints:
  - No emojis anywhere
  - Professional B2B tone
  - Language-aware section headers (German / English)
  - Action items grouped by owner
  - Graceful fallback: missing/empty fields are skipped
"""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List, Optional, Sequence, Tuple


# ---------------------------------------------------------------------------
# Language detection
# ---------------------------------------------------------------------------

_GERMAN_MARKERS = {
    "und", "der", "die", "das", "ist", "wird", "wurde", "fuer", "mit",
    "ein", "eine", "auf", "nicht", "werden", "soll", "muss", "kann",
    "zusammenfassung", "entscheidung", "aufgabe", "anforderung",
    "besprechung", "protokoll", "teilnehmer",
}


def _detect_protocol_language(protocol: Dict[str, Any]) -> str:
    """Return 'de' or 'en' based on protocol content."""
    sample = " ".join(filter(None, [
        protocol.get("title", ""),
        protocol.get("tldr", ""),
        protocol.get("executiveSummary", ""),
    ])).lower()
    words = set(re.findall(r"[a-zäöü]+", sample))
    hits = len(words & _GERMAN_MARKERS)
    return "de" if hits >= 2 else "en"


# Section header translations
_HEADERS: Dict[str, Dict[str, str]] = {
    "summary":              {"de": "Zusammenfassung", "en": "Executive Summary"},
    "decisions":            {"de": "Entscheidungen", "en": "Decisions"},
    "action_items":         {"de": "Aktionspunkte", "en": "Action Items"},
    "tech_requirements":    {"de": "Technische Anforderungen", "en": "Technical Requirements"},
    "open_questions":       {"de": "Offene Fragen", "en": "Open Questions"},
    "watchouts":            {"de": "Risiken und Hinweise", "en": "Risks and Watchouts"},
    "system_landscape":     {"de": "Systemlandschaft", "en": "System Landscape"},
    "implementation":       {"de": "Implementierungsdetails", "en": "Implementation Details"},
    "constraints":          {"de": "Einschraenkungen", "en": "Constraints"},
    "data_integration":     {"de": "Datenintegrationspunkte", "en": "Data Integration Points"},
    "next_steps":           {"de": "Naechste Schritte", "en": "Next Steps"},
    "tasks_count":          {"de": "Aufgaben", "en": "Tasks"},
    "date_label":           {"de": "Datum", "en": "Date"},
    "attendees_label":      {"de": "Teilnehmer", "en": "Attendees"},
}


def _h(key: str, lang: str) -> str:
    """Get a header string for the given key and language."""
    return _HEADERS.get(key, {}).get(lang, key)


# ---------------------------------------------------------------------------
# Helpers: extract fields from protocol dict (handles both camelCase & snake)
# ---------------------------------------------------------------------------

def _get(protocol: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Return the first non-None value for any of the given keys."""
    for k in keys:
        v = protocol.get(k)
        if v is not None:
            return v
    return default


def _escape_pipe(text: str) -> str:
    """Escape pipe characters for Markdown table cells."""
    return text.replace("|", "\\|").replace("\n", " ") if text else ""


# ---------------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------------

def render_protocol_to_markdown(protocol: Dict[str, Any]) -> str:
    """
    Render a meeting protocol dict to professional, table-heavy Markdown.

    The protocol dict may come from the two-pass LLM output and can contain
    any combination of the supported fields.  Missing fields are skipped.

    Args:
        protocol: Protocol data dict.

    Returns:
        Formatted Markdown string.
    """
    lang = _detect_protocol_language(protocol)
    sections: List[str] = []

    # -- Title --
    title = protocol.get("title", "Meeting Protocol")
    sections.append(f"# {title}")

    # -- Metadata line --
    date = protocol.get("date", datetime.now().strftime("%Y-%m-%d"))
    attendees = _get(protocol, "attendees", default=[])
    meta_parts = [f"**{_h('date_label', lang)}:** {date}"]
    if attendees:
        names = ", ".join(attendees) if isinstance(attendees, list) else str(attendees)
        meta_parts.append(f"**{_h('attendees_label', lang)}:** {names}")
    sections.append(" | ".join(meta_parts))
    sections.append("---")

    # -- Executive Summary / TLDR --
    tldr = _get(protocol, "tldr", "executiveSummary", "executive_summary")
    if tldr:
        sections.append(f"## {_h('summary', lang)}")
        sections.append(str(tldr))

    # -- Decisions (table with rationale) --
    _render_decisions_md(protocol, lang, sections)

    # -- Action Items (grouped by owner) --
    _render_action_items_md(protocol, lang, sections)

    # -- Technical Requirements --
    tech_reqs = _get(protocol, "technical_requirements", default=[])
    if tech_reqs and isinstance(tech_reqs, list):
        sections.append(f"## {_h('tech_requirements', lang)}")
        header = "| Anforderung | Typ | Prioritaet |" if lang == "de" else "| Requirement | Type | Priority |"
        sections.append(header)
        sections.append("|-------------|-----|-----------|")
        for item in tech_reqs:
            if isinstance(item, dict):
                req = _escape_pipe(str(item.get("requirement", "")))
                typ = _escape_pipe(str(item.get("type", "")))
                prio = _escape_pipe(str(item.get("priority", "")))
                sections.append(f"| {req} | {typ} | {prio} |")
            elif isinstance(item, str):
                sections.append(f"| {_escape_pipe(item)} | | |")

    # -- Open Questions --
    open_qs = _get(protocol, "open_technical_questions", "open_questions", default=[])
    if open_qs and isinstance(open_qs, list):
        sections.append(f"## {_h('open_questions', lang)}")
        for q in open_qs:
            sections.append(f"- {q}")

    # -- Watchouts / Risks --
    watchouts = _get(protocol, "watchouts", "risks", default=[])
    if watchouts and isinstance(watchouts, list):
        sections.append(f"## {_h('watchouts', lang)}")
        header = "| Nr. | Risiko |" if lang == "de" else "| No. | Risk |"
        sections.append(header)
        sections.append("|-----|--------|")
        for i, w in enumerate(watchouts, 1):
            sections.append(f"| {i} | {_escape_pipe(str(w))} |")

    # -- System Landscape --
    sys_landscape = _get(protocol, "system_landscape")
    if sys_landscape:
        sections.append(f"## {_h('system_landscape', lang)}")
        sections.append(str(sys_landscape))

    # -- Implementation Details --
    impl = _get(protocol, "implementation_details")
    if impl:
        sections.append(f"## {_h('implementation', lang)}")
        sections.append(str(impl))

    # -- Constraints --
    constraints = _get(protocol, "constraints_limitations", "constraints", default=[])
    if constraints and isinstance(constraints, list):
        sections.append(f"## {_h('constraints', lang)}")
        c_header = "| Einschraenkung | Typ |" if lang == "de" else "| Constraint | Type |"
        sections.append(c_header)
        sections.append("|----------------|-----|")
        for item in constraints:
            if isinstance(item, dict):
                c = _escape_pipe(str(item.get("constraint", "")))
                t = _escape_pipe(str(item.get("type", "")))
                sections.append(f"| {c} | {t} |")
            elif isinstance(item, str):
                sections.append(f"| {_escape_pipe(item)} | |")

    # -- Data Integration Points --
    data_pts = _get(protocol, "data_integration_points", default=[])
    if data_pts and isinstance(data_pts, list):
        sections.append(f"## {_h('data_integration', lang)}")
        if lang == "de":
            sections.append("| System | Datentyp | Richtung | Anmerkungen |")
        else:
            sections.append("| System | Data Type | Direction | Notes |")
        sections.append("|--------|----------|----------|-------------|")
        for item in data_pts:
            if isinstance(item, dict):
                sys = _escape_pipe(str(item.get("system", "")))
                dt = _escape_pipe(str(item.get("data_type", "")))
                dr = _escape_pipe(str(item.get("direction", "")))
                notes = _escape_pipe(str(item.get("notes", "")))
                sections.append(f"| {sys} | {dt} | {dr} | {notes} |")

    # -- Next Steps --
    next_steps = _get(protocol, "nextSteps", "next_steps", default=[])
    if next_steps and isinstance(next_steps, list):
        sections.append(f"## {_h('next_steps', lang)}")
        for i, step in enumerate(next_steps, 1):
            sections.append(f"{i}. {step}")

    # -- Custom Sections (template-specific) --
    custom = _get(protocol, "customSections", "custom_sections", default=[])
    if custom and isinstance(custom, list):
        for section in custom:
            if isinstance(section, dict):
                label = section.get("label", section.get("title", "Section"))
                content = section.get("content", "")
                sections.append(f"## {label}")
                if isinstance(content, list):
                    for item in content:
                        sections.append(f"- {item}")
                elif content:
                    sections.append(str(content))

    return "\n\n".join(sections)


def _render_decisions_md(
    protocol: Dict[str, Any], lang: str, sections: List[str]
) -> None:
    """Render decisions as a table with rationale column."""
    # Prefer technical_decisions (has rationale), fall back to decisions list
    tech_decisions = _get(protocol, "technical_decisions", default=[])
    plain_decisions = _get(protocol, "decisions", default=[])

    if tech_decisions and isinstance(tech_decisions, list):
        sections.append(f"## {_h('decisions', lang)}")
        if lang == "de":
            sections.append("| Nr. | Entscheidung | Begruendung |")
        else:
            sections.append("| No. | Decision | Rationale |")
        sections.append("|-----|-------------|------------|")
        for i, d in enumerate(tech_decisions, 1):
            if isinstance(d, dict):
                dec = _escape_pipe(str(d.get("decision", "")))
                rat = _escape_pipe(str(d.get("rationale", "")))
                sections.append(f"| {i} | {dec} | {rat} |")
            elif isinstance(d, str):
                sections.append(f"| {i} | {_escape_pipe(d)} | |")
    elif plain_decisions and isinstance(plain_decisions, list):
        sections.append(f"## {_h('decisions', lang)}")
        if lang == "de":
            sections.append("| Nr. | Entscheidung |")
            sections.append("|-----|-------------|")
        else:
            sections.append("| No. | Decision |")
            sections.append("|-----|----------|")
        for i, d in enumerate(plain_decisions, 1):
            if isinstance(d, dict):
                text = _escape_pipe(str(d.get("decision", d.get("text", str(d)))))
                sections.append(f"| {i} | {text} |")
            elif isinstance(d, str):
                sections.append(f"| {i} | {_escape_pipe(d)} |")


def _render_action_items_md(
    protocol: Dict[str, Any], lang: str, sections: List[str]
) -> None:
    """Render action items grouped by owner, each as a sub-table."""
    raw = _get(protocol, "action_items", "actionItems", default=[])
    if not raw or not isinstance(raw, list):
        return

    # Normalize items to dicts
    items: List[Dict[str, str]] = []
    for item in raw:
        if isinstance(item, dict):
            items.append({
                "owner": str(item.get("owner", item.get("assignee", ""))).strip(),
                "task": str(item.get("task", item.get("text", str(item)))).strip(),
                "due": str(item.get("due", item.get("dueDate", item.get("due_date", "")))).strip(),
            })
        elif isinstance(item, str):
            items.append({"owner": "", "task": item.strip(), "due": ""})

    if not items:
        return

    sections.append(f"## {_h('action_items', lang)}")

    # Group by owner
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for it in items:
        owner = it["owner"] or ("Nicht zugewiesen" if lang == "de" else "Unassigned")
        grouped[owner].append(it)

    # Sort groups: named owners first (alphabetical), then unassigned
    unassigned_keys = {"Nicht zugewiesen", "Unassigned", ""}
    sorted_owners = sorted(
        grouped.keys(),
        key=lambda o: (o in unassigned_keys, o.lower()),
    )

    tasks_label = _h("tasks_count", lang)
    due_label = "Faellig" if lang == "de" else "Due"

    for owner in sorted_owners:
        owner_items = grouped[owner]
        count = len(owner_items)
        sections.append(f"### {owner} ({count} {tasks_label})")
        sections.append(f"| Nr. | {'Aufgabe' if lang == 'de' else 'Task'} | {due_label} |")
        sections.append("|-----|---------|--------|")
        for i, it in enumerate(owner_items, 1):
            task = _escape_pipe(it["task"])
            due = _escape_pipe(it["due"])
            sections.append(f"| {i} | {task} | {due} |")


# ---------------------------------------------------------------------------
# ADF renderer
# ---------------------------------------------------------------------------

def render_protocol_to_adf(protocol: Dict[str, Any]) -> Dict[str, Any]:
    """
    Render a meeting protocol dict to Confluence ADF (Atlassian Document Format).

    Returns a complete ADF document dict ready for the Confluence API.

    Args:
        protocol: Protocol data dict.

    Returns:
        ADF document dict with type "doc".
    """
    lang = _detect_protocol_language(protocol)
    content: List[Dict[str, Any]] = []

    # -- Title --
    title = protocol.get("title", "Meeting Protocol")
    content.append(_adf_heading(title, 1))

    # -- Metadata --
    date = protocol.get("date", datetime.now().strftime("%Y-%m-%d"))
    attendees = _get(protocol, "attendees", default=[])
    meta_text = f"{_h('date_label', lang)}: {date}"
    if attendees:
        names = ", ".join(attendees) if isinstance(attendees, list) else str(attendees)
        meta_text += f"  |  {_h('attendees_label', lang)}: {names}"
    content.append(_adf_paragraph(meta_text, marks=[{"type": "strong"}]))
    content.append(_adf_rule())

    # -- Summary in info panel --
    tldr = _get(protocol, "tldr", "executiveSummary", "executive_summary")
    if tldr:
        content.append(_adf_heading(_h("summary", lang), 2))
        content.append(_adf_panel([_adf_paragraph(str(tldr))], "info"))

    # -- Decisions --
    _render_decisions_adf(protocol, lang, content)

    # -- Action Items --
    _render_action_items_adf(protocol, lang, content)

    # -- Technical Requirements --
    tech_reqs = _get(protocol, "technical_requirements", default=[])
    if tech_reqs and isinstance(tech_reqs, list):
        content.append(_adf_heading(_h("tech_requirements", lang), 2))
        headers = (
            ["Anforderung", "Typ", "Prioritaet"]
            if lang == "de"
            else ["Requirement", "Type", "Priority"]
        )
        rows: List[List[Any]] = []
        for item in tech_reqs:
            if isinstance(item, dict):
                prio = str(item.get("priority", ""))
                prio_node = _priority_lozenge(prio)
                rows.append([
                    str(item.get("requirement", "")),
                    str(item.get("type", "")),
                    prio_node,
                ])
            elif isinstance(item, str):
                rows.append([item, "", ""])
        content.append(_adf_table(headers, rows))

    # -- Open Questions --
    open_qs = _get(protocol, "open_technical_questions", "open_questions", default=[])
    if open_qs and isinstance(open_qs, list):
        content.append(_adf_heading(_h("open_questions", lang), 2))
        content.append(_adf_bullet_list([str(q) for q in open_qs]))

    # -- Watchouts in warning panel --
    watchouts = _get(protocol, "watchouts", "risks", default=[])
    if watchouts and isinstance(watchouts, list):
        content.append(_adf_heading(_h("watchouts", lang), 2))
        watchout_rows = [[str(i), str(w)] for i, w in enumerate(watchouts, 1)]
        table = _adf_table(
            ["Nr.", "Risiko" if lang == "de" else "Risk"],
            watchout_rows,
        )
        content.append(_adf_panel([table], "warning"))

    # -- System Landscape --
    sys_landscape = _get(protocol, "system_landscape")
    if sys_landscape:
        content.append(_adf_heading(_h("system_landscape", lang), 2))
        content.append(_adf_paragraph(str(sys_landscape)))

    # -- Implementation Details --
    impl = _get(protocol, "implementation_details")
    if impl:
        content.append(_adf_heading(_h("implementation", lang), 2))
        content.append(_adf_paragraph(str(impl)))

    # -- Constraints --
    constraints = _get(protocol, "constraints_limitations", "constraints", default=[])
    if constraints and isinstance(constraints, list):
        content.append(_adf_heading(_h("constraints", lang), 2))
        c_headers = (
            ["Einschraenkung", "Typ"] if lang == "de" else ["Constraint", "Type"]
        )
        c_rows: List[List[str]] = []
        for item in constraints:
            if isinstance(item, dict):
                c_rows.append([
                    str(item.get("constraint", "")),
                    str(item.get("type", "")),
                ])
            elif isinstance(item, str):
                c_rows.append([item, ""])
        content.append(_adf_table(c_headers, c_rows))

    # -- Data Integration Points --
    data_pts = _get(protocol, "data_integration_points", default=[])
    if data_pts and isinstance(data_pts, list):
        content.append(_adf_heading(_h("data_integration", lang), 2))
        d_headers = (
            ["System", "Datentyp", "Richtung", "Anmerkungen"]
            if lang == "de"
            else ["System", "Data Type", "Direction", "Notes"]
        )
        d_rows: List[List[str]] = []
        for item in data_pts:
            if isinstance(item, dict):
                d_rows.append([
                    str(item.get("system", "")),
                    str(item.get("data_type", "")),
                    str(item.get("direction", "")),
                    str(item.get("notes", "")),
                ])
        content.append(_adf_table(d_headers, d_rows))

    # -- Next Steps --
    next_steps = _get(protocol, "nextSteps", "next_steps", default=[])
    if next_steps and isinstance(next_steps, list):
        content.append(_adf_heading(_h("next_steps", lang), 2))
        content.append(_adf_bullet_list([str(s) for s in next_steps]))

    return {"version": 1, "type": "doc", "content": content}


def _render_decisions_adf(
    protocol: Dict[str, Any], lang: str, content: List[Dict[str, Any]]
) -> None:
    """Render decisions as ADF table with rationale."""
    tech_decisions = _get(protocol, "technical_decisions", default=[])
    plain_decisions = _get(protocol, "decisions", default=[])

    if tech_decisions and isinstance(tech_decisions, list):
        content.append(_adf_heading(_h("decisions", lang), 2))
        headers = (
            ["Nr.", "Entscheidung", "Begruendung"]
            if lang == "de"
            else ["No.", "Decision", "Rationale"]
        )
        rows: List[List[str]] = []
        for i, d in enumerate(tech_decisions, 1):
            if isinstance(d, dict):
                rows.append([
                    str(i),
                    str(d.get("decision", "")),
                    str(d.get("rationale", "")),
                ])
            elif isinstance(d, str):
                rows.append([str(i), d, ""])
        content.append(_adf_table(headers, rows))
    elif plain_decisions and isinstance(plain_decisions, list):
        content.append(_adf_heading(_h("decisions", lang), 2))
        headers = (
            ["Nr.", "Entscheidung"] if lang == "de" else ["No.", "Decision"]
        )
        rows = []
        for i, d in enumerate(plain_decisions, 1):
            text = d if isinstance(d, str) else str(d.get("decision", d.get("text", str(d)))) if isinstance(d, dict) else str(d)
            rows.append([str(i), text])
        content.append(_adf_table(headers, rows))


def _render_action_items_adf(
    protocol: Dict[str, Any], lang: str, content: List[Dict[str, Any]]
) -> None:
    """Render action items grouped by owner as ADF tables."""
    raw = _get(protocol, "action_items", "actionItems", default=[])
    if not raw or not isinstance(raw, list):
        return

    items: List[Dict[str, str]] = []
    for item in raw:
        if isinstance(item, dict):
            items.append({
                "owner": str(item.get("owner", item.get("assignee", ""))).strip(),
                "task": str(item.get("task", item.get("text", str(item)))).strip(),
                "due": str(item.get("due", item.get("dueDate", item.get("due_date", "")))).strip(),
            })
        elif isinstance(item, str):
            items.append({"owner": "", "task": item.strip(), "due": ""})

    if not items:
        return

    content.append(_adf_heading(_h("action_items", lang), 2))

    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for it in items:
        owner = it["owner"] or ("Nicht zugewiesen" if lang == "de" else "Unassigned")
        grouped[owner].append(it)

    unassigned_keys = {"Nicht zugewiesen", "Unassigned", ""}
    sorted_owners = sorted(
        grouped.keys(),
        key=lambda o: (o in unassigned_keys, o.lower()),
    )

    tasks_label = _h("tasks_count", lang)
    due_label = "Faellig" if lang == "de" else "Due"
    task_label = "Aufgabe" if lang == "de" else "Task"

    for owner in sorted_owners:
        owner_items = grouped[owner]
        count = len(owner_items)
        content.append(_adf_heading(f"{owner} ({count} {tasks_label})", 3))
        rows: List[List[str]] = []
        for i, it in enumerate(owner_items, 1):
            rows.append([str(i), it["task"], it["due"]])
        content.append(_adf_table(["Nr.", task_label, due_label], rows))


# ---------------------------------------------------------------------------
# ADF node builders
# ---------------------------------------------------------------------------

def _adf_heading(text: str, level: int = 2) -> Dict[str, Any]:
    """Create an ADF heading node."""
    return {
        "type": "heading",
        "attrs": {"level": level},
        "content": [{"type": "text", "text": text}],
    }


def _adf_paragraph(
    text: str,
    marks: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Create an ADF paragraph node."""
    text_node: Dict[str, Any] = {"type": "text", "text": text}
    if marks:
        text_node["marks"] = marks
    return {
        "type": "paragraph",
        "content": [text_node],
    }


def _adf_table(
    headers: Sequence[str],
    rows: Sequence[Sequence[Any]],
) -> Dict[str, Any]:
    """
    Create an ADF table with a header row and data rows.

    Cell values can be strings or ADF node dicts (e.g. status lozenges).
    """
    # Header row
    header_cells = []
    for h in headers:
        header_cells.append({
            "type": "tableHeader",
            "content": [_adf_paragraph(h, marks=[{"type": "strong"}])],
        })
    header_row = {"type": "tableRow", "content": header_cells}

    # Data rows
    data_rows = []
    for row in rows:
        cells = []
        for cell in row:
            if isinstance(cell, dict) and "type" in cell:
                # Already an ADF node -- wrap in paragraph if needed
                if cell["type"] == "paragraph":
                    cells.append({"type": "tableCell", "content": [cell]})
                else:
                    cells.append({
                        "type": "tableCell",
                        "content": [{"type": "paragraph", "content": [cell]}],
                    })
            else:
                cells.append({
                    "type": "tableCell",
                    "content": [_adf_paragraph(str(cell) if cell else "")],
                })
        data_rows.append({"type": "tableRow", "content": cells})

    return {
        "type": "table",
        "attrs": {"isNumberColumnEnabled": False, "layout": "default"},
        "content": [header_row] + data_rows,
    }


def _adf_panel(
    content_nodes: List[Dict[str, Any]],
    panel_type: str = "info",
) -> Dict[str, Any]:
    """
    Create an ADF panel node.

    panel_type: "info", "note", "warning", "error", "success"
    """
    return {
        "type": "panel",
        "attrs": {"panelType": panel_type},
        "content": content_nodes,
    }


def _adf_bullet_list(items: List[str]) -> Dict[str, Any]:
    """Create an ADF bullet list from string items."""
    list_items = []
    for item in items:
        list_items.append({
            "type": "listItem",
            "content": [_adf_paragraph(item)],
        })
    return {"type": "bulletList", "content": list_items}


def _adf_status(text: str, color: str = "neutral") -> Dict[str, Any]:
    """
    Create an ADF status lozenge node.

    color: "neutral", "purple", "blue", "red", "yellow", "green"
    """
    return {
        "type": "status",
        "attrs": {"text": text, "color": color, "style": ""},
    }


def _adf_rule() -> Dict[str, Any]:
    """Create an ADF horizontal rule."""
    return {"type": "rule"}


def _priority_lozenge(priority: str) -> Dict[str, Any]:
    """Map a priority string to a colored ADF status lozenge."""
    p = priority.lower().strip()
    if p in ("must-have", "must_have", "critical", "hoch", "high"):
        return _adf_status(priority, "red")
    elif p in ("should-have", "should_have", "medium", "mittel"):
        return _adf_status(priority, "yellow")
    elif p in ("nice-to-have", "nice_to_have", "low", "niedrig"):
        return _adf_status(priority, "green")
    elif p:
        return _adf_status(priority, "neutral")
    return _adf_paragraph("")
