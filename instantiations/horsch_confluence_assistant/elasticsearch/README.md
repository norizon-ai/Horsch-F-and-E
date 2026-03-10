# Elasticsearch Image with Pre-loaded Confluence Data

This directory contains everything needed to build a Docker image with Elasticsearch and pre-indexed Confluence data, ready for deployment.

## Overview

Creates a production-ready Elasticsearch container with:
- Elasticsearch 8.11.0
- Pre-indexed Confluence pages with vector embeddings
- Optimized for semantic + lexical hybrid search
- Ready to use with DeepResearch RAG pipeline

## Quick Start

### 1. Prepare Confluence Export

First, export your Confluence data using the Confluence connector:

```bash
cd ..  # Go to confluence connector directory
python main.py --base-url https://your-confluence.com --token YOUR_TOKEN
```

This creates a `confluence_export` directory with your data.

### 2. Build the Image

```bash
cd elasticsearch_image
./build.sh
```

By default, the script looks for the export in `../confluence_export`. You can override this:

```bash
export CONFLUENCE_EXPORT=/path/to/your/confluence_export
./build.sh
```

The build process:
1. Copies Confluence data into build context
2. Starts Elasticsearch during build
3. Indexes all pages with embeddings
4. Creates final image with data baked in

**Note:** Building can take 10-30 minutes depending on data size.

### 3. Test Locally

```bash
# Start the container
docker run -d --name es-test -p 9200:9200 confluence-elasticsearch:latest

# Wait for startup (30-60 seconds)
docker logs -f es-test

# Verify data
curl http://localhost:9200/confluence_kb/_count

# Test search
curl -X POST http://localhost:9200/confluence_kb/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"content": "your search term"}}, "size": 3}'

# Cleanup when done
docker rm -f es-test
```

### 4. Push to Docker Hub (Optional)

To share the image with your team:

```bash
export DOCKER_USERNAME=your-dockerhub-username
./push.sh
```

The image will be available as `your-username/confluence-elasticsearch:latest`.

## Configuration Options

All configuration is done via environment variables:

### Build Configuration

```bash
# Confluence export location
export CONFLUENCE_EXPORT=/path/to/confluence_export

# Image name and tag
export IMAGE_NAME=confluence-elasticsearch
export TAG=latest

# Then build
./build.sh
```

### Push Configuration

```bash
# Docker Hub credentials
export DOCKER_USERNAME=your-username
export DOCKER_REPOSITORY=confluence-elasticsearch  # Optional, defaults to IMAGE_NAME

# Then push
./push.sh
```

## Integration with Products

### Option 1: Use Pre-built Image (Recommended for Teams)

After pushing to Docker Hub, update your product's `docker-compose.yml`:

```yaml
services:
  elasticsearch:
    image: your-username/confluence-elasticsearch:latest
    container_name: horsch-es-confluence
    ports:
      - "9200:9200"
    environment:
      - ES_JAVA_OPTS=-Xms2g -Xmx2g
    networks:
      - horsch-network
```

### Option 2: Build Locally

Create a symlink from your product to the Confluence export:

```bash
cd products/horsch_confluence_assistant
ln -s /path/to/confluence_export elasticsearch_data
```

Then update `docker-compose.yml` to build locally:

```yaml
services:
  elasticsearch:
    build:
      context: ../../services/connectors/confluence/elasticsearch_image
      dockerfile: Dockerfile
    container_name: horsch-es-confluence
    ports:
      - "9200:9200"
```

### Option 3: Use Empty Elasticsearch and Index at Runtime

See the product's `scripts/index_confluence.sh` for runtime indexing.

## Index Schema

The pre-loaded index (`confluence_kb`) contains:

| Field | Type | Description |
|-------|------|-------------|
| `content` | text | Page content (searchable) |
| `title` | text | Page title |
| `space` | keyword | Confluence space key |
| `page_id` | keyword | Unique page ID |
| `url` | keyword | Pseudo-URL for reference |
| `section` | text | Space/title combination |
| `page` | integer | Chunk number within page |
| `vector` | dense_vector | 384-dim embeddings (all-MiniLM-L6-v2) |
| `indexed_at` | date | Indexing timestamp |

## Search Capabilities

The index supports:

**1. Full-text search (BM25):**
```bash
curl -X POST http://localhost:9200/confluence_kb/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"content": "jira workflow"}}}'
```

**2. Vector similarity search:**
```bash
curl -X POST http://localhost:9200/confluence_kb/_search \
  -H "Content-Type: application/json" \
  -d '{
    "knn": {
      "field": "vector",
      "query_vector": [...],  # 384-dimensional vector
      "k": 10,
      "num_candidates": 50
    }
  }'
```

