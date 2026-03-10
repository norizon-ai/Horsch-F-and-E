# HPC Deep Research System - Deployment Summary

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER ACCESS                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  OpenWebUI (https://openwebui-dev.ai.fau.de)                                │
│      │                                                                       │
│      │ HTTP POST /query                                                      │
│      ▼                                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                         OPENSTACK VM (RRZE)                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Floating IP: 172.17.70.18 (FAU-Intern)                             │    │
│  │  Internal IP: 10.240.60.10                                          │    │
│  │  VM Name: hpc-knowledge-database                                    │    │
│  │  Flavor: SCS-4V-16-100s (4 vCPU, 16GB RAM, 100GB disk)             │    │
│  │                                                                     │    │
│  │  ┌─────────────────┐    ┌─────────────────────────────────────┐    │    │
│  │  │   DR API        │    │   Elasticsearch 8.11.0              │    │    │
│  │  │   Port 8001     │───▶│   Port 9200                         │    │    │
│  │  │   (FastAPI)     │    │   - docs index (88 docs)            │    │    │
│  │  └────────┬────────┘    │   - tickets index (7,777 tickets)   │    │    │
│  │           │             └─────────────────────────────────────┘    │    │
│  └───────────┼─────────────────────────────────────────────────────────┘    │
│              │                                                               │
├──────────────┼───────────────────────────────────────────────────────────────┤
│              │ HTTPS API calls                                               │
│              ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  NHR Hub LLM Gateway                                                │    │
│  │  https://hub.nhr.fau.de/api/llmgw/v1                               │    │
│  │  Model: gpt-oss-120b                                                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Endpoints

| Service | URL | Purpose |
|---------|-----|---------|
| DR API | http://172.17.70.18:8001 | Deep Research query endpoint |
| Elasticsearch | http://172.17.70.18:9200 | Document search (internal) |
| LLM Gateway | https://hub.nhr.fau.de/api/llmgw/v1 | GPT-OSS 120B model |
| OpenWebUI | https://openwebui-dev.ai.fau.de | User interface |

## Key Files

| File | Purpose |
|------|---------|
| `deploy/terraform/main.tf` | OpenStack VM infrastructure |
| `deploy/terraform/network.tf` | Network, router, security groups |
| `deploy/terraform/variables.tf` | Configuration variables |
| `deploy/terraform/terraform.tfvars` | Credentials & settings (gitignored) |
| `docker-compose.yml` | Local development services |
| `Dockerfile.api` | DR API container image |
| `hpc_dr_function.py` | OpenWebUI function integration |
| `ticketknowledgedb/DR_Pipeline/` | Core research pipeline code |

## VM Configuration (OpenStack)

```
SSH Access:  ssh -i ~/.ssh/fau_openstack_key ubuntu@172.17.70.18
Services:    /opt/hpc-kb/docker-compose.yml
Logs:        docker logs dr-api
```

## Data Flow

1. User asks question in OpenWebUI
2. OpenWebUI function calls DR API (`POST /query`)
3. DR API searches Elasticsearch (docs + tickets)
4. DR API calls LLM for answer synthesis (up to 3 iterations)
5. Response returned with confidence score

## Docker Images

| Image | Registry |
|-------|----------|
| `lisarebecca/hpc-kb-dr-api:latest` | Docker Hub |
| `elasticsearch:8.11.0` | Docker official |

## Environment Variables (VM)

```bash
LLM_BASE_URL=https://hub.nhr.fau.de/api/llmgw/v1
LLM_API_KEY=<see nhr.key file>
LLM_MODEL=gpt-oss-120b
ELASTIC_URL=http://elasticsearch:9200
DOCS_INDEX=docs
TICKETS_INDEX=tickets
```

## Network Fix Applied

Static route added to bypass Docker network conflict:
```
172.17.64.0/20 via 10.240.60.1 dev ens3
```
Persisted in `/etc/netplan/99-fau-intern-route.yaml`

## Deployment Commands

```bash
# Deploy infrastructure
cd deploy/terraform && terraform apply

# Rebuild & push image
docker buildx build --platform linux/amd64 -t lisarebecca/hpc-kb-dr-api:latest -f Dockerfile.api . --push

# Update VM
ssh ubuntu@172.17.70.18 "cd /opt/hpc-kb && docker compose pull && docker compose up -d"
```
