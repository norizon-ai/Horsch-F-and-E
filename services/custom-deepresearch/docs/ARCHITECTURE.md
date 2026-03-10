# Norizon DeepSearch - Architecture Documentation

This document explains the architectural decisions made during the design of the Norizon DeepSearch microservice middleware. Each decision was driven by specific requirements for **modularity**, **configurability**, **transparency**, and **multi-company deployment**.

---

## TL;DR - Key Architecture Points

- **Multi-Agent System**: Supervisor LLM orchestrates specialized agents (web search, Elasticsearch, custom) via function calling
- **Extensible Design**: Add new agents, tools, processors, and search backends without modifying core code
- **External Configuration**: All prompts in YAML files, config via environment variables (12-factor app)
- **Quality-Based Iteration**: Continues searching until quality threshold met or max iterations reached
- **Real-time Streaming**: SSE streaming for progress updates during long search operations

**Quick Links**: [Adding Agents](#adding-a-new-agent-recommended) | [Adding Retrievers](#adding-a-new-retriever-legacysimple-mode) | [Adding Processors](#adding-a-new-processor) | [Adding Backends](#adding-a-new-search-backend)

---

## Table of Contents

1. [Overview](#overview)
2. [Core Design Principles](#core-design-principles)
3. [Component Architecture](#component-architecture)
   - [Supervisor Agent](#supervisor-agent)
   - [Tool Framework](#tool-framework)
   - [Agent Framework](#agent-framework)
   - [Retrievers (Legacy/Simple Mode)](#retrievers-legacysimple-mode)
   - [Processors](#processors)
   - [LLM Providers](#llm-providers)
   - [Prompt Management](#prompt-management)
   - [Configuration](#configuration)
   - [API Layer](#api-layer)
   - [Observability](#observability)
4. [Data Flow](#data-flow)
5. [Extension Points](#extension-points)

---

## Overview

The Norizon search microservice is a **modular multi-agent RAG system** where a supervisor LLM orchestrates specialized research agents via **function calling**. The architecture supports:

- Multiple LLM providers (GPT-OSS, OpenAI, Anthropic, Ollama)
- **Specialized research agents** with their own tools and reasoning loops
- Pluggable retriever backends (Elasticsearch, SearXNG, future: ChromaDB, Pinecone)
- Injectable processors for query/result modification
- External prompt configuration (no hardcoded prompts)
- Real-time streaming progress updates

```
┌─────────────────────────────────────────────────────────────────┐
│                        SUPERVISOR AGENT                         │
│    LLM with Function Calling (GPT-OSS/OpenAI/Anthropic/Ollama)  │
│    - Sees registered agents as delegate_to_<agent> functions    │
│    - Delegates research tasks to specialized agents             │
│    - Iterative OR parallel execution (configurable)             │
└──────────────────────────┬──────────────────────────────────────┘
                           │ delegate_to_<agent>(task)
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│  WebSearch    │  │  Confluence   │  │    Jira       │
│    Agent      │  │    Agent      │  │   Agent       │
├───────────────┤  ├───────────────┤  ├───────────────┤
│ Tools:        │  │ Tools:        │  │ Tools:        │
│ - web_search  │  │ - page_search │  │ - issue_search│
│ - fetch_url   │  │ - get_page    │  │ - get_issue   │
│ - extract     │  │ - get_comments│  │ - search_users│
├───────────────┤  ├───────────────┤  ├───────────────┤
│ Own LLM loop  │  │ Own LLM loop  │  │ Own LLM loop  │
│ Own prompts   │  │ Own prompts   │  │ Own prompts   │
└───────────────┘  └───────────────┘  └───────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                     AgentResult
                 (answer, sources,
                  confidence, trace)
```

---

## Core Design Principles

### 1. Separation of Concerns

**Decision**: Each component owns its own configuration and models.

**Reasoning**: The middleware will be deployed across different companies with different requirements. By keeping configuration local to each component:
- Search backend config lives with retrievers (not global)
- Assumption models live with AssumptionChecker (not in shared models)
- Each retriever can have different field mappings, indices, and processors

**Example**:
```python
# Each retriever configures its own backend
docs_retriever = DocsRetriever(
    search_backend=ElasticsearchBackend(
        config=ElasticsearchConfig(
            url="http://localhost:9200",
            index="company_docs",  # Company-specific index
            search_fields=["title^3", "content"],
        )
    ),
    processors=[QueryReformulator(), AssumptionChecker(...)],
)
```

### 2. Everything is Configurable

**Decision**: No hardcoded prompts, no hardcoded values.

**Reasoning**: Different use cases require different prompts. A prompt that works for HPC support won't work for legal search. By externalizing all prompts to YAML files:
- Prompts can be modified without code changes
- A/B testing of prompts becomes possible
- Domain experts can tune prompts without developer involvement

**Implementation**:
```yaml
# prompts/supervisor.yaml
assess_quality: |
  Assess the quality of this search answer.
  QUESTION: {query}
  ANSWER: {answer}
  ...
```

### 3. Plugin-Style Extensibility

**Decision**: Tools auto-register on import; processors are injectable via constructor.

**Reasoning**: New retrievers and tools should be addable without modifying core code. The supervisor automatically discovers registered tools and presents them to the LLM.

**Implementation**:
```python
# Creating a new retriever automatically makes it available
class MyCustomRetriever(BaseRetriever):
    @property
    def name(self) -> str:
        return "my_custom_retriever"

    @property
    def description(self) -> str:
        return "Search my custom data source"

# Register it
ToolRegistry.register(MyCustomRetriever(...))
# Supervisor now sees it as a callable function
```

### 4. Transparency and Debuggability

**Decision**: Structured JSON logging, correlation IDs, SSE streaming for progress.

**Reasoning**: When something goes wrong in a multi-agent system, debugging is difficult. Every request gets a correlation ID that flows through all components. Structured logs enable querying and analysis.

---

## Component Architecture

### Supervisor Agent

**Location**: `deepsearch/supervisor/agent.py`

**Purpose**: Orchestrates tools via LLM function calling to answer search questions.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Function Calling** (not ReAct, not LangGraph) | Native LLM capability, no custom parsing needed. Most reliable way for LLM to select tools. Works with all OpenAI-compatible providers. |
| **Configurable Execution Strategy** | Some use cases need iterative exploration (call one tool, analyze, call next). Others need speed (call all tools in parallel). Making this configurable serves both. |
| **Quality Assessment Loop** | Early stopping when quality threshold is met saves tokens and time. Continuing when quality is low improves results. |
| **Prompts from PromptManager** | All supervisor prompts are loaded from YAML, enabling customization per deployment. |

**Key Interfaces**:
```python
class SupervisorAgent:
    async def search(self, query: str, job_id: str = None) -> DRResult:
        """Main entry point - executes full search workflow."""
```

---

### Tool Framework

**Location**: `deepsearch/tools/`

**Purpose**: Provides the base interface for all tools the supervisor can call.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **BaseTool Abstract Class** | Common interface for all tools. Supervisor doesn't need to know implementation details. |
| **`name` + `description` Properties** | The LLM needs these to understand what each tool does. Kept simple (strings) rather than complex manifests. |
| **`to_function_schema()` Method** | Automatically generates OpenAI function calling schema from tool definition. No manual schema maintenance. |
| **ToolRegistry Singleton** | Central place to discover all available tools. Supervisor queries this to build function schemas. |
| **Auto-Registration Decorator** | `@register_tool` decorator enables automatic registration on instantiation, reducing boilerplate. |

**Why Not LangChain Tools?**:
- LangChain tools add unnecessary dependencies
- We need more control over the tool interface
- Our tools need processor injection which LangChain doesn't support well

---

### Agent Framework

**Location**: `deepsearch/agents/`

**Purpose**: Specialized research agents that operate autonomously with their own tools and reasoning loops.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Orchestrator-Worker Pattern** | Supervisor delegates to specialized agents, each expert in a domain. Scales better than monolithic tool calls. Inspired by Anthropic's multi-agent research system. |
| **Agents Have Their Own Tools** | Each agent knows its domain. A web agent has web tools; a Confluence agent has Confluence tools. No tool leakage between domains. |
| **Own LLM Reasoning Loop** | Agents can make multiple decisions autonomously before returning to supervisor. Reduces supervisor overhead and enables deeper exploration. |
| **ReasoningAgentMixin** | Common reasoning loop implementation that agents can inherit. ReAct-style: think → act → observe → repeat. |
| **AgentResult Return Type** | Structured output with confidence, sources, and reasoning trace. Supervisor can assess quality and decide if more research is needed. |
| **AgentRegistry** | Central discovery of available agents, similar to ToolRegistry. Generates `delegate_to_<agent>` function schemas. |
| **Backwards Compatible** | Tools still work directly. Agents are opt-in enhancement via `SupervisorConfig.use_agents`. |

**Key Classes**:

```python
# Base agent interface
class BaseAgent(ABC):
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def tools(self) -> List[BaseTool]: ...

    async def run(self, task: str, **kwargs) -> AgentResult:
        """Execute the research task."""

# Agent with standard reasoning loop
class WebSearchAgent(BaseAgent, ReasoningAgentMixin):
    async def run(self, task: str, **kwargs) -> AgentResult:
        return await self.reasoning_loop(task, **kwargs)
```

**Agent Execution Flow**:

```
1. Supervisor delegates task via delegate_to_<agent>(task)
   ↓
2. Agent builds system prompt with available tools
   ↓
3. Agent enters reasoning loop:
   a. LLM decides which tool to call (or answer directly)
   b. Execute tool, collect results
   c. Add observation to conversation
   d. Repeat until LLM answers or max iterations
   ↓
4. Agent returns AgentResult with:
   - answer: Synthesized findings
   - confidence: 0.0-1.0 score
   - sources: List of sources found
   - iterations: Trace of reasoning steps
   ↓
5. Supervisor receives result and decides:
   - Quality good? → Synthesize final answer
   - Quality poor? → Delegate to more agents
```

**Example: Creating a Custom Agent**:

```python
from deepsearch.agents import BaseAgent, ReasoningAgentMixin, AgentRegistry
from deepsearch.models import AgentResult

class ConfluenceAgent(BaseAgent, ReasoningAgentMixin):
    """Agent specialized for searching Confluence."""

    def __init__(self, llm, prompts, confluence_client):
        self._tools = [
            ConfluenceSearchTool(confluence_client),
            ConfluenceGetPageTool(confluence_client),
            ConfluenceGetCommentsTool(confluence_client),
        ]
        super().__init__(llm, prompts, max_iterations=5)

    @property
    def name(self) -> str:
        return "confluence_agent"

    @property
    def description(self) -> str:
        return "Searches Confluence for documentation, wiki pages, and knowledge base articles."

    @property
    def tools(self) -> List[BaseTool]:
        return self._tools

    async def run(self, task: str, **kwargs) -> AgentResult:
        return await self.reasoning_loop(task, **kwargs)

# Register the agent
AgentRegistry.register(ConfluenceAgent(llm, prompts, confluence_client))
```

---

### Retrievers (Legacy/Simple Mode)

**Location**: `deepsearch/retrievers/`

**Purpose**: Tools that perform search/retrieval operations with processor support.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **BaseRetriever extends BaseTool** | Retrievers ARE tools - they just have extra capabilities (search backend, processors). This inheritance makes the type hierarchy clear. |
| **Per-Retriever Search Backend Config** | Different retrievers search different indices with different field mappings. A docs retriever has different fields than a tickets retriever. Global config would limit flexibility. |
| **Injectable Processors via Constructor** | Composition over inheritance. Want query reformulation? Inject a QueryReformulator. Want assumption checking? Inject an AssumptionChecker. Mix and match per retriever. |
| **SearchBackend Abstraction** | Decouple retriever logic from search implementation. Today it's Elasticsearch, tomorrow it could be ChromaDB or Pinecone. |
| **Async HTTP with httpx** | The original code used synchronous `requests`. Async enables concurrent tool execution and better resource utilization. |

**Example Configuration**:
```python
# HPC Docs Retriever with reformulation and assumption checking
hpc_docs = DocsRetriever(
    search_backend=ElasticsearchBackend(
        config=ElasticsearchConfig(
            url="http://localhost:9200",
            index="hpc_documentation",
            search_fields=["title^3", "content", "commands^2"],
        )
    ),
    processors=[
        QueryReformulator(config=QueryReformulatorConfig(max_terms=8)),
        AssumptionChecker(llm=llm, prompts=prompts),
    ],
    llm=llm,
    prompts=prompts,
)

# Tickets Retriever with just reformulation (no assumption checking)
hpc_tickets = TicketsRetriever(
    search_backend=ElasticsearchBackend(
        config=ElasticsearchConfig(
            url="http://localhost:9200",
            index="hpc_tickets",
            search_fields=["problem^5", "solution^4", "title^2"],
        )
    ),
    processors=[
        QueryReformulator(config=QueryReformulatorConfig(max_terms=4)),
    ],
    llm=llm,
    prompts=prompts,
)
```

---

### Processors

**Location**: `deepsearch/processors/`

**Purpose**: Injectable components that modify queries (pre-process) and results (post-process).

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Injectable via Constructor** (not config-based) | Explicit dependency injection is clearer than magic configuration. You can see exactly what processors a retriever uses by looking at its instantiation. |
| **`pre_process` and `post_process` Hooks** | Two clear extension points in the retrieval pipeline. Pre-process modifies the query before search. Post-process modifies results after search. |
| **ProcessorChain for Composition** | Multiple processors can be chained. They execute in order, each one's output becoming the next one's input. |
| **Models Co-Located with Processor** | AssumptionChecker has its own models (UserAssumption, AssumptionValidation) in the same file. This keeps related code together and makes the processor self-contained. |
| **Multilingual Stopwords** (EN/DE) | The system is used in German-speaking environments. QueryReformulator uses nltk or stop-words library for proper multilingual support, not hardcoded word lists. |

**QueryReformulator Design**:
```python
class QueryReformulator(BaseProcessor):
    """
    Two modes:
    1. Simple mode (default): Extract key terms, remove stopwords
    2. LLM mode (use_llm=True): Use LLM to intelligently reformulate

    LLM mode loads prompts from PromptManager - no hardcoded prompts.
    """
```

**AssumptionChecker Design**:
```python
class AssumptionChecker(BaseProcessor):
    """
    Post-processor that:
    1. Extracts implicit assumptions from the original query
    2. Validates assumptions against search results
    3. Adds validation results to context for downstream use

    Models (UserAssumption, AssumptionValidation) are defined
    in the same file - co-located with the processor.
    """
```

---

### LLM Providers

**Location**: `deepsearch/llm/`

**Purpose**: Abstract interface for LLM providers with multi-provider support.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Multi-Provider from Day One** | The system needs to work with GPT-OSS (internal), OpenAI (cloud), Anthropic (alternative), and Ollama (local). All via one interface. |
| **OpenAI-Compatible API** | Most providers offer OpenAI-compatible endpoints. One implementation (`OpenAICompatProvider`) handles GPT-OSS, OpenAI, vLLM, and most others. |
| **ResponseProcessor for Cleanup** | GPT-OSS adds channel tags (`<\|channel\|>`, `<\|message\|>`) that need removal. Centralizing this in ResponseProcessor keeps provider-specific quirks isolated. |
| **Function Calling Support** | The supervisor needs `complete_with_functions()` to call tools. This is a first-class method, not an afterthought. |
| **Streaming Support** | For long search operations, streaming provides better UX. The interface supports it even if not all providers do. |

**Why Not LangChain?**:
- LangChain adds complexity for simple OpenAI-compatible calls
- We need more control over response processing (GPT-OSS cleanup)
- Direct httpx is faster and more debuggable

---

### Prompt Management

**Location**: `deepsearch/prompts/`

**Purpose**: Load and render prompts from external YAML files.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **External YAML Files** (not Python dicts, not Jinja2) | YAML is human-readable and editable by non-developers. Simpler than Jinja2 templates. Can be modified without redeployment. |
| **Category/Name Organization** | Prompts organized by component: `supervisor.yaml`, `retriever.yaml`, `assumption_checker.yaml`. Easy to find and modify. |
| **Variable Substitution with `{variable}`** | Simple string formatting. No complex template logic needed. |
| **Caching with Reload Support** | Prompts are cached for performance but can be reloaded (`manager.reload()`) for development. |

**File Structure**:
```
prompts/
├── supervisor.yaml          # system, search_query, assess_quality, generate_report
├── retriever.yaml           # generate_answer, estimate_confidence
├── query_reformulator.yaml  # reformulate_query, reformulate_for_tickets
└── assumption_checker.yaml  # extract_assumptions, validate_assumption
```

---

### Configuration

**Location**: `deepsearch/config.py`

**Purpose**: Centralized configuration with environment variable support.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Pydantic Settings** (not YAML config files) | Environment variables are the standard for containerized deployments. 12-factor app compliance. Easy to override per environment. |
| **`DR_` Prefix** | Namespaces our variables to avoid conflicts with other services. |
| **No Search Backend Config in Global Config** | Search backends are per-retriever. Each retriever manages its own connection. This enables multiple retrievers with different backends. |
| **Cached Singleton** | `get_config()` returns cached instance. Configuration is read once at startup. |

**What's in Global Config**:
- LLM settings (shared across all components)
- Supervisor settings (execution strategy, iterations)
- Prompts directory path
- API settings (host, port)
- Observability settings (logging, tracing)

**What's NOT in Global Config**:
- Elasticsearch URLs/indices (per-retriever)
- Search field mappings (per-retriever)
- Processor configurations (per-processor)

---

### API Layer

**Location**: `deepsearch/api/`

**Purpose**: REST API with SSE streaming for the search service.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **REST + SSE Streaming** | REST for simplicity (start job, get result). SSE for real-time progress during long search operations. |
| **Async Job Model** | search can take 30+ seconds. Async jobs with status polling and streaming provide good UX. |
| **Sync Endpoint Option** | `/search/sync` for simple integrations that don't need streaming. Blocks until complete. |
| **In-Memory Job Storage** | Simple for now. Replace with Redis for production multi-instance deployments. |
| **Dependency Injection for Supervisor** | Supervisor is injected via FastAPI's `Depends()`. Makes testing easier and configuration cleaner. |

**Endpoints**:
| Endpoint | Purpose |
|----------|---------|
| `POST /api/v1/search` | Start async job, returns job_id |
| `POST /api/v1/search/sync` | Sync execution, blocks until complete |
| `GET /api/v1/search/{job_id}` | Get job status |
| `GET /api/v1/search/{job_id}/result` | Get completed result |
| `GET /api/v1/search/{job_id}/stream` | SSE stream for progress |
| `GET /api/v1/tools` | List registered tools |
| `GET /api/v1/health` | Health check |

---

### Observability

**Location**: `deepsearch/observability/`

**Purpose**: Structured logging and tracing for debugging multi-agent workflows.

**Design Decisions**:

| Decision | Reasoning |
|----------|-----------|
| **Structured JSON Logging** | Logs can be queried and analyzed. Essential for production debugging. |
| **Correlation IDs** | Every request gets a unique ID that flows through all components. Makes tracing a request across logs trivial. |
| **Context Variables** | User query preview, request metadata added to all log entries automatically. |
| **Phoenix/OpenTelemetry Tracing** (optional) | For detailed LLM call tracing when needed. Disabled by default to reduce overhead. |

**Log Format**:
```json
{
  "timestamp": "2024-01-01T00:00:00Z",
  "level": "INFO",
  "message": "search_start",
  "correlation_id": "abc-123",
  "query_preview": "How do I submit...",
  "module": "supervisor.agent"
}
```

---

## Data Flow

### search Request Flow

```
1. API receives POST /search with query
   ↓
2. Create job record + event stream
   ↓
3. Background task starts SupervisorAgent.search()
   ↓
4. Supervisor builds function schemas from ToolRegistry
   ↓
5. Supervisor asks LLM: "Which tool should I call?"
   ↓
6. LLM returns function_call: {name: "docs_retriever", args: {...}}
   ↓
7. Supervisor executes tool:
   a. QueryReformulator.pre_process(query)  → optimized query
   b. ElasticsearchBackend.search(query)    → search results
   c. AssumptionChecker.post_process(results) → validated results
   d. BaseRetriever._generate_answer()      → searchAnswer
   ↓
8. Supervisor assesses quality
   ↓
9. If quality < threshold: repeat from step 5
   If quality >= threshold: proceed to step 10
   ↓
10. Supervisor generates final report + concise answer
    ↓
11. Return DRResult via SSE stream or polling
```

### Processor Pipeline

```
Original Query
      ↓
┌─────────────────────────────────────┐
│     QueryReformulator.pre_process   │
│     - Extract key terms             │
│     - Remove stopwords (EN/DE)      │
│     - Limit term count              │
└─────────────────────────────────────┘
      ↓
Optimized Query
      ↓
┌─────────────────────────────────────┐
│     SearchBackend.search            │
│     - Query Elasticsearch           │
│     - Parse results                 │
└─────────────────────────────────────┘
      ↓
Search Results
      ↓
┌─────────────────────────────────────┐
│   AssumptionChecker.post_process    │
│   - Extract assumptions from query  │
│   - Validate against results        │
│   - Add to context                  │
└─────────────────────────────────────┘
      ↓
Validated Results + Context
```

---

## Extension Points

### Adding a New Agent (Recommended)

The recommended way to extend the system is by creating specialized agents:

```python
from deepsearch.agents import BaseAgent, ReasoningAgentMixin, AgentRegistry
from deepsearch.tools import BaseTool
from deepsearch.models import AgentResult

# 1. Create tools for your agent
class JiraSearchTool(BaseTool):
    @property
    def name(self) -> str:
        return "jira_search"

    @property
    def description(self) -> str:
        return "Search Jira issues by query"

    async def execute(self, query: str, **kwargs) -> ToolResult:
        # Implementation
        ...

# 2. Create the agent
class JiraAgent(BaseAgent, ReasoningAgentMixin):
    """Agent specialized for Jira research."""

    def __init__(self, llm, prompts, jira_client):
        self._tools = [
            JiraSearchTool(jira_client),
            JiraGetIssueTool(jira_client),
        ]
        super().__init__(llm, prompts, max_iterations=5)

    @property
    def name(self) -> str:
        return "jira_agent"

    @property
    def description(self) -> str:
        return "Searches Jira for issues, bugs, and tickets"

    @property
    def tools(self) -> List[BaseTool]:
        return self._tools

    async def run(self, task: str, **kwargs) -> AgentResult:
        return await self.reasoning_loop(task, **kwargs)

# 3. Register the agent
jira_agent = JiraAgent(llm, prompts, jira_client)
AgentRegistry.register(jira_agent)

# 4. Create agent-specific prompts in prompts/jira_agent.yaml
```

### Adding a New Retriever (Legacy/Simple Mode)

For simple, deterministic retrieval without agent reasoning:

```python
from deepsearch.retrievers import BaseRetriever
from deepsearch.tools import ToolRegistry

class WikiRetriever(BaseRetriever):
    @property
    def name(self) -> str:
        return "wiki_retriever"

    @property
    def description(self) -> str:
        return "Search internal wiki for policies and procedures"

# Create and register
wiki = WikiRetriever(
    search_backend=ElasticsearchBackend(config=...),
    processors=[QueryReformulator()],
    llm=llm,
    prompts=prompts,
)
ToolRegistry.register(wiki)
```

### Adding a New Processor

```python
from deepsearch.processors import BaseProcessor

class LanguageDetector(BaseProcessor):
    """Detect query language and add to context."""

    async def pre_process(self, query: str, context: dict = None) -> str:
        context = context or {}
        context["detected_language"] = self._detect(query)
        return query  # Query unchanged, but context enriched
```

### Adding a New Search Backend

```python
from deepsearch.retrievers.search_backends import SearchBackend

class ChromaDBBackend(SearchBackend):
    @property
    def backend_name(self) -> str:
        return "chromadb"

    async def search(self, query: str, ...) -> SearchResponse:
        # Implement ChromaDB search
        ...
```

### Adding a New LLM Provider

```python
from deepsearch.llm import LLMProvider

class AnthropicNativeProvider(LLMProvider):
    """Direct Anthropic API (not OpenAI-compatible)."""

    @property
    def provider_name(self) -> str:
        return "anthropic-native"

    async def complete(self, messages, ...) -> LLMResponse:
        # Use anthropic SDK directly
        ...
```

---

## Summary of Key Decisions

| Area | Decision | Alternative Rejected | Reasoning |
|------|----------|---------------------|-----------|
| Tool Orchestration | Function Calling | ReAct, LangGraph | Native LLM capability, most reliable |
| Execution | Configurable (iterative/parallel) | Fixed strategy | Different use cases need different approaches |
| Config | Pydantic Settings | YAML files | 12-factor app, container-friendly |
| Prompts | External YAML | Python dicts, Jinja2 | Human-editable, no code changes needed |
| Processors | Constructor injection | Config-based composition | Explicit, debuggable, type-safe |
| Search Backend | Per-retriever config | Global config | Multiple indices, different field mappings |
| Assumption Models | Co-located with processor | Shared models folder | Separation of concerns |
| HTTP Client | httpx (async) | requests (sync) | Async enables parallel execution |
| Stopwords | Library (nltk/stop-words) | Hardcoded list | Multilingual support (EN/DE) |
| Authentication | Deferred | JWT from start | YAGNI - add when needed |

---

## Future Considerations

When extending this architecture, maintain these principles:

1. **New retrievers** should configure their own backends
2. **New processors** should be injectable, not hardcoded
3. **New prompts** go in YAML files, not code
4. **New LLM providers** implement the LLMProvider interface
5. **Global config** only for truly global settings
