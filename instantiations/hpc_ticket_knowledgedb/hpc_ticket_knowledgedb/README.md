# HPC Ticket Knowledge Database

Multi-agent deep research system for HPC support questions, built on top of historical ticket data, documentation, and knowledge base.

## Overview

This system provides intelligent Q&A capabilities for HPC support using a deep research approach:

- **Multi-Agent Research**: Supervisor orchestrates research agents to gather comprehensive answers
- **Multiple Knowledge Sources**: Queries HPC documentation, support tickets, and knowledge base
- **Assumption Validation**: Checks and reformulates user assumptions
- **Quality Assessment**: Iteratively refines answers until quality threshold is met
- **OpenWebUI Integration**: Exposes functionality through OpenWebUI pipelines

## Architecture

```
┌─────────────────────┐
│   OpenWebUI         │
│   Pipeline          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐      ┌─────────────────────┐
│   DR API            │─────▶│   Elasticsearch     │
│   (FastAPI)         │      │   - Docs Index      │
│                     │      │   - Tickets Index   │
│   - Supervisor      │      │   - KB Index        │
│   - Research Agent  │      └─────────────────────┘
│   - Assumption      │
│     Checker         │
└─────────────────────┘
```

## Quick Start

### Local Development

1. **Clone and navigate**:
   ```bash
   cd products/hpc_ticket_knowledgedb
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start services**:
   ```bash
   ./scripts/start_services.sh
   ```

4. **Index data** (first time only):
   ```bash
   ./scripts/index_data.sh
   ```

5. **Test API**:
   ```bash
   curl http://localhost:8001/health

   curl -X POST http://localhost:8001/query \
     -H "Content-Type: application/json" \
     -d '{"query": "How do I access my $WORK directory in JupyterHub?"}'
   ```

### Production Deployment (OpenStack)

1. **Build and push Docker images**:
   ```bash
   ./scripts/build_images.sh
   ./scripts/push_images.sh
   ```

2. **Configure Terraform**:
   ```bash
   cd deploy/terraform
   cp terraform.tfvars.example terraform.tfvars
   # Edit terraform.tfvars with your OpenStack credentials
   ```

3. **Deploy infrastructure**:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

4. **SSH to VM and verify**:
   ```bash
   # Get SSH command from terraform output
   terraform output ssh_command

   # SSH to VM
   ssh -i ~/.ssh/fau_openstack_key ubuntu@<floating-ip>

   # Check services
   cd /opt/hpc-knowledge-db
   docker compose ps
   ```

5. **Index data on VM**:
   ```bash
   # On the VM
   cd /opt/hpc-knowledge-db
   # Upload your data first, then run:
   docker compose --profile indexing up indexer
   ```

## API Endpoints

### Health Check
```bash
GET /health
```

Returns system status and configuration.

### Query (Synchronous)
```bash
POST /query
Content-Type: application/json

{
  "query": "How do I submit a SLURM job?",
  "brief": false,
  "max_iterations": 3
}
```

Returns complete research results.

### Query (Streaming)
```bash
POST /query/stream
Content-Type: application/json

{
  "query": "Why is my GPU job not starting?"
}
```

Returns Server-Sent Events (SSE) stream with incremental updates.

### Direct Search
```bash
POST /search
Content-Type: application/json

{
  "query": "JupyterHub",
  "index": "docs",
  "max_results": 10
}
```

Search Elasticsearch indices directly without DR processing.

## OpenWebUI Integration

### Installation

1. **Upload Pipeline**:
   - Copy `openwebui_pipeline.py` content
   - In OpenWebUI: Admin → Pipelines → Add Pipeline
   - Paste the code and save

2. **Configure Pipeline**:
   Set the Valves in OpenWebUI:
   - `DR_API_URL`: `http://<your-vm-ip>:8001`
   - `DR_API_TIMEOUT`: `180`
   - `ENABLE_BRIEF_MODE`: `false`
   - `ENABLE_STREAMING`: `true`

3. **Use in Chat**:
   - Select "HPC Deep Research" model in chat
   - Ask HPC-related questions
   - Get comprehensive, researched answers

## Data Structure

The system expects data in the following structure:

```
ticketknowledgedb/
├── DR_Pipeline/           # Deep research pipeline code
├── docsmd/               # HPC documentation
│   └── docs_data.jsonl   # Documentation in JSONL format
├── knowledgebase/        # Historical tickets
│   └── *.md             # Ticket markdown files
└── topic_clusters/       # Clustered tickets (optional)
    └── topic_*.md       # Topic cluster files
```

### Data Preparation

See existing scripts in `ticketknowledgedb/DR_Pipeline/data_preparations/`:
- `insert_docs_data.py` - Index documentation
- `insert_knowledgebase_data.py` - Index tickets
- `convert_knowledgebase_to_jsonl.py` - Convert tickets to JSONL

## Configuration

### Environment Variables

Key configuration options in `.env`:

