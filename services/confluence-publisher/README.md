# Confluence Publisher

Service for publishing generated documentation to Atlassian Confluence with proper formatting, templates, and media attachments.

## Overview

This service handles:
- Authentication with Confluence Cloud and Server
- Page creation with Atlassian Document Format (ADF)
- Template-based rendering (Q&A, Process Docs, Troubleshooting Guides)
- Media attachment upload (audio, video, PDFs)
- Page hierarchy and space management
- Retry logic for failed publishes

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Confluence Publisher                          │
│                         Port: 8003                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                      FastAPI App                             ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  ││
│  │  │  REST API   │  │  Job Queue  │  │   Template Engine   │  ││
│  │  │             │  │  Consumer   │  │   (Jinja2 + ADF)    │  ││
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘  ││
│  └─────────────────────────────────────────────────────────────┘│
│                              │                                   │
│  ┌───────────────────────────▼─────────────────────────────────┐│
│  │                   Confluence Client                          ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  ││
│  │  │   Cloud     │  │   Server    │  │   Attachment        │  ││
│  │  │   API v2    │  │   API v1    │  │   Handler           │  ││
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘  ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
           │                │                    │
           ▼                ▼                    ▼
    ┌────────────┐  ┌─────────────┐     ┌─────────────┐
    │ PostgreSQL │  │    Redis    │     │ Confluence  │
    │ (conn/logs)│  │  (queues)   │     │    API      │
    └────────────┘  └─────────────┘     └─────────────┘
```

## Quick Start

```bash
# Install dependencies
cd services/confluence-publisher
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env

# Start service
uvicorn app.main:app --reload --port 8003
```

## API Endpoints

### Connection Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/connections` | Add Confluence connection |
| `GET` | `/api/v1/connections` | List connections |
| `GET` | `/api/v1/connections/{id}` | Get connection details |
| `DELETE` | `/api/v1/connections/{id}` | Remove connection |
| `POST` | `/api/v1/connections/{id}/test` | Test connection |
| `GET` | `/api/v1/connections/{id}/spaces` | List available spaces |

### Publishing

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/publish` | Publish content |
| `GET` | `/api/v1/publish/{job_id}` | Get publish status |
| `GET` | `/api/v1/publish/{job_id}/result` | Get published page URL |
| `POST` | `/api/v1/publish/{job_id}/retry` | Retry failed publish |

### Templates

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/templates` | List templates |
| `GET` | `/api/v1/templates/{id}` | Get template details |
| `GET` | `/api/v1/templates/{id}/preview` | Preview with sample data |
| `POST` | `/api/v1/templates` | Create custom template |

### Pages (Direct Access)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/pages/{connection_id}/{page_id}` | Get page content |
| `PUT` | `/api/v1/pages/{connection_id}/{page_id}` | Update page |
| `DELETE` | `/api/v1/pages/{connection_id}/{page_id}` | Delete page |

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | - | PostgreSQL connection string |
| `REDIS_URL` | `redis://localhost:6379/3` | Redis for job queue |
| `OBJECT_STORAGE_URL` | `http://localhost:9000` | MinIO for attachments |
| `ENCRYPTION_KEY` | - | Key for encrypting credentials |
| `MAX_ATTACHMENT_SIZE` | `100MB` | Max attachment size |
| `PUBLISH_TIMEOUT` | `300` | Publish timeout in seconds |

### Connection Configuration

```json
{
  "name": "Company Confluence",
  "type": "cloud",
  "base_url": "https://company.atlassian.net/wiki",
  "auth": {
    "type": "api_token",
    "email": "user@company.com",
    "api_token": "xxx"
  },
  "default_space": "KB",
  "default_parent_page_id": "123456"
}
```

### Authentication Types

| Type | Cloud | Server | Description |
|------|-------|--------|-------------|
| `api_token` | Yes | No | Email + API token |
| `oauth2` | Yes | Yes | OAuth 2.0 flow |
| `pat` | No | Yes | Personal Access Token |
| `basic` | No | Yes | Username + Password (legacy) |

## Templates

### Built-in Templates

| Template | Description |
|----------|-------------|
| `interview_qa` | Q&A format from interview transcripts |
| `process_documentation` | Step-by-step process guide |
| `troubleshooting_guide` | Problem/solution format |
| `fraunhofer_10_step` | Full knowledge transfer document |
| `knowledge_article` | General knowledge base article |

### Template Structure

