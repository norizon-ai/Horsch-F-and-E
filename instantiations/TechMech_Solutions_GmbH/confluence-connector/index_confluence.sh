#!/bin/bash

# ====================================================
# DEMO CONFLUENCE ASSISTANT - INDEX DATA
# ====================================================
# Indexes the generated markdown files into Elasticsearch

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Demo Confluence Assistant - Indexing${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Load Configuration
# ----------------------------------------------------
ENV_FILE="$PROJECT_DIR/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo -e "${RED}Error: .env file not found${NC}"
    echo "Please run ./scripts/check_system_requirements.sh first"
    exit 1
fi

# Source the .env file
set -a
source "$ENV_FILE"
set +a

# ----------------------------------------------------
# Check Data Directory
# ----------------------------------------------------
DATA_DIR="$PROJECT_DIR/${CONFLUENCE_DATA_DIR:-./generated_confluence}"

if [ ! -d "$DATA_DIR" ]; then
    echo -e "${RED}Error: Data directory not found: $DATA_DIR${NC}"
    echo ""
    echo "Please generate the demo data first:"
    echo "  cd $PROJECT_DIR"
    echo "  python3 generate_confluence.py --api-key YOUR_KEY"
    exit 1
fi

# Count markdown files
MD_COUNT=$(find "$DATA_DIR" -name "*.md" | wc -l | tr -d ' ')
echo -e "Found ${GREEN}$MD_COUNT${NC} markdown files to index"

if [ "$MD_COUNT" -eq 0 ]; then
    echo -e "${RED}Error: No markdown files found in $DATA_DIR${NC}"
    exit 1
fi

echo ""

# ----------------------------------------------------
# Check Elasticsearch
# ----------------------------------------------------
echo -e "${YELLOW}Checking Elasticsearch availability...${NC}"

ES_URL="${ELASTICSEARCH_HOST:-http://localhost:${ELASTICSEARCH_PORT:-9200}}"

if ! curl -s -f "$ES_URL/_cluster/health" > /dev/null 2>&1; then
    echo -e "${RED}Error: Elasticsearch is not available at $ES_URL${NC}"
    echo ""
    echo "Please ensure Elasticsearch is running:"
    echo "  docker compose up -d elasticsearch"
    echo ""
    echo "Then wait for it to be healthy:"
    echo "  docker compose ps"
    exit 1
fi

echo -e "${GREEN}✓ Elasticsearch is available at $ES_URL${NC}"
echo ""

# ----------------------------------------------------
# Check Python Dependencies
# ----------------------------------------------------
echo -e "${YELLOW}Checking Python dependencies...${NC}"

REQUIRED_PACKAGES="elasticsearch sentence_transformers yaml dotenv"
MISSING_PACKAGES=""

for package in $REQUIRED_PACKAGES; do
    # Handle package name variations
    py_package=$(echo "$package" | tr '-' '_')
    if ! python3 -c "import $py_package" &> /dev/null 2>&1; then
        # Convert back to pip name
        pip_package=$(echo "$package" | tr '_' '-')
        MISSING_PACKAGES="$MISSING_PACKAGES $pip_package"
    fi
done

if [ -n "$MISSING_PACKAGES" ]; then
    echo -e "${YELLOW}Missing Python packages:$MISSING_PACKAGES${NC}"
    echo ""
    read -p "Do you want to install them now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Installing packages...${NC}"
        pip3 install $MISSING_PACKAGES pyyaml python-dotenv
        echo ""
    else
        echo -e "${RED}Cannot proceed without required packages${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✓ All Python dependencies available${NC}"
echo ""

# ----------------------------------------------------
# Run Indexer
# ----------------------------------------------------
echo -e "${BLUE}Starting indexing process...${NC}"
echo "This may take a few minutes depending on data size"
echo ""

# Export environment variables for the indexer
export ELASTICSEARCH_HOST="$ES_URL"
export ELASTICSEARCH_INDEX="${ELASTICSEARCH_INDEX:-demo_confluence_kb}"
export EMBED_MODEL="${EMBED_MODEL:-sentence-transformers/all-MiniLM-L6-v2}"
export CONFLUENCE_DATA_DIR="$DATA_DIR"

# Run the Python indexer
python3 "$SCRIPT_DIR/index_markdown.py"

INDEXER_EXIT_CODE=$?

if [ $INDEXER_EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✅ Indexing Complete!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "You can now query the system:"
    echo ""
    echo -e "${BLUE}1. Start the DeepResearch API:${NC}"
    echo "   docker compose up -d deepresearch-api"
    echo ""
    echo -e "${BLUE}2. Test with a query:${NC}"
    echo "   curl -X POST http://localhost:${DEEPRESEARCH_PORT:-8001}/query/sync \\"
    echo "     -H 'Content-Type: application/json' \\"
    echo "     -d '{\"question\": \"What are the main features of the RC-3000 robot cell?\"}'"
    echo ""
    echo -e "${BLUE}3. Access API documentation:${NC}"
    echo "   http://localhost:${DEEPRESEARCH_PORT:-8001}/docs"
    echo ""
else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}❌ Indexing Failed${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo "Please check the error messages above and try again."
    exit 1
fi
