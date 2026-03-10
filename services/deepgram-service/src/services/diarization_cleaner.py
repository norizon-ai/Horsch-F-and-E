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

from src.models.schemas import UnifiedTranscript, Segment

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
        """Calculate percentage reduction in segment count."""
        if self.original_segments == 0:
            return 0.0
        return (1 - self.final_segments / self.original_segments) * 100


class DiarizationCleaner:
    """
    Pre-processes transcripts to fix common diarization errors.

    Fixes:
        1. Remove noise: <0.5s segments with <3 words (diarization errors)
        2. Merge micro-segments: Speaker A talks <1s, then A again <1s later
        3. Remove orphans: Very short segments surrounded by same speaker (safer than flip-flop)
        4. Stitch segments: Merge adjacent same-speaker segments for better LLM context

    Algorithm:
        - Multi-phase chronological processing
        - Phase 1: Remove obvious noise
        - Phase 2: Merge micro-segments (same speaker, tiny gaps)
        - Phase 3: Remove orphans (very short, surrounded by same speaker)
        - Phase 4: Stitch adjacent segments (maximize LLM context)

    Performance:
        - O(n) time complexity per phase
        - O(n) space complexity
        - Handles 1000+ segments efficiently
    """

    def cleanup_diarization(
        self,
        transcript: UnifiedTranscript
    ) -> Tuple[UnifiedTranscript, CleanupMetrics]:
        """
        Clean up diarization errors before processing.

        Args:
            transcript: Original UnifiedTranscript

        Returns:
            Tuple of (cleaned UnifiedTranscript, CleanupMetrics)
        """
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

        # Phase 3: Remove orphans (replaces flip-flop consolidation)
        before_orphans = len(cleaned)
        cleaned = self._merge_orphans(cleaned)
        orphans_removed = before_orphans - len(cleaned)

        # Phase 4: Stitch segments (NEW - maximize LLM context)
        before_stitch = len(cleaned)
        cleaned = self._stitch_segments(cleaned)
        stitched_count = before_stitch - len(cleaned)

        # Build metrics
        metrics = CleanupMetrics(
            original_segments=original_count,
            final_segments=len(cleaned),
            noise_removed=noise_removed,
            micro_merged=merged_count,
            orphans_removed=orphans_removed,
            stitched_segments=stitched_count
        )

        logger.info(
            f"Cleanup complete: {original_count} → {len(cleaned)} segments "
            f"({metrics.reduction_percentage:.1f}% reduction) - "
            f"noise={noise_removed}, merged={merged_count}, "
            f"orphans={orphans_removed}, stitched={stitched_count}"
        )

        # Return new UnifiedTranscript with cleaned segments
        return UnifiedTranscript(
            text=transcript.text,
            segments=cleaned,
            word_timestamps=transcript.word_timestamps,
            engine_used=transcript.engine_used
        ), metrics

    def _remove_noise_segments(self, segments: List[Segment]) -> List[Segment]:
        """
        Remove segments that are likely diarization noise.

        Criteria:
            - Duration < 0.5s AND word_count < 3

        These are typically diarization errors where background noise or
        cross-talk is incorrectly attributed to a speaker.
        """
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
        """
        Merge consecutive segments from same speaker if gap < 1s.

        Example:
            Speaker A: 10.0-10.5s "Hello"
            Speaker B: 10.5-11.0s "Hi"
            Speaker A: 11.0-11.3s "How are you"

            → Don't merge (different speakers in between)

            Speaker A: 10.0-10.5s "Hello"
            Speaker A: 10.8-11.3s "there"

            → Merge (same speaker, gap=0.3s < 1.0s)
        """
        if not segments:
            return segments

        merged = [segments[0]]

        for current in segments[1:]:
            previous = merged[-1]

            # Same speaker and small gap?
            if (current.speaker == previous.speaker and
                current.start - previous.end < MERGE_GAP_THRESHOLD):
                # Merge into previous
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
        Merge very short "orphan" segments into surrounding speaker.

        Only merge segment B if:
        1. Speaker A appears strictly before AND after B
        2. B's duration < 1.0s (very short - likely diarization glitch)
        3. B is not a question or exclamation (preserve intent)

        This is safer than flip-flop consolidation because it:
        - Uses tighter duration thresholds (0.5s-1.0s vs 5s window)
        - Preserves questions/exclamations (maintains conversation flow)
        - Only removes segments surrounded by SAME speaker

        Example:
        [A: 5.2s] → [B: 0.4s "Yes"] → [A: 3.1s]
        B is < 1.0s, but contains meaningful response → Keep separate

        [A: 5.2s] → [B: 0.2s "Uh"] → [A: 3.1s]
        B is < 0.5s, likely noise → Remove (will merge in stitching)

        Args:
            segments: List of segments to process

        Returns:
            List of segments with orphans removed
        """
        result = []
        i = 0

        while i < len(segments):
            current = segments[i]

            # Check if this is a potential orphan (not first or last segment)
            if i > 0 and i < len(segments) - 1:
                prev_speaker = segments[i-1].speaker
                next_speaker = segments[i+1].speaker

                # Orphan criteria
                is_surrounded = prev_speaker == next_speaker and prev_speaker != current.speaker
                duration = current.end - current.start
                word_count = len(current.text.split())

                is_very_short = duration < ORPHAN_VERY_SHORT_THRESHOLD
                is_noise = word_count <= 2 and duration < ORPHAN_NOISE_THRESHOLD

                # Preserve meaningful short utterances
                has_question = '?' in current.text
                has_exclamation = '!' in current.text
                is_meaningful = has_question or has_exclamation

                if is_surrounded and (is_very_short or is_noise) and not is_meaningful:
                    # Skip this segment (orphan removed)
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
        """
        Merge adjacent segments from the same speaker.

        After cleanup, we may have multiple consecutive segments from the same
        speaker due to previous processing phases. This method stitches them
        together to create longer, more coherent segments.

        Example:
        Before: [Speaker 0: 5s] → [Speaker 0: 3s] → [Speaker 1: 2s]
        After:  [Speaker 0: 8s] → [Speaker 1: 2s]

        Goal: Maximize context for LLM evidence scanner by creating longer
              continuous segments from the same speaker.

        Args:
            segments: List of cleaned segments

        Returns:
            List of stitched segments with adjacent same-speaker segments merged
        """
        if not segments:
            return []

        result = []
        current_group = [segments[0]]

        for seg in segments[1:]:
            if seg.speaker == current_group[-1].speaker:
                # Same speaker - add to group
                current_group.append(seg)
            else:
                # Different speaker - stitch current group and start new one
                stitched = self._stitch_group(current_group)
                result.append(stitched)
                current_group = [seg]

        # Don't forget last group
        stitched = self._stitch_group(current_group)
        result.append(stitched)

        return result

    def _stitch_group(self, segments: List[Segment]) -> Segment:
        """
        Merge a group of consecutive segments from same speaker.

        Combines text with spaces and uses the first segment's start time
        and last segment's end time to create a single continuous segment.

        Args:
            segments: List of segments from same speaker to merge

        Returns:
            Single merged Segment
        """
        if len(segments) == 1:
            return segments[0]

        # Combine texts with space
        combined_text = ' '.join(seg.text for seg in segments)

        # Use first segment's start, last segment's end
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
