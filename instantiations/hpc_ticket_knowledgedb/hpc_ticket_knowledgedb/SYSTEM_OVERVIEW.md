# HPC Ticket Knowledge Database - System Overview

## System Purpose
Multi-agent deep research system for HPC support questions, built on historical ticket data, HPC documentation, and knowledge base. Provides intelligent Q&A capabilities through supervised research agents and Elasticsearch-backed knowledge retrieval.

## Technology Stack
- **API Framework**: FastAPI (Python)
- **Search Engine**: Elasticsearch 8.11.0
- **LLM Integration**: LangChain + OpenAI-compatible API
- **Agent Framework**: LangGraph multi-agent workflow
- **Deployment**: Docker Compose
- **Integration**: OpenWebUI pipeline

## System Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        A[OpenWebUI Interface]
        B[Direct API Client]
    end

    subgraph "API Layer"
        C["FastAPI Server<br/>Port 8001"]
        C1["POST /query"]
        C2["POST /query/stream"]
        C3["POST /search"]
        C4["GET /health"]
        C --> C1
        C --> C2
        C --> C3
        C --> C4
    end

    subgraph "Business Logic Layer"
        D[DR Workflow Orchestrator]
        E[Supervisor Agent]
        F[Research Agent]
        G[Assumption Checker]
    end

    subgraph "Data Layer"
        H[Search Service]
        I[Elasticsearch]
        I1[(docs index)]
        I2[(tickets index)]
        I --> I1
        I --> I2
    end

    subgraph "External Services"
        J[LLM Service<br/>GPT-OSS 120B]
    end

    A --> C
    B --> C
    C1 --> D
    C2 --> D
    C3 --> H
    D --> E
    E --> F
    E --> G
    F --> H
    G --> H
    H --> I
    E --> J
    F --> J
    G --> J

    style C fill:#4a90e2
    style D fill:#50c878
    style I fill:#f39c12
    style J fill:#e74c3c
```

## Request Processing Flow

```mermaid
sequenceDiagram
    actor User
    participant API as FastAPI
    participant DRW as DR Workflow
    participant SUP as Supervisor Agent
    participant RES as Research Agent
    participant ASM as Assumption Checker
    participant SRC as Search Service
    participant ES as Elasticsearch
    participant LLM as LLM Service

    User->>API: POST /query<br/>{query: "How to submit SLURM job?"}
    API->>DRW: process_query(query)

    DRW->>SUP: conduct_dr_workflow(query)

    rect rgb(240, 248, 255)
        Note over SUP,LLM: Iteration 1: Comprehensive Research
        SUP->>RES: research_zero_shot(query)
        RES->>LLM: Generate answer without docs
        LLM-->>RES: Initial answer

        SUP->>RES: research_from_docs(query)
        RES->>SRC: search(query, index=docs)
        SRC->>ES: Search docs index
        ES-->>SRC: Top 10 results
        SRC-->>RES: Search results
        RES->>LLM: Synthesize with docs
        LLM-->>RES: Docs-based answer

        SUP->>RES: research_from_tickets(query)
        RES->>SRC: search(query, index=tickets)
        SRC->>ES: Search tickets index
        ES-->>SRC: Top 10 results
        SRC-->>RES: Search results
        RES->>LLM: Synthesize with tickets
        LLM-->>RES: Ticket-based answer

        SUP->>ASM: check_assumptions(query, answers)
        ASM->>LLM: Identify assumptions
        LLM-->>ASM: Detected assumptions
        ASM->>SRC: Verify assumptions
        SRC->>ES: Search for facts
        ES-->>SRC: Verification data
        ASM->>LLM: Reformulate if needed
        LLM-->>ASM: Reformulated assumptions
        ASM-->>SUP: Assumption results

        SUP->>LLM: assess_quality(answers)
        LLM-->>SUP: Quality scores
    end

    SUP->>SUP: Check if quality sufficient<br/>(threshold: 0.7)

    alt Quality insufficient
        rect rgb(255, 248, 240)
            Note over SUP,LLM: Iteration 2+: Refinement
            SUP->>RES: targeted_research(gaps)
            RES->>SRC: search(refined_query)
            SRC->>ES: Search
            ES-->>SRC: Results
            RES->>LLM: Synthesize
            LLM-->>RES: Refined answer
            SUP->>LLM: Re-assess quality
            LLM-->>SUP: Updated scores
        end
    end

    SUP-->>DRW: iterations[]

    DRW->>SUP: generate_final_report(iterations)
    SUP->>LLM: Synthesize comprehensive report
    LLM-->>SUP: Final report

    DRW->>SUP: generate_concise_answer(report)
    SUP->>LLM: Extract concise answer
    LLM-->>SUP: Concise answer

    DRW-->>API: DRResult<br/>{answer, report, confidence, iterations}
    API-->>User: HTTP 200<br/>JSON response
