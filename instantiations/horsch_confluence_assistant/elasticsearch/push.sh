#!/bin/bash

# ====================================================
# Push Confluence Elasticsearch Image to Docker Hub
# ====================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Push to Docker Hub${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

# Get configuration from environment or prompt
LOCAL_IMAGE="${IMAGE_NAME:-confluence-elasticsearch}"
LOCAL_TAG="${TAG:-latest}"

if [ -z "$DOCKER_USERNAME" ]; then
    echo -e "${YELLOW}Docker Hub username not set${NC}"
    read -p "Enter your Docker Hub username: " DOCKER_USERNAME
fi

if [ -z "$DOCKER_REPOSITORY" ]; then
    DOCKER_REPOSITORY="$LOCAL_IMAGE"
fi

REMOTE_IMAGE="${DOCKER_USERNAME}/${DOCKER_REPOSITORY}"

echo ""
echo "Configuration:"
echo "  Local image:  ${LOCAL_IMAGE}:${LOCAL_TAG}"
echo "  Remote image: ${REMOTE_IMAGE}:${LOCAL_TAG}"
echo ""

# ----------------------------------------------------
# Check if Image Exists
# ----------------------------------------------------

if ! docker images "${LOCAL_IMAGE}:${LOCAL_TAG}" --format "{{.Repository}}" | grep -q "^${LOCAL_IMAGE}$"; then
    echo -e "${RED}Error: Local image not found: ${LOCAL_IMAGE}:${LOCAL_TAG}${NC}"
    echo ""
    echo "Please build the image first:"
    echo "  ./build.sh"
    exit 1
fi

IMAGE_SIZE=$(docker images "${LOCAL_IMAGE}:${LOCAL_TAG}" --format "{{.Size}}")
echo -e "${GREEN}✓ Found local image (size: ${IMAGE_SIZE})${NC}"
echo ""

# ----------------------------------------------------
# Docker Login
# ----------------------------------------------------

echo -e "${YELLOW}Logging in to Docker Hub...${NC}"

if ! docker login; then
    echo -e "${RED}Error: Docker login failed${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Logged in${NC}"
echo ""

# ----------------------------------------------------
# Tag Image
# ----------------------------------------------------

echo -e "${YELLOW}Tagging image...${NC}"
docker tag "${LOCAL_IMAGE}:${LOCAL_TAG}" "${REMOTE_IMAGE}:${LOCAL_TAG}"
docker tag "${LOCAL_IMAGE}:${LOCAL_TAG}" "${REMOTE_IMAGE}:latest"
echo -e "${GREEN}✓ Tagged as ${REMOTE_IMAGE}:${LOCAL_TAG}${NC}"
echo -e "${GREEN}✓ Tagged as ${REMOTE_IMAGE}:latest${NC}"
echo ""

# ----------------------------------------------------
# Push Image
# ----------------------------------------------------

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Pushing to Docker Hub${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "This may take several minutes depending on image size..."
echo ""

# Push both tags
docker push "${REMOTE_IMAGE}:${LOCAL_TAG}"
docker push "${REMOTE_IMAGE}:latest"

PUSH_EXIT=$?

echo ""

# ----------------------------------------------------
# Report Results
# ----------------------------------------------------

if [ $PUSH_EXIT -eq 0 ]; then
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✓ Push Successful!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo "Image pushed to Docker Hub:"
    echo "  ${REMOTE_IMAGE}:${LOCAL_TAG}"
    echo "  ${REMOTE_IMAGE}:latest"
    echo ""
    echo "Others can now pull your image:"
    echo "  docker pull ${REMOTE_IMAGE}:latest"
    echo ""
    echo "Update docker-compose.yml to use the remote image:"
    echo ""
    echo "  elasticsearch:"
    echo "    image: ${REMOTE_IMAGE}:latest"
    echo ""
    echo "Docker Hub URL:"
    echo "  https://hub.docker.com/r/${REMOTE_IMAGE}"
    echo ""
else
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}❌ Push Failed${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo "Check the error messages above for details"
    exit 1
fi
