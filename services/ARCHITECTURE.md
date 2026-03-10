# Norizon Services Architecture

This document describes the microservices architecture for the Norizon platform, including the existing DeepSearch system and the new Knowledge Transfer workflow.

## Overview

Norizon is built as a collection of loosely-coupled microservices that communicate via HTTP APIs and Redis message queues. The architecture prioritizes GDPR compliance, on-premise deployment capability, and integration with the existing DeepSearch multi-agent RAG system.

## Service Topology

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    NORA FRONTEND (SvelteKit)                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐ │
│  │  Chat Interface │  │ Workflow Home   │  │  Session View   │  │   Manager Review        │ │
│  │   (existing)    │  │ (10-step prog.) │  │ (recording UI)  │  │   Dashboard             │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  └───────────┬─────────────┘ │
└───────────┼───────────────────┼───────────────────┼──────────────────────────┼──────────────┘
            │                   │                   │                          │
            │ SSE              │ REST/SSE          │ WebSocket/SSE            │ REST
            │                   │                   │ (real-time)              │
┌───────────┴───────────────────┴───────────────────┴──────────────────────────┴──────────────┐
│                                      API GATEWAY                                             │
│                               (Kong/Traefik/Custom FastAPI)                                  │
│  - Authentication (JWT/OIDC)  - Rate limiting  - Request routing  - CORS                    │
└───────────┬───────────────────┬───────────────────┬──────────────────────────┬──────────────┘
            │                   │                   │                          │
┌───────────▼───────────┐ ┌─────▼─────────────┐ ┌───▼────────────────┐ ┌───────▼──────────────┐
│                       │ │                   │ │                    │ │                      │
│   DEEPSEARCH API      │ │ WORKFLOW SERVICE  │ │ TRANSCRIPTION SVC  │ │   CONFLUENCE         │
│   (existing)          │ │ (NEW)             │ │ (NEW)              │ │   PUBLISHER (NEW)    │
│   Port: 8000          │ │ Port: 8001        │ │ Port: 8002         │ │   Port: 8003         │
│                       │ │                   │ │                    │ │                      │
│ - Knowledge search    │ │ - Session CRUD    │ │ - Whisper/Cloud    │ │ - Page creation      │
│ - Multi-agent RAG     │ │ - 10-step state   │ │ - Streaming ASR    │ │ - Media attachment   │
│ - Report generation   │ │ - Interview AI    │ │ - Diarization      │ │ - Space management   │
│ - SSE streaming       │ │ - Content gen.    │ │ - Batch process    │ │ - Template rendering │
│                       │ │                   │ │                    │ │                      │
└───────────────────────┘ └───────────────────┘ └────────────────────┘ └──────────────────────┘
            │                   │                   │                          │
            └───────────────────┴───────────┬───────┴──────────────────────────┘
                                            │
┌───────────────────────────────────────────┴─────────────────────────────────────────────────┐
│                                    MESSAGE BROKER                                            │
│                                    Redis Streams                                             │
│                                                                                              │
│   Channels:                                                                                  │
│   - transcription.jobs.pending      - Audio files to transcribe                             │
│   - transcription.jobs.completed    - Completed transcripts                                 │
│   - content.generation.pending      - Content generation requests                           │
│   - content.generation.completed    - Generated content                                     │
│   - publishing.jobs.pending         - Pages to publish to Confluence                        │
│   - publishing.jobs.completed       - Published page confirmations                          │
│   - workflow.events                 - Session state changes (audit)                         │
└───────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                            │
┌───────────────────────────────────────────┴─────────────────────────────────────────────────┐
│                                    DATA LAYER                                                │
│                                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐ │
│  │   PostgreSQL     │  │  Elasticsearch   │  │  Object Storage  │  │       Redis          │ │
│  │   (primary DB)   │  │   (search index) │  │   (MinIO/S3)     │  │  (cache/sessions)    │ │
│  │                  │  │                  │  │                  │  │                      │ │
│  │ - User sessions  │  │ - Documents      │  │ - Audio/video    │  │ - Session state      │ │
│  │ - Workflows      │  │ - Transcripts    │  │ - Transcripts    │  │ - Job queues         │ │
│  │ - Audit logs     │  │ - Knowledge base │  │ - Generated docs │  │ - Rate limits        │ │
│  │ - Approvals      │  │                  │  │ - Attachments    │  │ - Pub/sub            │ │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Services

### Service Responsibility Matrix

