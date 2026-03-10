"""Generate per-speaker audio snippets using FFmpeg."""

import logging
import subprocess
from pathlib import Path
from typing import Optional, Tuple

from app.config import settings

logger = logging.getLogger(__name__)


class SnippetGenerator:
    """Generates audio snippets for speaker samples using FFmpeg."""

    def __init__(self, job_id: str):
        self.job_id = job_id
        self.snippets_dir = Path(settings.data_dir) / "jobs" / job_id / "snippets"
        self.snippets_dir.mkdir(parents=True, exist_ok=True)

    def generate_snippet(
        self,
        input_file: str,
        speaker_id: str,
        start_time: float,
        duration: Optional[float] = None,
    ) -> Optional[str]:
        """Generate an MP3 audio snippet for a speaker."""
        if duration is None:
            duration = settings.snippet_duration_secs

        output_file = self.snippets_dir / f"{speaker_id}.mp3"

        try:
            cmd = [
                "ffmpeg",
                "-ss", str(start_time),
                "-i", input_file,
                "-t", str(duration),
                "-acodec", "libmp3lame",
                "-y",
                output_file.as_posix()
            ]

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=settings.ffmpeg_timeout_secs
            )

            if result.returncode != 0:
                logger.error(f"FFmpeg failed for speaker {speaker_id}: {result.stderr.decode()}")
                return None

            relative_path = f"/data/jobs/{self.job_id}/snippets/{speaker_id}.mp3"
            logger.info(f"Generated snippet for speaker {speaker_id}: {relative_path}")
            return relative_path

        except subprocess.TimeoutExpired:
            logger.error(f"FFmpeg timeout for speaker {speaker_id}")
            return None
        except Exception as e:
            logger.error(f"Snippet generation failed for speaker {speaker_id}: {e}")
            return None

    def find_best_utterance(self, speaker_utterances: list) -> Optional[Tuple[float, str]]:
        """Find the longest clear utterance from a pre-filtered speaker list."""
        if not speaker_utterances:
            return None

        candidates = speaker_utterances[:settings.snippet_max_utterances]
        longest = max(candidates, key=lambda u: len(u.get("transcript", "")))

        start_time = longest.get("start", 0)
        transcript = longest.get("transcript", "")[:settings.snippet_text_max_chars]

        return (start_time, transcript)
