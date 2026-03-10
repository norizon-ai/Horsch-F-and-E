"""Pipeline orchestrator — chains all processing stages."""

import asyncio
import logging
import traceback
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Dict, List

from app.config import settings
from app.jobs import JobStatus, job_store
from app.models import TranscriptionUsageEvent
from app.providers import get_provider
from app.services.audio import preprocess_audio
from app.services.diarization import DiarizationCleaner
from app.services.inference import InferenceService
from app.services.snippet_generator import SnippetGenerator

logger = logging.getLogger(__name__)

# Ghost speaker filter: min words to keep an unidentified speaker
_MIN_GHOST_WORDS = 10


class TranscriptionPipeline:
    """
    Orchestrates the full transcription pipeline:
    1. FFmpeg preprocessing
    2. Provider transcription (Whisper + diarization)
    3. Diarization cleanup (4-phase)
    4. Speaker name inference (LLM, optional)
    5. Ghost speaker filter
    6. Audio snippet generation
    7. Emit SSE complete event + usage event
    """

    def __init__(self):
        self.provider = get_provider()
        self.cleaner = DiarizationCleaner()
        self.inference = InferenceService()

    async def process(
        self,
        job_id: str,
        file_path: str,
        glossary: List[str],
        language: str = "de",
        tenant_id: str | None = None,
    ) -> None:
        """Run the full pipeline with timeout and structured error handling."""
        job = await job_store.get(job_id)
        if not job:
            logger.error(f"Job {job_id} not found in store")
            return

        try:
            await asyncio.wait_for(
                self._run_pipeline(job_id, file_path, glossary, language, tenant_id),
                timeout=settings.max_processing_timeout,
            )
        except asyncio.TimeoutError:
            error_msg = (
                f"Processing timed out after {settings.max_processing_timeout}s"
            )
            logger.error(f"[{job_id}] {error_msg}")
            await job_store.set_status(job_id, JobStatus.FAILED)
            await job.publish({"type": "error", "error": error_msg})
        except Exception as e:
            error_msg = f"Processing failed: {e}"
            logger.error(f"[{job_id}] {error_msg}\n{traceback.format_exc()}")
            await job_store.set_status(job_id, JobStatus.FAILED)
            await job.publish({"type": "error", "error": error_msg})

    async def _run_pipeline(
        self,
        job_id: str,
        file_path: str,
        glossary: List[str],
        language: str,
        tenant_id: str | None,
    ) -> None:
        job = await job_store.get(job_id)
        await job_store.set_status(job_id, JobStatus.PROCESSING)

        # --- Stage 1: Audio preprocessing ---
        await job.publish({
            "type": "progress",
            "stage": "uploading",
            "percent": 5,
            "message": "Audio wird vorbereitet...",
        })

        loop = asyncio.get_event_loop()
        work_dir = f"{settings.data_dir}/jobs/{job_id}"
        wav_path = await loop.run_in_executor(
            None, preprocess_audio, file_path, work_dir
        )

        await job.publish({
            "type": "progress",
            "stage": "uploading",
            "percent": 15,
            "message": "Audio konvertiert...",
        })

        # --- Stage 2: Transcription + diarization ---
        async def _on_progress(stage: str, percent: int, message: str):
            await job.publish({
                "type": "progress",
                "stage": stage,
                "percent": percent,
                "message": message,
            })

        transcript = await self.provider.transcribe(
            wav_path, language=language, on_progress=_on_progress
        )

        # --- Stage 3: Diarization cleanup ---
        await job.publish({
            "type": "progress",
            "stage": "diarizing",
            "percent": 70,
            "message": "Sprecherzuordnung wird optimiert...",
        })

        transcript, cleanup_metrics = self.cleaner.cleanup_diarization(transcript)

        # Build speakers_data from transcript
        speakers_set = set()
        speaker_word_counts: Dict[str, int] = defaultdict(int)

        for word in transcript.word_timestamps:
            speakers_set.add(word.speaker)
            speaker_word_counts[word.speaker] += 1

        # Compute speaking time per speaker from word timestamps
        speaker_time: Dict[str, float] = defaultdict(float)
        for word in transcript.word_timestamps:
            speaker_time[word.speaker] += word.end - word.start

        speakers_data: List[Dict] = []
        for speaker_id in sorted(speakers_set):
            speakers_data.append({
                "id": speaker_id,
                "detectedName": speaker_id.replace("_", " ").title(),
                "confirmedName": "",
                "sampleAudioUrl": None,
                "speakingTime": int(speaker_time.get(speaker_id, 0)),
                "transcriptSnippet": None,
                "confidence": None,
                "isExternal": None,
                "waveformData": None,
                "hint": None,
            })

        # --- Stage 4: Speaker name inference (optional) ---
        await job.publish({
            "type": "progress",
            "stage": "identifying",
            "percent": 75,
            "message": "Sprechernamen werden erkannt...",
        })

        inferred, hints = self.inference.infer_speaker_names(
            transcript, language=language
        )

        for speaker_dict in speakers_data:
            speaker_num = int(speaker_dict["id"].replace("speaker_", ""))
            if speaker_num in inferred:
                name, confidence = inferred[speaker_num]
                speaker_dict["detectedName"] = name
                speaker_dict["confidence"] = round(confidence * 100, 1)
                logger.info(
                    f"[{job_id}] Inferred name for Speaker {speaker_num}: "
                    f"{name} (confidence={speaker_dict['confidence']})"
                )
            if speaker_num in hints and speaker_num not in inferred:
                speaker_dict["hint"] = hints[speaker_num]

        # Ghost speaker filter
        def _has_identified_name(sd: dict) -> bool:
            name = sd.get("detectedName", "")
            return bool(name) and not name.lower().startswith("speaker ")

        # Build word counts by speaker number
        word_counts_by_num: Dict[int, int] = {}
        for sid, count in speaker_word_counts.items():
            num = int(sid.replace("speaker_", ""))
            word_counts_by_num[num] = count

        before_count = len(speakers_data)
        speakers_data = [
            sd for sd in speakers_data
            if _has_identified_name(sd)
            or word_counts_by_num.get(
                int(sd["id"].replace("speaker_", "")), 0
            ) >= _MIN_GHOST_WORDS
        ]
        removed = before_count - len(speakers_data)
        if removed:
            logger.info(
                f"[{job_id}] Ghost filter: removed {removed} speaker(s) "
                f"with no name and < {_MIN_GHOST_WORDS} words"
            )

        # --- Stage 5: Snippet generation ---
        await job.publish({
            "type": "progress",
            "stage": "correcting",
            "percent": 85,
            "message": "Sprecherproben werden erstellt...",
        })

        snippet_gen = SnippetGenerator(job_id)

        # Group segments by speaker for snippet selection
        utterances_by_speaker: Dict[int, list] = defaultdict(list)
        for seg in transcript.segments:
            spk_num = int(seg.speaker.replace("speaker_", ""))
            utterances_by_speaker[spk_num].append({
                "start": seg.start,
                "transcript": seg.text,
            })

        speaker_by_id = {sd["id"]: sd for sd in speakers_data}

        snippet_tasks = []
        for speaker_dict in speakers_data:
            speaker_num = int(speaker_dict["id"].replace("speaker_", ""))
            best = snippet_gen.find_best_utterance(
                utterances_by_speaker.get(speaker_num, [])
            )
            if best:
                start_time, transcript_snippet = best
                snippet_tasks.append((speaker_dict, start_time, transcript_snippet))

        # Generate snippets in parallel threads
        if snippet_tasks:
            def _gen(task):
                sd, st, ts = task
                url = snippet_gen.generate_snippet(file_path, sd["id"], st)
                return sd["id"], url, ts

            with ThreadPoolExecutor(max_workers=len(snippet_tasks)) as pool:
                futures = {pool.submit(_gen, t): t for t in snippet_tasks}
                for fut in as_completed(futures):
                    try:
                        sid, url, ts = fut.result()
                        speaker_by_id[sid]["sampleAudioUrl"] = url
                        speaker_by_id[sid]["transcriptSnippet"] = ts
                    except Exception as e:
                        logger.warning(f"[{job_id}] Snippet generation error: {e}")

        # --- Save results ---
        await job_store.save_results(
            job_id,
            speakers=speakers_data,
            transcript=transcript.model_dump(),
        )
        await job_store.set_status(job_id, JobStatus.COMPLETED)

        # --- Emit usage event ---
        duration = 0.0
        if transcript.word_timestamps:
            duration = max(w.end for w in transcript.word_timestamps)

        usage_event = TranscriptionUsageEvent(
            tenant_id=tenant_id,
            job_id=job_id,
            duration_seconds=round(duration, 1),
            language=language,
            provider=transcript.engine_used,
            speaker_count=len(speakers_data),
            timestamp=datetime.now(timezone.utc),
        )
        logger.info(
            "usage_event " + usage_event.model_dump_json(),
            extra={"event_type": "transcription_usage"},
        )

        # --- Emit complete SSE event ---
        await job.publish({
            "type": "complete",
            "percent": 100,
            "message": "Transkription abgeschlossen",
            "speakers": speakers_data,
            "transcript": transcript.text,
        })

        logger.info(f"[{job_id}] Pipeline completed successfully")
