"""Local Whisper + Pyannote transcription provider."""

import asyncio
import logging
import os
from functools import lru_cache
from typing import Optional

from app.config import settings
from app.models import UnifiedTranscript, Word, Segment
from app.providers.base import TranscriptionProvider, ProgressCallback

logger = logging.getLogger(__name__)


def _apply_thread_limits():
    """
    Cap CPU threads for CTranslate2, PyTorch, and OpenMP so the service
    doesn't saturate all cores and freeze the machine.
    """
    n = settings.cpu_threads
    if n <= 0:
        return  # 0 = unlimited

    # OpenMP / MKL (used by numpy, scipy, ctranslate2)
    for var in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
        os.environ.setdefault(var, str(n))

    # PyTorch (used by pyannote)
    try:
        import torch
        torch.set_num_threads(n)
        torch.set_num_interop_threads(max(1, n // 2))
    except (ImportError, RuntimeError):
        pass

    logger.info(f"CPU thread limit set to {n} (of {os.cpu_count()} available)")


# Apply on module import — must happen before models are loaded
_apply_thread_limits()


def _resolve_device() -> str:
    """Determine the best available device."""
    device = settings.whisper_device
    if device != "auto":
        return device

    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
    except ImportError:
        pass
    return "cpu"


def _resolve_compute_type(device: str) -> str:
    """Pick optimal compute type for the device."""
    ct = settings.whisper_compute_type
    if ct != "auto":
        return ct
    return "float16" if device == "cuda" else "int8"


@lru_cache(maxsize=1)
def _load_whisper_model():
    """Lazy-load the faster-whisper model (cached across calls)."""
    from faster_whisper import WhisperModel

    device = _resolve_device()
    compute_type = _resolve_compute_type(device)

    logger.info(
        f"Loading Whisper model: {settings.whisper_model} "
        f"(device={device}, compute_type={compute_type})"
    )
    model_kwargs = {
        "device": device,
        "compute_type": compute_type,
    }
    if settings.cpu_threads > 0 and device == "cpu":
        model_kwargs["cpu_threads"] = settings.cpu_threads

    model = WhisperModel(settings.whisper_model, **model_kwargs)
    logger.info("Whisper model loaded")
    return model


@lru_cache(maxsize=1)
def _load_diarization_pipeline():
    """Lazy-load the pyannote diarization pipeline (cached across calls)."""
    from pyannote.audio import Pipeline

    if not settings.hf_token:
        raise RuntimeError(
            "HF_TOKEN is required for pyannote speaker diarization. "
            "Accept the license at https://huggingface.co/pyannote/speaker-diarization-3.1 "
            "and set HF_TOKEN in your environment."
        )

    logger.info(f"Loading diarization pipeline: {settings.diarization_model}")
    pipeline = Pipeline.from_pretrained(
        settings.diarization_model,
        token=settings.hf_token,
    )

    device = _resolve_device()
    if device == "cuda":
        import torch
        pipeline.to(torch.device("cuda"))

    logger.info("Diarization pipeline loaded")
    return pipeline


def _run_whisper(file_path: str, language: str) -> tuple:
    """Run Whisper transcription (CPU-bound, runs in executor)."""
    model = _load_whisper_model()

    segments_iter, info = model.transcribe(
        file_path,
        language=language,
        word_timestamps=True,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
    )

    # Materialize the iterator
    whisper_segments = []
    all_words = []
    full_text_parts = []

    for segment in segments_iter:
        full_text_parts.append(segment.text.strip())
        seg_words = []
        if segment.words:
            for w in segment.words:
                word_info = {
                    "word": w.word.strip(),
                    "start": w.start,
                    "end": w.end,
                }
                seg_words.append(word_info)
                all_words.append(word_info)

        whisper_segments.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip(),
            "words": seg_words,
        })

    full_text = " ".join(full_text_parts)
    logger.info(
        f"Whisper: {len(whisper_segments)} segments, "
        f"{len(all_words)} words, language={info.language}"
    )

    return whisper_segments, all_words, full_text, info


def _run_diarization(file_path: str) -> list:
    """Run pyannote diarization (CPU/GPU-bound, runs in executor)."""
    pipeline = _load_diarization_pipeline()
    result = pipeline(file_path)

    # pyannote 4.x returns DiarizeOutput; 3.x returns Annotation directly
    annotation = getattr(result, "speaker_diarization", result)

    turns = []
    for turn, _, speaker in annotation.itertracks(yield_label=True):
        turns.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker,
        })

    logger.info(f"Diarization: {len(turns)} speaker turns")
    return turns


