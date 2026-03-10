#!/bin/bash

# ====================================================
# HORSCH CONFLUENCE ASSISTANT - INDEX CONFLUENCE DATA
# ====================================================
# This script indexes Confluence export data into Elasticsearch
# Use this if you want to index custom Confluence data instead
# of using the pre-built Docker image.

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
ROOT_DIR="$(dirname "$(dirname "$PROJECT_DIR")")"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Horsch Confluence Assistant - Indexing${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Load Configuration
# ----------------------------------------------------
ENV_FILE="$PROJECT_DIR/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo -e "${RED}Error: .env file not found${NC}"
    echo "Please run ./scripts/setup.sh first"
    exit 1
fi

# Source the .env file
set -a
source "$ENV_FILE"
set +a

# ----------------------------------------------------
# Check Confluence Export Directory
# ----------------------------------------------------
if [ -z "$CONFLUENCE_EXPORT_DIR" ]; then
    echo -e "${YELLOW}CONFLUENCE_EXPORT_DIR not set in .env${NC}"
    echo ""
    read -p "Enter path to your Confluence export directory: " CONFLUENCE_DIR

    if [ ! -d "$CONFLUENCE_DIR" ]; then
        echo -e "${RED}Error: Directory not found: $CONFLUENCE_DIR${NC}"
        exit 1
    fi
else
    CONFLUENCE_DIR="$CONFLUENCE_EXPORT_DIR"
fi

# Expand ~ if present
CONFLUENCE_DIR="${CONFLUENCE_DIR/#\~/$HOME}"

echo -e "Using Confluence export directory: ${BLUE}$CONFLUENCE_DIR${NC}"
echo ""

# Verify directory structure
if [ ! -d "$CONFLUENCE_DIR/spaces" ]; then
    echo -e "${RED}Error: No 'spaces' directory found in $CONFLUENCE_DIR${NC}"
    echo "Please ensure you have a valid Confluence export with the following structure:"
    echo "  $CONFLUENCE_DIR/"
    echo "    └── spaces/"
    echo "        └── SPACE_KEY/"
    echo "            └── pages/"
    echo "                └── *.html"
    exit 1
fi

# Count HTML files
HTML_COUNT=$(find "$CONFLUENCE_DIR/spaces" -name "*.html" | wc -l | tr -d ' ')
echo -e "Found ${GREEN}$HTML_COUNT${NC} HTML files to index"

if [ "$HTML_COUNT" -eq 0 ]; then
    echo -e "${RED}Error: No HTML files found in $CONFLUENCE_DIR/spaces${NC}"
    exit 1
fi

echo ""

# ----------------------------------------------------
# Check Elasticsearch
# ----------------------------------------------------
echo -e "${YELLOW}Checking Elasticsearch availability...${NC}"

ES_URL="${ELASTICSEARCH_HOST:-http://localhost:9200}"

if ! curl -s -f "$ES_URL/_cluster/health" > /dev/null; then
    echo -e "${RED}Error: Elasticsearch is not available at $ES_URL${NC}"
    echo ""
    echo "Please ensure Elasticsearch is running:"
    echo "  docker compose up -d elasticsearch"
    echo ""
    echo "Then wait for it to be healthy:"
    echo "  docker compose ps"
    exit 1
fi

echo -e "${GREEN}✓ Elasticsearch is available${NC}"

# Check if index exists
INDEX_NAME="${ELASTICSEARCH_INDEX:-confluence_kb}"
if curl -s -f "$ES_URL/$INDEX_NAME/_count" > /dev/null 2>&1; then
    DOC_COUNT=$(curl -s "$ES_URL/$INDEX_NAME/_count" | grep -o '"count":[0-9]*' | cut -d':' -f2)
    echo -e "${YELLOW}Warning: Index '$INDEX_NAME' already exists with $DOC_COUNT documents${NC}"
    echo ""
    read -p "Do you want to DELETE and recreate the index? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Deleting existing index...${NC}"
        curl -X DELETE "$ES_URL/$INDEX_NAME" > /dev/null 2>&1
        echo -e "${GREEN}✓ Index deleted${NC}"
    else
        echo -e "${YELLOW}Appending to existing index${NC}"
        export INDEX_STRATEGY="APPEND"
    fi
else
    echo -e "Index '$INDEX_NAME' does not exist yet (will be created)"
    export INDEX_STRATEGY="${INDEX_STRATEGY:-RESET}"
fi

echo ""

# ----------------------------------------------------
# Run Indexing Script
# ----------------------------------------------------
echo -e "${YELLOW}Starting indexing process...${NC}"
echo "This may take several minutes depending on the size of your data"
echo ""

# Path to the indexing script
INDEX_SCRIPT="$ROOT_DIR/services/connectors/confluence/index_confluence.py"

if [ ! -f "$INDEX_SCRIPT" ]; then
    echo -e "${RED}Error: Indexing script not found at $INDEX_SCRIPT${NC}"
    exit 1
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is not installed${NC}"
    echo "Please install Python 3.7+ to run the indexing script"
    exit 1
fi

# Check if required Python packages are installed
REQUIRED_PACKAGES="elasticsearch sentence-transformers beautifulsoup4 html2text langchain-text-splitters python-dotenv"
MISSING_PACKAGES=""

for package in $REQUIRED_PACKAGES; do
    if ! python3 -c "import ${package//-/_}" &> /dev/null; then
        MISSING_PACKAGES="$MISSING_PACKAGES $package"
    fi
done

if [ -n "$MISSING_PACKAGES" ]; then
    echo -e "${YELLOW}Missing Python packages:$MISSING_PACKAGES${NC}"
    echo ""
    read -p "Do you want to install them now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Installing packages...${NC}"
        pip3 install $MISSING_PACKAGES
    else
        echo -e "${RED}Cannot proceed without required packages${NC}"
        exit 1
    fi
fi

echo ""
echo -e "${BLUE}Running indexer...${NC}"
echo ""

# Export environment variables for the indexer
export CONFLUENCE_DIR="$CONFLUENCE_DIR"
export ELASTIC_URL="$ES_URL"
export ELASTIC_INDEX="$INDEX_NAME"
export EMBED_MODEL="${EMBED_MODEL:-sentence-transformers/all-MiniLM-L6-v2}"

# Run the indexer
cd "$(dirname "$INDEX_SCRIPT")"
python3 index_confluence.py

# ----------------------------------------------------
# Verify Indexing
# ----------------------------------------------------
echo ""
echo -e "${YELLOW}Verifying indexed data...${NC}"

FINAL_COUNT=$(curl -s "$ES_URL/$INDEX_NAME/_count" | grep -o '"count":[0-9]*' | cut -d':' -f2)
INDEX_SIZE=$(curl -s "$ES_URL/_cat/indices/$INDEX_NAME?h=store.size" | tr -d ' ')

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Indexing Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "Index: ${BLUE}$INDEX_NAME${NC}"
echo -e "Documents: ${GREEN}$FINAL_COUNT${NC}"
echo -e "Size: ${GREEN}$INDEX_SIZE${NC}"
echo ""
echo -e "You can now query the index using the DeepResearch API:"
echo "  curl -X POST http://localhost:8000/query/sync \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"question\": \"Your question here\"}'"
echo ""
