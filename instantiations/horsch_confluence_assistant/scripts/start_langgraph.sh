#!/bin/bash

# ====================================================
# HORSCH CONFLUENCE ASSISTANT - START LANGGRAPH
# ====================================================
# Starts LangGraph dev server on port 2024

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
echo -e "${BLUE}Starting LangGraph Studio (Horsch)${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# ----------------------------------------------------
# Load Configuration
# ----------------------------------------------------
ENV_FILE="$PROJECT_DIR/.env"

if [ -f "$ENV_FILE" ]; then
    set -a
    source "$ENV_FILE"
    set +a
fi

LANGGRAPH_PORT="${LANGGRAPH_PORT:-2024}"

# ----------------------------------------------------
# Check Prerequisites
# ----------------------------------------------------
echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check if deepresearch service is installed
DEEPRESEARCH_DIR="$ROOT_DIR/services/deepresearch"

if [ ! -d "$DEEPRESEARCH_DIR" ]; then
    echo -e "${RED}Error: DeepResearch service not found${NC}"
    echo "Expected location: $DEEPRESEARCH_DIR"
    exit 1
fi

# Check if agentic_retrieval module is installed (the actual package name)
if ! python3 -c "import agentic_retrieval" &> /dev/null 2>&1; then
    echo -e "${YELLOW}Warning: agentic_retrieval module not installed${NC}"
    echo "Installing deepresearch package in editable mode..."
    echo ""
    pip3 install -e "$DEEPRESEARCH_DIR"
    echo ""
fi

echo -e "${GREEN}✓ Prerequisites OK${NC}"
echo ""

# ----------------------------------------------------
# Check if langgraph is available
# ----------------------------------------------------
if ! command -v langgraph &> /dev/null; then
    echo -e "${YELLOW}langgraph-cli not found, installing...${NC}"
    pip3 install "langgraph-cli[inmem]"
    echo ""
fi

# ----------------------------------------------------
# Start LangGraph
# ----------------------------------------------------
echo -e "${BLUE}Starting LangGraph dev server on port $LANGGRAPH_PORT...${NC}"
echo ""
echo -e "${YELLOW}Note: This will run in the foreground.${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop.${NC}"
echo ""
echo -e "Access LangGraph Studio at:"
echo -e "  ${GREEN}https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:$LANGGRAPH_PORT${NC}"
echo ""
echo "Starting in 3 seconds..."
sleep 3

cd "$DEEPRESEARCH_DIR"

# Export environment variables for Horsch demo
# Note: Set BOTH naming conventions (ELASTIC_* and ELASTICSEARCH_*)
ES_PORT="${ELASTICSEARCH_PORT:-9200}"
ES_INDEX="${ELASTICSEARCH_INDEX:-confluence_kb}"

# Export demo name for prompt loading
export DEMO_NAME="${DEMO_NAME:-horsch_confluence_assistant}"

export ELASTICSEARCH_HOST="http://localhost:${ES_PORT}"
export ELASTICSEARCH_INDEX="${ES_INDEX}"
export ELASTIC_URL="http://localhost:${ES_PORT}"
export ELASTIC_INDEX="${ES_INDEX}"

export OPENAI_API_KEY="${OPENAI_API_KEY}"
export SUPERVISOR_MODEL="${SUPERVISOR_MODEL:-openai:gpt-4o-mini}"
export RESEARCHER_MODEL="${RESEARCHER_MODEL:-openai:gpt-4o-mini}"
export EMBED_MODEL="${EMBED_MODEL:-sentence-transformers/all-MiniLM-L6-v2}"
export SEARCH_API="${SEARCH_API:-elasticsearch}"

# Print configuration for verification
echo -e "${BLUE}Configuration:${NC}"
echo -e "  Demo: Horsch Confluence Assistant"
echo -e "  Elasticsearch: ${ELASTICSEARCH_HOST}"
echo -e "  Index: ${ELASTICSEARCH_INDEX}"
echo -e "  Port: ${LANGGRAPH_PORT}"
echo -e "  Prompts: products/horsch_confluence_assistant/prompts"
echo ""

# Start LangGraph
# Use langgraph directly (installed in system Python with all dependencies)
exec langgraph dev --allow-blocking --port "$LANGGRAPH_PORT"
