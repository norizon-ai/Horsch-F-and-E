# OpenWebUI Integration Setup Guide

This guide explains how to set up and use OpenWebUI as a chat interface for the HPC Deep Research system.

## Overview

OpenWebUI provides a ChatGPT-like web interface for interacting with the HPC Knowledge Database. It uses a custom pipeline that connects to the DR API, providing:

- Real-time streaming responses
- Conversation history
- User-friendly chat interface
- Multi-turn conversations
- Confidence and metadata display

## Architecture

```
User Browser
    ↓ HTTP (port 3000)
OpenWebUI Container
    ↓ Pipeline: openwebui_pipeline.py
DR API Container (port 8000)
    ↓ orchestrates
DR Workflow (Supervisor + Research Agents)
    ↓ queries
Elasticsearch + External LLM
```

## Quick Start

### 1. Start Main Services

First, ensure the DR API and Elasticsearch are running:

```bash
./scripts/start_services.sh
```

Wait for services to be healthy (check with `docker ps`).

### 2. Start OpenWebUI

Use the helper script:

```bash
./scripts/start_openwebui.sh
```

Or manually:

```bash
docker compose -f docker-compose.yml -f docker-compose.openwebui.yml up -d openwebui
```

### 3. Access OpenWebUI

Open your browser to: **http://localhost:3000**

### 4. First-Time Setup

#### Create Admin Account

1. On first visit, you'll see a signup page
2. Create an account - **the first user is automatically admin**
3. Use a simple email/password (e.g., `admin@localhost` / `admin123`)

#### Install HPC Pipeline

1. Click your profile icon (top right) → **Admin Panel**
2. Go to **Settings** → **Pipelines**
3. Click **+ New Pipeline**
4. Click **Upload Pipeline** tab
5. Copy the contents of `openwebui_pipeline.py` from the repository
6. Paste into the code editor
7. Click **Save**

You should see "HPC Deep Research" appear in the pipelines list.

#### Enable the Pipeline

1. Go back to the main chat interface
2. Click the model selector dropdown (top of chat)
3. Select **HPC Deep Research**
4. Start chatting!

## Using the Chat Interface

### Example Queries

Try these HPC questions:

```
How do I submit a SLURM job?
```

```
What GPU models are available on the cluster?
```

```
How do I access my $WORK directory in JupyterHub?
```

```
My job says "InvalidPartitionName" - what does this mean?
```

### Understanding Responses

Responses include:

- **Main Answer**: Concise answer to your question (2-4 sentences)
- **Detailed Research**: Full report with sources (if not in brief mode)
- **Metadata**:
  - Confidence score (0.0-1.0)
  - Number of iterations (1-3)
  - Processing time (seconds)

Example:

```
You can submit a SLURM job using the sbatch command. Create a job
script with #SBATCH directives and run: sbatch myjob.sh

---
Confidence: 0.85 | Iterations: 1 | Time: 28.3s
```

### Response Times

- **Simple questions**: 20-40 seconds (1 iteration)
- **Complex questions**: 60-120 seconds (2-3 iterations)

The interface shows "typing..." while processing.

## Pipeline Configuration

### Environment Variables

The pipeline reads these environment variables (set in `docker-compose.openwebui.yml`):

| Variable | Default | Description |
|----------|---------|-------------|
| `DR_API_URL` | `http://dr-api:8000` | DR API endpoint (Docker network) |
| `DR_API_TIMEOUT` | `180` | Request timeout in seconds |
| `ENABLE_BRIEF_MODE` | `false` | Use brief mode (faster, less detail) |
| `ENABLE_STREAMING` | `true` | Stream responses in real-time |

### Adjusting Pipeline Settings

To change settings after installation:

1. **Admin Panel** → **Settings** → **Pipelines**
2. Click **Edit** on "HPC Deep Research"
3. Modify the `Valves` class defaults:

```python
class Valves(BaseModel):
    DR_API_URL: str = "http://dr-api:8000"
    DR_API_TIMEOUT: int = 180
    ENABLE_BRIEF_MODE: bool = False  # Change to True for faster responses
    ENABLE_STREAMING: bool = True
```

4. Click **Save**

### Brief Mode vs. Comprehensive Mode

**Brief Mode** (`ENABLE_BRIEF_MODE=True`):
- Faster responses (~20-30s)
- Only returns concise answer (no detailed report)
- Good for quick questions
- Lower confidence threshold

**Comprehensive Mode** (default):
- Slower responses (~30-120s)
- Returns concise answer + detailed research report
- Better for complex questions
- Higher quality answers

## Troubleshooting

