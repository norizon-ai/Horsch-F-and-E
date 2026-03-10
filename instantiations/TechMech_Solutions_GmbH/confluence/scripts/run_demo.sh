#!/bin/bash

# ====================================================
# DEMO CONFLUENCE ASSISTANT - RUN DEMO
# ====================================================
# Master script to start the complete demo workflow:
# 1. Start Elasticsearch
# 2. Index demo data
# 3. Start DeepResearch API
# 4. Optionally start LangGraph

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo ""
echo -e "${CYAN}${BOLD}╔════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}${BOLD}║  DEMO CONFLUENCE ASSISTANT - TRADE FAIR   ║${NC}"
echo -e "${CYAN}${BOLD}║      TechMech Solutions Synthetic Data     ║${NC}"
echo -e "${CYAN}${BOLD}╚════════════════════════════════════════════╝${NC}"
echo ""

# ----------------------------------------------------
# Run Setup if Needed
# ----------------------------------------------------
if [ ! -f "$PROJECT_DIR/.env" ]; then
    echo -e "${YELLOW}No .env file found. Running setup first...${NC}"
    echo ""
    "$SCRIPT_DIR/check_system_requirements.sh"
    echo ""
fi

# Load configuration
set -a
source "$PROJECT_DIR/.env"
set +a

# Get ports
ES_PORT="${ELASTICSEARCH_PORT:-9200}"
API_PORT="${DEEPRESEARCH_PORT:-8001}"
LANGGRAPH_PORT="${LANGGRAPH_PORT:-2025}"

echo -e "${BLUE}📋 Configuration${NC}"
echo -e "   Elasticsearch: ${BOLD}http://localhost:$ES_PORT${NC}"
echo -e "   DeepResearch API: ${BOLD}http://localhost:$API_PORT${NC}"
echo -e "   LangGraph: ${BOLD}http://localhost:$LANGGRAPH_PORT${NC}"
echo ""

