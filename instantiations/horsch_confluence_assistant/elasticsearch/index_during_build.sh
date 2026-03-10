#!/bin/bash
set -e

echo "=========================================="
echo "Starting Elasticsearch for indexing"
echo "=========================================="

# Start Elasticsearch in background
/usr/local/bin/docker-entrypoint.sh elasticsearch &
ES_PID=$!

# Wait for Elasticsearch to be ready
echo "Waiting for Elasticsearch to start..."
for i in {1..60}; do
    if curl -s -f http://localhost:9200/_cluster/health 2>/dev/null | grep -q '"status"'; then
        echo "✓ Elasticsearch is ready!"
        break
    fi
    echo "  Waiting... ($i/60)"
    sleep 3
done

# Verify Elasticsearch is responding
if ! curl -s -f http://localhost:9200/_cluster/health; then
    echo "❌ Error: Elasticsearch not responding"
    exit 1
fi

# Run indexing
echo ""
echo "=========================================="
echo "Indexing Confluence data"
echo "=========================================="
python3.9 /usr/share/elasticsearch/index_confluence.py

INDEXING_EXIT=$?

# Stop Elasticsearch gracefully
echo ""
echo "Stopping Elasticsearch..."
kill -TERM $ES_PID 2>/dev/null || true
wait $ES_PID 2>/dev/null || true

if [ $INDEXING_EXIT -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ Indexing complete!"
    echo "=========================================="
    exit 0
else
    echo ""
    echo "=========================================="
    echo "❌ Indexing failed!"
    echo "=========================================="
    exit $INDEXING_EXIT
fi