| Service | Port | Primary Responsibility | Data Owned | Dependencies | Scaling |
|---------|------|------------------------|------------|--------------|---------|
| **DeepSearch** | 8000 | Knowledge search, RAG | Search results | Elasticsearch, LLM | Horizontal |
| **Workflow Service** | 8001 | Session state, interview orchestration | Sessions, workflows | PostgreSQL, Redis, DeepSearch | Horizontal |
| **Transcription Service** | 8002 | Speech-to-text, diarization | Transcripts | Object Storage, Whisper | Vertical (GPU) |
| **Confluence Publisher** | 8003 | Document publishing | Publish logs | Confluence API | Horizontal |
| **Nora Frontend** | 5173/3000 | User interface | - | All backend services | Horizontal |

### DeepSearch (Existing)

**Location:** `services/custom-deepresearch/`

A multi-agent RAG system where a supervisor LLM orchestrates specialized research agents via function calling.

**Key Characteristics:**
- Stateless request-response pattern
- In-memory job storage with 1-hour TTL
- Maximum search timeout: 300 seconds
- SSE streaming for progress updates

**API Endpoints:**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/search` | Start async search job |
| `POST` | `/api/v1/search/sync` | Synchronous search (blocking) |
| `GET` | `/api/v1/search/{job_id}` | Get job status |
| `GET` | `/api/v1/search/{job_id}/stream` | SSE stream for progress |
| `GET` | `/api/v1/health` | Health check |

**Integration Point:** The Workflow Service calls DeepSearch's `/api/v1/search/sync` endpoint for content generation, treating it as a specialized "document generation" task.

### Workflow Service (New)

**Location:** `services/workflow-service/`

Manages Knowledge Transfer sessions and orchestrates the 10-step Fraunhofer methodology for knowledge capture.

**Responsibilities:**
- Manage Knowledge Transfer sessions (CRUD)
- Orchestrate 10-step Fraunhofer methodology
- Drive AI-assisted interview conversations
- Coordinate content generation across agents
- Handle approval workflows
- Emit audit events for compliance

**Core Entities:**

```
KnowledgeTransferSession
├── id: UUID
├── employee_id: UUID (departing expert)
├── manager_id: UUID (approver)
├── status: enum(DRAFT, IN_PROGRESS, REVIEW, APPROVED, PUBLISHED)
├── current_step: int (1-10)
├── steps: Step[]
├── created_at, updated_at
└── metadata: JSON

Step
├── step_number: int
├── title: string
├── status: enum(NOT_STARTED, IN_PROGRESS, COMPLETED)
├── interviews: Interview[]
├── generated_content: Content[]
└── approval_status: enum(PENDING, APPROVED, REVISION_REQUESTED)

Interview
├── id: UUID
├── audio_file_url: string
├── transcript_id: UUID
├── duration_seconds: int
├── speakers: Speaker[]
└── ai_questions: Question[]
```

**API Endpoints:**

```yaml
# Session Management
POST   /api/v1/sessions                    # Create new KT session
GET    /api/v1/sessions                    # List sessions (with filters)
GET    /api/v1/sessions/{id}               # Get session details
PATCH  /api/v1/sessions/{id}               # Update session metadata
DELETE /api/v1/sessions/{id}               # Soft delete session

# Step Management
GET    /api/v1/sessions/{id}/steps                    # List all steps
GET    /api/v1/sessions/{id}/steps/{step_num}         # Get step details
POST   /api/v1/sessions/{id}/steps/{step_num}/start   # Start a step
POST   /api/v1/sessions/{id}/steps/{step_num}/complete # Mark step complete

# Interview Recording
POST   /api/v1/sessions/{id}/interviews                     # Create interview
GET    /api/v1/sessions/{id}/interviews                     # List interviews
POST   /api/v1/sessions/{id}/interviews/{int_id}/upload     # Upload audio
WS     /api/v1/sessions/{id}/interviews/{int_id}/stream     # Real-time transcription

# Content Generation
POST   /api/v1/sessions/{id}/steps/{step_num}/generate      # Generate content
GET    /api/v1/sessions/{id}/steps/{step_num}/content       # Get content
POST   /api/v1/sessions/{id}/steps/{step_num}/content/refine # Refine with feedback
GET    /api/v1/sessions/{id}/steps/{step_num}/content/stream # SSE stream

# Approval Workflow
POST   /api/v1/sessions/{id}/submit-for-review              # Submit to manager
POST   /api/v1/sessions/{id}/approve                        # Manager approves
POST   /api/v1/sessions/{id}/request-revision               # Request changes

