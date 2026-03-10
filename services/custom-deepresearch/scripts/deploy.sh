#!/bin/bash
# Deploy DeepSearch with customer-specific configuration
#
# Usage:
#   ./scripts/deploy.sh customer-a          # Run customer-a config
#   ./scripts/deploy.sh customer-a --docker # Run in Docker
#   ./scripts/deploy.sh --list              # List available configs

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DEPLOY_DIR="$PROJECT_DIR/deploy"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

show_usage() {
    echo "Usage: $0 <customer-name> [options]"
    echo ""
    echo "Options:"
    echo "  --docker    Run in Docker container"
    echo "  --port NUM  Override API port (default from .env or 8000)"
    echo "  --list      List available customer configs"
    echo "  --validate  Validate config without starting"
    echo ""
    echo "Examples:"
    echo "  $0 customer-a                    # Run locally"
    echo "  $0 customer-a --docker           # Run in Docker"
    echo "  $0 customer-a --port 8001        # Custom port"
    echo "  $0 --list                        # List configs"
}

list_configs() {
    echo "Available customer configurations:"
    echo ""
    if [ -d "$DEPLOY_DIR" ]; then
        for dir in "$DEPLOY_DIR"/*/; do
            if [ -f "${dir}.env" ]; then
                customer=$(basename "$dir")
                echo "  - $customer"
                if [ -f "${dir}agents.yaml" ]; then
                    agents=$(grep -E "^\s{2}\w+:" "${dir}agents.yaml" 2>/dev/null | head -5 | sed 's/://g' | tr '\n' ', ')
                    echo "    Agents: ${agents%, }"
                fi
            fi
        done
    else
        echo "  No deploy/ directory found. Run: ./scripts/create_customer_config.sh <name>"
    fi
}

validate_config() {
    local customer=$1
    local config_dir="$DEPLOY_DIR/$customer"

    log_info "Validating configuration for: $customer"

    # Check .env exists
    if [ ! -f "$config_dir/.env" ]; then
        log_error "Missing: $config_dir/.env"
        return 1
    fi
    log_info "Found: .env"

    # Check agents.yaml exists
    if [ ! -f "$config_dir/agents.yaml" ]; then
        log_error "Missing: $config_dir/agents.yaml"
        return 1
    fi
    log_info "Found: agents.yaml"

    # Check prompts dir if specified
    source "$config_dir/.env"
    if [ -n "$DR_PROMPTS_DIR" ] && [ ! -d "$DR_PROMPTS_DIR" ]; then
        # Check relative to project dir
        if [ ! -d "$PROJECT_DIR/$DR_PROMPTS_DIR" ]; then
            log_warn "Prompts directory not found: $DR_PROMPTS_DIR"
        fi
    fi

    # Validate agents.yaml syntax (if pyyaml available)
    if command -v python3 &> /dev/null; then
        python3 -c "import yaml; yaml.safe_load(open('$config_dir/agents.yaml'))" 2>/dev/null
        if [ $? -eq 0 ]; then
            log_info "agents.yaml: valid YAML"
        else
            log_warn "agents.yaml: could not validate (pyyaml not installed)"
        fi
    fi

    log_info "Configuration valid!"
    return 0
}

run_local() {
    local customer=$1
    local port=$2
    local config_dir="$DEPLOY_DIR/$customer"

    log_info "Starting DeepSearch for: $customer"
    log_info "Config: $config_dir"

    # Source environment
    set -a
    source "$config_dir/.env"
    set +a

    # Override port if specified
    if [ -n "$port" ]; then
        export DR_API_PORT=$port
    fi

    # Set config paths relative to project
    export DR_AGENTS_CONFIG_PATH="$config_dir/agents.yaml"

    # Use customer prompts if they exist, otherwise default
    if [ -d "$config_dir/prompts" ]; then
        export DR_PROMPTS_DIR="$config_dir/prompts"
    fi

    log_info "LLM Provider: $DR_LLM_PROVIDER"
    log_info "LLM Model: $DR_LLM_MODEL"
    log_info "Agents Config: $DR_AGENTS_CONFIG_PATH"
    log_info "Prompts Dir: ${DR_PROMPTS_DIR:-prompts}"
    log_info "Port: ${DR_API_PORT:-8000}"

    cd "$PROJECT_DIR"

    # Run uvicorn
    exec uvicorn deepsearch.main:app \
        --host "${DR_API_HOST:-0.0.0.0}" \
        --port "${DR_API_PORT:-8000}" \
        --reload
}

run_docker() {
    local customer=$1
    local port=$2
    local config_dir="$DEPLOY_DIR/$customer"

    log_info "Starting DeepSearch in Docker for: $customer"

    cd "$PROJECT_DIR"

    # Build if needed
    docker-compose build

    # Run with customer config
    docker-compose \
        --env-file "$config_dir/.env" \
        -p "deepsearch-$customer" \
        up -d

    log_info "Container started: deepsearch-$customer"
    log_info "Logs: docker-compose -p deepsearch-$customer logs -f"
}

# Parse arguments
CUSTOMER=""
USE_DOCKER=false
PORT=""
VALIDATE_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --docker)
            USE_DOCKER=true
            shift
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        --list)
            list_configs
            exit 0
            ;;
        --validate)
            VALIDATE_ONLY=true
            shift
            ;;
        --help|-h)
            show_usage
            exit 0
            ;;
        -*)
            log_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
        *)
            CUSTOMER="$1"
            shift
            ;;
    esac
done

# Check customer specified
if [ -z "$CUSTOMER" ]; then
    log_error "Customer name required"
    show_usage
    exit 1
fi

# Check config exists
CONFIG_DIR="$DEPLOY_DIR/$CUSTOMER"
if [ ! -d "$CONFIG_DIR" ]; then
    log_error "Customer config not found: $CONFIG_DIR"
    log_info "Create it with: ./scripts/create_customer_config.sh $CUSTOMER"
    exit 1
fi

# Validate
if ! validate_config "$CUSTOMER"; then
    exit 1
fi

if [ "$VALIDATE_ONLY" = true ]; then
    exit 0
fi

# Run
if [ "$USE_DOCKER" = true ]; then
    run_docker "$CUSTOMER" "$PORT"
else
    run_local "$CUSTOMER" "$PORT"
fi
