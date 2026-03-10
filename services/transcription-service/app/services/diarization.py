"""
Diarization Cleanup Module

Fixes common diarization errors before speaker inference:
1. Remove noise segments (too short, too few words)
2. Merge micro-segments from same speaker with small gaps
3. Remove orphan segments (very short segments surrounded by same speaker)
4. Stitch adjacent same-speaker segments for maximum LLM context
"""

import logging
from dataclasses import dataclass
from typing import List, Tuple

from app.models import UnifiedTranscript, Segment

logger = logging.getLogger(__name__)

# Diarization cleanup thresholds
MERGE_GAP_THRESHOLD = 1.0  # seconds - merge if gap < 1s
NOISE_DURATION_THRESHOLD = 0.5  # seconds - remove if < 0.5s
NOISE_WORD_THRESHOLD = 3  # words - remove if < 3 words
ORPHAN_VERY_SHORT_THRESHOLD = 0.5  # seconds - very short orphan threshold
ORPHAN_NOISE_THRESHOLD = 1.0  # seconds - noise orphan threshold (2 words or less)


@dataclass
class CleanupMetrics:
    """Track diarization cleanup performance."""
    original_segments: int
    final_segments: int
    noise_removed: int
    micro_merged: int
    orphans_removed: int
    stitched_segments: int

    @property
    def reduction_percentage(self) -> float:
        if self.original_segments == 0:
            return 0.0
        return (1 - self.final_segments / self.original_segments) * 100


