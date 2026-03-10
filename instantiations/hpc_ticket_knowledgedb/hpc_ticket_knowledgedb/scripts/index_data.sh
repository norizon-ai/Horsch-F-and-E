#!/bin/bash
# Run the indexer to populate Elasticsearch with HPC data

set -e

echo "=================================="
echo "Indexing HPC Knowledge Data"
echo "=================================="

# Check if Elasticsearch is running
if ! curl -s http://localhost:9200/_cluster/health > /dev/null; then
    echo "[ERROR] Elasticsearch is not running on port 9200"
    echo "Please start the services first: docker-compose up -d elasticsearch"
    exit 1
fi

echo "Elasticsearch is running"
echo ""
echo "Starting indexer..."
echo ""

# Run indexer with docker-compose
docker-compose --profile indexing up indexer

echo ""
echo "Indexing completed!"
echo ""
echo "To verify, check the indices:"
echo "  curl http://localhost:9200/_cat/indices?v"
