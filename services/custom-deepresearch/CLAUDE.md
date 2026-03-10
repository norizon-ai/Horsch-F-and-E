# CLAUDE.md - Norizon DeepSearch

## What is DeepSearch?

DeepSearch is a multi-agent RAG (Retrieval-Augmented Generation) system where a supervisor LLM orchestrates specialized research agents via function calling. It's the backend service powering Nora's knowledge search capabilities.

**Core flow:** User query → Supervisor → Agents (Elasticsearch, Web, Custom) → Quality assessment → Final report

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         API Layer                            │
│  FastAPI: /api/v1/search, /search/sync, /stream, /health    │
├─────────────────────────────────────────────────────────────┤
│                      Orchestration                           │
│  SupervisorAgent → delegates to agents via function calling  │
│  QualityAssessor → decides CONTINUE or COMPLETE             │
├─────────────────────────────────────────────────────────────┤
│                       Agent Layer                            │
│  BaseAgent + ReasoningMixin → tool execution loop           │
│  ElasticsearchAgent, WebSearchAgent, Custom agents          │
├─────────────────────────────────────────────────────────────┤
│                      Core Components                         │
│  LLM Providers │ PromptManager │ Search Backends │ Tools    │
└─────────────────────────────────────────────────────────────┘
```

## Key Files

| File | Purpose |
|------|---------|
| `deepsearch/main.py` | FastAPI app entry point |
| `deepsearch/api/routes.py` | API endpoints |
| `deepsearch/supervisor/agent.py` | SupervisorAgent - main orchestrator |
| `deepsearch/agents/base.py` | BaseAgent, AgentRegistry |
| `deepsearch/agents/reasoning.py` | ReasoningAgentMixin - tool execution loop |
| `deepsearch/agents/elasticsearch/agent.py` | Elasticsearch search agent |
| `deepsearch/config.py` | Pydantic settings, env vars |
| `prompts/*.yaml` | All LLM prompts (externalized) |
| `agents.yaml` | Agent configuration per deployment |

## Running the Service

```bash
# Development
source venv/bin/activate
uvicorn deepsearch.main:app --reload --port 8000

# With dependencies
docker-compose up -d elasticsearch searxng
uvicorn deepsearch.main:app --reload

# Health check
curl http://localhost:8000/api/v1/health

# Test search
curl -X POST http://localhost:8000/api/v1/search/sync \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the RC-3000?"}'
```

## Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test files
pytest tests/unit/ -v
pytest tests/e2e/test_realistic_scenarios.py -v

# With coverage
pytest tests/ --cov=deepsearch
```

## Configuration

**Environment variables** (prefix `DR_`):
- `DR_LLM_PROVIDER`: `openai`, `anthropic`, `gpt-oss`, `ollama`
- `DR_LLM_BASE_URL`: API endpoint
- `DR_LLM_API_KEY`: API key
- `DR_LLM_MODEL`: Model name
- `DR_MAX_ITERATIONS`: Max search iterations (default: 3)
- `DR_QUALITY_THRESHOLD`: Stop when quality >= threshold (default: 0.7)

**Agent config** (`agents.yaml`):
```yaml
agents:
  docs:
    type: elasticsearch
    enabled: true
    backend:
      url: "http://localhost:9200"
      index: "documents"
```

## Extension Points

### Adding a New Agent

```python
# deepsearch/agents/my_agent/agent.py
from deepsearch.agents import BaseAgent, ReasoningAgentMixin, AgentRegistry

class MyAgent(BaseAgent, ReasoningAgentMixin):
    @property
    def name(self) -> str:
        return "my_agent"

    @property
    def tools(self) -> list:
        return [MySearchTool(), MyFetchTool()]

    async def run(self, task: str, **kwargs):
        return await self.reasoning_loop(task, **kwargs)

# Register in __init__.py or agent factory
AgentRegistry.register(MyAgent(llm, prompts))
```

### Adding a New Tool

```python
# deepsearch/tools/my_tool.py
from deepsearch.tools import BaseTool

class MyTool(BaseTool):
    @property
    def name(self) -> str:
        return "my_tool"

    @property
    def description(self) -> str:
        return "Does something useful"

    @property
    def parameters(self) -> dict:
        return {"type": "object", "properties": {...}}

    async def execute(self, **kwargs) -> ToolResult:
        # Implementation
        return ToolResult(output="...", metadata={})
```

### Modifying Prompts

All prompts are in `prompts/*.yaml`. Edit directly - no code changes needed.

```yaml
# prompts/supervisor.yaml
system: |
  You are a research supervisor...

generate_report: |
  Create a comprehensive report from: {agent_results}
```

## Code Patterns

### Async everywhere
All I/O operations are async. Use `async def` and `await`.

### Pydantic for data models
```python
from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    max_iterations: int = 3
```

### Function calling for agent delegation
Supervisor uses LLM function calling to select and delegate to agents:
```python
functions = [agent.to_function_schema() for agent in AgentRegistry.all_agents()]
response = await llm.complete_with_functions(messages, functions)
```

### SSE streaming for real-time updates
```python
stream.emit("progress", {"phase": "searching"})
stream.complete(result)  # Final event
```

## Common Development Tasks

### Add a new API endpoint
1. Add route in `deepsearch/api/routes.py`
2. Add request/response models in `deepsearch/api/models.py`

### Add a new search backend
1. Implement `SearchBackend` interface in `deepsearch/retrievers/search_backends/`
2. Register in backend factory

### Change LLM behavior
1. Edit relevant prompt in `prompts/*.yaml`
2. Test with evaluation suite: `pytest tests/evaluation/`

### Debug agent behavior
```bash
export DR_LOG_LEVEL=DEBUG
uvicorn deepsearch.main:app --reload
```

## Don'ts

- Don't hardcode prompts in Python code - use `prompts/*.yaml`
- Don't add synchronous I/O - everything is async
- Don't modify `config.py` for deployment-specific settings - use env vars
- Don't add agents without registering them in `AgentRegistry`

## Documentation

| Document | Location |
|----------|----------|
| Setup Guide | `docs/SETUP_GUIDE.md` |
| API Reference | `docs/API_REFERENCE.md` |
| Architecture | `ARCHITECTURE.md` |
| SSE Streaming | `docs/streaming.md` |
| Fine-tuning | `docs/guides/fine-tuning.md` |
| Testing | `docs/guides/testing.md` |
