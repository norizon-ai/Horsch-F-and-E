# Elasticsearch Image Builder - Template

This directory contains template files for building pre-loaded Elasticsearch images for new products.

## Overview

When creating a new product that needs Elasticsearch with pre-indexed data, you can:

1. Copy these template files to your product's build directory
2. Customize them for your specific data sources
3. Build your Elasticsearch image with baked-in data
4. Deploy your product with the pre-loaded image

## Example Structure

For a product at `products/my_product/`:

```
products/my_product/
├── docker-compose.yml
├── build/
│   ├── index_website.py       # Customize this indexer
│   ├── requirements.txt       # Add dependencies
│   └── elasticsearch/         # ES image builder
│       ├── Dockerfile
│       ├── build.sh
│       ├── push.sh
│       └── rebuild.sh
└── deploy/
    └── terraform/
```

## Quick Start

### 1. Copy Templates to Your Product

```bash
# From repository root
cp -r services/connectors/website_connector/examples/elasticsearch_build/ \
  products/my_product/build/elasticsearch/

cp services/connectors/website_connector/examples/index_website.py.example \
  products/my_product/build/index_website.py
```

### 2. Customize the Indexer

Edit `products/my_product/build/index_website.py`:

```python
# Set your data directories
MARKDOWN_DIRS = [
    os.getenv("MARKDOWN_DIR_1", "/path/to/your/data"),
    os.getenv("MARKDOWN_DIR_2", "/path/to/more/data"),
]

# Set your index name
INDEX_NAME = os.getenv("ELASTIC_INDEX", "my_product_kb")

# Customize the parser for your data format
class MyDataParser:
    def parse_file(self, file_path: Path):
        # Your custom parsing logic
        pass
```

### 3. Update Build Script

Edit `products/my_product/build/elasticsearch/build.sh`:

```bash
# Set your data directories
export MARKDOWN_DIR_1="/path/to/your/data"
export MARKDOWN_DIR_2="/path/to/more/data"
export ELASTIC_INDEX="my_product_kb"
```

### 4. Build the Image

```bash
cd products/my_product/build/elasticsearch
./build.sh
```

This will:
- Start temporary Elasticsearch
- Run your indexer to load data
- Export the data directory
- Build a Docker image with data baked in

### 5. Test the Image

```bash
docker run -d --name es-test -p 9200:9200 my-product-elasticsearch:latest
curl http://localhost:9200/my_product_kb/_count
docker rm -f es-test
```

### 6. Push to Docker Hub (Optional)

```bash
export DOCKER_USERNAME=your-username
./push.sh
```

### 7. Update docker-compose.yml

```yaml
services:
  elasticsearch:
    image: your-username/my-product-elasticsearch:latest
    # or build locally:
    # build:
    #   context: build/elasticsearch
    #   dockerfile: Dockerfile
```

## Template Files

### Dockerfile.example

Creates an Elasticsearch image with pre-loaded data. The data is copied into the image during build.

**Key customizations**:
- Elasticsearch version
- Memory settings
- Index settings

### build.sh.example

Orchestrates the build process:
1. Starts temporary ES
2. Indexes your data
3. Exports ES data directory
4. Builds final Docker image

**Key customizations**:
- Data directory paths
- Index name
- Elasticsearch version
- Image name

### index_website.py.example

Generic indexer for markdown/HTML files. Supports:
- Multiple data directories
- Chunking and embeddings
- Hybrid search (vector + BM25)

**Key customizations**:
- Data parser (parse_file method)
- Chunk size and overlap
- Metadata extraction
- URL/source generation

### push.sh.example

Pushes your built image to Docker Hub.

**Key customizations**:
- Image name
- Docker Hub username

## Real-World Example

See `products/fau_website_deepresearch/` for one complete working implementation:

```bash
products/fau_website_deepresearch/
├── build/
│   ├── index_website.py      # Customized for website data
│   ├── requirements.txt
│   └── elasticsearch/
│       ├── Dockerfile
│       ├── build.sh          # Sets data paths
│       ├── push.sh
│       └── rebuild.sh
```

## Tips

### Fast Iteration

During development, use runtime indexing instead of rebuilding images:

```yaml
# docker-compose.yml for development
elasticsearch:
  image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
  # Don't use pre-built image during dev
```

Then run indexer directly:
```bash
python build/index_website.py
```

Once stable, build the image for production.

### Large Datasets

For very large datasets (> 100k documents):
- Build on a machine with plenty of RAM (16GB+)
- Consider building in cloud CI/CD
- Use multi-stage Docker builds to keep final image smaller

### Index Strategies

The indexer supports different strategies:

```bash
# RESET: Delete and recreate index (default for image builds)
export INDEX_STRATEGY=RESET

# APPEND: Add to existing index (useful for incremental updates)
export INDEX_STRATEGY=APPEND
```

For pre-built images, always use RESET to ensure clean state.

## Troubleshooting

### Build Takes Too Long

- Reduce chunk size to process fewer chunks
- Use smaller embedding models
- Build on a faster machine

### Out of Memory

- Reduce `ES_JAVA_OPTS` memory settings
- Process data in smaller batches
- Close other applications during build

### Image Too Large

- Use Docker multi-stage builds
- Compress data before copying
- Consider storing only frequently-accessed data in image

## Support

For questions or issues:
1. Check existing product implementations (e.g., `products/fau_website_deepresearch/`)
2. Review build logs for errors
3. Test indexing locally before building image
