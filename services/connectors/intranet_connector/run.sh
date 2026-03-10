#!/bin/bash
# Run script for Intranet Connector Service
# Provides non-containerized execution with environment setup

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Intranet Connector Service${NC}"

# Check if virtual environment exists and is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo -e "${YELLOW}Warning: No virtual environment detected${NC}"
    echo "Please activate the virtual environment with: source venv/bin/activate"
    exit 1
fi

# Set default environment variables
export CRAWLER_RABBITMQ_URL="${CRAWLER_RABBITMQ_URL:-amqp://test_user:test_pass@localhost:5672/}"
export CRAWLER_INPUT_QUEUE="${CRAWLER_INPUT_QUEUE:-crawl.requested}"
export CRAWLER_OUTPUT_QUEUE="${CRAWLER_OUTPUT_QUEUE:-content.raw.received}"
export CRAWLER_STRATEGY="${CRAWLER_STRATEGY:-bfs}"
export CRAWLER_MAX_PAGES="${CRAWLER_MAX_PAGES:-20}"
export CRAWLER_MAX_DEPTH="${CRAWLER_MAX_DEPTH:-2}"
export CRAWLER_USE_PLAYWRIGHT="${CRAWLER_USE_PLAYWRIGHT:-false}"
export CRAWLER_EXCLUDE_EXTERNAL_LINKS="${CRAWLER_EXCLUDE_EXTERNAL_LINKS:-true}"
export CRAWLER_EXCLUDE_SOCIAL_MEDIA_LINKS="${CRAWLER_EXCLUDE_SOCIAL_MEDIA_LINKS:-true}"
export PYTHONUNBUFFERED=1

# Check if Docker services are running
echo -e "${YELLOW}Checking Docker services...${NC}"
if ! docker-compose ps | grep -q "rabbitmq.*Up"; then
    echo -e "${RED}RabbitMQ service not running. Please start with: docker-compose up -d${NC}"
    exit 1
fi

if ! docker-compose ps | grep -q "elasticsearch.*Up"; then
    echo -e "${RED}Elasticsearch service not running. Please start with: docker-compose up -d${NC}"
    exit 1
fi

echo -e "${GREEN}Docker services are running${NC}"

# Determine which service to run
SERVICE_MODE="${1:-full}"

case $SERVICE_MODE in
    "listener")
        echo -e "${GREEN}Starting Job Listener only...${NC}"
        python src/job_listener.py
        ;;
    "full")
        echo -e "${GREEN}Starting Full FastAPI Service...${NC}"
        python src/service.py
        ;;
    "crawler")
        echo -e "${GREEN}Running Crawler test...${NC}"
        python src/crawler.py
        ;;
    *)
        echo -e "${RED}Usage: $0 [listener|full|crawler]${NC}"
        echo "  listener - Start job listener only"
        echo "  full     - Start complete FastAPI service (default)"
        echo "  crawler  - Run crawler test with mock publisher"
        exit 1
        ;;
esac