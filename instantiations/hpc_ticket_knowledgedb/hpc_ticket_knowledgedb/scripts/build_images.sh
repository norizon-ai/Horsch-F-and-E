#!/bin/bash
# Build and push Docker images for HPC Knowledge Database

set -e

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Configuration
REGISTRY="${DOCKER_REGISTRY:-lisarebecca}"
API_TAG="${DR_API_IMAGE_TAG:-latest}"
INDEXER_TAG="${INDEXER_IMAGE_TAG:-latest}"

echo "=================================="
echo "Building HPC Knowledge DB Images"
echo "=================================="
echo "Registry: $REGISTRY"
echo "API Tag: $API_TAG"
echo "Indexer Tag: $INDEXER_TAG"
echo "=================================="

# Build API image
echo ""
echo "Building DR API image..."
docker build -f Dockerfile.api -t "${REGISTRY}/hpc-kb-dr-api:${API_TAG}" .

# Build Indexer image
echo ""
echo "Building Indexer image..."
docker build -f Dockerfile.indexer -t "${REGISTRY}/hpc-kb-indexer:${INDEXER_TAG}" .

echo ""
echo "Images built successfully!"
echo ""
echo "To push images to registry:"
echo "  docker push ${REGISTRY}/hpc-kb-dr-api:${API_TAG}"
echo "  docker push ${REGISTRY}/hpc-kb-indexer:${INDEXER_TAG}"
echo ""
echo "Or run: ./scripts/push_images.sh"