# Publishing
POST   /api/v1/sessions/{id}/publish                        # Publish to Confluence
GET    /api/v1/sessions/{id}/publish-status                 # Get publish progress
```

### Transcription Service (New)

**Location:** `services/transcription-service/`

Handles speech-to-text conversion with support for real-time streaming and batch processing.

**Responsibilities:**
- Accept audio/video uploads (WebM, MP4, WAV, MP3, M4A)
- Real-time streaming transcription during recording
- Batch transcription for uploaded files
- Speaker diarization
- Language detection (German primary, English secondary)
- Timestamp alignment for citations

**Processing Modes:**
1. **Streaming Mode**: WebSocket connection during recording
2. **Batch Mode**: Async job queue for uploaded files
3. **Hybrid**: Start streaming, finalize with batch for accuracy

**API Endpoints:**

```yaml
# Batch Transcription
POST   /api/v1/jobs                        # Submit transcription job
GET    /api/v1/jobs/{id}                   # Get job status
GET    /api/v1/jobs/{id}/result            # Get transcript
DELETE /api/v1/jobs/{id}                   # Cancel job

# Streaming Transcription
WS     /api/v1/stream                      # Real-time transcription

# Transcript Management
GET    /api/v1/transcripts/{id}            # Get transcript
GET    /api/v1/transcripts/{id}/segments   # Get timestamped segments
GET    /api/v1/transcripts/{id}/speakers   # Get speaker segments
PATCH  /api/v1/transcripts/{id}            # Edit transcript (corrections)
```

### Confluence Publisher (New)

**Location:** `services/confluence-publisher/`

Handles publishing generated content to Confluence with proper formatting and media attachments.

**Responsibilities:**
- Authenticate with Confluence Cloud/Server (OAuth2, API token)
- Create pages with Atlassian Document Format (ADF)
- Render templates (Q&A, Process Doc, Troubleshooting Guide)
- Attach media files (audio, video, PDFs)
- Manage page hierarchy and spaces
- Handle publish failures with retry

**API Endpoints:**

```yaml
# Connection Management
POST   /api/v1/connections                 # Add Confluence connection
GET    /api/v1/connections                 # List connections
GET    /api/v1/connections/{id}/spaces     # List available spaces
DELETE /api/v1/connections/{id}            # Remove connection

# Publishing
POST   /api/v1/publish                     # Publish content
GET    /api/v1/publish/{job_id}            # Get publish job status
GET    /api/v1/publish/{job_id}/result     # Get published page URL

# Templates
GET    /api/v1/templates                   # List available templates
GET    /api/v1/templates/{id}/preview      # Preview with sample data
```

## Data Flows

### Interview Recording Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│   Frontend   │     │  Workflow    │     │  Transcription   │     │   Object     │
│   (Svelte)   │     │   Service    │     │     Service      │     │   Storage    │
└──────┬───────┘     └──────┬───────┘     └────────┬─────────┘     └──────┬───────┘
       │                    │                      │                      │
       │ 1. Start Interview │                      │                      │
       │───────────────────>│                      │                      │
       │                    │                      │                      │
       │   2. Interview ID  │                      │                      │
       │<───────────────────│                      │                      │
       │                    │                      │                      │
       │ 3. WebSocket Connect (audio stream)       │                      │
       │──────────────────────────────────────────>│                      │
       │                    │                      │                      │
       │                    │                      │ 4. Buffer & Store    │
       │                    │                      │─────────────────────>│
       │                    │                      │                      │
       │ 5. Partial Transcript (SSE)               │                      │
       │<──────────────────────────────────────────│                      │
       │                    │                      │                      │
       │ ... (continues during recording) ...      │                      │
       │                    │                      │                      │
       │ 6. Stop Recording  │                      │                      │
       │───────────────────>│                      │                      │
       │                    │ 7. Finalize Job      │                      │
       │                    │─────────────────────>│                      │
       │                    │                      │                      │
       │                    │ 8. Transcript Ready  │                      │
       │                    │<─────────────────────│                      │
       │                    │                      │                      │
       │ 9. Interview Complete                     │                      │
       │<───────────────────│                      │                      │
```

