# Horsch Confluence Assistant

A complete pipeline connecting **Confluence Export → Elasticsearch → DeepResearch → LangGraph Frontend** for intelligent question answering over Horsch Confluence documentation.

## Overview

This pipeline provides agentic retrieval-augmented generation (RAG) over Confluence data, enabling:

- **Deep Research**: Multi-agent system that decomposes questions and performs iterative research
- **Hybrid Search**: Combines semantic (vector) and lexical (BM25) search for optimal retrieval
- **Pre-indexed Data**: Uses pre-built Elasticsearch image with Horsch Confluence data
- **Flexible Architecture**: Easy to customize for different data sources or models

## Architecture

```
┌─────────────────────┐
│ Confluence Export   │ (Data Source)
│ - HTML pages        │
│ - Attachments       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Elasticsearch      │ (Knowledge Base)
│  - Full-text index  │
│  - Vector embeddings│
│  - Port: 9200       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ DeepResearch API    │ (Agentic RAG)
│ - Supervisor Agent  │
│ - Research Agents   │
│ - Port: 8000        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ User Interfaces     │
│ - REST API          │
│ - LangGraph Studio  │
│ - Custom frontends  │
└─────────────────────┘
```

## Quick Start

### Prerequisites

- **Docker Desktop** installed and running
- **At least 4GB free RAM** (2GB for Elasticsearch, 2GB for DeepResearch)
- **At least 5GB free disk space**
- **OpenAI API key** (or alternative model backend)

### 1. Setup

Run the setup script to configure your environment:

```bash
cd products/horsch_confluence_assistant
./scripts/setup.sh
```

This will:
- Check prerequisites (Docker, resources)
- Create `.env` file from template
- Pull required Docker images
- Verify configuration

### 2. Configure API Keys

Edit the `.env` file and add your API key:

```bash
# Edit .env
nano .env

# Or use your preferred editor
vim .env
```

**Minimum required:**
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Start the Pipeline

Start all services with Docker Compose:

```bash
docker compose up -d
```

This starts:
- **Elasticsearch**: Knowledge base with pre-indexed Horsch Confluence data (port 9200)
- **DeepResearch API**: Agentic RAG service (port 8000)

### 4. Verify Services

Check that all services are healthy:

```bash
# View service status
docker compose ps

# Check Elasticsearch
curl http://localhost:9200/_cluster/health

# Check DeepResearch API
curl http://localhost:8000/health

# View document count
curl http://localhost:9200/confluence_kb/_count
```

### 5. Query the System

**Synchronous query (wait for result):**
```bash
curl -X POST http://localhost:8000/query/sync \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the main features of the HORSCH product line?"}'
```

**Asynchronous query (background processing):**
```bash
# Submit query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "Explain the HORSCH cultivation technology"}'

# Returns: {"job_id": "abc-123", "status": "pending"}

# Check status
curl http://localhost:8000/status/abc-123

# Get result when complete
curl http://localhost:8000/result/abc-123
```

**Interactive API documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Advanced Usage

### Building Your Own Elasticsearch Image

If you want to create your own pre-loaded Elasticsearch image with custom Confluence data:

#### 1. Export Confluence Data

```bash
cd ../../services/connectors/confluence
python main.py --base-url https://your-confluence.com --token YOUR_TOKEN
```

This creates a `confluence_export` directory with your data.

#### 2. Build the Elasticsearch Image

**Important:** Set the Confluence base URL before building to ensure proper clickable links:

```bash
# Set the Confluence base URL (adjust if using a different instance)
export CONFLUENCE_BASE_URL=https://confluence.horsch.com

cd elasticsearch_image
./build.sh
```

This will:
- Copy your Confluence data into the Docker build
- Start Elasticsearch and index all pages with embeddings
- Extract proper Confluence URLs from metadata (instead of pseudo-URLs)
- Create a final image with data baked in

Build time: 10-30 minutes depending on data size.

**Note:** If you previously built an image without `CONFLUENCE_BASE_URL`, sources in reports will show `local:///` URLs. Re-build with the environment variable set to get proper clickable Confluence links.

#### 3. Test Your Image Locally

```bash
docker run -d --name es-test -p 9200:9200 confluence-elasticsearch:latest
curl http://localhost:9200/confluence_kb/_count
docker rm -f es-test
```

#### 4. Push to Docker Hub (Optional)