def _align_words_to_speakers(words: list, diarization_turns: list) -> list:
    """
    Assign each word to a speaker by checking which diarization turn
    contains the word's midpoint.
    """
    # Build a speaker map from turns
    speaker_labels = sorted(set(t["speaker"] for t in diarization_turns))
    speaker_map = {label: f"speaker_{i}" for i, label in enumerate(speaker_labels)}

    aligned = []
    turn_idx = 0

    for word in words:
        midpoint = (word["start"] + word["end"]) / 2

        # Advance turn index to find the right turn
        while (turn_idx < len(diarization_turns) - 1 and
               diarization_turns[turn_idx]["end"] < midpoint):
            turn_idx += 1

        # Check if midpoint falls within current turn
        turn = diarization_turns[turn_idx]
        if turn["start"] <= midpoint <= turn["end"]:
            speaker = speaker_map[turn["speaker"]]
        else:
            # Word falls in a gap — assign to nearest turn
            best_turn = min(
                diarization_turns,
                key=lambda t: min(abs(t["start"] - midpoint), abs(t["end"] - midpoint))
            )
            speaker = speaker_map[best_turn["speaker"]]

        aligned.append({
            **word,
            "speaker": speaker,
        })

    return aligned


def _build_segments(aligned_words: list) -> list:
    """
    Build segments by grouping consecutive words from the same speaker.
    """
    if not aligned_words:
        return []

    segments = []
    current_speaker = aligned_words[0]["speaker"]
    current_words = [aligned_words[0]]

    for word in aligned_words[1:]:
        if word["speaker"] == current_speaker:
            current_words.append(word)
        else:
            segments.append({
                "start": current_words[0]["start"],
                "end": current_words[-1]["end"],
                "text": " ".join(w["word"] for w in current_words),
                "speaker": current_speaker,
            })
            current_speaker = word["speaker"]
            current_words = [word]

    # Last segment
    segments.append({
        "start": current_words[0]["start"],
        "end": current_words[-1]["end"],
        "text": " ".join(w["word"] for w in current_words),
        "speaker": current_speaker,
    })

    return segments


class WhisperLocalProvider(TranscriptionProvider):
    """
    Local transcription using faster-whisper + pyannote.

    Models are lazy-loaded on first use and cached for subsequent calls.
    All CPU-bound work runs in a thread executor to avoid blocking the event loop.
    """

    async def transcribe(
        self,
        file_path: str,
        language: str = "de",
        on_progress: Optional[ProgressCallback] = None,
    ) -> UnifiedTranscript:
        loop = asyncio.get_event_loop()

        # Step 1: Whisper transcription
        if on_progress:
            await on_progress("transcribing", 10, "Sprache wird erkannt...")

        whisper_segments, all_words, full_text, info = await loop.run_in_executor(
            None, _run_whisper, file_path, language
        )

        if on_progress:
            await on_progress("transcribing", 40, "Transkription abgeschlossen...")

        # Step 2: Speaker diarization
        if on_progress:
            await on_progress("diarizing", 50, "Sprecher werden identifiziert...")

        diarization_turns = await loop.run_in_executor(
            None, _run_diarization, file_path
        )

        if on_progress:
            await on_progress("diarizing", 65, "Sprecher zugeordnet...")

        # Step 3: Align words to speakers
        aligned_words = _align_words_to_speakers(all_words, diarization_turns)

        # Step 4: Build segments from aligned words
        segments = _build_segments(aligned_words)

        # Build model objects
        word_timestamps = [
            Word(word=w["word"], start=w["start"], end=w["end"], speaker=w["speaker"])
            for w in aligned_words
        ]

        transcript_segments = [
            Segment(start=s["start"], end=s["end"], text=s["text"], speaker=s["speaker"])
            for s in segments
        ]

        logger.info(
            f"Transcription complete: {len(transcript_segments)} segments, "
            f"{len(word_timestamps)} words, {len(set(w['speaker'] for w in aligned_words))} speakers"
        )

        return UnifiedTranscript(
            text=full_text,
            segments=transcript_segments,
            word_timestamps=word_timestamps,
            engine_used="whisper_local",
        )
