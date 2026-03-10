# HPC Ticket Knowledge Database - Insomnia API Collection

Complete Insomnia API collection for testing the HPC Ticket Knowledge Database system. This collection includes all DR API endpoints, direct Elasticsearch access, and realistic HPC query examples.

## Overview

This Insomnia collection provides:
- **18 pre-configured requests** across 3 organized folders
- **2 environments**: Local Development and OpenStack Production
- **Realistic HPC examples**: SLURM, GPU, modules, JupyterHub, troubleshooting
- **Direct Elasticsearch access**: For debugging and raw queries

### Services Covered

1. **DR API** (port 8001) - Deep Research multi-agent system
   - Query processing (synchronous & streaming)
   - Direct search (docs & tickets)
   - Health checks

2. **Elasticsearch** (port 9200) - Knowledge base storage
   - Cluster health and index management
   - Direct search queries
   - Document counts

## Prerequisites

- **Insomnia Desktop** installed ([Download here](https://insomnia.rest/download))
- **Services running**:
  - Local: `./scripts/start_services.sh`
  - OpenStack: Terraform deployment completed
- **VPN connection** (for LLM access when using DR queries)

## Installation

### Step 1: Download Insomnia

If you don't have Insomnia installed:

1. Visit https://insomnia.rest/download
2. Download for your platform (macOS, Windows, Linux)
3. Install and launch Insomnia Desktop

### Step 2: Import Collection

1. Open Insomnia Desktop
2. Click **Application** menu → **Preferences** → **Data** tab
3. Click **Import Data**
4. Select `hpc-knowledgedb-insomnia.json` from this directory
5. Collection "HPC Ticket Knowledge Database" appears in left sidebar

![Import Process](https://insomnia.rest/images/import-data.png)

## Environment Setup

The collection includes two pre-configured environments. Select the appropriate one before running requests.

### Local Development (Default)

**For testing on your local machine:**

1. Click the environment dropdown (top-left, near "No Environment")
2. Select **"Local Development"**
3. No configuration needed - uses localhost:8001 and localhost:9200

**Use when:**
- Running `./scripts/start_services.sh` locally
- Using `docker compose up` in the project directory
- Testing during development

### OpenStack Production

**For testing deployed services:**

1. Click the environment dropdown
2. Select **"OpenStack Production"**
3. Click environment dropdown again → **Manage Environments**
4. Find "OpenStack Production" and click **Edit**
5. Update `floating_ip` value:
   ```json
   {
     "floating_ip": "131.188.45.123"  // Your actual floating IP
   }
   ```
6. Click **Done**

**Get your floating IP:**
```bash
cd deploy/terraform
terraform output dr_api_url
# Output: http://131.188.45.123:8001
# Use: 131.188.45.123 (without http:// or port)
```

**Use when:**
- Testing OpenStack deployment
- Running integration tests against production
- Verifying deployment worked correctly

## ⚠️ Important: Set Timeout First!

**Before testing**, increase Insomnia's timeout to avoid request timeouts:

1. **Preferences** → **Request/Response** → **Request timeout**
2. Change from `30000` ms to **`120000`** ms (2 minutes)
3. Click **Done**

DR queries take 10-120 seconds depending on complexity. The default 30s timeout is too short.

## Quick Start Testing

Recommended testing workflow to verify everything works:

### 1. Health Checks (30 seconds)

Run these requests first to verify all services are online:

- **DR API Endpoints** → **Health Check**
  - Expected: `{"status": "healthy", "elasticsearch_connected": true, ...}`
- **Elasticsearch Direct Access** → **Cluster Health**
  - Expected: `{"status": "green" or "yellow", ...}`
- **Elasticsearch Direct Access** → **List Indices**
  - Expected: See `docs` and `tickets` indices
- **LLM Direct Access** → **List Models** (requires VPN)
  - Expected: List of available models including `openai/gpt-oss-120b`

### 2. Basic Functionality (2 minutes)

Test simple operations:

- **Example Queries** → **Example: Module Loading** (brief mode, 10-20s)
  - Tests basic DR query with fast response
- **DR API Endpoints** → **Direct Search (Docs)** (1-5s)
  - Tests search without LLM calls

### 3. Deep Research Testing (10 minutes)

Test the full DR pipeline:

- **Example Queries** → **Example: SLURM Job Submission** (20-40s)
  - Basic question, should get high confidence (0.8+)
- **Example Queries** → **Example: GPU Configuration** (40-80s)
  - Intermediate complexity, multiple sources
- **Example Queries** → **Example: Error Troubleshooting** (80-180s)
  - Complex question, 3 iterations, comprehensive answer

### 4. Streaming Test (3 minutes)

Test real-time updates:

- **DR API Endpoints** → **Query (Streaming SSE)**
  - Watch Timeline tab for incremental events
  - Look for `type: "completed"` event

### 5. Elasticsearch Direct (2 minutes)

Test raw Elasticsearch queries:

- **Elasticsearch Direct Access** → **Search Docs Index**
  - See raw search results with scores
- **Elasticsearch Direct Access** → **Count Docs** & **Count Tickets**
  - Verify data is indexed

## Request Reference

### Folder 1: DR API Endpoints (7 requests)

| Request | Method | Response Time | Description |
|---------|--------|--------------|-------------|
| Get Service Info | GET / | <1s | Service metadata |
| Health Check | GET /health | <5s | System health status |
| Query (Brief Mode) | POST /query | 10-60s | Concise answer only |
| Query (Comprehensive Mode) | POST /query | 60-180s | Full research report |
| Query (Streaming SSE) | POST /query/stream | 60-180s | Real-time updates |
| Direct Search (Docs) | POST /search | 1-5s | Search docs index |
| Direct Search (Tickets) | POST /search | 1-5s | Search tickets index |

### Folder 2: Elasticsearch Direct Access (6 requests)

| Request | Method | Response Time | Description |
|---------|--------|--------------|-------------|
| Cluster Health | GET /_cluster/health | <1s | ES cluster status |
| List Indices | GET /_cat/indices?v | <2s | All indices with stats |
| Search Docs Index | POST /docs/_search | 1-5s | Raw docs search |
| Search Tickets Index | POST /tickets/_search | 1-5s | Raw tickets search |
| Count Docs | GET /docs/_count | <1s | Total docs count |
| Count Tickets | GET /tickets/_count | <1s | Total tickets count |

### Folder 3: Example Queries (5 requests)

| Request | Complexity | Response Time | Notes |
|---------|-----------|--------------|-------|
| Example: SLURM Job Submission | Basic | 10-30s | High confidence expected |
| Example: GPU Configuration | Intermediate | 30-60s | Multiple sources |
| Example: Module Loading | Simple | 10-20s | Brief mode, fast |
| Example: JupyterHub Access | Intermediate | 30-60s | Assumption checking |
| Example: Error Troubleshooting | Complex | 60-120s | 3 iterations, deep research |

### Folder 4: LLM Direct Access (3 requests)

| Request | Method | Response Time | Description |
|---------|--------|--------------|-------------|
| List Models | GET /v1/models | <2s | List available LLM models |
| LLM Health Check | POST /v1/chat/completions | 5-15s | Simple "OK" test |
| Test HPC Question | POST /v1/chat/completions | 10-20s | Technical query test |

## Testing the LLM Directly

The **LLM Direct Access** folder contains requests to test the LLM endpoint independently of the DR Pipeline. This is useful for:

- **Verifying VPN connectivity** - Ensure you can reach the LLM server
- **Debugging LLM issues** - Test if problems are in DR Pipeline or LLM itself
- **Checking model availability** - See which models are accessible
- **Testing response quality** - Verify LLM is answering correctly

### LLM Request Details

**1. List Models** - `GET /v1/models`
```bash
# Shows all available models
# Useful for: Verifying connectivity and seeing model options
# Expected response: List of model IDs
```

**2. LLM Health Check** - `POST /v1/chat/completions`
```bash
# Sends simple "Say OK if you are working" prompt
# Useful for: Quick connectivity test
# Expected response: "OK" or similar acknowledgment
```

**3. Test HPC Question** - `POST /v1/chat/completions`
```bash
# Asks "What does the SLURM sbatch command do?"
# Useful for: Testing technical knowledge and reasoning
# Expected response: Accurate explanation of sbatch command
```

### LLM Environment Variables

The collection uses these environment variables for LLM testing:

- `llm_base_url`: LLM endpoint (default: `http://lme49.cs.fau.de:30000/v1`)
- `llm_api_key`: API key (default: `dummy` for GPT-OSS)
- `llm_model`: Model identifier (default: `openai/gpt-oss-120b`)

**To change LLM endpoint:**
1. Click environment dropdown → Manage Environments
2. Edit your environment (Local or OpenStack)
3. Update `llm_base_url`, `llm_api_key`, or `llm_model`
4. Click Done

### VPN Requirement

The LLM endpoint (`lme49.cs.fau.de`) **requires VPN access**. If requests fail:

1. **Check VPN**: Ensure you're connected to the FAU network
2. **Test connectivity**: Run "List Models" request
3. **Check firewall**: Ensure port 30000 is accessible

Without VPN:
- LLM requests will timeout (30 seconds)
- DR API `/health` will show `llm_configured: true` but queries will fail
- Direct LLM tests will return connection errors

## Configuration Notes

### Timeout Settings

Long-running queries may timeout with default settings. To adjust:

1. **Global timeout** (recommended):
   - Go to **Preferences** → **Request/Response**
   - Set "Request timeout" to `300000` ms (5 minutes)

2. **Per-request timeout**:
   - Open request
   - Go to request **Settings** tab (gear icon)
   - Set timeout to desired value

**Recommended timeouts:**
- Health checks: 10,000 ms (10 seconds)
- Direct search: 30,000 ms (30 seconds)
- Brief queries: 90,000 ms (1.5 minutes)
- Comprehensive queries: 240,000 ms (4 minutes)
- Streaming queries: 300,000 ms (5 minutes)

### Server-Sent Events (SSE)

The `/query/stream` endpoint uses SSE for real-time updates:

**How to view:**
1. Send request
2. Click **Timeline** tab (bottom panel)
3. Watch events arrive in real-time

**Event types:**
```
data: {"type": "started", "query": "..."}
data: {"type": "iteration", "number": 1, "total": 3}
data: {"type": "completed", "answer": "...", "confidence": 0.85}
```

**Final answer** is in the `type: "completed"` event.

### Environment Variables

All requests use environment variables for flexibility:

- `{{ _.base_url }}` - DR API base URL
- `{{ _.elasticsearch_url }}` - Elasticsearch base URL
- `{{ _.docs_index }}` - Docs index name (default: "docs")
- `{{ _.tickets_index }}` - Tickets index name (default: "tickets")

**To modify:**
1. Click environment dropdown → **Manage Environments**
2. Edit environment
3. Change variable values
4. Click **Done**

## Troubleshooting

### "Connection refused" on DR API

**Error**: `Failed to connect to http://localhost:8001`

**Solutions:**
1. Verify services are running:
   ```bash
   docker compose ps
   # Should show: hpc-kb-dr-api (Up), hpc-kb-elasticsearch (Up)
   ```
2. Check port 8001 is not in use:
   ```bash
   lsof -i :8001
   ```
3. Restart services:
   ```bash
   docker compose restart dr-api
   ```
4. Verify environment URL matches your setup

### "Connection refused" on Elasticsearch

**Error**: `Failed to connect to http://localhost:9200`

**Solutions:**
1. Wait 30 seconds after `docker compose up` (Elasticsearch startup time)
2. Test directly:
   ```bash
   curl http://localhost:9200/_cluster/health
   ```
3. Check logs:
   ```bash
   docker compose logs elasticsearch
   ```
4. Increase Docker memory (Elasticsearch needs 2GB+)

### "LLM connection failed" in /health

**Error**: Health check shows `llm_configured: false`

**Solutions:**
1. Verify `LLM_BASE_URL` in `.env` file
2. Test LLM endpoint:
   ```bash
   curl $LLM_BASE_URL/models
   ```
3. **VPN**: Ensure VPN is connected if LLM is internal
4. Note: System will start but queries will fail without LLM

### "No results found" in search

**Error**: Search returns `"total": 0`

**Solutions:**
1. Run indexer to populate data:
   ```bash
   ./scripts/index_data.sh
   ```
2. Verify indices exist:
   - Run **List Indices** request
   - Should see `docs` and `tickets`
3. Check document counts:
   - Run **Count Docs** and **Count Tickets**
   - Should return > 0
4. Verify index names in environment match `.env` configuration

### Timeout on long queries

**Error**: Request times out after 30 seconds

**Solutions:**
1. Increase timeout in Insomnia settings (see Configuration Notes above)
2. Use **brief mode** for faster responses:
   ```json
   {"query": "...", "brief": true}
   ```
3. Reduce `max_iterations`:
   ```json
   {"query": "...", "max_iterations": 1}
   ```
4. Check VPN connection (LLM timeout is 30s without VPN)

### SSE stream not showing progress

**Issue**: Streaming endpoint doesn't show incremental updates

**Explanation**: This is expected behavior. The current implementation sends all events when processing completes, not during processing. To see events:

1. Send streaming request
2. Wait for completion (60-180 seconds)
3. Check Timeline tab - all events appear together

**Note**: For true real-time streaming, see SCALABILITY_PLAN.md Phase 2 improvements.

### Response is very slow

**Expected response times:**

| Query Type | Brief Mode | Comprehensive Mode |
|-----------|------------|-------------------|
| Simple (e.g., "What is SLURM?") | 10-20s | 20-40s |
| Intermediate (e.g., GPU config) | 20-40s | 40-80s |
| Complex (e.g., troubleshooting) | 40-60s | 80-180s |

**If slower than expected:**
1. Check VPN connection (LLM latency: 10-15s per call)
2. Verify Elasticsearch is responsive (run Cluster Health)
3. Check system resources (Docker CPU/memory limits)
4. Review logs: `docker compose logs -f dr-api`

## Advanced Usage

### Custom Iteration Limits

Override the default 3 iterations:

```json
{
  "query": "Your question here",
  "brief": false,
  "max_iterations": 5
}
```

Lower values = faster response, potentially less comprehensive.

### Modifying Elasticsearch Queries

Customize search behavior in direct Elasticsearch requests:

**Add fuzziness** (typo tolerance):
```json
{
  "query": {
    "multi_match": {
      "query": "SLRM",  // Typo: SLRM instead of SLURM
      "fields": ["title^3", "text"],
      "fuzziness": "AUTO"
    }
  }
}
```

**Adjust field weights**:
```json
{
  "fields": [
    "title^5",           // Title 5x more important
    "problem_description^3",
    "text"
  ]
}
```

**Date range filter**:
```json
{
  "query": {
    "bool": {
      "must": { "match": { "title": "GPU" }},
      "filter": {
        "range": {
          "created_at": { "gte": "2024-01-01" }
        }
      }
    }
  }
}
```

### Performance Testing

Track response times for optimization:

1. **Use "Send and Download"**:
   - Right-click request → "Send and Download"
   - Check download time in response metadata

2. **Monitor `processing_time` field**:
   ```json
   {
     "processing_time": 45.23,  // Seconds
     "total_iterations": 2
   }
   ```

3. **Compare brief vs comprehensive**:
   - Run same query with `brief: true` vs `brief: false`
   - Measure time difference
   - Use brief mode when full report not needed

### Batch Testing

Test multiple requests sequentially:

1. Install "Insomnia CLI" (optional): `npm install -g @kong/insomnia-cli`
2. Export collection to file
3. Run: `inso run test hpc-knowledgedb-insomnia.json --env "Local Development"`

Or use collection runner in Insomnia:
- Select folder (e.g., "Example Queries")
- Click **Run** button
- Watch all requests execute sequentially

## Response Quality Indicators

### Good Answers

Look for these indicators of high-quality responses:

- `confidence_score >= 0.7` - High confidence in answer
- `total_iterations: 2-3` - Comprehensive research
- Multiple sources cited in `iterations[].research_answers[].sources`
- Clear, actionable content in `concise_answer`

### Warning Signs

These may indicate issues:

- `confidence_score < 0.5` - Low confidence, may need reformulation
- `total_iterations: 1` with complex query - Shallow research
- Empty `sources` arrays - Knowledge base missing data
- Very generic answers - May need more specific query

**If answer quality is low:**
1. Rephrase query to be more specific
2. Check knowledge base has relevant data (run direct search)
3. Review `user_assumptions` in response (may have incorrect assumptions)
4. Increase `max_iterations` for complex questions

## Integration Examples

### Use in CI/CD

Test DR API in continuous integration:

```bash
#!/bin/bash
# test_dr_api.sh

# Health check
curl -f http://localhost:8001/health || exit 1

# Test query
response=$(curl -s -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I submit a SLURM job?", "brief": true}')

confidence=$(echo $response | jq -r '.confidence_score')

# Assert confidence >= 0.6
if (( $(echo "$confidence >= 0.6" | bc -l) )); then
  echo "Test passed: confidence = $confidence"
  exit 0
else
  echo "Test failed: confidence = $confidence (expected >= 0.6)"
  exit 1
fi
```

### Use in Application Code

Example Python integration:

```python
import requests

BASE_URL = "http://localhost:8001"

def query_hpc_knowledge(question: str, brief: bool = True) -> dict:
    """Query HPC knowledge database via DR API"""
    response = requests.post(
        f"{BASE_URL}/query",
        json={"query": question, "brief": brief},
        timeout=120
    )
    response.raise_for_status()
    return response.json()

# Usage
result = query_hpc_knowledge("How do I submit a SLURM job?")
print(f"Answer: {result['concise_answer']}")
print(f"Confidence: {result['confidence_score']}")
```

## Additional Resources

- **Main Documentation**: See `../README.md` for project overview
- **API Documentation**: See `../api/main.py` for endpoint details
- **Example Questions**: See `../example_questions.md` for more query examples
- **Deployment Guide**: See `../deploy/README.md` for OpenStack deployment
- **Scalability Planning**: See `../SCALABILITY_PLAN.md` for performance optimization roadmap

## Support

For issues or questions:

1. Check this README's Troubleshooting section
2. Review logs: `docker compose logs -f dr-api`
3. Test services manually: `./scripts/start_services.sh`
4. Verify data is indexed: `./scripts/index_data.sh`

## License

This collection is part of the HPC Ticket Knowledge Database project.