```bash
cd ../../services/connectors/confluence/elasticsearch_image
export DOCKER_USERNAME=your-dockerhub-username
./push.sh
```

#### 5. Update docker-compose.yml

```yaml
elasticsearch:
  image: your-username/confluence-elasticsearch:latest
```

For detailed instructions, see [Elasticsearch Image README](../../services/connectors/confluence/elasticsearch_image/README.md).

### Runtime Indexing (Alternative Method)

If you prefer to index data at runtime instead of building an image:

1. Export your Confluence data

2. Set the configuration in `.env`:
   ```env
   CONFLUENCE_EXPORT_DIR=/path/to/your/confluence_export
   CONFLUENCE_BASE_URL=https://confluence.horsch.com
   ```

3. Update `docker-compose.yml` to use empty Elasticsearch:
   ```yaml
   elasticsearch:
     image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
   ```

4. Start Elasticsearch and run the indexing script:
   ```bash
   docker compose up -d elasticsearch
   ./scripts/index_confluence.sh
   ```

**Note:** The `CONFLUENCE_BASE_URL` setting ensures that sources in reports contain proper clickable Confluence URLs (e.g., `https://confluence.horsch.com/spaces/...`) instead of pseudo-URLs like `local:///`.

### Using Alternative Model Backends

The pipeline supports multiple LLM backends:

**Groq (Fast inference):**
```env
GROQ_API_KEY=your-groq-api-key
SUPERVISOR_MODEL=groq:llama-3.1-70b-versatile
RESEARCHER_MODEL=groq:llama-3.1-8b-instant
```

**Ollama (Local models):**
```env
# Uncomment ollama service in docker-compose.yml first
OLLAMA_BASE_URL=http://ollama:11434
SUPERVISOR_MODEL=ollama:llama3.1
RESEARCHER_MODEL=ollama:llama3.1
```

**Custom OpenAI-compatible API:**
```env
CUSTOM_API_URL=https://your-api.example.com/v1
CUSTOM_API_KEY=your-api-key
SUPERVISOR_MODEL=custom:your-model-name
```

### Configuration Options

All configuration is in `.env`. Key settings:

**Model Selection:**
- `SUPERVISOR_MODEL`: Model for planning and coordination (default: `openai:gpt-4o-mini`)
- `RESEARCHER_MODEL`: Model for research tasks (default: `openai:gpt-4o-mini`)

**Search Configuration:**
- `SEARCH_API`: Backend type (`elasticsearch` or `searxng`)
- `ELASTIC_INDEX`: Index name (default: `confluence_kb`)
- `EMBED_MODEL`: Embedding model (must match indexed data)

**Confluence Integration:**
- `CONFLUENCE_BASE_URL`: Base URL for generating clickable links (default: `https://confluence.horsch.com`)
  - **Important:** If re-indexing from an older version, set this to generate proper Confluence URLs instead of pseudo-URLs

**Research Behavior:**
- `MAX_SEARCH_DEPTH`: How many iterations per research section (default: 2)
- `NUMBER_OF_QUERIES`: Queries generated per section (default: 4)
- `HYBRID_ALPHA`: Balance between semantic and lexical search (0.0-1.0)

### LangGraph Studio Integration

Make sure that you are in an env where the local module in the folder `services/deepresearch` is installed (`pip install -e .`).

For interactive debugging and visualization:

```bash
# From the repository root
cd services/deepresearch
uvx --from "langgraph-cli[inmem]" --python 3.13 langgraph dev --allow-blocking
```

Then access the Studio UI at: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

## Service Management

### View Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f deepresearch-api
docker compose logs -f elasticsearch
```

### Restart Services

```bash
# Restart all
docker compose restart

# Restart specific service
docker compose restart deepresearch-api
```

### Stop Services

```bash
# Stop all (keeps data)
docker compose stop

# Stop and remove containers (keeps volumes)
docker compose down