### Content Generation Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│   Frontend   │     │  Workflow    │     │   DeepSearch     │     │    Redis     │
│   (Svelte)   │     │   Service    │     │   (Content AI)   │     │   (Queue)    │
└──────┬───────┘     └──────┬───────┘     └────────┬─────────┘     └──────┬───────┘
       │                    │                      │                      │
       │ 1. Generate Content│                      │                      │
       │───────────────────>│                      │                      │
       │                    │                      │                      │
       │                    │ 2. Queue Job         │                      │
       │                    │─────────────────────────────────────────────>│
       │                    │                      │                      │
       │ 3. SSE Stream Start│                      │                      │
       │<───────────────────│                      │                      │
       │                    │                      │ 4. Process Job       │
       │                    │                      │<─────────────────────│
       │                    │                      │                      │
       │                    │ 5. Content Chunks    │                      │
       │                    │<─────────────────────│                      │
       │                    │                      │                      │
       │ 6. SSE Content     │                      │                      │
       │<───────────────────│                      │                      │
       │                    │                      │                      │
       │ 7. SSE Complete    │                      │                      │
       │<───────────────────│                      │                      │
```

### Publishing Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌──────────────┐
│   Frontend   │     │  Workflow    │     │   Confluence     │     │  Confluence  │
│   (Svelte)   │     │   Service    │     │   Publisher      │     │    API       │
└──────┬───────┘     └──────┬───────┘     └────────┬─────────┘     └──────┬───────┘
       │                    │                      │                      │
       │ 1. Publish Session │                      │                      │
       │───────────────────>│                      │                      │
       │                    │ 2. Publish Request   │                      │
       │                    │─────────────────────>│                      │
       │                    │                      │                      │
       │ 3. Job Started     │                      │                      │
       │<───────────────────│                      │                      │
       │                    │                      │ 4. Create Page       │
       │                    │                      │─────────────────────>│
       │                    │                      │                      │
       │                    │                      │ 5. Upload Media      │
       │                    │                      │─────────────────────>│
       │                    │                      │                      │
       │                    │ 6. Publish Complete  │                      │
       │                    │<─────────────────────│                      │
       │                    │                      │                      │
       │ 7. Published Event │                      │                      │
       │<───────────────────│                      │                      │
```

## Event Types

### SSE Events (Frontend)

```typescript
type WorkflowEvent =
  | { type: 'session_created'; session_id: string }
  | { type: 'step_started'; step_num: number }
  | { type: 'step_completed'; step_num: number }
  | { type: 'interview_started'; interview_id: string }
  | { type: 'transcript_partial'; text: string; speaker?: string }
  | { type: 'transcript_complete'; transcript_id: string }
  | { type: 'content_chunk'; content: string }
  | { type: 'content_complete'; content_id: string }
  | { type: 'approval_requested'; approver_id: string }
  | { type: 'approved'; approver_id: string }
  | { type: 'revision_requested'; comments: string }
  | { type: 'published'; page_url: string }
  | { type: 'error'; message: string; code: string };
```

### Redis Streams Channels

```
transcription.jobs.pending      # Audio files to transcribe
transcription.jobs.completed    # Completed transcripts
content.generation.pending      # Content generation requests
content.generation.completed    # Generated content
publishing.jobs.pending         # Pages to publish
publishing.jobs.completed       # Published confirmations
workflow.events                 # Audit events
```

## Storage Strategy

### Data Distribution

| Data Type | Primary Storage | Secondary/Index | Retention |
|-----------|----------------|-----------------|-----------|
| Sessions/Workflows | PostgreSQL | Elasticsearch | Indefinite |
| Transcripts (text) | PostgreSQL | Elasticsearch | 7 years (GDPR) |
| Audio/Video files | MinIO | - | Configurable |
| Generated content | PostgreSQL + MinIO | Elasticsearch | Indefinite |
| Audit logs | PostgreSQL | Elasticsearch | 10 years |
| Session state | Redis | - | Session TTL |
| Job queues | Redis Streams | - | 24 hours |

### Object Storage Structure

```
/norizon-media/
├── /audio/{tenant_id}/{session_id}/{interview_id}/
│   ├── recording.webm          # Original upload
│   ├── recording.wav           # Converted for processing
│   └── segments/               # Speaker-separated segments
├── /transcripts/{tenant_id}/{session_id}/{interview_id}/
│   ├── transcript.json         # Full structured transcript
│   └── transcript.vtt          # WebVTT for playback
├── /content/{tenant_id}/{session_id}/{step_num}/
│   ├── draft_v1.md
│   ├── draft_v2.md             # After feedback
│   └── final.md
└── /exports/{tenant_id}/{session_id}/
    ├── knowledge_transfer.pdf
    └── knowledge_transfer.docx
```