# ----------------------------------------------------
# Step 1: Start Elasticsearch
# ----------------------------------------------------
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}Step 1/5: Starting Elasticsearch${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

cd "$PROJECT_DIR"

# Check if already running
if docker compose ps elasticsearch | grep -q "Up"; then
    echo -e "${GREEN}✓ Elasticsearch is already running${NC}"
else
    echo "Starting Elasticsearch container..."
    docker compose up -d elasticsearch

    echo ""
    echo "⏳ Waiting for Elasticsearch to be healthy..."

    # Wait up to 60 seconds for Elasticsearch
    for i in {1..60}; do
        if curl -s -f "http://localhost:$ES_PORT/_cluster/health" > /dev/null 2>&1; then
            echo -e "${GREEN}✓ Elasticsearch is healthy${NC}"
            break
        fi
        if [ $i -eq 60 ]; then
            echo -e "${RED}❌ Elasticsearch failed to start${NC}"
            echo "Check logs with: docker compose logs elasticsearch"
            exit 1
        fi
        echo -n "."
        sleep 1
    done
fi

echo ""

# ----------------------------------------------------
# Step 2: Check for Indexed Data
# ----------------------------------------------------
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}Step 2/5: Checking Indexed Data${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

INDEX_NAME="${ELASTICSEARCH_INDEX:-demo_confluence_kb}"
ES_URL="http://localhost:$ES_PORT"

if curl -s -f "$ES_URL/$INDEX_NAME/_count" > /dev/null 2>&1; then
    DOC_COUNT=$(curl -s "$ES_URL/$INDEX_NAME/_count" | grep -o '"count":[0-9]*' | cut -d':' -f2)
    echo -e "${GREEN}✓ Index '$INDEX_NAME' exists with $DOC_COUNT documents${NC}"

    if [ "$DOC_COUNT" -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Index is empty, will run indexing...${NC}"
        NEED_INDEXING=true
    else
        echo ""
        read -p "Do you want to re-index the data? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            NEED_INDEXING=true
        else
            NEED_INDEXING=false
        fi
    fi
else
    echo -e "${YELLOW}Index '$INDEX_NAME' does not exist yet${NC}"
    NEED_INDEXING=true
fi

echo ""

# ----------------------------------------------------
# Step 3: Index Data (if needed)
# ----------------------------------------------------
if [ "$NEED_INDEXING" = true ]; then
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Step 3/5: Indexing Demo Data${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    "$SCRIPT_DIR/index_confluence.sh"

    echo ""
else
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Step 3/5: Skipping Indexing${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${GREEN}✓ Using existing indexed data${NC}"
    echo ""
fi

# ----------------------------------------------------
# Step 4: Start DeepResearch API
# ----------------------------------------------------
# echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
# echo -e "${YELLOW}Step 4/5: Starting DeepResearch API${NC}"
# echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
# echo ""

cd "$PROJECT_DIR"

# Check if already running
if docker compose ps deepresearch-api | grep -q "Up"; then
    echo -e "${GREEN}✓ DeepResearch API is already running${NC}"
else
    echo "Starting DeepResearch API container..."
    docker compose up -d deepresearch-api

    echo ""
    echo "⏳ Waiting for API to be ready..."

    # Wait up to 60 seconds for API
    for i in {1..60}; do
        if curl -s -f "http://localhost:$API_PORT/health" > /dev/null 2>&1; then
            echo -e "${GREEN}✓ DeepResearch API is ready${NC}"
            break
        fi
        if [ $i -eq 60 ]; then
            echo -e "${RED}❌ API failed to start${NC}"
            echo "Check logs with: docker compose logs deepresearch-api"
            exit 1
        fi
        echo -n "."
        sleep 1
    done
fi

# echo ""

# ----------------------------------------------------
# Step 5: LangGraph (Optional)
# ----------------------------------------------------
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}Step 5/5: LangGraph Studio (Optional)${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

read -p "Do you want to start LangGraph Studio? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    if [ -f "$SCRIPT_DIR/start_langgraph.sh" ]; then
        "$SCRIPT_DIR/start_langgraph.sh"
    else
        echo -e "${YELLOW}⚠️  start_langgraph.sh not found, skipping${NC}"
    fi
else
    echo -e "${BLUE}ℹ️  Skipping LangGraph Studio${NC}"
    echo "   You can start it later with: ./scripts/start_langgraph.sh"
fi

echo ""

# ----------------------------------------------------
# Success Summary
# ----------------------------------------------------
echo ""
echo -e "${GREEN}${BOLD}╔════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}${BOLD}║          🎉 DEMO IS READY! 🎉             ║${NC}"
echo -e "${GREEN}${BOLD}╚════════════════════════════════════════════╝${NC}"
echo ""

echo -e "${CYAN}📡 Access Points:${NC}"
echo ""
echo -e "  ${BOLD}Elasticsearch:${NC}"
echo -e "    http://localhost:$ES_PORT"
echo ""
echo -e "  ${BOLD}DeepResearch API:${NC}"
echo -e "    http://localhost:$API_PORT/docs"
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "  ${BOLD}LangGraph Studio:${NC}"
    echo -e "    http://127.0.0.1:$LANGGRAPH_PORT"
    echo ""
fi

echo -e "${CYAN}🧪 Try a Test Query:${NC}"
echo ""
echo -e "${BLUE}curl -X POST http://localhost:$API_PORT/query/sync \\${NC}"
echo -e "${BLUE}  -H 'Content-Type: application/json' \\${NC}"
echo -e "${BLUE}  -d '{\"question\": \"What are the main features of the RC-3000 robot cell?\"}' \\${NC}"
echo -e "${BLUE}  | jq -r '.report' | head -50${NC}"
echo ""

echo -e "${CYAN}📊 View Service Status:${NC}"
echo -e "  docker compose ps"
echo ""

echo -e "${CYAN}📝 View Logs:${NC}"
echo -e "  docker compose logs -f deepresearch-api"
echo ""

echo -e "${CYAN}🛑 Stop Demo:${NC}"
echo -e "  ./scripts/stop_demo.sh"
echo ""

echo -e "${GREEN}Ready for your trade fair presentation! 🚀${NC}"
echo ""
