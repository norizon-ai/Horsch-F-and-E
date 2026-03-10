# Nora

**Knowledge Search Assistant**

## Overview

Nora is a conversational research assistant that synthesizes information from multiple sources and presents cohesive answers with inline citations. Unlike traditional search engines that return lists of links, Nora provides verified, well-sourced answers that allow users to explore source material.

The system supports two search modes:
- **Web Search**: Real-time web search via SearXNG metasearch engine
- **Knowledge Base Search**: Search internal documents indexed in Elasticsearch (Confluence, SharePoint, websites, etc.)

## Architecture

```
+---------------------------------------------------+
|              Frontend (SvelteKit)                 |
|  - Chat interface with streaming responses        |
|  - Inline citations with source tooltips          |
|  - Session management (localStorage)              |
|  - Source summary cards                           |
+-------------------------+-------------------------+
                          |
                          | HTTP/SSE
                          v
+---------------------------------------------------+
|           custom-deepresearch Backend             |
|  - Multi-agent supervisor pattern                 |
|  - Iterative search refinement                    |
|  - LLM-based answer synthesis                     |
|  - Server-Sent Events for progress streaming      |
+-------+------------------+----------------+-------+
        |                  |                |
        v                  v                v
+---------------+  +---------------+  +-------------+
| LLM Provider  |  | Elasticsearch |  |  SearXNG    |
| - OpenAI      |  | - Confluence  |  | - Web search|
| - Ollama      |  | - SharePoint  |  | - Multi-eng |
| - GPT-OSS     |  | - Websites    |  | - Privacy   |
+---------------+  +---------------+  +-------------+
```

## Features

- **Multi-Agent Research**: Supervisor pattern coordinates specialized agents (Elasticsearch, Web Search)
- **Streaming Progress**: Real-time search progress as agents work
- **Source Citations**: Numbered inline citations linked to source material
- **Configurable Agents**: Enable/disable agents, customize search fields via YAML
- **Multiple LLM Providers**: OpenAI, Ollama, GPT-OSS (FAU), or any OpenAI-compatible API
- **Session History**: Chat sessions persist in localStorage
- **Responsive Design**: Mobile and desktop support

## Quick Start

### Prerequisites

- Docker and Docker Compose
- LLM API key (OpenAI, or compatible provider)

### Development Setup

1. Navigate to the service directory:
   ```bash
   cd services/norizon-research
   ```

2. Create environment file:
   ```bash
   cp frontend/.env.example frontend/.env
   ```

3. Set your API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

4. Start all services:
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

5. Access the application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - SearXNG: http://localhost:8080

### With Tracing (Optional)

To enable OpenTelemetry tracing with Phoenix:

```bash
DR_ENABLE_TRACING=true docker-compose -f docker-compose.dev.yml --profile with-tracing up -d
```

Phoenix UI available at http://localhost:6006

## Docker Services

| Service | Port | Description |
|---------|------|-------------|
| frontend | 5173 | SvelteKit frontend with hot reload |
| deepsearch | 8000 | custom-deepresearch backend API |
| searxng | 8080 | Privacy-respecting metasearch engine |
| phoenix | 6006 | OpenTelemetry trace UI (optional) |

## Configuration

### Frontend Environment Variables

Create `frontend/.env` from `.env.example`:

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_BASE_URL` | Browser-side API URL | `http://localhost:8000/api/v1` |
| `VITE_SSR_API_BASE_URL` | Server-side API URL (Docker internal) | `http://deepsearch:8000/api/v1` |
| `VITE_APP_TITLE` | Application title | `Nora` |
| `VITE_APP_DESCRIPTION` | Application description | `Knowledge Search Assistant` |
| `VITE_ENABLE_SHARE` | Enable share button | `true` |
| `VITE_ENABLE_EXPORT` | Enable export button | `true` |

### Backend Environment Variables

Set in `docker-compose.dev.yml` or via environment:

**LLM Configuration:**

