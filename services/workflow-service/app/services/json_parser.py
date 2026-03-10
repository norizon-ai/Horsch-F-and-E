"""
Robust JSON extraction from LLM responses.

Handles responses from models that may not support response_format=json_object
(e.g. IONOS/vLLM-hosted open-source models). Falls back through multiple
parsing strategies.
"""

import json
import logging
import re

logger = logging.getLogger(__name__)


def _strip_trailing_commas(text: str) -> str:
    """Remove trailing commas before } or ] (common Llama output artifact)."""
    return re.sub(r',\s*([}\]])', r'\1', text)


def extract_json_from_response(content: str) -> dict:
    """
    Extract a JSON object from an LLM response string.

    Tries three strategies in order:
    1. Direct json.loads (model returned pure JSON)
    2. Strip markdown code fences (```json ... ```)
    3. Find outermost {...} by brace-counting

    Args:
        content: Raw LLM response text

    Returns:
        Parsed dict

    Raises:
        ValueError: If no valid JSON object can be extracted
    """
    content = content.strip()

    # Strategy 1: Direct parse
    try:
        cleaned = _strip_trailing_commas(content)
        result = json.loads(cleaned)
        if isinstance(result, dict):
            return result
    except json.JSONDecodeError:
        pass

    # Strategy 2: Strip markdown code fences
    fenced = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", content, re.DOTALL)
    if fenced:
        try:
            cleaned = _strip_trailing_commas(fenced.group(1).strip())
            result = json.loads(cleaned)
            if isinstance(result, dict):
                logger.debug("Extracted JSON from markdown code fence")
                return result
        except json.JSONDecodeError:
            pass

    # Strategy 3: Brace-counting to find outermost { ... }
    start = content.find("{")
    if start != -1:
        depth = 0
        in_string = False
        escape_next = False
        for i in range(start, len(content)):
            ch = content[i]
            if escape_next:
                escape_next = False
                continue
            if ch == "\\":
                escape_next = True
                continue
            if ch == '"' and not escape_next:
                in_string = not in_string
                continue
            if in_string:
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    candidate = content[start:i + 1]
                    candidate = _strip_trailing_commas(candidate)
                    try:
                        result = json.loads(candidate)
                        if isinstance(result, dict):
                            logger.debug("Extracted JSON via brace-counting")
                            return result
                    except json.JSONDecodeError:
                        break

    raise ValueError(
        f"Could not extract valid JSON from LLM response. "
        f"Response starts with: {content[:200]!r}"
    )
