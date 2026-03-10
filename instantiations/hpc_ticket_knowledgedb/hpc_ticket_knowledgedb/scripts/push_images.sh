#!/bin/bash
# Push Docker images to registry

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
echo "Pushing HPC Knowledge DB Images"
echo "=================================="
echo "Registry: $REGISTRY"
echo "=================================="

# Login to registry if username is provided
if [ -n "$DOCKER_USERNAME" ]; then
    echo ""
    echo "Logging in to Docker registry..."
    docker login -u "$DOCKER_USERNAME"
fi

# Push images
echo ""
echo "Pushing DR API image..."
docker push "${REGISTRY}/hpc-kb-dr-api:${API_TAG}"

echo ""
echo "Pushing Indexer image..."
docker push "${REGISTRY}/hpc-kb-indexer:${INDEXER_TAG}"

echo ""
echo "Images pushed successfully!"