| Variable | Description | Default |
|----------|-------------|---------|
| `DR_LLM_PROVIDER` | LLM provider (`openai`, `ollama`, `gpt-oss`) | `openai` |
| `DR_LLM_BASE_URL` | LLM API endpoint | `https://api.openai.com/v1` |
| `DR_LLM_API_KEY` | API key for LLM provider | - |
| `DR_LLM_MODEL` | Model name | `gpt-4o-mini` |
| `DR_LLM_TEMPERATURE` | Response temperature (0-1) | `0.2` |
| `DR_LLM_MAX_TOKENS` | Max tokens per response | `2000` |
| `DR_LLM_TIMEOUT` | Request timeout in seconds | `120` |

**Search Configuration:**

| Variable | Description | Default |
|----------|-------------|---------|
| `DR_MAX_ITERATIONS` | Max search iterations | `3` |
| `DR_QUALITY_THRESHOLD` | Quality score threshold (0-1) | `0.7` |
| `DR_SEARCH_TIMEOUT` | Search timeout in seconds | `300` |
| `DR_AGENTS_CONFIG_PATH` | Path to agents.yaml | `/app/agents.yaml` |
| `DR_PROMPTS_DIR` | Path to prompts directory | `/app/prompts` |

**Observability:**

| Variable | Description | Default |
|----------|-------------|---------|
| `DR_LOG_LEVEL` | Log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) | `INFO` |
| `DR_LOG_FORMAT` | Log format (`json`, `text`) | `json` |
| `DR_ENABLE_TRACING` | Enable OpenTelemetry tracing | `false` |
| `DR_PHOENIX_ENDPOINT` | Phoenix collector endpoint | `http://phoenix:6006/v1/traces` |

### Agent Configuration (agents.yaml)

Agents are configured via `agents.yaml`. Each agent can be enabled/disabled and customized:

```yaml
agents:
  - type: elasticsearch
    enabled: true
    name: "Knowledge Base"
    description: "Search internal documentation"
    icon_url: "/icons/database.svg"
    source_type: "confluence"
    config:
      es_url: "${ELASTICSEARCH_URL:-http://elasticsearch:9200}"
      es_index: "my_knowledge_base"
      search_fields:
        - "title^3"        # Boost title matches
        - "content"
        - "headers^2"
      source_fields:
        - "title"
        - "url"
        - "content"
        - "space_name"
      field_mapping:
        id: "_id"
        title: "title"
        content: "content"
        url: "url"

  - type: websearch
    enabled: true
    name: "Web Search"
    description: "Search the web for current information"
    config:
      searxng_url: "${SEARXNG_URL:-http://searxng:8080}"
      default_engines:
        - google
        - bing
        - duckduckgo
```

### Prompt Customization

All prompts are externalized in the `prompts/` directory:

- `supervisor.yaml` - Main orchestration prompts
- `elasticsearch_agent.yaml` - Knowledge base search prompts
- `websearch_agent.yaml` - Web search prompts

Mount custom prompts by modifying the volume in docker-compose:

```yaml
volumes:
  - ./my-custom-prompts:/app/prompts:ro
```

## Multi-Client Deployment

To deploy for different clients with different data sources, create a product directory:

```
products/my_client/
  docker-compose.yml     # Points to base service images
  .env                   # Client-specific configuration
  agents.yaml            # Client-specific agents (ES index, etc.)
  prompts/               # Optional: client-specific prompts
```

Example `docker-compose.yml` for a client deployment:

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ../../services/norizon-research/frontend
    ports:
      - "3000:3000"
    environment:
      - VITE_API_BASE_URL=http://localhost:8001/api/v1
      - VITE_APP_TITLE=Client Knowledge Search

  deepsearch:
    build:
      context: ../../services/custom-deepresearch
    ports:
      - "8001:8000"
    env_file:
      - .env
    volumes:
      - ./agents.yaml:/app/agents.yaml:ro
      - ./prompts:/app/prompts:ro

  elasticsearch:
    image: elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=true  # Enable for production
    volumes:
      - es_data:/usr/share/elasticsearch/data

volumes:
  es_data:
```

See `products/demo_confluence_assistant/` for a complete example.

## API Overview

### Start Search
**POST** `/api/v1/search`
```json
{
  "query": "How do I configure the CNC machine?",
  "search_type": "hybrid"
}
```

Response:
```json
{
  "job_id": "abc123",
  "status": "pending",
  "created_at": "2025-01-07T12:00:00Z"
}
```

### Stream Results
**GET** `/api/v1/search/{job_id}/stream`

Returns Server-Sent Events:
```
event: progress
data: {"phase": "searching", "message": "Searching knowledge base..."}

event: agent_status
data: {"agent": "elasticsearch", "status": "running", "message": "Found 5 documents"}

event: report_chunk
data: {"content": "Based on the documentation..."}

event: complete
data: {"final_report": "...", "sources": [...], "confidence_score": 0.85}
```

### Health Check
**GET** `/api/v1/health`

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "components": {
    "agents": true,
    "tools": true,
    "llm": true
  }
}
```

### List Tools
**GET** `/api/v1/tools`

Returns available search tools/agents.

## Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Start dev server (requires backend running)
npm run dev

# Build for production
npm run build

# Type checking
npm run check
```

## Troubleshooting

### Frontend shows "error while researching"

1. Check backend logs:
   ```bash
   docker logs nora-deepsearch-dev --tail 50
   ```

2. Verify backend health:
   ```bash
   curl http://localhost:8000/api/v1/health
   ```

3. Check LLM API key is set:
   ```bash
   echo $OPENAI_API_KEY
   ```

### No sources returned from web search

1. Verify SearXNG is working:
   ```bash
   curl "http://localhost:8080/search?q=test&format=json"
   ```

2. If 403 errors, check `searxng/settings.yml` has JSON format enabled:
   ```yaml
   search:
     formats:
       - html
       - json
   ```

### Elasticsearch connection errors

1. Check Elasticsearch is running:
   ```bash
   curl http://localhost:9200/_cluster/health
   ```

2. Verify index exists:
   ```bash
   curl http://localhost:9200/your_index_name/_count
   ```

3. Check `agents.yaml` has correct `es_url` and `es_index`.

### LLM timeout errors

1. Increase timeout:
   ```bash
   DR_LLM_TIMEOUT=180
   ```

2. Try a faster model:
   ```bash
   DR_LLM_MODEL=gpt-4o-mini
   ```

### Viewing traces

1. Start with tracing profile:
   ```bash
   DR_ENABLE_TRACING=true docker-compose -f docker-compose.dev.yml --profile with-tracing up -d
   ```

2. Open Phoenix UI: http://localhost:6006

## Project Structure

```
norizon-research/
  frontend/               # SvelteKit application
    src/
      lib/
        api/              # API client (searchApi.ts)
        components/       # UI components
        stores/           # Svelte stores (chatStore.ts)
        types/            # TypeScript types
      routes/             # SvelteKit routes
    .env.example          # Frontend environment template
  searxng/                # SearXNG configuration
    settings.yml          # Search engine settings
  proxy/                  # Optional: auth proxy for production
  k8s/                    # Kubernetes manifests
  docker-compose.dev.yml  # Development setup
  docker-compose.yml      # Production setup
```

## Production Considerations

Before deploying to production:

1. **Security**:
   - Enable Elasticsearch authentication (`xpack.security.enabled=true`)
   - Configure CORS to specific origins (not `*`)
   - Use secrets management for API keys (not environment variables)
   - Enable HTTPS/TLS

2. **Scalability**:
   - Replace in-memory job storage with Redis
   - Use ReadWriteMany PVCs for multi-replica deployments
   - Pin Docker image versions (not `latest`)

3. **Observability**:
   - Enable tracing for production debugging
   - Add Prometheus metrics endpoint
   - Configure log aggregation

4. **GDPR/Compliance** (for EU deployments):
   - Ensure data residency in EU region
   - Document data processing agreements with LLM providers
   - Consider self-hosted models (Ollama) for sensitive data

See `services/custom-deepresearch/ARCHITECTURE.md` for detailed backend documentation.

## License

Proprietary - Norizon Software GmbH

## Support

For issues or questions, create an issue in the repository.