```

## Core Components

### 1. API Layer (`api/main.py`)
**Purpose**: Expose DR functionality via REST endpoints

**Key Endpoints**:
- `GET /health` - System health check
- `POST /query` - Synchronous query processing
- `POST /query/stream` - Server-sent events streaming
- `POST /search` - Direct Elasticsearch search bypass

**Configuration**: Environment-based via `DRConfig.from_env()`

### 2. DR Workflow (`DR_Pipeline/dr_workflow.py`)
**Purpose**: Orchestrate multi-agent research process

**Responsibilities**:
- Coordinate supervisor and agents
- Manage iteration loop (max 3 iterations)
- Calculate final confidence scores
- Generate comprehensive reports

### 3. Supervisor Agent (`DR_Pipeline/supervisor_agent.py`)
**Purpose**: Decision-making and quality control

**Functions**:
- Determine research strategies
- Assess answer quality (5-point scale)
- Decide when to stop iterating
- Synthesize final outputs

### 4. Research Agent (`DR_Pipeline/research_agent.py`)
**Purpose**: Execute different research strategies

**Research Types**:
- **Zero-shot**: LLM knowledge only
- **Docs-based**: HPC documentation search
- **Tickets-based**: Historical ticket search
- **Combined**: Multi-source synthesis

### 5. Assumption Checker (`DR_Pipeline/assumption_checker.py`)
**Purpose**: Validate and reformulate user assumptions

**Process**:
1. Extract implicit assumptions from query
2. Fact-check against documentation
3. Reformulate incorrect assumptions
4. Return positive statements only

### 6. Search Service (`DR_Pipeline/search_service.py`)
**Purpose**: Interface with Elasticsearch

**Features**:
- Multi-index search (docs, tickets)
- Query optimization for performance
- Retry logic with exponential backoff
- Result ranking and highlighting

## Data Flow Summary

1. **User Query** → FastAPI endpoint
2. **DR Workflow** initiates with supervisor
3. **Iteration Loop**:
   - Research agent queries Elasticsearch
   - LLM synthesizes results
   - Assumption checker validates facts
   - Supervisor assesses quality
   - Loop continues if quality < threshold
4. **Final Generation**:
   - Comprehensive report from all iterations
   - Concise answer (max 4 sentences)
   - Confidence scoring
5. **Response** returned to client

## Deployment Configuration

### Docker Compose Services
- **elasticsearch**: Single-node cluster, 2GB heap, volume persistence
- **dr-api**: FastAPI server, depends on Elasticsearch
- **indexer**: One-time data loading (profile: indexing)

### Environment Variables (Key)
```bash
# LLM
LLM_BASE_URL=http://lme49.cs.fau.de:30000/v1
LLM_MODEL=openai/gpt-oss-120b
LLM_TEMPERATURE=0.2

# Elasticsearch
ELASTIC_URL=http://elasticsearch:9200
DOCS_INDEX=docs
TICKETS_INDEX=tickets

# DR Settings
MAX_ITERATIONS=3
CONFIDENCE_THRESHOLD=0.6
MAX_SEARCH_RESULTS=10
```

## Performance Characteristics

- **Simple queries** (FAQ hit): 10-30 seconds
- **Complex queries** (multi-iteration): 60-120 seconds
- **Average confidence**: 0.75-0.85
- **Multi-iteration rate**: ~30% of queries

## Integration Points

### OpenWebUI Pipeline
- Exposes as model in OpenWebUI chat interface
- Streaming support via SSE
- Configurable timeouts and brief mode

### Elasticsearch Indices
- **docs**: HPC documentation (title, text, URL)
- **tickets**: Support tickets (problem, solution, root cause)

## Security Model (Current)

- **Authentication**: None (open endpoints)
- **CORS**: Wildcard allowed origins
- **Elasticsearch**: No authentication (single-node dev mode)
- **Secrets**: Environment variables

## Known Limitations

1. **Channel Tag Formatting**: GPT-OSS models occasionally include internal reasoning tags
2. **Sequential Processing**: No true parallel agent communication
3. **Search Strategy**: Simple keyword matching, no semantic embeddings
4. **Resource Limits**: No rate limiting or quota management
5. **Error Handling**: Broad exception catching without fine-grained recovery

## Monitoring & Observability

**Current State**:
- Print-based logging to stdout
- Basic health check endpoint
- No structured metrics
- No distributed tracing

**Recommended Additions**:
- Prometheus metrics
- Structured JSON logging
- Request correlation IDs
- Performance profiling

---

**Last Updated**: 2025-12-06
**Version**: 1.0.0
**Status**: Development (Not Production Ready)
