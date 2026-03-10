#!/bin/bash
# Run DR API locally (without Docker) for easier debugging

set -e  # Exit on error

cd "$(dirname "$0")/.."

echo "Setting up local DR API development environment..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "[!] .env file not found. Copying from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your configuration"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install --upgrade pip > /dev/null
pip install -r api_requirements.txt > /dev/null

echo ""
echo "Dependencies installed successfully!"
echo ""

# Load environment variables
export $(cat .env | grep -v '^#' | xargs)

# Override Elasticsearch URL for local development
# When running locally, connect to Elasticsearch on localhost instead of 'elasticsearch' hostname
export ELASTIC_URL="http://localhost:${ELASTICSEARCH_PORT:-9200}"

echo "Starting HPC DR API locally..."
echo "  LLM Model: ${LLM_MODEL}"
echo "  LLM URL: ${LLM_BASE_URL}"
echo "  Elasticsearch: ${ELASTIC_URL}"
echo "  DR API Port: 8000"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Run the API using uvicorn directly
cd api
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
