# CLAUDE.md - Norizon Software Suite

## What is Norizon?

Norizon is an AI-powered knowledge management platform for German mid-sized manufacturing and IT companies. The core problem we solve: 13 million German workers will retire by 2037, taking billions worth of undocumented expertise with them. Norizon captures, structures, and makes that knowledge accessible before it walks out the door.

## The Big Picture

Norizon is NOT just a chatbot. It's a platform with three layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATIONS LAYER                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │    Tools    │  │  Workflows  │  │ Industry Modules    │  │
│  │ (chat-based)│  │   (apps)    │  │ (domain-specific)   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    NORIZON PLATFORM                          │
│  ┌─────────────────┐  ┌──────────────────────────────────┐  │
│  │ Domain-specific │  │ Self-maintaining Knowledge Base  │  │
│  │ AI Models       │  │ (Knowledge Graph + Vector DB)    │  │
│  └─────────────────┘  └──────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    INTEGRATIONS LAYER                        │
│  SharePoint │ Confluence │ Jira │ SAP │ Slack │ Email │ ... │
└─────────────────────────────────────────────────────────────┘
```

## Product: "Nora" - The User-Facing Interface

Nora is the consumer-facing name for our knowledge assistant. It's what employees interact with daily.

### Core Concepts

**Tools** = Chat-based, stateless interactions that start a new conversation
- Knowledge Search (default) - searches across all connected sources
- Quote Generator - creates quotes from pricing rules and product catalog
- Product Troubleshooter - diagnoses issues using technical documentation
- Policy Assistant - answers HR/compliance questions
- More can be added per customer

**Workflows** = Multi-step, stateful processes that open as dedicated apps
- Employee Onboarding - guided new hire setup
- Employee Offboarding / Knowledge Transfer - AI-interviewed documentation (Fraunhofer 10-step methodology)
- Compliance Audit - checklist with evidence collection
- More can be added per customer

**Auto-matching** = When a user types in the search box, Nora detects intent and selects the appropriate tool automatically. Users can override this.

## Repository Structure

```
rag-server/
├── assets/                     # Brand assets (logo)
├── docs/                       # Architecture diagrams, security strategy
├── instantiations/             # Customer-specific deployments
│   ├── horsch_confluence_assistant/
│   ├── hpc_ticket_knowledgedb/
│   └── TechMech_Solutions_GmbH/
└── services/                   # Microservices (see below)
```

## Services Architecture

### Core RAG & Search

- **custom-deepresearch** (Port 8000) - Multi-agent RAG system with supervisor pattern. Orchestrates specialized research agents via function calling. SSE streaming. YAML-based agent configuration. Supports OpenAI, Anthropic, Ollama, GPT-OSS providers.
- **norizon-research** (Port 5173/3000) - SvelteKit frontend. Chat interface with streaming, inline citations, session management, SearXNG metasearch integration.

### Knowledge Management

- **knowledge-studio** (Port 8092) - Full knowledge capture/documentation workflow. React/TypeScript frontend + Python backend. RabbitMQ for async. Transcription via AssemblyAI & Deepgram.
- **kstudio** (Port 5173) - Lightweight alternative/preview. Python backend + frontend.
- **workflow-service** (Port 8001) - Orchestrates Knowledge Transfer sessions. 10-step Fraunhofer methodology. Interview AI, content generation, approval workflows.

### Transcription & Audio

- **transcription-service** (Port 8002) - Speech-to-text. Streaming + batch. Speaker diarization, language detection (DE primary, EN secondary). FastAPI.
- **deepgram-service** (Port 8002) - Deepgram Nova-2 transcription. Redis event streaming. FFmpeg audio processing.

### Content Publishing

- **confluence-publisher** (Port 8003) - Publishes generated content to Confluence. ADF support, template rendering (Q&A, Process Doc, Troubleshooting). OAuth2 + API token auth.

### Data Integration & Connectors

- **connectors** - Confluence, Jira, Intranet (web crawling), Website (domain crawling). Data extraction and indexing.
- **confluence-mcp** (Port 8005) - MCP (Model Context Protocol) server for Confluence queries. Used by DeepSearch.

### Ingestion & Processing

- **ingestion_worker** - Document processing pipeline. Converts documents to embeddings.
- **add-knowledge** (Port 8092) - UI for adding documents to knowledge base. File upload and processing.
- **documentation-assistant** - Documentation workflow assistant. Backend + Frontend.

### AI Models & Inference

- **model_service** (Port 8000/8001) - Serves ML models via Ray + vLLM (OpenAI-compatible API). NER models. GPU support (NVIDIA CUDA, Apple Metal, CPU-only).
- **pi_service** - PII detection and anonymization. Plugin-based architecture. Microsoft Presidio, spaCy, Flair.

## Technical Stack

### Backend
- **Language:** Python (async-first)
- **Framework:** FastAPI + Uvicorn + Pydantic
- **LLM Providers:** OpenAI, Anthropic, Ollama, GPT-OSS
- **Model Serving:** Ray, vLLM

### Frontend
- **Primary:** SvelteKit (norizon-research)
- **Knowledge Studio:** React + TypeScript
- **Build:** Vite

### Data & Storage
- **PostgreSQL** - Primary database (sessions, workflows, audit logs)
- **Elasticsearch** - Search index and document indexing
- **Redis** - Caching, sessions, job queues (Redis Streams)
- **MinIO** - Object storage (S3-compatible)
- **RabbitMQ** - Message queue (knowledge-studio)

### Deployment
- **Docker & Docker Compose** - Primary deployment mechanism
- **Kubernetes** - K8s manifests available per service
- **Terraform** - Infrastructure as code (OpenStack deployments)
- **Target:** On-premise or EU-Cloud (Azure), GDPR-compliant

### Observability
- **OpenTelemetry** - Distributed tracing
- **Phoenix** - Trace visualization

### Key Libraries
- Deepgram SDK, AssemblyAI - Transcription
- Microsoft Presidio, spaCy, Flair - NLP / PII
- FFmpeg - Audio processing
- SearXNG - Privacy-respecting metasearch

## Design System

### Color Palette (MUST USE)
```css
/* Primary gradient - used for CTAs, logo, accents */
--gradient-warm: linear-gradient(135deg, #F97316 0%, #3B82F6 100%);

/* Orange spectrum */
--orange-500: #F97316;
--orange-100: #FFEDD5;
--orange-50: #FFF7ED;

/* Blue spectrum */
--blue-600: #2563EB;
--blue-500: #3B82F6;
--blue-100: #DBEAFE;
--blue-50: #EFF6FF;

/* Slate (neutrals) */
--slate-900: #0F172A;
--slate-700: #334155;
--slate-500: #64748B;
--slate-400: #94A3B8;
--slate-200: #E2E8F0;
--slate-100: #F1F5F9;
--slate-50: #F8FAFC;

/* Semantic colors */
--green-500: #22C55E;   /* success, approved */
--amber-500: #F59E0B;   /* warning, pending */
--purple-500: #A855F7;  /* workflows */
--red-500: #EF4444;     /* error, recording */
```

### Typography
- **Display/Logo:** Fraunces (serif)
- **Body:** DM Sans (sans-serif)
- **No emojis in UI**

### Design Principles
1. **Clarity over decoration** - Users should immediately understand what Nora does
2. **Sources matter** - Always show where information comes from (inline citations)
3. **Tools vs Workflows distinction must be visible** - Different icons, badges, and actions
4. **Progress transparency** - For workflows, always show where the user is in the process
5. **Professional B2B aesthetic** - Not consumer-playful, not enterprise-boring

## Key User Personas

1. **Office Worker (primary)** - Searching for internal knowledge, doesn't know/care where info is stored
2. **Departing Expert** - Senior employee documenting their knowledge before leaving
3. **Manager** - Reviews and approves knowledge documentation
4. **HR** - Initiates onboarding/offboarding workflows
5. **IT Admin** - Manages integrations and connected sources

## GDPR & Security

- Soft delete with configurable retention; hard delete (Article 17)
- Data portability exports (Article 20)
- TLS 1.3 for all service communication
- AES-256 encryption at rest (MinIO, PostgreSQL)
- Audit logging for all data access
- Role-based access control
- Audio/video encrypted in storage, optional deletion after approval
- PII anonymization pipeline (pi_service)

## Current Development Focus

### What Exists
- Multi-agent RAG system (custom-deepresearch) with streaming
- SvelteKit chat interface with inline citations (norizon-research)
- Knowledge Studio for knowledge capture workflows
- SharePoint/Confluence integrations and connectors
- Confluence publisher with ADF template rendering
- Model serving infrastructure (Ray + vLLM)
- PII detection/anonymization pipeline
- Transcription services (Deepgram, AssemblyAI)
- Workflow orchestration service (Fraunhofer 10-step)
- MCP server for Confluence

### What's Being Built
- Confluence agent integration into DeepSearch
- Advanced transcription pipeline refinements
- Knowledge Transfer workflow polish

### Roadmap
- Marketplace UI with Tools and Workflows
- Auto-matching search
- Usage Analytics & ROI dashboards
- Behavioral Engagement Framework
- Self-maintaining knowledge base
- Multi-tenant SaaS architecture
- SOC2 / BSI Grundschutz compliance

## Important Context

- **Target customers:** German mid-sized companies (50-500 employees) in Manufacturing (NACE C28) and IT Services (NACE J62)
- **Language:** UI should support German, but designs can be in English
- **White-labeling:** Nora can be renamed per customer, so avoid hardcoding the name where possible
- **Pricing:** Per-user-per-month SaaS model
- **Timeline:** SaaS launch November 2026, EXIST funding through June 2026

## When Working on Norizon Code

1. **Always use the established color palette** - The orange-to-blue gradient is our brand
2. **SvelteKit for norizon-research, React for knowledge-studio** - Check which service you're working in
3. **Inline citations** - Never use separate source panels that disconnect from content
4. **Tools start chats, Workflows open apps** - This distinction is fundamental
5. **German industrial context** - Think CNC machines, not Silicon Valley startups
6. **No emojis, no sycophancy** - Professional tone throughout
7. **Async-first Python** - All backend services use FastAPI with async/await
8. **Docker Compose** - Each service has its own compose file for local dev
9. **YAML configs** - Agent behavior is configured via YAML, not hardcoded
