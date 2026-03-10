# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## System Overview

This is a **multi-agent deep research system** for HPC support questions. It uses a supervisor-orchestrated workflow where multiple research agents query Elasticsearch-backed knowledge bases (docs and support tickets) and synthesize answers via an external LLM (GPT-OSS 120B). The system validates user assumptions, assesses answer quality, and iterates up to 3 times until confidence thresholds are met.

**Key insight**: This is NOT a simple RAG system - it's a multi-iteration research pipeline with quality feedback loops.

## Architecture: Three-Layer Design

```
FastAPI Layer (api/main.py)
    ↓ orchestrates
DR Workflow Layer (ticketknowledgedb/DR_Pipeline/)
    ├── dr_workflow.py        - Main orchestrator
    ├── supervisor_agent.py   - Decision-making, quality control
    ├── research_agent.py     - Multi-source research execution
    ├── assumption_checker.py - Fact validation
    └── search_service.py     - Elasticsearch interface
    ↓ queries
Data Layer
    ├── Elasticsearch (docs, tickets indices)
    └── External LLM Service
```

**Critical architectural note**: The `dr_workflow` instance is currently a **global singleton** (api/main.py:42), which causes race conditions under concurrent load. This is a known issue that must be addressed for production use.

## Development Commands

### Local Development Setup
```bash
# First time setup
cp .env.example .env  # Edit with your LLM_BASE_URL and other config

# Start services (Elasticsearch + DR API)
./scripts/start_services.sh

# Index data into Elasticsearch (required before first query)
./scripts/index_data.sh

# Check everything is working
curl http://localhost:8001/health | jq
```

### Running the DR Pipeline Directly
```bash
# From ticketknowledgedb/DR_Pipeline/ directory
python run_dr.py --query "How do I submit a SLURM job?"
python run_dr.py --interactive  # Interactive mode
python run_dr.py --test-connections  # Verify Elasticsearch + LLM
```

### API Testing
```bash
# Health check
curl http://localhost:8001/health | jq

# Synchronous query
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I load modules?", "brief": true}' | jq

# Streaming query (SSE)
curl -N -X POST http://localhost:8001/query/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "Why is my GPU job slow?"}'

# Direct search (bypasses DR pipeline)
curl -X POST http://localhost:8001/search \
  -H "Content-Type: application/json" \
  -d '{"query": "SLURM", "index": "tickets", "max_results": 5}' | jq
```

### Docker Operations
```bash
# Start services
docker compose up -d elasticsearch dr-api

# View logs
docker compose logs -f dr-api
docker compose logs -f elasticsearch

# Run indexer (one-time or re-index)
docker compose --profile indexing up indexer

# Stop services
docker compose down

# Rebuild after code changes
docker compose build dr-api
docker compose up -d dr-api
```

### Deployment
```bash
# Build and push images
./scripts/build_images.sh
./scripts/push_images.sh

# Terraform deployment to OpenStack
cd deploy/terraform
terraform init
terraform plan
terraform apply
```

## Critical Code Patterns

### 1. Dual Import Pattern (Required)
All DR_Pipeline modules use try/except imports to work both as direct scripts and as package imports:

```python
try:
    from dr_models import ResearchType  # Direct execution
except ImportError:
    from .dr_models import ResearchType  # Package import
```

**Always maintain this pattern** when adding new modules.

### 2. Async/Await Throughout
All I/O operations (LLM calls, Elasticsearch queries) are async:

```python
# In research_agent.py
async def research_from_docs(self, query: str) -> ResearchAnswer:
    search_request = HPCSearchRequest(query=query, search_type="docs")
    search_response = await search_service.search(search_request)
    response = await self.llm.ainvoke(messages)
```

**Never use blocking calls** in the DR pipeline or API layer.

### 3. Configuration via Environment Variables
Configuration is centralized in `DR_Pipeline/dr_config.py` with environment variable fallbacks:

```python
@dataclass
class DRConfig:
    llm_base_url: str = "http://lme49.cs.fau.de:30000/v1"

    @classmethod
    def from_env(cls) -> 'DRConfig':
        return cls(
            llm_base_url=os.getenv("LLM_BASE_URL", cls.llm_base_url),
            # ...
        )

config = DRConfig.from_env()  # Global instance
```

All services read from this global `config` instance. Changes require container restart.

### 4. Data Models (dr_models.py)
The system uses strongly-typed dataclasses and enums:

- **ResearchType**: ZERO_SHOT, DOCS_ONLY, TICKETS_ONLY, SOLUTION_FOCUSED
- **QualityScore**: 5-point scale (INSUFFICIENT to EXCELLENT)
- **DRIteration**: Contains research_answers, user_assumptions, quality_assessments
- **DRResult**: Final output with iterations, final_report, concise_answer, confidence_score

