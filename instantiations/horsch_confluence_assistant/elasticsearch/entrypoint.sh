#!/bin/bash
# Entrypoint for pre-loaded Elasticsearch image
# Simply starts Elasticsearch normally since data is already indexed

echo "Starting Elasticsearch with pre-loaded Confluence data..."
exec /usr/local/bin/docker-entrypoint.sh elasticsearch
