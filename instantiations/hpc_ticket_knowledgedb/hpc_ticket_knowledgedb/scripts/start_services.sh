#!/bin/bash
# Start HPC Knowledge Database services

set -e

echo "=================================="
echo "Starting HPC Knowledge DB Services"
echo "=================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "[!] Warning: .env file not found"
    echo "Creating from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your configuration"
fi

# Start core services (elasticsearch and dr-api)
echo ""
echo "Starting Elasticsearch and DR API..."
docker-compose up -d elasticsearch dr-api

echo ""
echo "Waiting for services to be healthy..."
sleep 10

# Check health
echo ""
echo "Checking service health..."

# Check Elasticsearch
if curl -s http://localhost:9200/_cluster/health > /dev/null; then
    echo "  Elasticsearch is healthy"
else
    echo "  [ERROR] Elasticsearch is not responding"
fi

# Check DR API
if curl -s http://localhost:8001/health > /dev/null; then
    echo "  DR API is healthy"
else
    echo "  [!] DR API is not responding yet (may still be starting)"
fi

echo ""
echo "Services started!"
echo ""
echo "Next steps:"
echo "  1. Index data: ./scripts/index_data.sh"
echo "  2. Test API: curl http://localhost:8001/health"
echo "  3. View logs: docker-compose logs -f dr-api"
echo ""
echo "To stop services: docker-compose down"