**3. Hybrid search (recommended):**

Use the DeepResearch API which automatically combines both methods.

## Architecture

```
Build Time:
┌──────────────────┐
│ Confluence Export│
│  (HTML + JSON)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Docker Build     │
│ - Copy data      │
│ - Start ES       │
│ - Index pages    │
│ - Generate       │
│   embeddings     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Final Image      │
│ - Elasticsearch  │
│ - Indexed data   │
│ - Ready to use   │
└──────────────────┘

Runtime:
┌──────────────────┐
│ Start Container  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Elasticsearch    │
│ with pre-loaded  │
│ data available   │
└──────────────────┘
```

## Performance Considerations

### Build Time
- **Small exports** (< 100 pages): 5-10 minutes
- **Medium exports** (100-1000 pages): 10-20 minutes
- **Large exports** (1000+ pages): 20-45 minutes

Factors:
- Number of pages
- Page size
- Embedding generation (CPU-bound)
- Disk I/O

### Image Size
- Base Elasticsearch: ~600 MB
- Python + dependencies: ~1.5 GB
- Your data + embeddings: varies
- **Typical total**: 2-4 GB

### Runtime Performance
- **Startup time**: 30-60 seconds (data already indexed)
- **Search latency**: 10-100ms typical
- **Memory**: 2GB minimum, 4GB recommended

## Troubleshooting

### Build fails with "out of memory"

Increase Docker's memory allocation:
- Docker Desktop → Settings → Resources → Memory → 4GB+

### Build fails during indexing

Check the logs in the build output. Common issues:
- Confluence export missing or corrupted
- HTML files in wrong directory structure
- Insufficient disk space

### Image is too large

The image size depends on your data volume. Options:
1. Use a private registry with good bandwidth
2. Export/import as tar file for local sharing
3. Reduce Confluence export size (exclude old spaces)

### Container won't start

```bash
# Check logs
docker logs <container-name>

# Common issues:
# - Port 9200 already in use
# - Insufficient memory
# - Corrupted data volume
```

### No search results

```bash
# Verify index exists
curl http://localhost:9200/_cat/indices

# Check document count
curl http://localhost:9200/confluence_kb/_count

# Test basic search
curl -X POST http://localhost:9200/confluence_kb/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match_all": {}}, "size": 1}'
```

## File Structure

```
elasticsearch_image/
├── Dockerfile              # Multi-stage build with indexing
├── index_confluence.py     # Python indexer script
├── index_during_build.sh   # Build-time indexing wrapper
├── entrypoint.sh           # Runtime entrypoint
├── build.sh                # Build automation script
├── push.sh                 # Docker Hub push script
└── README.md               # This file
```

## Data Privacy & Security

⚠️ **Important Security Considerations:**

1. **Sensitive Data**: The image contains your Confluence data. Ensure:
   - Use private Docker registry for sensitive content
   - Implement access controls
   - Document data classification

2. **Credentials**: Never include:
   - API tokens in the image
   - Passwords or secrets
   - Personal information

3. **Access Control**: Consider:
   - Private Docker Hub repositories
   - Corporate registry with authentication
   - Network policies in production

## Advanced Usage

### Custom Embedding Model

Edit `Dockerfile` and change the model:

```dockerfile
ENV EMBED_MODEL=sentence-transformers/all-mpnet-base-v2
```

**Note:** Model must match what DeepResearch uses at runtime!

### Custom Index Name

Edit `index_confluence.py`:

```python
INDEX_NAME = os.getenv("ELASTIC_INDEX", "my_custom_index")
```

### Adjust Chunking

Edit `index_confluence.py`:

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Larger chunks
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)
```

### Multi-stage Build for Smaller Image

The current Dockerfile indexes during build for reliability. For a smaller final image, you could:
1. Index in a separate builder stage
2. Export the data directory
3. Import into a fresh ES image

(This is more complex and may have reliability trade-offs)

## Support

For issues:
1. Check logs: `docker logs <container-name>`
2. Verify Confluence export structure
3. Test with small data set first
4. Review Docker resource allocation

## Related Documentation

- [Confluence Connector README](../README.md) - Export Confluence data
- [Horsch Product README](../../../products/horsch_confluence_assistant/README.md) - Full pipeline
- [DeepResearch Service](../../../services/deepresearch/README.md) - RAG system

## License

Part of the Norizon Knowledge Management Platform.
