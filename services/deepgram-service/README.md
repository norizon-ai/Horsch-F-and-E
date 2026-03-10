# Deepgram Service

Deepgram-based transcription service for Nora Knowledge Studio. Replaces the previous KStudio service with a simplified pipeline using Deepgram's API.

## Features

- **Deepgram Nova-2 Model**: State-of-the-art transcription accuracy
- **Speaker Diarization**: Automatic speaker detection and separation
- **Custom Vocabulary**: Glossary support via Deepgram keywords
- **Audio Snippets**: FFmpeg-generated speaker samples
- **Real-time Progress**: Server-Sent Events (SSE) streaming
- **Redis Integration**: Event streaming and result storage

## API Contract

Maintains 100% compatibility with the original KStudio API:

### POST `/internal/transcribe/{job_id}/process`
Start transcription processing for a job.

**Request Body:**
```json
{
  "file_path": "/app/uploads/meeting.mp3",
  "glossary": ["technical", "terms"]
}
```

**Response:**
```json
{
  "job_id": "abc-123",
  "status": "processing"
}
```

### GET `/internal/transcribe/{job_id}/stream`
Server-Sent Events stream for real-time progress updates.

**Events:**
- `progress`: Processing progress (0-100%)
- `complete`: Processing finished successfully
- `error`: Processing failed with error message

### GET `/internal/jobs/{job_id}/speakers`
Retrieve detected speakers for a completed job.

**Response:**
```json
{
  "speakers": [
    {
      "id": "speaker_0",
      "detectedName": "Speaker 0",
      "sampleAudioUrl": "/data/jobs/abc-123/snippets/speaker_0.mp3",
      "speakingTime": 45,
      "transcriptSnippet": "Sample of what speaker said..."
    }
  ]
}
```

## Environment Variables

```bash
DEEPGRAM_API_KEY=your_api_key_here  # Required
DEEPGRAM_MODEL=nova-2               # Default
REDIS_URL=redis://redis:6379/0      # Default
UPLOAD_DIR=/app/uploads             # Default
DATA_DIR=/app/data                  # Default
DEBUG=false                         # Default
```

## Development

```bash
# Install dependencies
cd services/deepgram-service
pip install -r requirements.txt

# Run locally
uvicorn src.main:app --reload --port 8002

# Run with Docker Compose
cd services/norizon-research
docker-compose -f docker-compose.dev.yml up deepgram-service
```

## Architecture

```
┌─────────────────────┐
│  Workflow Service   │
└──────────┬──────────┘
           │ POST /process
           ▼
┌─────────────────────┐
│ Deepgram Service    │
│  (Port 8002)        │
└──────────┬──────────┘
           │
    ┌──────┴────────┬──────────┬──────────┐
    ▼               ▼          ▼          ▼
┌─────────┐   ┌─────────┐  ┌─────┐  ┌────────┐
│Deepgram │   │ FFmpeg  │  │Redis│  │Frontend│
│   API   │   │Snippets │  │     │  │  SSE   │
└─────────┘   └─────────┘  └─────┘  └────────┘
```

## Pipeline Flow

1. **Upload**: Workflow service saves audio to shared volume
2. **Trigger**: POST request starts background processing
3. **Transcribe**: Deepgram API processes audio (diarization enabled)
4. **Parse**: Convert Deepgram response to UnifiedTranscript format
5. **Snippets**: FFmpeg generates 5-second samples for each speaker
6. **Store**: Save results to Redis (speakers + transcript)
7. **Stream**: Publish progress events via Redis PubSub
8. **Complete**: Frontend receives SSE notifications

## Dependencies

- **FastAPI**: Async web framework
- **Deepgram SDK**: Official Python SDK
- **Redis**: Event streaming and caching
- **FFmpeg**: Audio processing for snippets
- **Pydantic**: Data validation and settings
