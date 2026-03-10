#!/bin/bash
# Run DeepSearch with TechMech Solutions GmbH configuration
#
# This script properly exports environment variables and ensures
# the customer config takes precedence over any project-level .env

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="/Users/lisaschmidt/Documents/GitHub/rag-server/services/custom-deepresearch"

echo "Starting DeepSearch for TechMech Solutions GmbH"
echo "Config: $SCRIPT_DIR"
echo ""

# Change to project directory (where deepsearch package lives)
cd "$PROJECT_DIR"

# IMPORTANT: Use set -a to auto-export all variables from .env
# This ensures they override any .env in the project directory
set -a
source "$SCRIPT_DIR/.env"
set +a

# Show which config is being used
echo "LLM Provider: $DR_LLM_PROVIDER"
echo "LLM Model:    $DR_LLM_MODEL"
echo "Prompts:      $DR_PROMPTS_DIR"
echo "Agents:       $DR_AGENTS_CONFIG_PATH"
echo ""

# Run uvicorn
exec uvicorn deepsearch.main:app --reload --host "${DR_API_HOST:-0.0.0.0}" --port "${DR_API_PORT:-8000}"