Understanding these models is essential for working with the DR pipeline.

### 5. GPT-OSS Model Workarounds
This system is adapted for GPT-OSS models which have specific quirks:

**Channel Tag Cleanup** (in supervisor_agent.py):
```python
# GPT-OSS sometimes outputs <|channel|>analysis<|message|>content
if "<|channel|>" in answer:
    if "<|channel|>final<|message|>" in answer:
        answer = answer.split("<|channel|>final<|message|>")[-1]
    answer = answer.replace("<|channel|>", "").replace("<|message|>", "")
```

**Positive Reformulation Only**:
The assumption checker never says "FALSE" - it reformulates negatively into positive statements to avoid model confusion.

**Query Simplification**:
To avoid Elasticsearch "too many clauses" errors, queries are simplified to max 4 key terms in `research_agent._simplify_query_for_tickets()`.

## Environment Variables Reference

Required in `.env` for local development:

```bash
# LLM Configuration
LLM_BASE_URL=http://lme49.cs.fau.de:30000/v1  # Your LLM endpoint
LLM_MODEL=openai/gpt-oss-120b
LLM_TEMPERATURE=0.2
LLM_API_KEY=dummy  # Often not needed for internal endpoints

# Elasticsearch
ELASTIC_URL=http://elasticsearch:9200  # In Docker: elasticsearch
ELASTICSEARCH_PORT=9200
DOCS_INDEX=docs
TICKETS_INDEX=tickets

# DR Pipeline
MAX_ITERATIONS=3
CONFIDENCE_THRESHOLD=0.6
MAX_SEARCH_RESULTS=10

# API
DR_API_PORT=8001
```

## Working with the DR Pipeline

### Request Flow (Typical Query)
1. **API receives POST /query** → `process_query()` in api/main.py
2. **DRWorkflow.process_query()** → Starts iteration loop
3. **SupervisorAgent.conduct_dr_workflow()**:
   - **Iteration 1**: Comprehensive research
     - ResearchAgent: zero_shot, docs_only, tickets_only research
     - AssumptionChecker: validates user assumptions
     - SupervisorAgent: assesses quality of all answers
     - Decision: Continue if quality < threshold, stop if excellent
   - **Iteration 2+**: Solution-focused refinement (if needed)
4. **Generate outputs**:
   - `generate_final_report()`: Comprehensive synthesis
   - `generate_concise_answer()`: Max 4 sentences, fact-checked
5. **Return DRResult** with confidence score

### Adding a New Research Type
1. Add enum to `dr_models.py`:
   ```python
   class ResearchType(Enum):
       YOUR_TYPE = "your_type"
   ```

2. Implement method in `research_agent.py`:
   ```python
   async def research_your_type(self, query: str) -> ResearchAnswer:
       # Implementation
   ```

3. Update supervisor logic in `supervisor_agent.py`:
   ```python
   # In conduct_dr_workflow(), add call to new research type
   ```

### Debugging Common Issues

**"Elasticsearch connection failed"**:
- Check `curl http://localhost:9200/_cluster/health`
- Verify indices exist: `curl http://localhost:9200/_cat/indices?v`
- Re-run indexer if needed: `./scripts/index_data.sh`

**"LLM connection failed"**:
- Verify `LLM_BASE_URL` in .env
- Test manually: `curl $LLM_BASE_URL/models`
- Check network connectivity to LLM server

**"Channel tags in output"**:
- This is a known GPT-OSS issue
- Workaround is in supervisor_agent.py lines ~580-585
- May need adjustment based on model version

**"Too many clauses" Elasticsearch error**:
- Query is too complex
- Check `research_agent._simplify_query_for_tickets()`
- Reduce MAX_SEARCH_RESULTS if needed

**"Import errors"**:
- Ensure dual import pattern (try/except) is used
- Check Python path includes DR_Pipeline directory
- In api/main.py, sys.path.insert handles this

## Data Indexing

### Data Structure Expected
```
ticketknowledgedb/
├── docsmd/
│   └── docs_data.jsonl        # HPC documentation
│       Format: {"id": "...", "title": "...", "text": "...", "url": "..."}
├── knowledgebase/
│   └── *.md                   # Historical support tickets
└── topic_clusters/            # Optional clustered tickets
    └── topic_*.md
```

### Indexing Process
The indexer (`indexer/index_all.py`) reads data and creates Elasticsearch indices with specific mappings:

