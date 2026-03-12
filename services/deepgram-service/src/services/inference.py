"""
Strict-Grounding Speaker Inference System

Pipeline:
  0. Clean diarization errors
  1. Extract all unique speaker IDs
  2. Format full transcript
  3. Single LLM call — must analyze EVERY speaker ID
  4. Quote verification: discard any name whose evidence_quote is not
     a substring of the actual transcript (anti-hallucination shield)
"""

import difflib
import json
import logging
import re
from typing import Dict, Tuple

from openai import OpenAI

from src.config import settings
from src.models.schemas import UnifiedTranscript
from src.services.diarization_cleaner import DiarizationCleaner

logger = logging.getLogger(__name__)

# Junk-name filter — discard generic placeholder names
_JUNK_RE = re.compile(
    r"^(Speaker|Sprecher|Unknown|Unbekannt|Anonymous|Moderator|"
    r"Interviewer|Guest|Person|Host)\s*\d*$",
    re.IGNORECASE,
)


def _quote_verified(quote: str, text: str, threshold: float = 0.80) -> bool:
    """
    Check if quote exists in text with fuzzy matching to tolerate minor ASR/LLM typos.
    Uses a sliding window of quote-length over text and computes SequenceMatcher ratio.
    Returns True if best match ratio >= threshold.
    """
    if not quote:
        return False
    # Normalize whitespace
    q = " ".join(quote.split()).lower()
    t = " ".join(text.split()).lower()
    # Exact match fast path
    if q in t:
        return True
    # Sliding window fuzzy search
    q_len = len(q)
    best = 0.0
    step = max(1, q_len // 4)  # step by quarter-length for speed
    for i in range(0, max(1, len(t) - q_len + 1), step):
        window = t[i:i + q_len]
        ratio = difflib.SequenceMatcher(None, q, window).ratio()
        if ratio > best:
            best = ratio
        if best >= threshold:
            return True
    return best >= threshold


_SYSTEM_PROMPT = """\
You are a forensic transcript analyst.

INPUT: A list of Speaker IDs and a dialogue transcript.
TASK: Identify the real name of EACH speaker in the provided list.

RULES:
1. NO HALLUCINATIONS. You must find EXPLICIT evidence in the text:
   - Self-introduction: "I am [Name]", "My name is [Name]", "This is [Name] speaking"
   - Confirmed direct address: another speaker calls them by name AND they respond
2. DIFFERENTIATION — BEING vs. ADDRESSING:
   - If [Speaker 0] says "Hi Elon", Speaker 0 is NOT Elon. Speaker 0 is addressing Elon.
   - Only assign a name to the speaker who IS that person.
3. QUOTE REQUIRED. For every identified name you MUST return the EXACT substring from the
   transcript that proves it. Copy-paste it character-for-character.
4. UNKNOWNS. If a speaker's name is not explicitly stated, set name to "Unknown".
   Do NOT guess the name, but DO describe their apparent role in the reasoning field.
   IMPORTANT: Use a CONCISE 1-2 word role description in the SAME LANGUAGE as the transcript.
   Examples (English): "Host", "Expert", "Manager", "Participant", "Moderator"
   Examples (German): "Gastgeber", "Experte", "Manager", "Teilnehmer", "Moderator"
   Base role descriptions only on what they actually say and how others respond to them.
5. EXHAUSTIVE. You MUST return one JSON entry for every Speaker ID in the requested list.
   Omitting a speaker is an error.
6. CONFIDENCE. Only set confidence > 0.7 if the evidence is unambiguous.
7. UNIQUE NAMES. Never assign the same name to two different speakers. If the same name appears
   to match multiple speakers, only assign it to the one with the strongest evidence. Set the
   others to "Unknown".
8. LANGUAGE MATCHING. All text in your response (names, reasoning) must be in the SAME LANGUAGE
   as the transcript. If the transcript is in German, respond in German. If English, respond in English.

JSON OUTPUT FORMAT (return ONLY this, no extra text):
{
  "analysis": [
    {
      "speaker_id": 0,
      "name": "Exact Name Found or Unknown",
      "confidence": 0.0,
      "evidence_quote": "The exact text substring used as proof (empty string if Unknown)",
      "reasoning": "1-2 word role description in transcript language (e.g., 'Host', 'Expert', 'Moderator')"
    }
  ]
}
"""


def _spk_num(speaker_id: str) -> int:
    """Extract integer from speaker ID string: 'speaker_0' → 0, '3' → 3."""
    m = re.search(r"\d+", str(speaker_id))
    return int(m.group()) if m else -1


def _load_transcript_text(transcript: UnifiedTranscript) -> str:
    """Format transcript segments into dialogue text for LLM input."""
    lines = [f"[Speaker {_spk_num(seg.speaker)}]: {seg.text}" for seg in transcript.segments]
    return "\n".join(lines)


class InferenceService:
    """
    Strict-grounding speaker inference.

    Prevents hallucinations by verifying every LLM-returned evidence quote
    exists verbatim in the transcript before accepting a name.
    """

    def __init__(self):
        self.cleaner = DiarizationCleaner()
        if not settings.openai_api_key:
            logger.warning("No OpenAI API key configured — inference disabled")
            self.client = None
        else:
            self.client = OpenAI(api_key=settings.openai_api_key)
            logger.info("InferenceService initialized (strict-grounding mode)")

    def infer_speaker_names(
        self,
        transcript: UnifiedTranscript,
        max_chars: int | None = None,
        language: str = "en",
    ) -> Tuple[Dict[int, Tuple[str, float]], Dict[int, str]]:
        """
        Analyze transcript and return verified speaker names.

        Args:
            transcript: The transcript to analyze
            max_chars: Maximum characters to send to LLM
            language: UI language for hints (de/en)

        Returns:
            names: Dict[speaker_id, (name, confidence)]
            hints: Dict[speaker_id, reasoning_with_quote]
        """
        if not self.client:
            logger.info("Skipping inference — no API key")
            return {}, {}

        try:
            # Phase 0: Clean diarization noise
            logger.info("Phase 0: Cleaning diarization...")
            cleaned, _ = self.cleaner.cleanup_diarization(transcript)

            # Phase 1: Extract speaker IDs (as integers) and format transcript
            speaker_ids = sorted({_spk_num(seg.speaker) for seg in cleaned.segments})
            char_limit = max_chars or settings.inference_max_chars
            full_text = _load_transcript_text(cleaned)[:char_limit]
            logger.info(
                f"Phase 1: {len(speaker_ids)} speakers, "
                f"{len(full_text)} chars — IDs: {speaker_ids}"
            )

            # Phase 2: Build prompt and call LLM
            lang_full = "German" if language == "de" else "English"
            user_msg = (
                f"CRITICAL: Respond in {lang_full}. All text fields (reasoning, hints) MUST be in {lang_full}.\n\n"
                f"Analyze the following Speaker IDs: {speaker_ids}\n\n"
                f"Transcript:\n{full_text}\n\n"
                f"Return one JSON entry for EACH of these Speaker IDs: {speaker_ids}"
            )

            logger.info(f"Phase 2: Calling LLM (language={language})...")
            response = self.client.chat.completions.create(
                model=settings.openai_model,
                messages=[
                    {"role": "system", "content": _SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0.0,
                max_tokens=2000,
                response_format={"type": "json_object"},
            )

            content = response.choices[0].message.content.strip()
            logger.info(f"Phase 2: Response received ({len(content)} chars)")
            logger.debug(f"LLM raw response: {content}")

            # Phase 3: Parse + quote verification (anti-hallucination shield)
            data = json.loads(content)
            analysis = data.get("analysis", [])
            logger.info(f"Phase 3: Verifying {len(analysis)} entries...")

            names: Dict[int, Tuple[str, float]] = {}
            hints: Dict[int, str] = {}

            for item in analysis:
                spk_id = _spk_num(item.get("speaker_id", -1))
                name = str(item.get("name", "")).strip()
                confidence = float(item.get("confidence", 0.0))
                quote = str(item.get("evidence_quote", "")).strip()
                reasoning = str(item.get("reasoning", ""))

                if spk_id < 0:
                    continue

                # Skip unknowns and junk names — but still record hint
                if not name or name.lower() in {"unknown", "anonymous"} or _JUNK_RE.match(name):
                    # Use concise role description from LLM
                    hints[spk_id] = reasoning if reasoning else "Unknown"
                    logger.debug(f"Speaker {spk_id}: no name identified, role: {reasoning}")
                    continue

                # ANTI-HALLUCINATION: verify quote exists in transcript (fuzzy)
                if quote:
                    if not _quote_verified(quote, full_text):
                        logger.warning(
                            f"Hallucination detected — Speaker {spk_id}: "
                            f"quote not verified in transcript (fuzzy < 80%). "
                            f"Discarding name '{name}'. Quote: '{quote[:100]}'"
                        )
                        # Fall back to role description if verification fails
                        hints[spk_id] = reasoning if reasoning else "Unknown"
                        continue
                else:
                    # Fall back to role description if no quote provided
                    hints[spk_id] = reasoning if reasoning else "Unknown"
                    logger.warning(
                        f"Speaker {spk_id}: name '{name}' rejected — no evidence quote provided"
                    )
                    continue

                names[spk_id] = (name, confidence)
                # Use concise role description without quote
                hints[spk_id] = reasoning
                logger.info(
                    f"Speaker {spk_id}: '{name}' (conf={confidence:.2f}) "
                    f"— quote verified"
                )

            logger.info(f"Phase 3 complete: {len(names)} verified name(s): {names}")
            return names, hints

        except Exception as e:
            logger.error(f"Speaker inference failed: {e}", exc_info=True)
            return {}, {}


__all__ = ["InferenceService"]
