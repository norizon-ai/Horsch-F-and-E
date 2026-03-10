# Transcription Service

Local speech-to-text with speaker diarization using [faster-whisper](https://github.com/SYSTRAN/faster-whisper) and [pyannote.audio](https://github.com/pyannote/pyannote-audio).

Replaces the Deepgram cloud API with a fully local pipeline. Same API contract — the workflow-service doesn't know the difference.

## Pipeline

```
Audio file -> FFmpeg (16kHz WAV) -> Whisper (word timestamps + VAD)
    -> Pyannote (speaker diarization) -> Align words to speakers
    -> 4-phase diarization cleanup -> LLM speaker name inference (optional)
    -> Audio snippet generation -> SSE complete event
```

## Quick start

```bash
# 1. Create Python 3.11 venv
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Install FFmpeg
brew install ffmpeg          # macOS
# apt-get install ffmpeg     # Ubuntu/Debian

# 3. Configure
cp .env.example .env
# Edit .env — at minimum set HF_TOKEN

# 4. Run
uvicorn app.main:app --port 8002
```

For faster iteration during development, use a smaller Whisper model:

```bash
WHISPER_MODEL=small uvicorn app.main:app --port 8002 --reload
```

## Prerequisites

### Hugging Face token

Pyannote requires accepting gated model licenses:

1. Create account at [huggingface.co](https://huggingface.co)
2. Accept license at [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
3. Accept license at [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)
4. Accept license at [pyannote/speaker-diarization-community-1](https://huggingface.co/pyannote/speaker-diarization-community-1)
5. Create token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) with "Read access to contents of all public gated repos you can access"

### Model download

On first request, the service downloads:
- **Whisper large-v3** (~3GB) — CTranslate2 format (or `small` ~500MB)
- **Pyannote speaker-diarization-3.1** (~100MB)

Subsequent requests use the cached models.

## Configuration

All settings are environment variables (or `.env` file). See `.env.example` for full reference.

| Variable | Default | Description |
|---|---|---|
| `HF_TOKEN` | — | Hugging Face token (required) |
| `WHISPER_MODEL` | `large-v3` | Whisper model size (`tiny`, `base`, `small`, `medium`, `large-v3`) |
| `WHISPER_DEVICE` | `auto` | Compute device (`auto`, `cpu`, `cuda`) |
| `WHISPER_COMPUTE_TYPE` | `auto` | Quantization (`auto`, `int8`, `float16`, `float32`) |
| `DEFAULT_LANGUAGE` | `de` | Default transcription language |
| `OPENAI_API_KEY` | — | For LLM speaker name inference (optional) |
| `OPENAI_MODEL` | `gpt-4o-mini` | LLM model for inference |
| `LLM_BASE_URL` | — | Custom OpenAI-compatible endpoint (e.g. IONOS EU) |
| `CPU_THREADS` | `half of cores` | Max CPU threads for Whisper + Pyannote (0 = unlimited) |
| `MAX_PROCESSING_TIMEOUT` | `14400` | Pipeline timeout in seconds |
| `TRANSCRIPTION_PROVIDER` | `whisper_local` | Provider (`whisper_local`, `azure_speech`) |

## API

### Health check

```bash
curl http://localhost:8002/health
# {"status":"ok","service":"transcription-service"}
```

### Full workflow via curl

Run a complete transcription job from the command line:

```bash
JOB_ID="meeting-$(date +%s)"
AUDIO_FILE="/path/to/recording.m4a"

# Step 1: Upload
curl -X POST "http://localhost:8002/internal/jobs/${JOB_ID}/upload" \
  -F "file=@${AUDIO_FILE}"

# Step 2: Start processing
FILE_EXT="${AUDIO_FILE##*.}"
curl -X POST "http://localhost:8002/internal/transcribe/${JOB_ID}/process" \
  -H "Content-Type: application/json" \
  -d "{\"file_path\": \"/tmp/transcription-uploads/${JOB_ID}.${FILE_EXT}\", \"language\": \"de\"}"

# Step 3: Stream progress (SSE) — blocks until complete
curl -N "http://localhost:8002/internal/transcribe/${JOB_ID}/stream"

# Step 4: Retrieve results
curl "http://localhost:8002/internal/jobs/${JOB_ID}/speakers"
curl "http://localhost:8002/internal/jobs/${JOB_ID}/transcript"
```

### Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Liveness probe |
| `GET` | `/ready` | Readiness probe |
| `POST` | `/internal/jobs/{job_id}/upload` | Upload audio file (multipart) |
| `POST` | `/internal/transcribe/{job_id}/process` | Start async processing |
| `GET` | `/internal/transcribe/{job_id}/stream` | SSE progress stream |
| `GET` | `/internal/jobs/{job_id}/speakers` | Get detected speakers |
| `GET` | `/internal/jobs/{job_id}/transcript` | Get full transcript with segments |

### POST /internal/transcribe/{job_id}/process

Request body:

```json
{
  "file_path": "/tmp/transcription-uploads/meeting-1.m4a",
  "language": "de",
  "glossary": ["Norizon", "Fraunhofer"],
  "tenant_id": "customer-123"
}
```

The `process` endpoint is idempotent — calling it again for an in-progress or completed job returns the existing status without starting a duplicate pipeline.

### GET /internal/transcribe/{job_id}/stream

Server-Sent Events stream. Stages flow in order:

```
data: {"type":"progress","stage":"uploading","percent":5,"message":"Audio wird vorbereitet..."}
data: {"type":"progress","stage":"transcribing","percent":10,"message":"Sprache wird erkannt..."}
data: {"type":"progress","stage":"diarizing","percent":70,"message":"Sprecherzuordnung wird optimiert..."}
data: {"type":"progress","stage":"identifying","percent":75,"message":"Sprechernamen werden erkannt..."}
data: {"type":"progress","stage":"correcting","percent":85,"message":"Sprecherproben werden erstellt..."}
data: {"type":"complete","percent":100,"speakers":[...],"transcript":"full text"}
```

On error:

```
data: {"type":"error","error":"Processing timed out after 1800s"}
```

Reconnecting to the stream after completion returns the `complete` event immediately.

### GET /internal/jobs/{job_id}/speakers

```json
{
  "speakers": [
    {
      "id": "speaker_0",
      "detectedName": "Lisa",
      "confirmedName": "",
      "sampleAudioUrl": "/data/jobs/meeting-1/snippets/speaker_0.mp3",
      "speakingTime": 2546,
      "transcriptSnippet": "Also die zehn Minuten sind eine sehr großzügig...",
      "confidence": 90.0,
      "hint": null
    }
  ]
}
```

### GET /internal/jobs/{job_id}/transcript

Returns the full `UnifiedTranscript` with word-level timestamps and speaker-labeled segments:

```json
{
  "text": "full transcript...",
  "segments": [
    {"start": 0.0, "end": 3.5, "text": "Hallo zusammen", "speaker": "speaker_0"}
  ],
  "word_timestamps": [
    {"word": "Hallo", "start": 0.0, "end": 0.4, "speaker": "speaker_0", "confidence": 0.95}
  ],
  "engine_used": "whisper_local"
}
```

## Apple Silicon notes

- `faster-whisper` (CTranslate2) runs on **CPU only** — no MPS support. Uses int8 quantization.
- `large-v3` runs at ~2-4x realtime on M-series; use `small` for dev (~6x realtime)
- `pyannote.audio` uses PyTorch (CPU). For a 1h30m file, expect ~50 min diarization time on CPU.
- Total processing time for a 1h30m file with `small` model: ~1h20m on M-series CPU

### Preventing laptop freeze

By default, the service limits itself to **half your CPU cores** (`CPU_THREADS`). This keeps your machine responsive while transcribing. To change:

```bash
CPU_THREADS=2 uvicorn app.main:app --port 8002   # very gentle, laptop stays cool
CPU_THREADS=0 uvicorn app.main:app --port 8002   # unlimited, fastest but may freeze
```

## Enterprise features

- **Idempotency guard**: duplicate `/process` calls return existing status
- **Processing timeout**: configurable pipeline deadline (`MAX_PROCESSING_TIMEOUT`)
- **Structured JSON logging**: `python-json-logger` with job_id correlation
- **Usage events**: `TranscriptionUsageEvent` logged on completion (tenant_id, duration, speaker count)
- **Provider abstraction**: `TRANSCRIPTION_PROVIDER` env var for future Azure Speech integration
- **Disk persistence**: results saved to `DATA_DIR/jobs/{job_id}/results.json` on completion
- **LLM base URL**: `LLM_BASE_URL` for EU-hosted inference (IONOS, Azure OpenAI, etc.)

## Integration with workflow-service

Set in workflow-service `.env`:

```env
USE_MOCKS=false
KSTUDIO_URL=http://localhost:8002
```