# Stop and remove everything including data
docker compose down -v
```

### Rebuild Services

After code changes:

```bash
# Rebuild and restart
docker compose up -d --build deepresearch-api
```

## Troubleshooting

### Elasticsearch Won't Start

**Error: "max virtual memory areas vm.max_map_count too low"**

**Linux:**
```bash
sudo sysctl -w vm.max_map_count=262144
```

**macOS/Windows:** Increase Docker Desktop memory to at least 4GB in Settings → Resources

### API Returns "OpenAI API key not found"

1. Check your `.env` file has the correct API key
2. Restart the service: `docker compose restart deepresearch-api`
3. Verify with: `docker compose exec deepresearch-api env | grep OPENAI`

### No Results from Queries

1. Verify Elasticsearch has data:
   ```bash
   curl http://localhost:9200/confluence_kb/_count
   ```

2. Check index name matches:
   ```bash
   curl http://localhost:9200/_cat/indices
   ```

3. Verify embedding model in `.env` matches the indexed data

### Services Crash or OOM

1. Check Docker Desktop has at least 4GB RAM allocated
2. Reduce Elasticsearch memory in `docker-compose.yml`:
   ```yaml
   ES_JAVA_OPTS=-Xms1g -Xmx1g  # Instead of 2g
   ```

### Port Already in Use

If ports 8000 or 9200 are already in use, change them in `.env`:

```env
ELASTICSEARCH_PORT=9201
DEEPRESEARCH_PORT=8001
```

## API Reference

### Health Check

```bash
GET /health
```

Returns service status and configuration.

### Synchronous Query

```bash
POST /query/sync
Content-Type: application/json

{
  "question": "Your question here",
  "config": {
    "search_api": "elasticsearch",
    "max_search_depth": 2,
    "number_of_queries": 4
  }
}
```

Returns complete research report (may take 30-120 seconds).

### Asynchronous Query

```bash
# Submit
POST /query
Content-Type: application/json

{
  "question": "Your question here"
}

# Returns: {"job_id": "uuid", "status": "pending"}

# Check status
GET /status/{job_id}

# Get result
GET /result/{job_id}
```

### Batch Queries

```bash
POST /batch
Content-Type: application/json

{
  "questions": [
    "Question 1?",
    "Question 2?"
  ],
  "config": {
    "search_api": "elasticsearch"
  }
}
```

For full API documentation, see http://localhost:8000/docs when running.

## Performance Tuning

### For Faster Queries

1. **Use faster models:**
   ```env
   SUPERVISOR_MODEL=openai:gpt-4o-mini
   RESEARCHER_MODEL=openai:gpt-4o-mini
   ```

2. **Reduce search depth:**
   ```env
   MAX_SEARCH_DEPTH=1
   ```

3. **Use Groq for faster inference:**
   ```env
   GROQ_API_KEY=your-key
   RESEARCHER_MODEL=groq:llama-3.1-8b-instant
   ```

### For Better Quality

1. **Use more capable models:**
   ```env
   SUPERVISOR_MODEL=openai:gpt-4o
   RESEARCHER_MODEL=openai:gpt-4o
   ```

2. **Increase search depth:**
   ```env
   MAX_SEARCH_DEPTH=3
   NUMBER_OF_QUERIES=6
   ```

3. **Adjust hybrid search:**
   ```env
   HYBRID_ALPHA=0.5  # Equal weight to semantic and lexical
   ```

## Project Structure

```
products/horsch_confluence_assistant/
├── docker-compose.yml          # Service orchestration
├── .env.example                # Configuration template
├── .env                        # Your configuration (git-ignored)
├── README.md                   # This file
└── scripts/
    ├── setup.sh                # Initial setup
    └── index_confluence.sh     # Custom data indexing
```

## Integration with Norizon Architecture

This pipeline implements the following components from the [Norizon Architecture](../../norizon_architecture_diagram.yaml):

**Knowledge Producers:**
- Confluence Connector (services/connectors/confluence/)

**Norizon (Core Intelligence):**
- Search Modules → Agentic - Deep Research
- Non Agentic - RAG (hybrid search in Elasticsearch)

**Shared Components:**
- Databases → Elastic DB (Elasticsearch)
- Embedding Service (sentence-transformers)
- Chat Model (OpenAI/Groq/Ollama)

**Knowledge Consumers:**
- API Gateway (DeepResearch API endpoints)
- DevHero - MCP Tools (can integrate via API)
- ChatKit (can integrate via API)

## Related Documentation

- [Confluence Connector](../../services/connectors/confluence/README.md) - Export Confluence data
- [DeepResearch Service](../../services/deepresearch/README.md) - Agentic RAG details
- [Norizon Architecture](../../norizon_architecture_diagram.yaml) - Overall system design

## Support

For issues or questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review service logs: `docker compose logs -f`
3. Verify configuration: `cat .env`
4. Open an issue in the project repository

## License

This project is part of the Norizon Knowledge Management Platform.
