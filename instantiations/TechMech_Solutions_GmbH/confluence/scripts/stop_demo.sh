#!/bin/bash

# ====================================================
# DEMO CONFLUENCE ASSISTANT - STOP DEMO
# ====================================================
# Stops all demo services

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
echo -e "${BLUE}Stopping Demo Confluence Assistant${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

cd "$PROJECT_DIR"

# ----------------------------------------------------
# Stop Docker Services
# ----------------------------------------------------
echo -e "${YELLOW}Stopping Docker services...${NC}"
docker compose down

echo -e "${GREEN}✓ All services stopped${NC}"
echo ""

# ----------------------------------------------------
# Optional: Clear Data
# ----------------------------------------------------
echo -e "${YELLOW}Do you want to clear the indexed data? (y/n)${NC}"
read -p "This will delete the Elasticsearch volume: " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Removing volumes...${NC}"
    docker compose down -v
    echo -e "${GREEN}✓ Data cleared${NC}"
else
    echo -e "${BLUE}ℹ️  Data preserved (will be available on next start)${NC}"
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Demo stopped successfully${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "To start again, run:"
echo "  ./scripts/run_demo.sh"
echo ""
