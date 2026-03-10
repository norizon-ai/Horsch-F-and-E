# Setup Guide

This guide walks you through setting up a local development environment for Norizon DeepSearch.

## Prerequisites

- **Python 3.10+**
- **Docker & Docker Compose** (for SearXNG, Elasticsearch)
- **LLM API access** (OpenAI, Anthropic, or self-hosted)

## Local Development Setup

### 1. Create Virtual Environment

```bash
cd services/custom-deepresearch

# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the example configuration files:

```bash
cp .env.example .env
cp agents.example.yaml agents.yaml
```

Edit `.env` with your LLM credentials:

```bash
# === LLM Configuration ===

# OpenAI
DR_LLM_PROVIDER=openai
DR_LLM_BASE_URL=https://api.openai.com/v1
DR_LLM_API_KEY=sk-your-key
DR_LLM_MODEL=gpt-4o-mini

# Or: Anthropic
# DR_LLM_PROVIDER=anthropic
# DR_LLM_BASE_URL=https://api.anthropic.com
# DR_LLM_API_KEY=sk-ant-your-key
# DR_LLM_MODEL=claude-3-haiku-20240307

# Or: Local/Self-hosted (OpenAI-compatible API)
# DR_LLM_PROVIDER=gpt-oss
# DR_LLM_BASE_URL=http://localhost:30000/v1
# DR_LLM_API_KEY=dummy
# DR_LLM_MODEL=your-model-name

# Or: Ollama
# DR_LLM_PROVIDER=ollama
# DR_LLM_BASE_URL=http://localhost:11434/v1
# DR_LLM_API_KEY=ollama
# DR_LLM_MODEL=llama3
```

### 4. Start Dependencies

Start required services with Docker Compose:

```bash
# Start all services
docker-compose up -d

# Or start specific services
docker-compose up -d elasticsearch searxng
```

### 5. Run the Service

```bash
uvicorn deepsearch.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Verify Setup

Check health endpoint:

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{
  "status": "healthy",
  "agents": ["elasticsearch_confluence", "websearch"],
  "tools": 2
}
```

Test a search:

```bash
curl -X POST http://localhost:8000/api/v1/search/sync \
  -H "Content-Type: application/json" \
  -d '{"query": "What is Kubernetes?"}'
```

---

## Configuration Reference

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| **LLM Settings** | | |
| `DR_LLM_PROVIDER` | `gpt-oss` | Provider: `openai`, `anthropic`, `gpt-oss`, `ollama` |
| `DR_LLM_BASE_URL` | - | API endpoint URL |
| `DR_LLM_API_KEY` | - | API key |
| `DR_LLM_MODEL` | - | Model name |
| `DR_LLM_TEMPERATURE` | `0.2` | Generation temperature |
| `DR_LLM_MAX_TOKENS` | `2000` | Max response tokens |
| **Search Settings** | | |
| `DR_MAX_ITERATIONS` | `3` | Max search iterations |
| `DR_QUALITY_THRESHOLD` | `0.7` | Stop when quality >= threshold |
| `DR_CONFIDENCE_THRESHOLD` | `0.6` | Min confidence for answers |
| **Logging** | | |
| `DR_LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `DR_LOG_FORMAT` | `json` | `json` or `text` |

### Agent Configuration (`agents.yaml`)

#### Web Search Agent (SearXNG)

```yaml
agents:
  web_search:
    type: websearch
    enabled: true
    max_iterations: 5
    backend:
      searxng_url: "http://localhost:8080"
      default_engines: [google, bing, duckduckgo]
      timeout: 30.0
```

**Requires**: SearXNG instance with JSON API enabled.

#### Elasticsearch Agent

```yaml
agents:
  docs:
    type: elasticsearch
    enabled: true
    description: "Search documentation"
    max_iterations: 3
    backend:
      url: "http://localhost:9200"
      index: "documents"
      search_fields: ["title^3", "content"]
      # Optional authentication:
      # api_key: "${ES_API_KEY}"
```

#### Multiple Instances

Run multiple agents of the same type with different configurations:

```yaml
agents:
  docs:
    type: elasticsearch
    enabled: true
    backend:
      url: "http://es:9200"
      index: "documents"

  tickets:
    type: elasticsearch
    enabled: true
    backend:
      url: "http://es:9200"
      index: "tickets"
```

#### Custom Agent (Plugin)

```yaml
agents:
  my_agent:
    type: custom
    enabled: true
    class: "mypackage.agents.MyAgent"
    backend:
      api_url: "http://my-api:8000"
```

#### Environment Variable Substitution

Use `${VAR}` syntax to inject environment variables:

```yaml
backend:
  api_key: "${ES_API_KEY}"
```

---

## Deployment Profiles

### Web Search Only

Minimal setup with just web search:

```yaml
# agents.yaml
agents:
  web_search:
    type: websearch
    enabled: true
    backend:
      searxng_url: "http://searxng:8080"
```

Start SearXNG:

```bash
docker run -d --name searxng -p 8080:8080 searxng/searxng
```

### With Elasticsearch

Full setup with document search:

```bash
docker-compose --profile with-elasticsearch up -d
```

### Production (Docker Compose)

```bash
docker-compose up -d
```

---

## SearXNG Setup

SearXNG must have JSON API enabled. After starting the container:

```bash
docker exec searxng sh -c 'cat >> /etc/searxng/settings.yml << EOF
search:
  formats:
    - html
    - json
EOF'
docker restart searxng
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `tools: 0` in health | No agents enabled in `agents.yaml` |
| `LLM connection failed` | Check `DR_LLM_*` settings in `.env` |
| SearXNG 403 errors | Enable JSON format (see SearXNG Setup above) |
| Multiple iterations for simple queries | SearXNG may be misconfigured or returning poor results |
| `Supervisor not configured` | App startup failed - check logs for errors |
| Elasticsearch connection refused | Ensure Elasticsearch is running: `docker-compose up -d elasticsearch` |
| `No module found` errors | Ensure virtual environment is activated and dependencies installed |

### Debugging

Enable debug logging:

```bash
export DR_LOG_LEVEL=DEBUG
uvicorn deepsearch.main:app --reload
```

View structured logs:

```bash
# JSON logs (default)
uvicorn deepsearch.main:app 2>&1 | jq '.'

# Text logs
export DR_LOG_FORMAT=text
uvicorn deepsearch.main:app
```

---

## Next Steps

- [API Reference](API_REFERENCE.md) - Full endpoint documentation
- [Architecture](../ARCHITECTURE.md) - System design and extension points
- [Streaming](streaming.md) - SSE streaming details
- [Testing Guide](guides/testing.md) - QA and evaluation framework