### OpenWebUI won't start

**Check DR API is running**:
```bash
docker ps | grep hpc-kb-dr-api
curl http://localhost:8001/health | jq
```

If not running:
```bash
./scripts/start_services.sh
```

**Check logs**:
```bash
docker logs hpc-kb-openwebui-test
```

### Pipeline not appearing

**Verify installation**:
1. Admin Panel → Settings → Pipelines
2. Check "HPC Deep Research" is listed
3. Check for errors in Status column

**Reinstall pipeline**:
1. Delete existing pipeline
2. Follow "Install HPC Pipeline" steps again
3. Ensure entire `openwebui_pipeline.py` content is copied

### Queries timeout

**Increase timeout in pipeline**:
```python
DR_API_TIMEOUT: int = 300  # 5 minutes
```

Or use brief mode for faster responses.

### Connection errors

**Error**: `Could not connect to DR API`

**Solutions**:
1. Check DR API health: `curl http://localhost:8001/health`
2. Verify Docker network: `docker network ls | grep hpc-kb-network`
3. Check container names match: `docker ps`
4. Restart OpenWebUI: `docker compose -f docker-compose.openwebui.yml restart`

### LLM errors

**Error**: `LLM connection failed`

**Solutions**:
1. Check VPN connection (required for GPT-OSS access)
2. Verify LLM_BASE_URL in `.env`
3. Test LLM directly:
   ```bash
   curl http://lme49.cs.fau.de:30000/v1/models
   ```

### Empty results

**Error**: `No search results found`

**Solution**: Index data first:
```bash
./scripts/index_data.sh
```

Verify indices exist:
```bash
curl http://localhost:9200/_cat/indices?v
```

## Advanced Usage

### Multi-Turn Conversations

OpenWebUI maintains conversation history. You can:

1. Ask follow-up questions
2. Reference previous answers
3. Build context over multiple queries

Example conversation:
```
You: How do I submit a SLURM job?
Bot: [explains sbatch command]

You: What partitions are available?
Bot: [lists partitions based on knowledge base]

You: Which partition should I use for GPU jobs?
Bot: [recommends partition with context from previous question]
```

### Creating Multiple Users

As admin:

1. **Admin Panel** → **Settings** → **Users**
2. Click **+ Add User**
3. Set email, password, role
4. User can now log in

Or enable signup in `.env`:
```bash
OPENWEBUI_ENABLE_SIGNUP=true
```

### Customizing the Interface

**Change name**:

In `docker-compose.openwebui.yml`:
```yaml
- WEBUI_NAME=My Custom HPC Assistant
```

**Change port**:

In `.env`:
```bash
OPENWEBUI_PORT=8080
```

Then restart:
```bash
docker compose -f docker-compose.openwebui.yml restart
```

## Production Deployment Notes

This setup is for **local testing only**. For production:

1. **Use existing OpenWebUI instance** - Don't deploy a second instance
2. **Upload pipeline only** - Copy `openwebui_pipeline.py` to production OpenWebUI
3. **Update DR_API_URL** - Point to production DR API endpoint:
   ```python
   DR_API_URL: str = "http://<production-ip>:8001"
   ```
4. **Enable authentication** - Disable signup, create specific users
5. **Use HTTPS** - Set up reverse proxy (nginx/traefik)
6. **Monitor resources** - OpenWebUI + DR API can use significant memory under load

## Stopping OpenWebUI

**Stop container**:
```bash
docker compose -f docker-compose.openwebui.yml down
```

**Stop and remove data** (fresh start):
```bash
docker compose -f docker-compose.openwebui.yml down -v
```

**Keep main services running**:
The above commands only stop OpenWebUI, not DR API or Elasticsearch.

## File Reference

| File | Purpose |
|------|---------|
| `docker-compose.openwebui.yml` | OpenWebUI service definition |
| `openwebui_pipeline.py` | DR Pipeline integration code |
| `scripts/start_openwebui.sh` | Helper script to start OpenWebUI |
| `.env` | Configuration variables |

## Next Steps

After successful testing with OpenWebUI:

1. Test various HPC questions to validate answers
2. Monitor response times and quality
3. Adjust brief mode / timeouts based on needs
4. Share feedback on answer quality
5. Prepare for production deployment (update pipeline in production OpenWebUI)

## Support

For issues:
- Check logs: `docker logs hpc-kb-openwebui-test`
- Check DR API: `curl http://localhost:8001/health | jq`
- Check Elasticsearch: `curl http://localhost:9200/_cluster/health | jq`
- Review CLAUDE.md for DR Pipeline details
