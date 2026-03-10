#!/usr/bin/env bash
# =============================================================================
# Norizon Internal Dogfooding — start script
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "================================================"
echo "  Norizon Internal Setup"
echo "================================================"
echo ""

# ---------------------------------------------------------------------------
# Check required env files
# ---------------------------------------------------------------------------
MISSING=0

for envfile in atlassian.env deepsearch.env workflow.env; do
  if [ ! -f "$envfile" ]; then
    echo -e "${RED}Missing:${NC} $envfile"
    MISSING=1
  else
    echo -e "${GREEN}Found:${NC}   $envfile"
  fi
done

if [ "$MISSING" -eq 1 ]; then
  echo ""
  echo -e "${RED}Please create the missing env file(s) before starting.${NC}"
  echo "See README.md for the required variables."
  exit 1
fi

# ---------------------------------------------------------------------------
# Check Microsoft Teams config (optional)
# ---------------------------------------------------------------------------
echo ""
if grep -q 'WORKFLOW_MS_CLIENT_ID=.' workflow.env 2>/dev/null; then
  echo -e "${GREEN}Microsoft Teams:${NC} configured"
else
  echo -e "${YELLOW}Microsoft Teams:${NC} not configured (Teams import will be disabled)"
  echo "  Fill in WORKFLOW_MS_* values in workflow.env to enable."
fi

# ---------------------------------------------------------------------------
# Start
# ---------------------------------------------------------------------------
echo ""
echo "Starting services..."
echo ""

docker compose up --build "$@"
