# Norizon Internal Dogfooding Setup

Full stack for internal use: Confluence search, meeting documentation workflow with Teams import.

## Deployment Options

| Method | Use case | Guide |
|--------|----------|-------|
| **Docker Compose** (local) | Development, testing | This file (below) |
| **Azure Container Apps** (cloud) | Internal dogfooding, shared access | [azure/RUNBOOK.md](azure/RUNBOOK.md) |

---

## Local Development (Docker Compose)

## Prerequisites

- Docker & Docker Compose
- Three env files in this directory (all gitignored):
  - `atlassian.env` — Confluence credentials
  - `deepsearch.env` — LLM provider key + config
  - `workflow.env` — Workflow service + Microsoft Teams OAuth

## Quick Start

```bash
cd instantiations/internal_setup
./start.sh
```

Or directly:

```bash
docker compose up --build
```

Open http://localhost:3000 in your browser.

## Services

| Service | Port | Purpose |
|---------|------|---------|
| frontend | 3000 | SvelteKit UI (norizon-research) |
| deepsearch | 8000 | RAG supervisor with Confluence search agent |
| workflow-service | 8001 | Meeting documentation orchestration + Teams import |
| kstudio | 8002 | Transcription + ML pipeline |
| confluence-publisher | 8003 | Protocol → Confluence page |
| confluence-mcp | 8005 | mcp-atlassian MCP server |

## Env Files

### `atlassian.env`

```
CONFLUENCE_URL=https://norizon.atlassian.net/wiki/
CONFLUENCE_USERNAME=your-email@norizon.de
CONFLUENCE_API_TOKEN=your-api-token
```

Generate an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

### `deepsearch.env`

```
DR_LLM_PROVIDER=openai
DR_LLM_BASE_URL=https://api.openai.com/v1
DR_LLM_API_KEY=sk-...
DR_LLM_MODEL=gpt-4o-mini
DR_LLM_TEMPERATURE=0.2
DR_LLM_MAX_TOKENS=2000
DR_LLM_TIMEOUT=120
DR_EXECUTION_STRATEGY=iterative
DR_MAX_ITERATIONS=3
DR_QUALITY_THRESHOLD=0.7
DR_LOG_LEVEL=INFO
```

### `workflow.env`

```
WORKFLOW_USE_MOCKS=false
WORKFLOW_KSTUDIO_URL=http://kstudio:8000
WORKFLOW_DEEPSEARCH_URL=http://deepsearch:8000
WORKFLOW_CONFLUENCE_PUBLISHER_URL=http://confluence-publisher:8003

# Microsoft Teams (optional — leave empty to disable Teams import)
WORKFLOW_MS_TENANT_ID=your-azure-tenant-id
WORKFLOW_MS_CLIENT_ID=your-app-client-id
WORKFLOW_MS_CLIENT_SECRET=your-client-secret
WORKFLOW_MS_REDIRECT_URI=http://localhost:8001/auth/microsoft/callback
```

## Microsoft Teams Setup

To enable the "Import from Teams" feature in the meeting documentation workflow:

1. Go to [Azure Entra ID → App registrations](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
2. Click **New registration**
   - Name: `Norizon Meeting Import (Dev)`
   - Supported account types: Single tenant
   - Redirect URI: Web → `http://localhost:8001/auth/microsoft/callback`
3. Under **API permissions**, add these **delegated** permissions:
   - `User.Read`
   - `OnlineMeetings.Read`
   - `OnlineMeetingRecording.Read.All`
   - `Calendars.Read`
4. Grant admin consent
5. Under **Certificates & secrets**, create a client secret
6. Copy tenant ID, client ID, and secret into `workflow.env`

If the `WORKFLOW_MS_CLIENT_ID` is empty, the "Import from Teams" tab will show a "not configured" message instead.

## Test Endpoints

Search:
```bash
curl -X POST http://localhost:8000/api/v1/search/sync \
  -H "Content-Type: application/json" \
  -d '{"query": "your search term"}'
```

Workflow health:
```bash
curl http://localhost:8001/health
```

Teams auth status:
```bash
curl http://localhost:8001/auth/microsoft/status
```

Publish:
```bash
curl -X POST http://localhost:8003/internal/publish \
  -H "Content-Type: application/json" \
  -d '{
    "protocol": {
      "title": "Test Protocol",
      "date": "2026-02-10",
      "attendees": ["Lisa Schmidt"],
      "executiveSummary": "Testing the publisher.",
      "decisions": ["Use MCP for Confluence"],
      "nextSteps": ["Validate results"]
    },
    "space_key": "DOCS"
  }'
```