### PostgreSQL Schema (Key Tables)

```sql
CREATE TABLE kt_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    employee_id UUID NOT NULL,
    manager_id UUID,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'DRAFT',
    current_step INT DEFAULT 1,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    deleted_at TIMESTAMPTZ  -- Soft delete for GDPR
);

CREATE TABLE kt_steps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES kt_sessions(id),
    step_number INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'NOT_STARTED',
    approval_status VARCHAR(50),
    approved_by UUID,
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(session_id, step_number)
);

CREATE TABLE kt_interviews (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES kt_sessions(id),
    step_id UUID REFERENCES kt_steps(id),
    audio_file_url VARCHAR(1024),
    duration_seconds INT,
    transcript_id UUID,
    status VARCHAR(50) DEFAULT 'PENDING',
    speakers JSONB DEFAULT '[]',
    ai_questions JSONB DEFAULT '[]',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE kt_content (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES kt_sessions(id),
    step_id UUID REFERENCES kt_steps(id),
    version INT DEFAULT 1,
    template_id VARCHAR(100),
    content_markdown TEXT,
    content_file_url VARCHAR(1024),
    feedback JSONB DEFAULT '[]',
    status VARCHAR(50) DEFAULT 'DRAFT',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    created_by UUID
);

CREATE TABLE kt_audit_log (
    id BIGSERIAL PRIMARY KEY,
    session_id UUID,
    user_id UUID,
    action VARCHAR(100) NOT NULL,
    details JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Technology Choices

### Transcription

| Option | Latency | Cost | GDPR | Use Case |
|--------|---------|------|------|----------|
| **Whisper (local)** | 5-15min CPU, 1-3min GPU | Infrastructure | Full control | **Primary (on-premise)** |
| **Azure Speech** | 30s-2min | ~$1/hour | EU region | **Primary (EU-Cloud)** |
| **Whisper API** | 30s-2min | $0.006/min | US data | Not recommended |

**Configuration:**
```yaml
transcription:
  default_provider: whisper
  providers:
    whisper:
      model: large-v3
      device: cuda  # or cpu
      language: de
      compute_type: float16
    azure:
      region: westeurope
      language: de-DE
      diarization: true
```

### Message Queue

**Choice:** Redis Streams

- Already in the stack for caching/sessions
- Sufficient for expected throughput (<100 concurrent users)
- Simple deployment and operations

### Content Generation

Extend DeepSearch with a content generation agent:

```yaml
# agents.yaml extension
agents:
  content_generator:
    type: content
    enabled: true
    display_name: "Content Generator"
    description: "Generates structured documentation from transcripts"
    max_iterations: 5
    templates:
      - interview_qa
      - process_documentation
      - troubleshooting_guide
      - fraunhofer_10_step
```

## GDPR Compliance

### Data Protection Measures

1. **Data Minimization**
   - Only capture necessary audio
   - Transcripts can be anonymized post-processing
   - Option to delete source audio after approval

2. **Encryption**
   - TLS 1.3 for all service communication
   - AES-256 encryption at rest (MinIO, PostgreSQL)

3. **Access Control**
   - Role-based access (Employee, Manager, Admin)
   - Session-level permissions
   - Audit logging for all data access

4. **Data Deletion**
   - Soft delete with configurable retention
   - Hard delete capability per GDPR Article 17
   - Cascade deletion across services

5. **Data Portability**
   - Export session as ZIP (markdown + audio + metadata)
   - Standard formats (WebVTT, Markdown, PDF)

### Required GDPR Endpoints

```python
# Workflow Service GDPR endpoints
GET    /api/v1/gdpr/export/{user_id}      # Article 20: Data portability
DELETE /api/v1/gdpr/delete/{user_id}      # Article 17: Right to erasure
GET    /api/v1/gdpr/records/{user_id}     # Article 30: Processing records
```

## Infrastructure

### Docker Compose

```yaml
# docker-compose.workflows.yml
version: '3.8'