class DiarizationCleaner:
    """
    Pre-processes transcripts to fix common diarization errors.

    Phases:
        1. Remove noise: <0.5s segments with <3 words
        2. Merge micro-segments: same speaker, tiny gaps (<1s)
        3. Remove orphans: very short segments surrounded by same speaker
        4. Stitch segments: merge adjacent same-speaker for better LLM context
    """

    def cleanup_diarization(
        self,
        transcript: UnifiedTranscript
    ) -> Tuple[UnifiedTranscript, CleanupMetrics]:
        if not transcript.segments:
            logger.warning("No segments to clean - returning empty transcript")
            metrics = CleanupMetrics(
                original_segments=0,
                final_segments=0,
                noise_removed=0,
                micro_merged=0,
                orphans_removed=0,
                stitched_segments=0
            )
            return transcript, metrics

        original_count = len(transcript.segments)
        logger.info(f"Cleaning {original_count} segments...")

        segments = list(transcript.segments)

        # Phase 1: Remove noise segments
        cleaned = self._remove_noise_segments(segments)
        noise_removed = original_count - len(cleaned)

        # Phase 2: Merge micro-segments
        before_merge = len(cleaned)
        cleaned = self._merge_micro_segments(cleaned)
        merged_count = before_merge - len(cleaned)

        # Phase 3: Remove orphans
        before_orphans = len(cleaned)
        cleaned = self._merge_orphans(cleaned)
        orphans_removed = before_orphans - len(cleaned)

        # Phase 4: Stitch segments
        before_stitch = len(cleaned)
        cleaned = self._stitch_segments(cleaned)
        stitched_count = before_stitch - len(cleaned)

        metrics = CleanupMetrics(
            original_segments=original_count,
            final_segments=len(cleaned),
            noise_removed=noise_removed,
            micro_merged=merged_count,
            orphans_removed=orphans_removed,
            stitched_segments=stitched_count
        )

        logger.info(
            f"Cleanup complete: {original_count} -> {len(cleaned)} segments "
            f"({metrics.reduction_percentage:.1f}% reduction) - "
            f"noise={noise_removed}, merged={merged_count}, "
            f"orphans={orphans_removed}, stitched={stitched_count}"
        )

        return UnifiedTranscript(
            text=transcript.text,
            segments=cleaned,
            word_timestamps=transcript.word_timestamps,
            engine_used=transcript.engine_used
        ), metrics

    def _remove_noise_segments(self, segments: List[Segment]) -> List[Segment]:
        """Remove segments that are likely diarization noise (<0.5s AND <3 words)."""
        cleaned = []
        for seg in segments:
            duration = seg.end - seg.start
            word_count = len(seg.text.split())

            if duration < NOISE_DURATION_THRESHOLD and word_count < NOISE_WORD_THRESHOLD:
                logger.debug(
                    f"Removed noise: speaker_{seg.speaker} at {seg.start:.1f}s "
                    f"(duration={duration:.1f}s, words={word_count}, text='{seg.text}')"
                )
                continue
            cleaned.append(seg)

        return cleaned

    def _merge_micro_segments(self, segments: List[Segment]) -> List[Segment]:
        """Merge consecutive segments from same speaker if gap < 1s."""
        if not segments:
            return segments

        merged = [segments[0]]

        for current in segments[1:]:
            previous = merged[-1]

            if (current.speaker == previous.speaker and
                    current.start - previous.end < MERGE_GAP_THRESHOLD):
                merged_text = f"{previous.text} {current.text}".strip()
                merged_seg = Segment(
                    speaker=previous.speaker,
                    text=merged_text,
                    start=previous.start,
                    end=current.end
                )
                merged[-1] = merged_seg
                logger.debug(
                    f"Merged micro-segments: speaker_{previous.speaker} "
                    f"[{previous.start:.1f}-{previous.end:.1f}] + "
                    f"[{current.start:.1f}-{current.end:.1f}]"
                )
            else:
                merged.append(current)

        return merged

    def _merge_orphans(self, segments: List[Segment]) -> List[Segment]:
        """
        Merge very short orphan segments into surrounding speaker.

        Only merge segment B if:
        1. Speaker A appears before AND after B
        2. B's duration < 1.0s
        3. B is not a question or exclamation (preserve intent)
        """
        result = []
        i = 0

        while i < len(segments):
            current = segments[i]

            if i > 0 and i < len(segments) - 1:
                prev_speaker = segments[i-1].speaker
                next_speaker = segments[i+1].speaker

                is_surrounded = prev_speaker == next_speaker and prev_speaker != current.speaker
                duration = current.end - current.start
                word_count = len(current.text.split())

                is_very_short = duration < ORPHAN_VERY_SHORT_THRESHOLD
                is_noise = word_count <= 2 and duration < ORPHAN_NOISE_THRESHOLD

                has_question = '?' in current.text
                has_exclamation = '!' in current.text
                is_meaningful = has_question or has_exclamation

                if is_surrounded and (is_very_short or is_noise) and not is_meaningful:
                    logger.debug(
                        f"Orphan removed: speaker_{current.speaker} "
                        f"(duration={duration:.1f}s, words={word_count}, text='{current.text}') "
                        f"surrounded by speaker_{prev_speaker}"
                    )
                    i += 1
                    continue

            result.append(current)
            i += 1

        return result

    def _stitch_segments(self, segments: List[Segment]) -> List[Segment]:
        """Merge adjacent segments from the same speaker."""
        if not segments:
            return []

        result = []
        current_group = [segments[0]]

        for seg in segments[1:]:
            if seg.speaker == current_group[-1].speaker:
                current_group.append(seg)
            else:
                stitched = self._stitch_group(current_group)
                result.append(stitched)
                current_group = [seg]

        stitched = self._stitch_group(current_group)
        result.append(stitched)

        return result

    def _stitch_group(self, segments: List[Segment]) -> Segment:
        """Merge a group of consecutive segments from same speaker."""
        if len(segments) == 1:
            return segments[0]

        combined_text = ' '.join(seg.text for seg in segments)

        stitched = Segment(
            speaker=segments[0].speaker,
            text=combined_text,
            start=segments[0].start,
            end=segments[-1].end
        )

        logger.debug(
            f"Stitched {len(segments)} segments for speaker_{stitched.speaker} "
            f"[{stitched.start:.1f}-{stitched.end:.1f}s] "
            f"(total duration={stitched.end - stitched.start:.1f}s)"
        )

        return stitched
