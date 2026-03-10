# Multi-Customer Deployment Guide

This directory contains deployment configurations for different customers.
Each customer gets their own subdirectory with isolated config.

## Directory Structure

```
deploy/
├── README.md
├── customer-a/
│   ├── .env                    # Environment variables
│   ├── agents.yaml             # Agent configuration
│   ├── prompts/                # Customer-specific prompts (optional)
│   └── golden_answers.yaml     # Customer-specific evaluation data
├── customer-b/
│   └── ...
└── docker-compose.override.yml # Multi-instance compose (optional)
```

## Quick Start

### 1. Create Customer Configuration

```bash
# Copy template for new customer
./scripts/create_customer_config.sh customer-a

# Or manually:
mkdir -p deploy/customer-a/prompts
cp .env.example deploy/customer-a/.env
cp agents.example.yaml deploy/customer-a/agents.yaml
cp -r prompts/* deploy/customer-a/prompts/
cp tests/evaluation/golden_answers.yaml deploy/customer-a/golden_answers.yaml
```

### 2. Customize Configuration

Edit `deploy/customer-a/.env`:
```bash
# Customer-specific LLM
DR_LLM_PROVIDER=openai
DR_LLM_MODEL=gpt-4o
DR_LLM_API_KEY=sk-customer-a-key

# Customer-specific settings
DR_MAX_ITERATIONS=5
DR_QUALITY_THRESHOLD=0.8

# Point to customer prompts
DR_PROMPTS_DIR=deploy/customer-a/prompts
DR_AGENTS_CONFIG_PATH=deploy/customer-a/agents.yaml
```

Edit `deploy/customer-a/agents.yaml`:
```yaml
agents:
  confluence:
    type: elasticsearch
    enabled: true
    description: "Search Customer A Confluence"
    backend:
      url: "http://customer-a-es:9200"
      index: "confluence_customer_a"
```

### 3. Run with Customer Config

```bash
# Option A: Source the .env file
source deploy/customer-a/.env && uvicorn deepsearch.main:app --port 8000

# Option B: Use the deployment script
./scripts/deploy.sh customer-a

# Option C: Docker Compose override
docker-compose --env-file deploy/customer-a/.env up
```

### 4. Run Multiple Instances

To run multiple customers simultaneously on different ports:

```bash
# Terminal 1: Customer A on port 8001
DR_API_PORT=8001 ./scripts/deploy.sh customer-a

# Terminal 2: Customer B on port 8002
DR_API_PORT=8002 ./scripts/deploy.sh customer-b
```

### 5. Evaluate Customer Config

```bash
# Run evaluation with customer-specific golden dataset
OPENAI_API_KEY=sk-xxx python scripts/evaluate_answer_quality.py \
  --api-url http://localhost:8001 \
  --dataset deploy/customer-a/golden_answers.yaml
```

## Configuration Reference

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DR_LLM_PROVIDER` | LLM provider (openai, anthropic, gpt-oss, ollama) | gpt-oss |
| `DR_LLM_MODEL` | Model identifier | openai/gpt-oss-120b |
| `DR_LLM_API_KEY` | API key | dummy |
| `DR_MAX_ITERATIONS` | Max search iterations | 3 |
| `DR_QUALITY_THRESHOLD` | Stop when quality >= threshold | 0.7 |
| `DR_PROMPTS_DIR` | Path to prompts directory | prompts |
| `DR_AGENTS_CONFIG_PATH` | Path to agents.yaml | agents.yaml |
| `DR_API_PORT` | Server port | 8000 |

### Agent Types

| Type | Backend | Use Case |
|------|---------|----------|
| `elasticsearch` | Elasticsearch | Internal docs, Confluence, SharePoint |
| `websearch` | SearXNG | Public web search |
| `custom` | Any | Custom proprietary systems |

## Typical Customer Configurations

### Manufacturing Company (On-Premise)
- Elasticsearch with Confluence data
- German prompts
- No web search
- High quality threshold (0.85)

### IT Consulting (Cloud)
- Multiple Elasticsearch indices (projects, tickets, docs)
- Bilingual prompts
- Web search enabled
- Medium quality threshold (0.7)

### Enterprise (Hybrid)
- Custom agent for proprietary systems
- Strict German-only responses
- Compliance-focused prompts
- Maximum iterations (5)