services:
  workflow-service:
    build: ./services/workflow-service
    ports:
      - "8001:8001"
    environment:
      - DATABASE_URL=postgresql://norizon:norizon@postgres:5432/workflows
      - REDIS_URL=redis://redis:6379/1
      - DEEPSEARCH_URL=http://deepsearch:8000
      - TRANSCRIPTION_URL=http://transcription:8002
      - CONFLUENCE_PUBLISHER_URL=http://confluence-publisher:8003
      - OBJECT_STORAGE_URL=http://minio:9000
    depends_on:
      - postgres
      - redis
      - minio

  transcription-service:
    build: ./services/transcription-service
    ports:
      - "8002:8002"
    environment:
      - WHISPER_MODEL=large-v3
      - WHISPER_DEVICE=cuda
      - REDIS_URL=redis://redis:6379/2
      - OBJECT_STORAGE_URL=http://minio:9000
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  confluence-publisher:
    build: ./services/confluence-publisher
    ports:
      - "8003:8003"
    environment:
      - DATABASE_URL=postgresql://norizon:norizon@postgres:5432/publisher
      - REDIS_URL=redis://redis:6379/3

  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=norizon
      - POSTGRES_PASSWORD=norizon
    volumes:
      - postgres_data:/var/lib/postgresql/data

  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    environment:
      - MINIO_ROOT_USER=norizon
      - MINIO_ROOT_PASSWORD=${MINIO_SECRET_KEY}
    volumes:
      - minio_data:/data
    ports:
      - "9000:9000"
      - "9001:9001"

volumes:
  postgres_data:
  minio_data:
```

### Scaling Considerations

| Service | Initial | 10-50 Users | 50+ Users |
|---------|---------|-------------|-----------|
| Workflow Service | 1 replica | 2 replicas | Horizontal auto-scale |
| Transcription | CPU worker | 1 GPU node | GPU cluster (K8s) |
| Confluence Publisher | 1 replica | 2 replicas | Horizontal auto-scale |
| PostgreSQL | Single node | Primary + replica | Managed service |
| MinIO | Single node | Clustered | S3-compatible cloud |

### Storage Estimates (100 users, 1 year)

- 2 sessions/month/user average
- 30 minutes audio + video per session
- ~500MB per session
- **Total: ~1.2TB/year**

## Implementation Roadmap

### Phase 1: Core Infrastructure (2 weeks)
- [ ] PostgreSQL schema + migrations
- [ ] MinIO object storage setup
- [ ] Redis Streams configuration
- [ ] Basic Workflow Service (sessions CRUD)

### Phase 2: Transcription Pipeline (3 weeks)
- [ ] Whisper integration (batch mode)
- [ ] WebSocket streaming transcription
- [ ] Speaker diarization
- [ ] Frontend recording component

### Phase 3: Content Generation (2 weeks)
- [ ] Content Generator agent (DeepSearch extension)
- [ ] Fraunhofer 10-step templates
- [ ] SSE streaming content generation
- [ ] Feedback/refinement loop

### Phase 4: Publishing & Approval (2 weeks)
- [ ] Confluence Publisher service
- [ ] Manager approval workflow
- [ ] Audit logging
- [ ] Export capabilities (PDF/Word)

### Phase 5: Frontend Integration (2 weeks)
- [ ] Workflow dashboard
- [ ] Session/step views
- [ ] Recording interface
- [ ] Manager review interface

## File Structure

```
services/
├── custom-deepresearch/          # Existing DeepSearch service
│   ├── deepsearch/
│   │   └── agents/
│   │       └── content/          # NEW: Content generation agent
│   └── agents.yaml               # Extended with content_generator
│
├── workflow-service/             # NEW: Workflow orchestration
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── models/
│   │   │   └── session.py
│   │   ├── services/
│   │   │   ├── interview.py
│   │   │   └── content.py
│   │   └── main.py
│   ├── migrations/
│   ├── Dockerfile
│   └── requirements.txt
│
├── transcription-service/        # NEW: Speech-to-text
│   ├── app/
│   │   ├── whisper_worker.py
│   │   ├── streaming.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── confluence-publisher/         # NEW: Confluence integration
│   ├── app/
│   │   ├── templates/
│   │   ├── publisher.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── norizon-research/
│   └── frontend/                 # Existing frontend
│       └── src/
│           └── routes/
│               └── workflows/    # NEW: Workflow UI routes
│                   └── knowledge-transfer/
│
└── ARCHITECTURE.md               # This document
```

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-01 | Separate microservice for workflows | DeepSearch is stateless (5min jobs), workflows are stateful (30min+ sessions) |
| 2025-01 | Redis Streams over RabbitMQ | Already in stack, sufficient for scale |
| 2025-01 | Whisper (local) as primary transcription | GDPR compliance, no external data transfer |
| 2025-01 | PostgreSQL for session state | Durable storage vs DeepSearch's in-memory cache |
| 2025-01 | HTTP integration with DeepSearch | Loose coupling, independent scaling |
