#!/bin/bash
# Create a new customer configuration from templates
#
# Usage:
#   ./scripts/create_customer_config.sh <customer-name> <target-directory>
#


set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

show_usage() {
    echo "Usage: $0 <customer-name> <target-directory>"
    echo ""
    echo "Creates a new customer configuration in the specified directory."
    echo ""
    echo "Arguments:"
    echo "  customer-name      Name of the customer (used in config paths)"
    echo "  target-directory   Directory where the configuration will be created"
    echo ""
    echo "Examples:"
    echo "  $0 fau ~/projects/fau-research"
    echo "  $0 demo-company ./deploy/demo-company"
}

if [ -z "$1" ] || [ -z "$2" ]; then
    show_usage
    exit 1
fi

CUSTOMER="$1"
TARGET_DIR="$2"

# Expand ~ if used
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"

# Convert to absolute path
TARGET_DIR="$(cd "$(dirname "$TARGET_DIR")" 2>/dev/null && pwd)/$(basename "$TARGET_DIR")" || TARGET_DIR="$2"

if [ -d "$TARGET_DIR" ] && [ "$(ls -A "$TARGET_DIR" 2>/dev/null)" ]; then
    echo "Error: Target directory already exists and is not empty: $TARGET_DIR"
    exit 1
fi

echo "Creating customer configuration:"
echo "  Customer: $CUSTOMER"
echo "  Target:   $TARGET_DIR"
echo ""

# Create directory structure
mkdir -p "$TARGET_DIR/prompts"

# Copy templates
cp "$PROJECT_DIR/.env.example" "$TARGET_DIR/.env"
cp "$PROJECT_DIR/agents.example.yaml" "$TARGET_DIR/agents.yaml"
cp -r "$PROJECT_DIR/prompts/"* "$TARGET_DIR/prompts/"

# Copy golden dataset if exists
if [ -f "$PROJECT_DIR/tests/evaluation/golden_answers.yaml" ]; then
    cp "$PROJECT_DIR/tests/evaluation/golden_answers.yaml" "$TARGET_DIR/golden_answers.yaml"
fi

# Update .env with customer-specific paths (use absolute paths for standalone deployment)
sed -i.bak "s|DR_PROMPTS_DIR=prompts|DR_PROMPTS_DIR=$TARGET_DIR/prompts|" "$TARGET_DIR/.env"
sed -i.bak "s|# DR_AGENTS_CONFIG_PATH|DR_AGENTS_CONFIG_PATH=$TARGET_DIR/agents.yaml|" "$TARGET_DIR/.env"
rm -f "$TARGET_DIR/.env.bak"

echo "Created:"
echo "  $TARGET_DIR/"
echo "  ├── .env                 # Environment variables"
echo "  ├── agents.yaml          # Agent configuration"
echo "  ├── prompts/             # LLM prompts"
echo "  │   ├── supervisor.yaml"
echo "  │   ├── elasticsearch_agent.yaml"
echo "  │   └── ..."
echo "  └── golden_answers.yaml  # Evaluation dataset"
echo ""
echo "Next steps:"
echo "  1. Edit $TARGET_DIR/.env with customer-specific settings"
echo "  2. Edit $TARGET_DIR/agents.yaml to configure data sources"
echo "  3. Customize prompts in $TARGET_DIR/prompts/ if needed"
echo "  4. Create customer-specific golden questions in golden_answers.yaml"
echo ""
echo "Run with:"
echo "  source $TARGET_DIR/.env && uvicorn deepsearch.main:app --reload"