```yaml
# templates/interview_qa.yaml
name: Interview Q&A
description: Question and answer format from interviews
variables:
  - name: title
    type: string
    required: true
  - name: expert_name
    type: string
    required: true
  - name: qa_pairs
    type: array
    items:
      - question: string
      - answer: string
      - timestamp: string
  - name: related_documents
    type: array
    required: false

adf_template: |
  {
    "type": "doc",
    "content": [
      {
        "type": "heading",
        "attrs": {"level": 1},
        "content": [{"type": "text", "text": "{{ title }}"}]
      },
      {
        "type": "panel",
        "attrs": {"panelType": "info"},
        "content": [
          {"type": "paragraph", "content": [
            {"type": "text", "text": "Expert: {{ expert_name }}"}
          ]}
        ]
      },
      {% for qa in qa_pairs %}
      {
        "type": "heading",
        "attrs": {"level": 2},
        "content": [{"type": "text", "text": "Q: {{ qa.question }}"}]
      },
      {
        "type": "paragraph",
        "content": [{"type": "text", "text": "{{ qa.answer }}"}]
      },
      {% endfor %}
    ]
  }
```

## Publish Request

```json
{
  "connection_id": "uuid",
  "space_key": "KB",
  "parent_page_id": "123456",
  "template_id": "interview_qa",
  "title": "Machine Calibration - Expert Interview",
  "data": {
    "expert_name": "Hans Mueller",
    "qa_pairs": [
      {
        "question": "How do you calibrate the CNC machine?",
        "answer": "First, ensure the machine is at operating temperature...",
        "timestamp": "00:05:23"
      }
    ]
  },
  "attachments": [
    {
      "name": "interview_recording.mp3",
      "url": "s3://transcription/audio/xxx/recording.mp3"
    }
  ],
  "labels": ["knowledge-transfer", "cnc", "calibration"]
}
```

## Project Structure

```
confluence-publisher/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── connections.py
│   │   │   ├── publish.py
│   │   │   ├── templates.py
│   │   │   └── pages.py
│   │   └── models.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── clients/
│   │   ├── confluence_cloud.py
│   │   ├── confluence_server.py
│   │   └── base.py
│   ├── templates/
│   │   ├── engine.py
│   │   ├── adf_builder.py
│   │   └── builtin/
│   │       ├── interview_qa.yaml
│   │       ├── process_documentation.yaml
│   │       └── troubleshooting_guide.yaml
│   ├── workers/
│   │   └── publish_worker.py
│   ├── models/
│   │   ├── connection.py
│   │   └── publish_job.py
│   ├── schemas/
│   │   └── *.py
│   └── main.py
├── tests/
├── Dockerfile
├── requirements.txt
└── .env.example
```

## Atlassian Document Format (ADF)

The service converts Markdown to ADF for Confluence. Supported elements:

| Markdown | ADF Node |
|----------|----------|
| `# Heading` | `heading` (level 1-6) |
| `**bold**` | `strong` mark |
| `*italic*` | `em` mark |
| `[link](url)` | `link` mark |
| `` `code` `` | `code` mark |
| ```` ```code``` ```` | `codeBlock` |
| `- list item` | `bulletList` |
| `1. list item` | `orderedList` |
| `> quote` | `blockquote` |
| `| table |` | `table` |
| `---` | `rule` |

### Custom Macros

```json
{
  "type": "extension",
  "attrs": {
    "extensionType": "com.atlassian.confluence.macro.core",
    "extensionKey": "toc",
    "parameters": {
      "macroParams": {}
    }
  }
}
```

## Error Handling

| Error Code | Description | Retry |
|------------|-------------|-------|
| `CONN_FAILED` | Connection to Confluence failed | Yes |
| `AUTH_FAILED` | Authentication failed | No |
| `SPACE_NOT_FOUND` | Space doesn't exist | No |
| `PARENT_NOT_FOUND` | Parent page doesn't exist | No |
| `PERMISSION_DENIED` | No write permission | No |
| `RATE_LIMITED` | API rate limit exceeded | Yes (with backoff) |
| `ATTACHMENT_TOO_LARGE` | Attachment exceeds limit | No |

## Testing

```bash
pytest tests/ -v

# Integration test with real Confluence
CONFLUENCE_TEST_URL=https://xxx.atlassian.net/wiki \
CONFLUENCE_TEST_TOKEN=xxx \
pytest tests/integration/ -v
```

## Docker

```bash
docker build -t confluence-publisher .
docker run -p 8003:8003 --env-file .env confluence-publisher
```

## Security

- API tokens are encrypted at rest using Fernet (AES-128)
- OAuth tokens are refreshed automatically
- All connections validated on creation
- Audit logging for all publish operations

## License

Proprietary - Norizon GbR