```bash
# Service Ports
ELASTICSEARCH_PORT=9200
DR_API_PORT=8001

# LLM Configuration
LLM_BASE_URL=http://lme49.cs.fau.de:30000/v1
LLM_MODEL=openai/gpt-oss-120b
LLM_TEMPERATURE=0.2

# Elasticsearch Indices
DOCS_INDEX=docs
TICKETS_INDEX=tickets

# Deep Research Settings
MAX_ITERATIONS=3
CONFIDENCE_THRESHOLD=0.6
MAX_SEARCH_RESULTS=10
```

### Terraform Variables

Key OpenStack deployment options in `deploy/terraform/terraform.tfvars`:

```hcl
# VM Configuration
flavor_name  = "SCS-4V-16-100"  # 4 vCPU, 16GB RAM
vm_name      = "hpc-knowledge-database"

# Storage
elasticsearch_volume_size = 100  # GB

# Security (IMPORTANT: Restrict in production!)
ssh_allowed_cidr = "your-ip-range/32"
api_allowed_cidr = "your-openwebui-ip/32"
```

## Testing

### Test API Locally
```bash
# Health check
curl http://localhost:8001/health | jq

# Simple query
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I load modules?", "brief": true}' | jq

# Search specific index
curl -X POST http://localhost:8001/search \
  -H "Content-Type: application/json" \
  -d '{"query": "SLURM", "index": "tickets", "max_results": 5}' | jq
```

### Test OpenWebUI Pipeline
```python
# Run locally
python openwebui_pipeline.py
```

## Monitoring

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f dr-api
docker compose logs -f elasticsearch
```

### Check Elasticsearch
```bash
# Cluster health
curl http://localhost:9200/_cluster/health?pretty

# List indices
curl http://localhost:9200/_cat/indices?v

# Count documents
curl http://localhost:9200/docs/_count
curl http://localhost:9200/tickets/_count
```

### Check Service Status
```bash
docker compose ps
docker compose top
```

## Troubleshooting

### Elasticsearch Not Starting
```bash
# Check logs
docker compose logs elasticsearch

# Common issues:
# 1. Insufficient memory - Increase vm.max_map_count
sudo sysctl -w vm.max_map_count=262144

# 2. Permission issues
sudo chmod 777 /var/lib/elasticsearch
```

### DR API Not Responding
```bash
# Check if Elasticsearch is healthy
curl http://localhost:9200/_cluster/health

# Check API logs
docker compose logs dr-api

# Restart API
docker compose restart dr-api
```

### OpenWebUI Pipeline Timeout
- Increase `DR_API_TIMEOUT` in pipeline valves
- Check network connectivity to VM
- Verify firewall rules allow port 8001

### No Search Results
```bash
# Verify data is indexed
curl http://localhost:9200/_cat/indices?v

# Re-index if needed
./scripts/index_data.sh
```

## Project Structure

```
hpc_ticket_knowledgedb/
├── README.md                      # This file
├── docker-compose.yml             # Local development stack
├── .env.example                   # Environment template
├── Dockerfile.api                 # DR API service image
├── Dockerfile.indexer            # Data indexer image
├── api_requirements.txt          # API Python dependencies
├── indexer_requirements.txt      # Indexer Python dependencies
├── openwebui_pipeline.py         # OpenWebUI integration
├── api/                          # FastAPI application
│   ├── __init__.py
│   └── main.py                   # API endpoints
├── indexer/                      # Data indexing service
│   ├── __init__.py
│   └── index_all.py              # Unified indexer
├── scripts/                      # Helper scripts
│   ├── build_images.sh           # Build Docker images
│   ├── push_images.sh            # Push to registry
│   ├── index_data.sh             # Run indexer
│   └── start_services.sh         # Start local stack
├── deploy/terraform/             # OpenStack deployment
│   ├── main.tf                   # Main infrastructure
│   ├── network.tf                # Network configuration
│   ├── variables.tf              # Variable definitions
│   ├── user_data.sh              # VM initialization
│   └── terraform.tfvars.example  # Configuration template
└── ticketknowledgedb/            # Existing code & data
    ├── DR_Pipeline/              # Deep research system
    ├── docsmd/                   # Documentation
    ├── knowledgebase/            # Tickets
    └── ...                       # Analysis scripts
```

## Security Considerations

1. **API Access**: Restrict `api_allowed_cidr` to known IPs
2. **SSH Access**: Use key-based authentication only
3. **Elasticsearch**: Never expose port 9200 publicly
4. **Secrets**: Never commit `.env` or `terraform.tfvars` files
5. **LLM API**: Ensure LLM endpoint is secure or internal

## Contributing

When adding features:
1. Update API endpoints in `api/main.py`
2. Add configuration to `.env.example`
3. Update this README
4. Test locally before deploying

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
- Check `ticketknowledgedb/DR_Pipeline/README.md` for DR system details
- Review logs with `docker compose logs`
- Contact HPC team for domain-specific questions

## Example Questions

See `example_questions.md` for a list of test queries and expected behavior.
