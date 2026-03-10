#!/bin/bash
set -e

echo "========================================"
echo "Rebuilding FAU Website Elasticsearch Image"
echo "========================================"

# Set absolute paths to the markdown directories
export MARKDOWN_DIR_1="/Users/lisaschmidt/Documents/GitHub/rag-server/services/connectors/website_connector/fau_docsmd"
export MARKDOWN_DIR_2="/Users/lisaschmidt/Documents/GitHub/rag-server/services/connectors/website_connector/lme_docsmd"
export WEBSITE_BASE_URL="https://www.fau.de"

echo "Markdown directories:"
echo "  DIR 1: $MARKDOWN_DIR_1"
echo "  DIR 2: $MARKDOWN_DIR_2"
echo ""

# Count markdown files
FAU_COUNT=$(find "$MARKDOWN_DIR_1" -name "*.md" 2>/dev/null | wc -l)
LME_COUNT=$(find "$MARKDOWN_DIR_2" -name "*.md" 2>/dev/null | wc -l)
TOTAL_COUNT=$((FAU_COUNT + LME_COUNT))

echo "Found markdown files:"
echo "  FAU: $FAU_COUNT files"
echo "  LME: $LME_COUNT files"
echo "  Total: $TOTAL_COUNT files"
echo ""

read -p "Continue with build? [y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Build cancelled"
    exit 0
fi

# Run the build script
./build.sh

echo ""
echo "Build complete! Next steps:"
echo "  1. Test: docker run -d --name es-test -p 9200:9200 fau-website-elasticsearch:latest"
echo "  2. Verify: curl http://localhost:9200/website_kb/_count"
echo "  3. Cleanup: docker rm -f es-test"
echo "  4. Push: export DOCKER_USERNAME=your-username && ./push.sh"
