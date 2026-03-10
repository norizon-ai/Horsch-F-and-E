#!/bin/bash

# ====================================================
# Build Elasticsearch Image with Pre-loaded Confluence Data
# ====================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Confluence Elasticsearch Image Builder${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

# Default values
DEFAULT_CONFLUENCE_EXPORT="../confluence_export"
DEFAULT_IMAGE_NAME="confluence-elasticsearch"
DEFAULT_TAG="latest"

# Get configuration from environment or use defaults
CONFLUENCE_EXPORT="${CONFLUENCE_EXPORT:-$DEFAULT_CONFLUENCE_EXPORT}"
IMAGE_NAME="${IMAGE_NAME:-$DEFAULT_IMAGE_NAME}"
TAG="${TAG:-$DEFAULT_TAG}"

# ----------------------------------------------------
# Check Confluence Export
# ----------------------------------------------------

echo -e "${YELLOW}Checking Confluence export...${NC}"

if [ ! -d "$CONFLUENCE_EXPORT" ]; then
    echo -e "${RED}Error: Confluence export not found at: $CONFLUENCE_EXPORT${NC}"
    echo ""
    echo "Please provide the path to your Confluence export directory:"
    echo ""
    echo "Option 1: Set environment variable"
    echo "  export CONFLUENCE_EXPORT=/path/to/confluence_export"
    echo "  ./build.sh"
    echo ""
    echo "Option 2: Create symlink"
    echo "  ln -s /path/to/confluence_export ../confluence_export"
    echo "  ./build.sh"
    echo ""
    exit 1
fi

# Check if export has required structure
if [ ! -d "$CONFLUENCE_EXPORT/spaces" ]; then
    echo -e "${RED}Error: No 'spaces' directory found in $CONFLUENCE_EXPORT${NC}"
    echo "Please ensure you have a valid Confluence export"
    exit 1
fi

# Count HTML files
HTML_COUNT=$(find "$CONFLUENCE_EXPORT/spaces" -name "*.html" 2>/dev/null | wc -l | tr -d ' ')

if [ "$HTML_COUNT" -eq 0 ]; then
    echo -e "${RED}Error: No HTML files found in Confluence export${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Found Confluence export with $HTML_COUNT HTML files${NC}"
echo ""

# ----------------------------------------------------
# Prepare Build Context
# ----------------------------------------------------

echo -e "${YELLOW}Preparing build context...${NC}"

BUILD_DIR="build_context"

# Clean previous build
if [ -d "$BUILD_DIR" ]; then
    echo "  Cleaning previous build context..."
    rm -rf "$BUILD_DIR"
fi

# Create build context
mkdir -p "$BUILD_DIR"

# Copy Dockerfile and scripts
echo "  Copying Dockerfile and scripts..."
cp Dockerfile "$BUILD_DIR/"
cp index_confluence.py "$BUILD_DIR/"
cp index_during_build.sh "$BUILD_DIR/"
cp entrypoint.sh "$BUILD_DIR/"

# Copy Confluence export
echo "  Copying Confluence export (this may take a moment)..."
cp -r "$CONFLUENCE_EXPORT" "$BUILD_DIR/confluence_export"

echo -e "${GREEN}✓ Build context ready${NC}"
echo ""

# ----------------------------------------------------
# Estimate Image Size
# ----------------------------------------------------

EXPORT_SIZE=$(du -sh "$CONFLUENCE_EXPORT" | awk '{print $1}')
echo -e "${YELLOW}Info: Confluence export size: $EXPORT_SIZE${NC}"
echo "      Final image will be larger due to Elasticsearch and indexed data"
echo ""

# ----------------------------------------------------
# Build Image
# ----------------------------------------------------

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Building Docker Image${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Image: ${GREEN}${IMAGE_NAME}:${TAG}${NC}"
echo ""

# Build with progress
docker build \
    --progress=plain \
    -t "${IMAGE_NAME}:${TAG}" \
    "$BUILD_DIR"

BUILD_EXIT=$?

# ----------------------------------------------------
# Cleanup
# ----------------------------------------------------

echo ""
echo -e "${YELLOW}Cleaning up build context...${NC}"
rm -rf "$BUILD_DIR"
echo -e "${GREEN}✓ Cleanup complete${NC}"

# ----------------------------------------------------
# Report Results
# ----------------------------------------------------

echo ""

if [ $BUILD_EXIT -eq 0 ]; then
    # Get image size
    IMAGE_SIZE=$(docker images "${IMAGE_NAME}:${TAG}" --format "{{.Size}}")

    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✓ Build Successful!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo "Image: ${IMAGE_NAME}:${TAG}"
    echo "Size: ${IMAGE_SIZE}"
    echo "Documents: ${HTML_COUNT} pages"
    echo ""
    echo "Next steps:"
    echo ""
    echo "1. Test locally:"
    echo "   docker run -d --name es-test -p 9200:9200 ${IMAGE_NAME}:${TAG}"
    echo "   curl http://localhost:9200/confluence_kb/_count"
    echo ""
    echo "2. Push to Docker Hub:"
    echo "   export DOCKER_USERNAME=your-dockerhub-username"
    echo "   ./push.sh"
    echo ""
    echo "3. Use in product:"
    echo "   Update docker-compose.yml:"
    echo "   image: your-username/${IMAGE_NAME}:${TAG}"
    echo ""
else
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}❌ Build Failed${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo "Check the error messages above for details"
    exit 1
fi