**docs index**: title (text), text (text), url (keyword)
**tickets index**: title, problem_description, solution, root_cause, keywords, etc.

Run indexer:
```bash
docker compose --profile indexing up indexer
```

### Verify Indexing
```bash
# Check indices exist
curl http://localhost:9200/_cat/indices?v

# Count documents
curl http://localhost:9200/docs/_count
curl http://localhost:9200/tickets/_count

# Sample search
curl -X POST http://localhost:9200/docs/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"title": "SLURM"}}, "size": 1}'
```

## Known Limitations & Security Issues

### CRITICAL - Security Gaps (Not Production Ready)
- **No authentication** on API endpoints (SEC-002)
- **CORS wide open** to all origins (SEC-001)
- **Elasticsearch no auth** (SEC-003)
- **No rate limiting** (SEC-007)
- **Global mutable state** causing race conditions (REL-001)

**Do not deploy to production** without addressing these. See the code review report for details.

### Performance Characteristics
- Simple queries: 10-30 seconds
- Complex queries: 60-120 seconds
- Current capacity: 1 concurrent user (due to global workflow instance)
- No caching (every query hits LLM + Elasticsearch)

### Model-Specific Behavior
- GPT-OSS 120B model has 10-15 second latency per call
- Multi-iteration queries make 5-10+ LLM calls
- Assumption reformulation prefers positive statements
- Quality assessment uses simplified 5-point scale

## File Structure Guide

```
hpc_ticket_knowledgedb/
├── api/
│   └── main.py                      # FastAPI app, endpoints, CORS config
├── ticketknowledgedb/DR_Pipeline/   # Core DR system
│   ├── run_dr.py                    # CLI entry point for testing
│   ├── dr_workflow.py               # Main orchestrator
│   ├── dr_config.py                 # Configuration (reads env vars)
│   ├── dr_models.py                 # Type definitions (MUST understand these)
│   ├── supervisor_agent.py          # Quality control, iteration decisions
│   ├── research_agent.py            # Multi-source research execution
│   ├── assumption_checker.py        # Fact validation logic
│   └── search_service.py            # Elasticsearch client with retry logic
├── indexer/
│   └── index_all.py                 # Data indexing to Elasticsearch
├── scripts/
│   ├── start_services.sh            # Local development startup
│   ├── index_data.sh                # Run indexer
│   ├── build_images.sh              # Docker build
│   └── push_images.sh               # Docker push to registry
├── docker-compose.yml               # Services: elasticsearch, dr-api, indexer
├── Dockerfile.api                   # DR API container
├── Dockerfile.indexer               # Indexer container
└── .env.example                     # Config template
```

## Testing Strategy

**No unit tests currently exist** - this is a critical gap (QUA-001).

For manual testing:
1. Use `run_dr.py --test-connections` to verify services
2. Test API endpoints with curl examples above
3. Check Elasticsearch query results directly
4. Monitor logs for LLM response quality
5. Verify assumption reformulation in output

## OpenWebUI Integration

The `openwebui_pipeline.py` file exposes this system as a model in OpenWebUI:
- Streams responses via SSE
- Configurable timeouts (default 180s)
- Brief mode toggle
- Forwards to `/query` or `/query/stream` endpoints

Deploy by pasting code into OpenWebUI Admin → Pipelines.

## Scalability Considerations

See the comprehensive scalability documentation:
- `SCALABILITY_PLAN.md` - 3-phase implementation roadmap
- `ARCHITECTURE.md` - Target architecture diagrams
- `OPTION_COMPARISON.md` - OpenStack vs. AWS cost analysis

**Current bottlenecks**:
1. Global singleton workflow instance
2. No connection pooling
3. No caching layer
4. Single Elasticsearch node
5. No horizontal scaling

**Phase 1 quick wins** (1-2 weeks):
- Fix global state with request-scoped instances
- Add basic caching (in-memory TTL cache)
- Implement rate limiting
- Add authentication

## When Making Changes

**Always consider**:
1. Maintain dual import pattern in DR_Pipeline modules
2. Keep async/await for all I/O
3. Update dr_models.py if changing data structures
4. Test with both direct execution and API access
5. Verify Elasticsearch query performance (check for "too many clauses")
6. Monitor for GPT-OSS channel tag leakage in outputs
7. Update .env.example if adding new config
8. Rebuild Docker images after code changes

**Never**:
- Use blocking I/O in async contexts
- Hardcode file paths (use environment variables)
- Skip the channel tag cleanup logic
- Assume concurrent safety (global state issue exists)
- Expose Elasticsearch port 9200 publicly
- Commit .env or terraform.tfvars files
