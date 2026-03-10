#!/bin/bash
# Start OpenWebUI for local testing of HPC DR Pipeline integration

set -e

cd "$(dirname "$0")/.."

echo "Starting OpenWebUI for HPC Knowledge Assistant Testing..."
echo ""

# Check if DR API is accessible (either Docker or local)
DR_RUNNING=false
API_MODE=""

# Check for Docker container
if docker ps | grep -q "hpc-kb-dr-api"; then
    DR_RUNNING=true
    API_MODE="Docker"
    export DR_API_URL="http://dr-api:8000"
fi

# Check for local API on port 8000
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    DR_RUNNING=true
    API_MODE="Local"
    export DR_API_URL="http://host.docker.internal:8000"
fi

if [ "$DR_RUNNING" = false ]; then
    echo "[!] DR API is not running!"
    echo "    Start services with: ./scripts/start_services.sh (Docker)"
    echo "    Or run locally with: ./scripts/run_api_local.sh"
    echo ""
    read -p "Do you want to start Docker services now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Starting main services..."
        ./scripts/start_services.sh
        API_MODE="Docker"
        export DR_API_URL="http://dr-api:8000"
    else
        echo "Aborting. Please start DR API first."
        exit 1
    fi
else
    echo "DR API detected: $API_MODE mode"
    echo "  API URL (from container): $DR_API_URL"
fi

echo ""
echo "Starting OpenWebUI container..."
echo ""

# Start OpenWebUI using both compose files
docker compose -f docker-compose.yml -f docker-compose.openwebui.yml up -d openwebui

echo ""
echo "Waiting for OpenWebUI to be healthy..."
sleep 5

# Wait for health check
max_attempts=30
attempt=0
while [ $attempt -lt $max_attempts ]; do
    if docker ps | grep -q "hpc-kb-openwebui-test.*healthy"; then
        echo ""
        echo "OpenWebUI is ready!"
        break
    fi
    echo -n "."
    sleep 2
    attempt=$((attempt + 1))
done

if [ $attempt -eq $max_attempts ]; then
    echo ""
    echo "[!] OpenWebUI did not become healthy in time"
    echo "    Check logs: docker logs hpc-kb-openwebui-test"
    exit 1
fi

echo ""
echo "============================================"
echo "  OpenWebUI Started Successfully!"
echo "============================================"
echo ""
echo "Access OpenWebUI at: http://localhost:${OPENWEBUI_PORT:-3000}"
echo ""
echo "First-time Setup:"
echo "  1. Create an admin account (first user is admin)"
echo "  2. Go to Admin Panel → Settings → Pipelines"
echo "  3. Click '+ New Pipeline' → 'Upload Pipeline'"
echo "  4. Copy the contents of openwebui_pipeline.py"
echo "  5. Paste and click 'Save'"
echo ""
echo "Then you can chat with HPC Deep Research!"
echo ""
echo "Useful commands:"
echo "  View logs:        docker logs -f hpc-kb-openwebui-test"
echo "  Stop OpenWebUI:   docker compose -f docker-compose.openwebui.yml down"
echo "  Restart:          docker compose -f docker-compose.openwebui.yml restart openwebui"
echo ""
