import asyncio
import logging
import os
import traceback
from typing import List, Dict, Any
from src.config import settings
from src.services.redis_manager import RedisManager
from src.services.deepgram_client import DeepgramService
from src.services.snippet_generator import SnippetGenerator
from src.services.inference import InferenceService
from src.models.schemas import UnifiedTranscript, Word, Segment

logger = logging.getLogger(__name__)

class AudioProcessor:
    """Orchestrates the full audio processing pipeline."""
    
    def __init__(self):
        self.redis = RedisManager()
        self.deepgram = DeepgramService()
        self.inference = InferenceService()
    
    async def process(self, job_id: str, file_path: str, glossary: List[str], language: str = "en") -> None:
        """
        Process audio file through full pipeline.
        
        Pipeline:
        1. Deepgram API transcription + diarization
        2. Parse results into UnifiedTranscript format
        3. Generate speaker audio snippets with FFmpeg
        4. Save results to Redis
        5. Publish completion event
        """
        try:
            logger.info(f"Starting processing for job {job_id}")
            
            # Step 1: Start transcription
            self.redis.publish_event(job_id, {
                "type": "progress",
                "stage": "transcribing",
                "percent": 0,
                "message": "Starting transcription..."
            })
            
            # SMF CIFS DirCache Delay Workaround:
            # Wait for file to be visible from workflow-service across nodes
            for attempt in range(60):
                if os.path.exists(file_path):
                    break
                logger.info(f"Waiting for file via SMB sync: {file_path} (Attempt {attempt+1}/60)")
                await asyncio.sleep(1)
            else:
                raise FileNotFoundError(f"[Errno 2] No such file or directory after 60s: {file_path}")
            
            # Step 2: Call Deepgram API
            logger.info(f"Calling Deepgram API for {file_path} (Language: {language})")
            deepgram_response = await self.deepgram.transcribe_file(file_path, glossary, language=language)
            
            self.redis.publish_event(job_id, {
                "type": "progress",
                "stage": "diarizing",
                "percent": 50,
                "message": "Identifying speakers..."
            })
            
            # Step 3: Parse Deepgram response
            transcript, speakers_data = self._parse_deepgram_response(deepgram_response)
            
            utterances = deepgram_response.get("results", {}).get("utterances", [])

            # Step 4: Infer speaker names using LLM
            self.redis.publish_event(job_id, {
                "type": "progress",
                "stage": "identifying",
                "percent": 60,
                "message": "Identifying speakers..."
            })

            inferred, hints = self.inference.infer_speaker_names(transcript, language=language)

            for speaker_dict in speakers_data:
                speaker_num = int(speaker_dict["id"].replace("speaker_", ""))
                if speaker_num in inferred:
                    name, confidence = inferred[speaker_num]
                    speaker_dict["detectedName"] = name
                    speaker_dict["confidence"] = round(confidence * 100, 1)
                    logger.info(
                        f"Inferred name for Speaker {speaker_num}: "
                        f"{name} (confidence={speaker_dict['confidence']})"
                    )
                # Only show hint when name is not already confirmed
                if speaker_num in hints and speaker_num not in inferred:
                    speaker_dict["hint"] = hints[speaker_num]
                    logger.info(f"Hint for Speaker {speaker_num}: {hints[speaker_num]}")

            # Post-inference ghost filter: remove speakers with no identified name
            # AND fewer than MIN_GHOST_WORDS total words. Runs AFTER inference so
            # self-introducing speakers ("I'm Geoffrey") are named first.
            _MIN_GHOST_WORDS = 5
            word_counts: dict[int, int] = {}
            for u in utterances:
                spk = u.get("speaker", 0)
                word_counts[spk] = word_counts.get(spk, 0) + len(u.get("transcript", "").split())

            def _has_identified_name(sd: dict) -> bool:
                name = sd.get("detectedName", "")
                return bool(name) and not name.lower().startswith("speaker ")

            before_count = len(speakers_data)
            
            # Never delete the only speaker in the file
            if before_count > 1:
                speakers_data = [
                    sd for sd in speakers_data
                    if _has_identified_name(sd)
                    or word_counts.get(int(sd["id"].replace("speaker_", "")), 0) >= _MIN_GHOST_WORDS
                ]
                removed = before_count - len(speakers_data)
                if removed:
                    logger.info(
                        f"Post-inference ghost filter: removed {removed} speaker(s) "
                        f"with no name and < {_MIN_GHOST_WORDS} words"
                    )

            # Step 5: Generate speaker snippets
            self.redis.publish_event(job_id, {
                "type": "progress",
                "stage": "correcting",
                "percent": 80,
                "message": "Generating speaker samples..."
            })

            snippet_gen = SnippetGenerator(job_id)

            # Group utterances by speaker once — avoids repeated O(N) scans

            from collections import defaultdict
            utterances_by_speaker: dict[int, list] = defaultdict(list)
            for u in utterances:
                utterances_by_speaker[u.get("speaker", 0)].append(u)

            speaker_by_id = {sd["id"]: sd for sd in speakers_data}

            snippet_tasks = []
            for speaker_dict in speakers_data:
                speaker_num = int(speaker_dict["id"].replace("speaker_", ""))
                best_utterance = snippet_gen.find_best_utterance(
                    utterances_by_speaker.get(speaker_num, [])
                )
                if best_utterance:
                    start_time, transcript_snippet = best_utterance
                    snippet_tasks.append((speaker_dict, start_time, transcript_snippet))

            from concurrent.futures import ThreadPoolExecutor, as_completed

            def _gen(task):
                sd, st, ts = task
                url = snippet_gen.generate_snippet(file_path, sd["id"], st)
                return sd["id"], url, ts

            with ThreadPoolExecutor(max_workers=len(snippet_tasks) or 1) as pool:
                futures = {pool.submit(_gen, t): t for t in snippet_tasks}
                for fut in as_completed(futures):
                    sid, url, ts = fut.result()
                    speaker_by_id[sid]["sampleAudioUrl"] = url
                    speaker_by_id[sid]["transcriptSnippet"] = ts
            
            # Step 5: Save to Redis
            logger.info(f"Saving results to Redis for job {job_id}")
            self.redis.save_transcript(job_id, transcript.model_dump())
            self.redis.save_speakers(job_id, speakers_data)
            
            # Step 6: Publish completion with speakers data and full transcript
            self.redis.publish_event(job_id, {
                "type": "complete",
                "percent": 100,
                "message": "Transcription complete",
                "speakers": speakers_data,
                "transcript": transcript.text  # Full transcript text for protocol generation
            })
            
            logger.info(f"Processing completed successfully for job {job_id}")
            
        except Exception as e:
            error_msg = f"Processing failed: {str(e)}"
            logger.error(f"{error_msg}\n{traceback.format_exc()}")
            
            # Publish error event
            self.redis.publish_event(job_id, {
                "type": "error",
                "message": error_msg
            })
    
    def _parse_deepgram_response(self, response: Dict[str, Any]) -> tuple[UnifiedTranscript, List[Dict[str, Any]]]:
        """Parse Deepgram response into UnifiedTranscript and speakers list."""

        results = response.get("results", {})
        channels = results.get("channels", [])
        
        if not channels:
            raise ValueError("No channels found in Deepgram response")
        
        channel = channels[0]
        alternatives = channel.get("alternatives", [])
        
        if not alternatives:
            raise ValueError("No alternatives found in Deepgram response")
        
        alternative = alternatives[0]
        
        full_text = alternative.get("transcript", "")
        
        words_raw = alternative.get("words", [])
        word_timestamps = []
        
        for word_data in words_raw:
            word_timestamps.append(Word(
                word=word_data.get("word", ""),
                start=word_data.get("start", 0),
                end=word_data.get("end", 0),
                speaker=f"speaker_{word_data.get('speaker', 0)}"
            ))
        
        utterances = results.get("utterances", [])
        segments = []
        
        for utterance in utterances:
            segments.append(Segment(
                start=utterance.get("start", 0),
                end=utterance.get("end", 0),
                text=utterance.get("transcript", ""),
                speaker=f"speaker_{utterance.get('speaker', 0)}"
            ))
        
        transcript = UnifiedTranscript(
            text=full_text,
            segments=segments,
            word_timestamps=word_timestamps,
            engine_used="deepgram"
        )
        
        speakers_set = set()
        speaker_stats = {}
        
        for word in words_raw:
            speaker_id = f"speaker_{word.get('speaker', 0)}"
            speakers_set.add(speaker_id)
            
            duration = word.get("end", 0) - word.get("start", 0)
            speaker_stats[speaker_id] = speaker_stats.get(speaker_id, 0) + duration
        
        speakers_data = []
        for speaker_id in sorted(speakers_set):
            speakers_data.append({
                "id": speaker_id,
                "detectedName": speaker_id.replace("_", " ").title(),
                "confirmedName": "",
                "sampleAudioUrl": None,
                "speakingTime": int(speaker_stats.get(speaker_id, 0)),
                "transcriptSnippet": None,
                "confidence": None,
                "isExternal": None,
                "waveformData": None,
                "hint": None
            })
        
        if len(segments) == 0 or len(speakers_data) == 0:
            import json
            logger.warning(
                f"Parsed 0 segments or speakers! "
                f"Segments: {len(segments)}, Speakers: {len(speakers_data)}. "
                f"Full text length: {len(full_text)}. "
                f"Raw response transcript: '{full_text[:200]}...'"
            )
            # Log the full structure of the response keys to see what's missing
            logger.debug(f"Deepgram response structure: {list(response.keys())}")
            if "results" in response:
                logger.debug(f"Deepgram results keys: {list(response['results'].keys())}")
        
        logger.info(f"Parsed {len(segments)} segments and {len(speakers_data)} speakers")

        return transcript, speakers_data