#!/bin/bash
set -e

# Configuration
DOCKER_USERNAME="omarkh98"
IMAGE_PREFIX="nora"
VERSION="${1:-latest}"
PLATFORM="linux/amd64"

echo "======================================"
echo "Building Norizon Research (Nora)"
echo "======================================"
echo "Docker Hub: ${DOCKER_USERNAME}"
echo "Image Prefix: ${IMAGE_PREFIX}"
echo "Version: ${VERSION}"
echo "Platform: ${PLATFORM}"
echo "======================================"

# Login to Docker Hub (if not already logged in)
echo ""
echo "Checking Docker Hub login..."
if ! docker info | grep -q "Username: ${DOCKER_USERNAME}"; then
    echo "Please login to Docker Hub:"
    docker login
fi

# Build Frontend
echo ""
echo "======================================"
echo "Building Frontend Image"
echo "======================================"
cd frontend
docker buildx build \
    --platform ${PLATFORM} \
    -t ${DOCKER_USERNAME}/${IMAGE_PREFIX}-frontend:${VERSION} \
    -t ${DOCKER_USERNAME}/${IMAGE_PREFIX}-frontend:latest \
    --push \
    .
cd ..

# Build Proxy
echo ""
echo "======================================"
echo "Building Proxy Image"
echo "======================================"
cd proxy
docker buildx build \
    --platform ${PLATFORM} \
    -t ${DOCKER_USERNAME}/${IMAGE_PREFIX}-proxy:${VERSION} \
    -t ${DOCKER_USERNAME}/${IMAGE_PREFIX}-proxy:latest \
    --push \
    .
cd ..

echo ""
echo "======================================"
echo "Build Complete!"
echo "======================================"
echo "Images pushed to Docker Hub:"
echo "  - ${DOCKER_USERNAME}/${IMAGE_PREFIX}-frontend:${VERSION}"
echo "  - ${DOCKER_USERNAME}/${IMAGE_PREFIX}-frontend:latest"
echo "  - ${DOCKER_USERNAME}/${IMAGE_PREFIX}-proxy:${VERSION}"
echo "  - ${DOCKER_USERNAME}/${IMAGE_PREFIX}-proxy:latest"
echo ""
echo "To deploy to Kubernetes:"
echo "  cd k8s"
echo "  ./deploy.sh"
echo "======================================"
