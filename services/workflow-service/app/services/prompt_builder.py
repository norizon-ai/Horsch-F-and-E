"""
Template-aware prompt construction for protocol generation.

Reads the full YAML template schemas and builds LLM prompts that include
per-field extraction instructions, keyword hints, field type descriptions,
validation rules, and a concrete JSON output skeleton.
"""

import json
import logging
from typing import Any, Dict, List, Optional

from app.services.template_loader import (
    get_raw_template_schema,
    get_validation_rules,
    load_yaml_templates,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Language detection
# ---------------------------------------------------------------------------
_GERMAN_MARKERS = frozenset([
    "der", "die", "das", "und", "ist", "wir", "ich", "nicht", "mit",
    "ein", "eine", "auch", "auf", "für", "haben", "wird", "dass",
    "aber", "noch", "dann", "kann", "diese", "oder", "schon", "wenn",
    "machen", "gibt", "halt", "genau", "eigentlich", "quasi", "sozusagen",
])


def _detect_language(transcript: str) -> str:
    """Detect transcript language via German word frequency. Returns 'de' or 'en'."""
    words = transcript.lower().split()[:500]
    if not words:
        return "en"
    german_count = sum(1 for w in words if w.strip(".,!?:;()") in _GERMAN_MARKERS)
    return "de" if german_count / len(words) > 0.08 else "en"


# Shared mapping: field key -> (display label, CustomSection type)
# Used by both prompt_builder and _map_llm_output_to_protocol
SECTION_LABELS: Dict[str, tuple[str, str]] = {
    "status_updates": ("Status Updates", "text"),
    "key_insights": ("Key Insights", "text"),
    "watchouts": ("Watchouts", "list"),
    "client_sentiment": ("Client Sentiment", "text"),
    "open_questions": ("Open Questions", "list"),
    "technical_requirements": ("Technical Requirements", "list"),
    "system_landscape": ("System Landscape", "text"),
    "technical_decisions": ("Technical Decisions", "list"),
    "constraints_limitations": ("Constraints & Limitations", "list"),
    "data_integration_points": ("Data Integration Points", "list"),
    "implementation_details": ("Implementation Details", "text"),
    "open_technical_questions": ("Open Technical Questions", "list"),
    "company_context": ("Company Context", "text"),
    "pain_points": ("Pain Points", "list"),
    "interest_level": ("Interest Level", "text"),
    "questions_asked": ("Questions Asked", "list"),
    "objections_concerns": ("Objections & Concerns", "list"),
    "discussion_topics": ("Discussion Topics", "list"),
    "potential_value": ("Potential Value", "text"),
    "concerns_blockers": ("Concerns & Blockers", "list"),
    "topics_discussed": ("Topics Discussed", "list"),
    "feedback_received": ("Feedback Received", "list"),
    "recommendations": ("Recommendations", "list"),
    "their_background": ("Their Background", "text"),
    "what_theyre_working_on": ("What They're Working On", "text"),
    "updates_by_person": ("Updates by Person", "text"),
    "blockers": ("Blockers", "list"),
    "problem_statement": ("Problem Statement", "text"),
    "user_flow": ("User Flow", "list"),
    "design_decisions": ("Design Decisions", "list"),
    "open_questions_tbd": ("Open Questions / TBD", "list"),
    "edge_cases": ("Edge Cases", "list"),
    "follow_up_commitment": ("Follow-up Commitment", "text"),
    "notes": ("Notes", "text"),
    "next_steps": ("Next Steps", "list"),
}

def _specificity_instructions(lang: str, template_id: Optional[str] = None) -> str:
    """Return quality/specificity rules in the appropriate language."""
    # Disambiguation rules for client-facing templates
    is_client_meeting = template_id and any(
        kw in template_id.upper() for kw in ["CLIENT", "PROSPECT", "SALES"]
    )

    if lang == "de":
        rules = """## Qualitätsregeln – UNBEDINGT EINHALTEN
- VOLLSTÄNDIGKEIT: Gehe das GESAMTE Transkript Abschnitt für Abschnitt durch. Überspringe KEINE Themen.
- MINDESTANZAHL: Extrahiere mindestens 8 Aktionspunkte und mindestens 5 Entscheidungen aus einem Meeting über 30 Minuten. Bei einem 90-Minuten-Meeting erwarte ich 15+ Aktionspunkte.
- Aktionspunkte: „Angebot an Firma X bis Freitag schicken" ist gut, „Follow-up durchführen" ist schlecht. Jede Aufgabe einzeln auflisten, NICHT zusammenfassen.
- Entscheidungen: Nur explizite Vereinbarungen, keine Vorschläge oder Möglichkeiten.
- Verwende exakte Formulierungen und Zitate aus dem Transkript wenn möglich.
- Bei Personen immer den vollständigen Namen verwenden, wie oben angegeben. Erfinde KEINE Namen, die nicht im Transkript vorkommen.
- Technische Details: Konkrete Versionen (z.B. „Ubuntu 24 LTS"), Systemnamen (z.B. „Bookstack", „GitLab"), Konfigurationen, Speichergrößen, RAM-Angaben angeben.
- Anforderungen: Jede Anforderung separat mit konkreter Spezifikation auflisten, NICHT zusammenfassen zu „Hardware-Anforderungen".
- AUSFÜHRLICHKEIT: Schreibe detaillierte Beschreibungen, nicht Stichworte. Die Zusammenfassung soll mindestens 4 Sätze umfassen. Jedes Feld soll substantiellen Inhalt haben.
"""
        if is_client_meeting:
            rules += """
## WICHTIG: Unterscheidung Anbieter vs. Kunde
Dieses Meeting ist ein Kundengespräch. Unterscheide klar zwischen:
- **Bestehende Funktionen**: Wenn ein Sprecher erklärt, was das eigene Produkt BEREITS kann (z.B. „Wir machen das aktuell per Cron-Job", „Das verarbeiten wir auf deutschen Servern"), dann ist das KEINE Anforderung und KEIN Action Item. Das sind bestehende Features.
- **Kundenanforderungen**: Was der Kunde BRAUCHT oder sich WÜNSCHT (z.B. „Wir brauchen Bookstack-Integration", „Das muss auf unserem Server laufen").
- **Action Items**: Nur NEUE Aufgaben, die jemand NACH dem Meeting erledigen muss. „Docker-Compose vorbereiten" ist KEIN Action Item wenn das bereits existiert. „Angebot schicken" oder „Server bereitstellen" SIND Action Items.
- **Entscheidungen**: Nur Vereinbarungen zwischen den Parteien, nicht einseitige Erklärungen über bestehende Architektur.
"""
        return rules

    rules = """## Quality Rules – MUST FOLLOW
- COMPLETENESS: Go through the ENTIRE transcript section by section. Do NOT skip any topics.
- MINIMUM COUNTS: Extract at least 8 action items and at least 5 decisions from a meeting over 30 minutes. For a 90-minute meeting, expect 15+ action items.
- Action items: "Send proposal to Firma X by Friday" is good, "Follow up" is bad. List each task separately, do NOT merge them.
- Decisions: Only explicit agreements, not suggestions or possibilities.
- Use exact phrasing and quotes from the transcript when possible.
- Always use full person names as listed above. Do NOT invent names that don't appear in the transcript.
- Technical details: Include specific versions (e.g. "Ubuntu 24 LTS"), system names (e.g. "Bookstack", "GitLab"), configurations, storage sizes, RAM specs.
- Requirements: List each requirement separately with concrete specs, do NOT summarize as "Hardware requirements".
- THOROUGHNESS: Write detailed descriptions, not keywords. The summary should be at least 4 sentences. Every field should have substantial content.
"""
    if is_client_meeting:
        rules += """
## IMPORTANT: Distinguish Provider vs. Client
This is a client meeting. Clearly distinguish between:
- **Existing capabilities**: When a speaker explains what their product ALREADY does (e.g. "We currently do this via cron job", "We process on German servers"), this is NOT a requirement and NOT an action item. These are existing features.
- **Client requirements**: What the client NEEDS or WANTS (e.g. "We need Bookstack integration", "This must run on our server").
- **Action items**: Only NEW tasks someone must complete AFTER the meeting. "Prepare Docker Compose" is NOT an action item if it already exists. "Send proposal" or "Provision server" ARE action items.
- **Decisions**: Only agreements between the parties, not one-sided explanations of existing architecture.
"""
    return rules


# Fields that are always handled as top-level Protocol fields, not custom sections
_STANDARD_FIELDS = {
    "metadata", "tldr", "decisions", "action_items",
    "full_transcript", "next_steps", "follow_up_actions",
}


def build_template_aware_prompt(
    transcript: str,
    template_id: Optional[str],
    speaker_names: List[str],
    model_name: str = "",
) -> str:
    """
    Build a detailed LLM prompt for protocol generation.

    If template_id is provided, loads the full YAML schema and includes
    per-field extraction instructions, patterns, type descriptions, and
    a JSON output skeleton.

    For no-template or unknown template, falls back to base fields only.

    Args:
        transcript: Full meeting transcript text
        template_id: Template ID (e.g. "CLIENT_TECHNICAL") or None
        speaker_names: Confirmed speaker names
        model_name: LLM model name (used to adapt formatting instructions)

    Returns:
        Complete prompt string
    """
    schema = get_raw_template_schema(template_id) if template_id else None
    lang = _detect_language(transcript)

    # Speaker mapping section
    speaker_section = ""
    if speaker_names:
        if lang == "de":
            speaker_section = "\n## Sprecher-Zuordnung\n"
            speaker_section += "Das Transkript verwendet Sprecher-IDs. Ersetze sie durch diese bestätigten Namen:\n"
        else:
            speaker_section = "\n## Speaker Name Mapping\n"
            speaker_section += "The transcript uses speaker IDs. Replace them with these confirmed names:\n"
        for i, name in enumerate(speaker_names):
            speaker_section += f"- Speaker {i} / Sprecher {i} → {name}\n"
        if lang == "de":
            speaker_section += f"\nVerwende AUSSCHLIESSLICH diese Namen: {', '.join(speaker_names)}\n"
        else:
            speaker_section += f"\nUse ONLY these names: {', '.join(speaker_names)}\n"

    if schema:
        return _build_template_prompt(transcript, schema, speaker_section, model_name, lang, template_id)
    else:
        return _build_base_prompt(transcript, speaker_section, model_name, lang)


def _build_base_prompt(
    transcript: str,
    speaker_section: str,
    model_name: str,
    lang: str = "en",
) -> str:
    """Build a generic prompt for protocol generation without a template."""
    if lang == "de":
        json_skeleton = json.dumps({
            "title": "<prägnanter Meeting-Titel>",
            "tldr": "<Zusammenfassung in 2-3 Sätzen>",
            "action_items": [
                {"owner": "<Personenname>", "task": "<konkrete Aufgabe>", "due": "<Datum oder TBD>"}
            ],
            "decisions": ["<Entscheidung 1>"],
            "next_steps": ["<nächster Schritt 1>"],
        }, indent=2, ensure_ascii=False)

        prompt = f"""Du bist ein erfahrener Protokollschreiber für Meetings.

WICHTIGE ANWEISUNGEN / CRITICAL INSTRUCTIONS:
1. SPRACHE / LANGUAGE: Das Transkript ist auf Deutsch. Alle Textinhalte (Titel, Zusammenfassung, Beschreibungen, Aufgaben) MÜSSEN auf Deutsch verfasst werden. Nur die JSON-Schlüssel bleiben auf Englisch.
2. SPEZIFITÄT: Verwende konkrete Namen, Zahlen, Termine und Zitate aus dem Transkript. Vermeide generische Beschreibungen.
3. Verwende die unten aufgeführten bestätigten Sprechernamen, NICHT die Sprecher-IDs.
4. Gib ausschließlich gültiges JSON aus.
{speaker_section}
## Aufgabe
Extrahiere ein strukturiertes Meeting-Protokoll mit diesen Feldern:
- **title**: Prägnanter, beschreibender Meeting-Titel auf Deutsch
- **tldr**: Zusammenfassung in 2-3 Sätzen: Wer war dabei, Hauptthema, wichtigstes Ergebnis, nächster Schritt
- **action_items**: Array von Objekten mit owner (konkreter Personenname), task (konkrete Aufgabe mit Details), due (Datum oder "TBD")
- **decisions**: Array expliziter Vereinbarungen (keine Vorschläge oder Möglichkeiten)
- **next_steps**: Array konkreter nächster Schritte

{_specificity_instructions(lang)}
## JSON-Ausgabeformat
{json_skeleton}

---
## Transkript
{transcript}

---
Erstelle jetzt die JSON-Ausgabe. Alle Werte auf Deutsch, nur die Schlüssel auf Englisch. Sei AUSFÜHRLICH.
"""
    else:
        json_skeleton = json.dumps({
            "title": "<concise meeting title>",
            "tldr": "<2-3 sentence summary>",
            "action_items": [
                {"owner": "<person name>", "task": "<specific task>", "due": "<date or TBD>"}
            ],
            "decisions": ["<decision 1>"],
            "next_steps": ["<next step 1>"],
        }, indent=2, ensure_ascii=False)

        prompt = f"""You are an expert meeting protocol writer.

CRITICAL INSTRUCTIONS:
1. Respond in the SAME LANGUAGE as the transcript.
2. SPECIFICITY: Use concrete names, numbers, dates, and quotes from the transcript. Avoid generic descriptions.
3. Use the confirmed speaker names below, NOT the speaker IDs from the transcript.
4. Output valid JSON only.
{speaker_section}
## Task
Extract a structured meeting protocol with these fields:
- **title**: A concise meeting title
- **tldr**: 2-3 sentence summary covering who met, main topic, key outcome, next step
- **action_items**: Array of objects with owner (specific person), task (concrete action with details), due (date or "TBD")
- **decisions**: Array of explicit agreements made (not suggestions or possibilities)
- **next_steps**: Array of what should happen next

{_specificity_instructions(lang)}
## Output JSON Schema
{json_skeleton}

---
## Transcript
{transcript}

---
Produce the JSON output now. Be THOROUGH and COMPREHENSIVE.
"""
    prompt += _json_formatting_instructions(model_name, lang)
    return prompt


def _build_template_prompt(
    transcript: str,
    schema: Dict[str, Any],
    speaker_section: str,
    model_name: str,
    lang: str = "en",
    template_id: Optional[str] = None,
) -> str:
    """Build a template-aware prompt with per-field extraction instructions."""
    # Separate standard fields from template-specific fields
    field_instructions: List[str] = []
    skeleton: Dict[str, Any] = {}

    for field_name, field_def in schema.items():
        if field_name in _STANDARD_FIELDS:
            _add_standard_field(field_name, field_def, field_instructions, skeleton, lang)
        elif field_name in SECTION_LABELS:
            _add_custom_field(field_name, field_def, field_instructions, skeleton, lang)
        # else: skip unknown fields silently

    # Ensure base fields are always present
    for base_field in ["tldr", "action_items", "decisions"]:
        if base_field not in skeleton:
            if base_field == "tldr":
                if lang == "de":
                    skeleton["tldr"] = "<Zusammenfassung in 2-3 Sätzen>"
                    field_instructions.append(
                        "- **tldr** (string): Zusammenfassung in 2-3 Sätzen: Wer war dabei, Hauptthema, Ergebnis."
                    )
                else:
                    skeleton["tldr"] = "<2-3 sentence summary>"
                    field_instructions.append(
                        "- **tldr** (string): Summarize in 2-3 sentences: who met, main topic, key outcome."
                    )
            elif base_field == "action_items":
                if lang == "de":
                    skeleton["action_items"] = [{"owner": "<Personenname>", "task": "<konkrete Aufgabe>", "due": "TBD"}]
                    field_instructions.append(
                        "- **action_items** (array of objects): Jeweils mit owner, task, due. Jede Aufgabe einzeln auflisten."
                    )
                else:
                    skeleton["action_items"] = [{"owner": "<name>", "task": "<task>", "due": "TBD"}]
                    field_instructions.append(
                        "- **action_items** (array of objects): Each with owner, task, due. List each task separately."
                    )
            elif base_field == "decisions":
                if lang == "de":
                    skeleton["decisions"] = ["<Entscheidung>"]
                    field_instructions.append(
                        "- **decisions** (array of strings): Explizite Vereinbarungen aus dem Meeting."
                    )
                else:
                    skeleton["decisions"] = ["<decision>"]
                    field_instructions.append(
                        "- **decisions** (array of strings): Explicit agreements made."
                    )

    # Always add title
    if lang == "de":
        skeleton = {"title": "<prägnanter Meeting-Titel>", **skeleton}
        field_instructions.insert(0, "- **title** (string): Prägnanter, beschreibender Meeting-Titel auf Deutsch.")
    else:
        skeleton = {"title": "<concise meeting title>", **skeleton}
        field_instructions.insert(0, "- **title** (string): A concise, descriptive meeting title.")

    # Validation rules
    validation = get_validation_rules()
    validation_section = _format_validation_rules(validation)

    json_skeleton = json.dumps(skeleton, indent=2, ensure_ascii=False)

    if lang == "de":
        prompt = f"""Du bist ein erfahrener Protokollschreiber mit tiefem Verständnis für Meeting-Vorlagen.

WICHTIGE ANWEISUNGEN / CRITICAL INSTRUCTIONS:
1. SPRACHE / LANGUAGE: Das Transkript ist auf Deutsch. Alle Textinhalte (Titel, Zusammenfassung, Beschreibungen, Aufgaben) MÜSSEN auf Deutsch verfasst werden. Nur die JSON-Schlüssel bleiben auf Englisch.
2. SPEZIFITÄT: Verwende konkrete Namen, Zahlen, Termine und Zitate aus dem Transkript. Vermeide generische Beschreibungen wie „das Projekt wurde besprochen".
3. Verwende die unten aufgeführten bestätigten Sprechernamen, NICHT die Sprecher-IDs.
4. Gib ausschließlich gültiges JSON aus.
5. Extrahiere ALLE unten aufgeführten Felder. Verwende "TBD" oder leere Arrays für fehlende Informationen.
6. Erfinde KEINE Informationen, die nicht im Transkript stehen.
{speaker_section}
## Zu extrahierende Felder
{chr(10).join(field_instructions)}

{_specificity_instructions(lang, template_id)}
{validation_section}
## JSON-Ausgabeformat
```json
{json_skeleton}
```

---
## Transkript
Lies das folgende Transkript VOLLSTÄNDIG und extrahiere ALLE relevanten Informationen für die oben aufgeführten Felder.

{transcript}

---
Erstelle jetzt die JSON-Ausgabe basierend auf dem gesamten Transkript oben.
Alle Werte auf Deutsch, nur die Schlüssel auf Englisch.
WICHTIG: Sei AUSFÜHRLICH und VOLLSTÄNDIG. Das Transkript ist lang – gehe es Abschnitt für Abschnitt durch. Kurze, oberflächliche Antworten mit nur 2-3 Aktionspunkten sind NICHT akzeptabel für ein Meeting dieser Länge.
"""
    else:
        prompt = f"""You are an expert meeting protocol writer with deep template understanding.

CRITICAL INSTRUCTIONS:
1. Respond in the SAME LANGUAGE as the transcript.
2. SPECIFICITY: Use concrete names, numbers, dates, and quotes from the transcript. Avoid generic descriptions like "the project was discussed".
3. Use the confirmed speaker names below, NOT speaker IDs.
4. Output valid JSON only.
5. Extract ALL fields listed below. Use "TBD" or empty arrays for missing information.
6. Do NOT invent information not in the transcript.
{speaker_section}
## Fields to Extract
{chr(10).join(field_instructions)}

{_specificity_instructions(lang, template_id)}
{validation_section}
## Output JSON Schema
```json
{json_skeleton}
```

---
## Transcript
Read the following transcript COMPLETELY and extract ALL relevant information for the fields listed above.

{transcript}

---
Produce the JSON output based on the entire transcript above.
IMPORTANT: Be THOROUGH and COMPREHENSIVE. The transcript is long – go through it section by section. Short, superficial responses with only 2-3 action items are NOT acceptable for a meeting of this length.
"""
    prompt += _json_formatting_instructions(model_name, lang)
    return prompt


_PROP_PLACEHOLDERS_DE = {
    "owner": "<Personenname>",
    "task": "<konkrete Aufgabe>",
    "due": "<Datum oder TBD>",
    "name": "<Personenname>",
    "description": "<Beschreibung>",
    "priority": "<Priorität>",
    "status": "<Status>",
}


def _placeholder_for_prop(prop_names: list, lang: str) -> Dict[str, str]:
    """Generate language-aware placeholder dict for object properties."""
    if lang == "de":
        return {k: _PROP_PLACEHOLDERS_DE.get(k, f"<{k}>") for k in prop_names}
    return {k: f"<{k}>" for k in prop_names}


def _add_standard_field(
    field_name: str,
    field_def: Any,
    instructions: List[str],
    skeleton: Dict[str, Any],
    lang: str = "en",
) -> None:
    """Add extraction instructions for a standard Protocol field."""
    if field_name == "metadata":
        return

    if field_name == "full_transcript":
        return

    if not isinstance(field_def, dict):
        return

    field_type = field_def.get("type", "string")
    extraction_prompt = field_def.get("extraction_prompt", "")
    extraction_patterns = field_def.get("extraction_patterns", [])

    # Language-aware placeholder labels
    _ph = {
        "summary": "<Zusammenfassung>" if lang == "de" else "<summary>",
        "decision": "<Entscheidung>" if lang == "de" else "<decision>",
        "next_step": "<nächster Schritt>" if lang == "de" else "<next step>",
    }

    if field_name == "tldr":
        max_sentences = field_def.get("max_sentences", 4)
        desc = f"(string, max {max_sentences} sentences)"
        if extraction_prompt:
            desc += f": {extraction_prompt.strip()}"
        instructions.append(f"- **tldr** {desc}")
        skeleton["tldr"] = _ph["summary"]

    elif field_name == "decisions":
        desc = "(array of strings)"
        if extraction_prompt:
            desc += f": {extraction_prompt.strip()}"
        if extraction_patterns:
            desc += f"\n  Keywords: {', '.join(extraction_patterns[:6])}"
        instructions.append(f"- **decisions** {desc}")
        skeleton["decisions"] = [_ph["decision"]]

    elif field_name == "action_items":
        items_def = field_def.get("items", {})
        props = items_def.get("properties", {})
        prop_names = list(props.keys()) if props else ["owner", "task", "due"]
        desc = f"(array of objects with: {', '.join(prop_names)})"
        if extraction_prompt:
            desc += f": {extraction_prompt.strip()}"
        if extraction_patterns:
            desc += f"\n  Keywords: {', '.join(extraction_patterns[:6])}"
        instructions.append(f"- **action_items** {desc}")
        _ph_props = _placeholder_for_prop(prop_names, lang)
        skeleton["action_items"] = [_ph_props]

    elif field_name == "next_steps":
        _add_next_steps(field_def, instructions, skeleton, lang)

    elif field_name == "follow_up_actions":
        items_def = field_def.get("items", {})
        props = items_def.get("properties", {})
        prop_names = list(props.keys()) if props else ["owner", "task", "due"]
        instructions.append(f"- **follow_up_actions** (array of objects with: {', '.join(prop_names)})")
        _ph_props = _placeholder_for_prop(prop_names, lang)
        skeleton["follow_up_actions"] = [_ph_props]


def _add_next_steps(
    field_def: Any,
    instructions: List[str],
    skeleton: Dict[str, Any],
    lang: str = "en",
) -> None:
    """Handle next_steps which can be string, array of strings, or array of objects."""
    if not isinstance(field_def, dict):
        return

    field_type = field_def.get("type", "string")
    extraction_prompt = field_def.get("extraction_prompt", "")
    _ph = "<nächste Schritte>" if lang == "de" else "<next steps>"
    _ph_item = "<nächster Schritt>" if lang == "de" else "<next step>"

    if field_type == "string":
        desc = "(string)"
        if extraction_prompt:
            desc += f": {extraction_prompt.strip()}"
        instructions.append(f"- **next_steps** {desc}")
        skeleton["next_steps"] = _ph
    elif field_type == "array":
        items = field_def.get("items", {})
        if isinstance(items, dict) and items.get("type") == "object":
            props = items.get("properties", {})
            prop_names = list(props.keys()) if props else ["task"]
            instructions.append(f"- **next_steps** (array of objects with: {', '.join(prop_names)})")
            skeleton["next_steps"] = [_placeholder_for_prop(prop_names, lang)]
        else:
            instructions.append(f"- **next_steps** (array of strings)")
            skeleton["next_steps"] = [_ph_item]


def _add_custom_field(
    field_name: str,
    field_def: Any,
    instructions: List[str],
    skeleton: Dict[str, Any],
    lang: str = "en",
) -> None:
    """Add extraction instructions for a template-specific custom field."""
    if not isinstance(field_def, dict):
        return

    label, _ = SECTION_LABELS[field_name]
    field_type = field_def.get("type", "string")
    extraction_prompt = field_def.get("extraction_prompt", "")
    extraction_patterns = field_def.get("extraction_patterns", [])

    type_desc = _describe_field_type(field_name, field_def)
    desc = f"{type_desc}"
    if extraction_prompt:
        desc += f": {extraction_prompt.strip()}"
    if extraction_patterns:
        desc += f"\n  Keywords: {', '.join(extraction_patterns[:8])}"

    instructions.append(f"- **{field_name}** [{label}] {desc}")
    skeleton[field_name] = _skeleton_for_type(field_def, lang)


def _describe_field_type(field_name: str, field_def: Dict[str, Any]) -> str:
    """Generate a human-readable type description for a field."""
    field_type = field_def.get("type", "string")

    if field_type == "string":
        return "(string)"
    elif field_type == "enum":
        values = field_def.get("values", [])
        return f"(one of: {', '.join(str(v) for v in values)})"
    elif field_type == "object":
        props = field_def.get("properties", {})
        if props:
            prop_descs = []
            for pk, pv in props.items():
                if isinstance(pv, dict):
                    pt = pv.get("type", "string")
                    if pt == "enum":
                        vals = pv.get("values", [])
                        prop_descs.append(f"{pk}: one of [{', '.join(str(v) for v in vals)}]")
                    elif pt == "array":
                        prop_descs.append(f"{pk}: array")
                    else:
                        prop_descs.append(f"{pk}: {pt}")
                else:
                    prop_descs.append(pk)
            return f"(object with: {', '.join(prop_descs)})"
        return "(object)"
    elif field_type == "array":
        items = field_def.get("items", {})
        if isinstance(items, dict):
            item_type = items.get("type", "string")
            if item_type == "object":
                props = items.get("properties", {})
                if props:
                    prop_names = []
                    for pk, pv in props.items():
                        if isinstance(pv, dict) and pv.get("type") == "enum":
                            vals = pv.get("values", [])
                            prop_names.append(f"{pk}: one of [{', '.join(str(v) for v in vals)}]")
                        else:
                            prop_names.append(pk)
                    return f"(array of objects with: {', '.join(prop_names)})"
                return "(array of objects)"
            elif item_type == "string":
                return "(array of strings)"
        return "(array)"
    return f"({field_type})"


def _skeleton_for_type(field_def: Dict[str, Any], lang: str = "en") -> Any:
    """Generate a JSON skeleton value for a field type."""
    field_type = field_def.get("type", "string")
    _ellipsis = "<...>"
    _item_ph = "<Eintrag>" if lang == "de" else "<item>"

    if field_type == "string":
        return _ellipsis
    elif field_type == "enum":
        values = field_def.get("values", [])
        return values[0] if values else _ellipsis
    elif field_type == "object":
        props = field_def.get("properties", {})
        if props:
            obj = {}
            for pk, pv in props.items():
                if isinstance(pv, dict):
                    obj[pk] = _skeleton_for_type(pv, lang)
                else:
                    obj[pk] = _PROP_PLACEHOLDERS_DE.get(pk, f"<{pk}>") if lang == "de" else f"<{pk}>"
            return obj
        return {}
    elif field_type == "array":
        items = field_def.get("items", {})
        if isinstance(items, dict):
            item_type = items.get("type", "string")
            if item_type == "object":
                props = items.get("properties", {})
                if props:
                    obj = {}
                    for pk, pv in props.items():
                        if isinstance(pv, dict):
                            obj[pk] = _skeleton_for_type(pv, lang)
                        else:
                            obj[pk] = _PROP_PLACEHOLDERS_DE.get(pk, f"<{pk}>") if lang == "de" else f"<{pk}>"
                    return [obj]
                return [{}]
            return [_item_ph]
        return []
    return _ellipsis


def _format_validation_rules(validation: Dict[str, Any]) -> str:
    """Format validation rules from the YAML into prompt text."""
    if not validation:
        return ""

    lines = ["## Quality Rules"]
    for section_name, section_data in validation.items():
        if isinstance(section_data, dict) and "rules" in section_data:
            rules = section_data["rules"]
            for rule in rules:
                lines.append(f"- {rule}")

    if len(lines) <= 1:
        return ""
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Two-pass prompt builders
# ---------------------------------------------------------------------------
#
# Strategy comparison (see also docstrings below):
#
#   TWO-PASS (structure-then-extract):
#     Best when the transcript is long (>30 min) and the template has many
#     fields. Pass 1 produces a topic-level outline so Pass 2 can focus on
#     filling in structured fields without losing track of distant context.
#     Works well within a single context window.
#
#   CHUNKING (split-by-time, extract-per-chunk, merge):
#     Best when the transcript exceeds the model's effective context window
#     or when latency matters less than cost (smaller model on each chunk).
#     Requires a merge step that can introduce duplicates.  Not implemented
#     yet, but the two-pass design is compatible: Pass 1 could run on chunks
#     independently, producing per-chunk outlines that get merged before
#     Pass 2 runs once on the unified structure + full transcript.
#
#   COMBINED (chunk + two-pass):
#     For very long meetings (>2 hours / >120k chars), run Pass 1 on chunks,
#     merge the outlines, then run Pass 2 on the merged outline + full
#     transcript. This is the eventual target architecture.


def build_structure_pass_prompt(
    transcript: str,
    speaker_names: list[str],
    model_name: str = "",
) -> str:
    """
    Build the Pass 1 prompt: ask the LLM to analyze the transcript and
    produce a structured meeting outline.

    The outline captures *what* was discussed, *by whom*, and *when* --
    without yet mapping into template fields.  This lets the model focus
    on comprehension rather than formatting.

    The output schema is intentionally simple and template-agnostic so it
    can be reused regardless of which template is selected in Pass 2.

    If chunking is added later, this function can be called once per chunk
    and the resulting outlines merged before Pass 2.

    Args:
        transcript: Full meeting transcript text
        speaker_names: Confirmed speaker names
        model_name: LLM model name (used for formatting hints)

    Returns:
        Complete prompt string for the structure pass
    """
    lang = _detect_language(transcript)

    # Speaker mapping (reuse the same pattern as build_template_aware_prompt)
    speaker_section = ""
    if speaker_names:
        if lang == "de":
            speaker_section = "\n## Sprecher-Zuordnung\n"
            speaker_section += "Das Transkript verwendet Sprecher-IDs. Ersetze sie durch diese bestätigten Namen:\n"
        else:
            speaker_section = "\n## Speaker Name Mapping\n"
            speaker_section += "The transcript uses speaker IDs. Replace them with these confirmed names:\n"
        for i, name in enumerate(speaker_names):
            speaker_section += f"- Speaker {i} / Sprecher {i} → {name}\n"

    # Output schema for the structure pass
    structure_skeleton = json.dumps({
        "meeting_title": "<concise title>",
        "duration_estimate": "<e.g. 45 minutes>",
        "participants_active": ["<names of people who spoke>"],
        "topics": [
            {
                "topic_title": "<descriptive topic name>",
                "time_range": "<e.g. 00:00-12:30 or 'early in meeting'>",
                "speakers_involved": ["<name1>", "<name2>"],
                "summary": "<2-4 sentences: what was discussed, what positions were taken>",
                "key_statements": [
                    "<direct quote or close paraphrase with speaker attribution>"
                ],
                "decisions_made": ["<any explicit agreement reached on this topic>"],
                "action_items_mentioned": [
                    "<any task assigned, with who and what>"
                ],
                "open_questions": ["<unresolved points>"],
            }
        ],
        "cross_cutting_themes": ["<themes that span multiple topics>"],
        "overall_tone": "<e.g. constructive, contentious, exploratory>",
    }, indent=2, ensure_ascii=False)

    if lang == "de":
        prompt = f"""Du bist ein erfahrener Meeting-Analyst. Deine Aufgabe ist es, das folgende Transkript zu analysieren und eine detaillierte inhaltliche Gliederung zu erstellen.

WICHTIGE ANWEISUNGEN:
1. SPRACHE: Alle Textinhalte MÜSSEN auf Deutsch verfasst werden. Nur die JSON-Schlüssel bleiben auf Englisch.
2. VOLLSTÄNDIGKEIT: Gehe das GESAMTE Transkript durch. Überspringe KEINE Themen, auch nicht kurze Nebendiskussionen.
3. GENAUIGKEIT: Verwende konkrete Namen, Zahlen, Systemnamen und möglichst wörtliche Zitate.
4. GRANULARITÄT: Lieber zu viele Topics als zu wenige. Jeder thematische Wechsel verdient einen eigenen Eintrag.
5. Verwende die bestätigten Sprechernamen, NICHT die Sprecher-IDs.
6. Gib ausschließlich gültiges JSON aus.
{speaker_section}
## Aufgabe
Analysiere das Transkript und erstelle eine strukturierte Gliederung. Für JEDES besprochene Thema:
- Wer hat daran teilgenommen?
- Was wurde gesagt (Kernaussagen, möglichst nah am Wortlaut)?
- Welche Entscheidungen wurden getroffen?
- Welche Aufgaben wurden vergeben?
- Welche Fragen blieben offen?

## JSON-Ausgabeformat
```json
{structure_skeleton}
```

---
## Transkript
{transcript}

---
Erstelle jetzt die JSON-Gliederung. Sei AUSFÜHRLICH und DETAILLIERT. Bei einem langen Meeting erwarte ich 8-15+ Topics.
Alle Werte auf Deutsch, nur die Schlüssel auf Englisch.
"""
    else:
        prompt = f"""You are an expert meeting analyst. Your task is to analyze the following transcript and produce a detailed structural outline.

CRITICAL INSTRUCTIONS:
1. LANGUAGE: Respond in the SAME LANGUAGE as the transcript.
2. COMPLETENESS: Go through the ENTIRE transcript. Do NOT skip any topics, even brief side discussions.
3. ACCURACY: Use concrete names, numbers, system names, and near-verbatim quotes.
4. GRANULARITY: More topics is better than fewer. Each thematic shift deserves its own entry.
5. Use the confirmed speaker names, NOT speaker IDs.
6. Output valid JSON only.
{speaker_section}
## Task
Analyze the transcript and produce a structured outline. For EACH topic discussed:
- Who participated?
- What was said (key statements, as close to verbatim as possible)?
- What decisions were made?
- What tasks were assigned?
- What questions remain open?

## Output JSON Schema
```json
{structure_skeleton}
```

---
## Transcript
{transcript}

---
Produce the JSON outline now. Be THOROUGH and DETAILED. For a long meeting, expect 8-15+ topics.
"""

    prompt += _json_formatting_instructions(model_name, lang)
    return prompt


def build_extraction_pass_prompt(
    transcript: str,
    structure_json: dict,
    template_id: Optional[str],
    speaker_names: list[str],
    model_name: str = "",
) -> str:
    """
    Build the Pass 2 prompt: given the structural outline from Pass 1 and
    the original transcript, extract the final protocol in the template's
    JSON schema.

    This prompt is shorter on comprehension instructions (the LLM already
    did that work in Pass 1) and heavier on extraction precision and
    field-level formatting.

    Args:
        transcript: Full meeting transcript text
        structure_json: The outline dict produced by Pass 1
        template_id: Template ID (e.g. "CLIENT_TECHNICAL") or None
        speaker_names: Confirmed speaker names
        model_name: LLM model name

    Returns:
        Complete prompt string for the extraction pass
    """
    schema = get_raw_template_schema(template_id) if template_id else None
    lang = _detect_language(transcript)

    # Build field instructions + skeleton (reuse existing helpers)
    field_instructions: list[str] = []
    skeleton: dict[str, Any] = {}

    if schema:
        for field_name, field_def in schema.items():
            if field_name in _STANDARD_FIELDS:
                _add_standard_field(field_name, field_def, field_instructions, skeleton, lang)
            elif field_name in SECTION_LABELS:
                _add_custom_field(field_name, field_def, field_instructions, skeleton, lang)

    # Ensure base fields
    for base_field in ["tldr", "action_items", "decisions"]:
        if base_field not in skeleton:
            if base_field == "tldr":
                skeleton["tldr"] = "<Zusammenfassung>" if lang == "de" else "<summary>"
                instr = "- **tldr** (string): " + (
                    "Zusammenfassung in 2-3 Sätzen." if lang == "de"
                    else "2-3 sentence summary."
                )
                field_instructions.append(instr)
            elif base_field == "action_items":
                ph = {"owner": "<Personenname>", "task": "<konkrete Aufgabe>", "due": "TBD"} if lang == "de" else {"owner": "<name>", "task": "<task>", "due": "TBD"}
                skeleton["action_items"] = [ph]
                instr = "- **action_items** (array of objects): " + (
                    "Jeweils mit owner, task, due." if lang == "de"
                    else "Each with owner, task, due."
                )
                field_instructions.append(instr)
            elif base_field == "decisions":
                skeleton["decisions"] = ["<Entscheidung>" if lang == "de" else "<decision>"]
                instr = "- **decisions** (array of strings): " + (
                    "Explizite Vereinbarungen." if lang == "de"
                    else "Explicit agreements made."
                )
                field_instructions.append(instr)

    # Title
    if lang == "de":
        skeleton = {"title": "<prägnanter Meeting-Titel>", **skeleton}
        field_instructions.insert(0, "- **title** (string): Prägnanter Meeting-Titel auf Deutsch.")
    else:
        skeleton = {"title": "<concise meeting title>", **skeleton}
        field_instructions.insert(0, "- **title** (string): A concise meeting title.")

    json_skeleton = json.dumps(skeleton, indent=2, ensure_ascii=False)
    structure_text = json.dumps(structure_json, indent=2, ensure_ascii=False)

    # Speaker section (compact for pass 2 -- the structure already uses names)
    speaker_list = ", ".join(speaker_names) if speaker_names else "unknown"

    # Validation rules
    validation = get_validation_rules()
    validation_section = _format_validation_rules(validation)

    if lang == "de":
        prompt = f"""Du bist ein erfahrener Protokollschreiber. Du erhältst zwei Eingaben:
1. Eine **inhaltliche Gliederung** des Meetings (aus einer Voranalyse)
2. Das **Original-Transkript** als Referenz

Deine Aufgabe: Erstelle das finale Meeting-Protokoll im vorgegebenen JSON-Format.

WICHTIGE ANWEISUNGEN:
1. SPRACHE: Alle Textinhalte auf Deutsch. Nur JSON-Schlüssel auf Englisch.
2. Die Gliederung ist deine Hauptquelle für Struktur und Themen. Das Transkript ist deine Quelle für exakte Zitate, Namen und Details.
3. SPEZIFITÄT: Konkrete Namen, Zahlen, Systemnamen, Termine. Keine generischen Beschreibungen.
4. VOLLSTÄNDIGKEIT: Jedes Topic aus der Gliederung muss sich in mindestens einem Feld des Protokolls wiederfinden.
5. Erfinde KEINE Informationen, die weder in der Gliederung noch im Transkript stehen.
6. Gib ausschließlich gültiges JSON aus.

Teilnehmer: {speaker_list}

## Inhaltliche Gliederung (Voranalyse)
```json
{structure_text}
```

## Zu extrahierende Felder
{chr(10).join(field_instructions)}

{_specificity_instructions(lang, template_id)}
{validation_section}
## JSON-Ausgabeformat
```json
{json_skeleton}
```

---
## Original-Transkript (als Referenz für Details und Zitate)
{transcript}

---
Erstelle jetzt die JSON-Ausgabe. Nutze die Gliederung als Leitfaden und das Transkript für Details.
WICHTIG: Sei AUSFÜHRLICH. Jedes Topic aus der Gliederung muss abgedeckt sein. Kurze Antworten mit nur 2-3 Aktionspunkten sind NICHT akzeptabel.
"""
    else:
        prompt = f"""You are an expert meeting protocol writer. You receive two inputs:
1. A **structural outline** of the meeting (from a prior analysis)
2. The **original transcript** as reference

Your task: Produce the final meeting protocol in the specified JSON format.

CRITICAL INSTRUCTIONS:
1. LANGUAGE: Respond in the same language as the transcript.
2. The outline is your primary source for structure and topics. The transcript is your source for exact quotes, names, and details.
3. SPECIFICITY: Concrete names, numbers, system names, dates. No generic descriptions.
4. COMPLETENESS: Every topic from the outline must appear in at least one field of the protocol.
5. Do NOT invent information not in the outline or transcript.
6. Output valid JSON only.

Participants: {speaker_list}

## Structural Outline (Prior Analysis)
```json
{structure_text}
```

## Fields to Extract
{chr(10).join(field_instructions)}

{_specificity_instructions(lang, template_id)}
{validation_section}
## Output JSON Schema
```json
{json_skeleton}
```

---
## Original Transcript (reference for details and quotes)
{transcript}

---
Produce the JSON output now. Use the outline as your guide and the transcript for details.
IMPORTANT: Be THOROUGH. Every topic from the outline must be covered. Short responses with only 2-3 action items are NOT acceptable.
"""

    prompt += _json_formatting_instructions(model_name, lang)
    return prompt


def _json_formatting_instructions(model_name: str, lang: str = "en") -> str:
    """
    Add explicit JSON formatting instructions for open-source models
    that may not support response_format=json_object.
    """
    model_lower = model_name.lower() if model_name else ""
    is_open_source = any(
        name in model_lower
        for name in ["llama", "mistral", "mixtral", "qwen", "gemma", "phi"]
    )

    if is_open_source:
        if lang == "de":
            return (
                "\n\nWICHTIG / IMPORTANT FORMATTING: "
                "Deine Antwort muss ausschließlich gültiges JSON sein. "
                "Beginne mit `{` und ende mit `}`. "
                "Kein Text, keine Erklärungen, kein Markdown vor oder nach dem JSON. "
                "Alle Textinhalte auf Deutsch, nur JSON-Schlüssel auf Englisch."
            )
        return (
            "\n\nIMPORTANT FORMATTING: Your response must be ONLY valid JSON. "
            "Start your response with `{` and end with `}`. "
            "Do NOT include any text, explanation, or markdown before or after the JSON."
        )
    return ""
