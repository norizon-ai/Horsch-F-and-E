#!/usr/bin/env bash
# =============================================================================
# deploy-services.sh — Build, push, and deploy all services
# =============================================================================
# Builds Docker images for all 6 services, pushes to ACR, and updates
# Container Apps to use the new images.
#
# Prerequisites:
#   - Azure CLI logged in
#   - Docker running locally
#   - setup-infra.sh has been run
#
# Usage:
#   cd instantiations/internal_setup/azure
#   ./scripts/deploy-services.sh              # Deploy all services
#   ./scripts/deploy-services.sh deepsearch   # Deploy single service
#   ./scripts/deploy-services.sh frontend     # Deploy single service

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AZURE_DIR="$(dirname "$SCRIPT_DIR")"
SETUP_DIR="$(dirname "$AZURE_DIR")"
REPO_ROOT="$(cd "$SETUP_DIR/../../.." && pwd)"

# Load Azure config
if [ -f "$AZURE_DIR/.env.azure" ]; then
    set -a
    source "$AZURE_DIR/.env.azure"
    set +a
fi

: "${AZURE_SUBSCRIPTION_ID:?Set AZURE_SUBSCRIPTION_ID in .env.azure}"
: "${AZURE_RESOURCE_GROUP:=norizon-internal-rg}"
ACR_NAME="${AZURE_ACR_NAME:-norizonacr}"

az account set --subscription "$AZURE_SUBSCRIPTION_ID"

# Image tag: git short SHA
GIT_SHA=$(cd "$REPO_ROOT" && git rev-parse --short HEAD 2>/dev/null || echo "unknown")
IMAGE_TAG="${GIT_SHA}"

echo "=== Norizon Internal — Deploy Services ==="
echo "ACR:       $ACR_NAME"
echo "Image tag: $IMAGE_TAG"
echo ""

# Login to ACR
echo "--- Logging in to ACR..."
az acr login --name "$ACR_NAME"

ACR_SERVER="${ACR_NAME}.azurecr.io"

# Service definitions (Bash 3.2 compatible — no associative arrays)
ALL_SERVICE_NAMES="confluence-mcp confluence-publisher deepsearch deepgram-service workflow-service frontend"

get_context() {
    case "$1" in
        confluence-mcp)       echo "services/confluence-mcp" ;;
        confluence-publisher) echo "services/confluence-publisher" ;;
        deepsearch)           echo "services/custom-deepresearch" ;;
        deepgram-service)     echo "services/deepgram-service" ;;
        workflow-service)     echo "services/workflow-service" ;;
        frontend)             echo "services/norizon-research/frontend" ;;
        *) echo "" ;;
    esac
}

# Filter to specific services if arguments provided
if [ $# -gt 0 ]; then
    DEPLOY_SERVICES="$*"
else
    DEPLOY_SERVICES="$ALL_SERVICE_NAMES"
fi

# Build and push each service
for SERVICE_NAME in $DEPLOY_SERVICES; do
    CONTEXT=$(get_context "$SERVICE_NAME")
    if [ -z "$CONTEXT" ]; then
        echo "ERROR: Unknown service '$SERVICE_NAME'"
        echo "Available: $ALL_SERVICE_NAMES"
        exit 1
    fi

    FULL_IMAGE="$ACR_SERVER/norizon/$SERVICE_NAME:$IMAGE_TAG"
    LATEST_IMAGE="$ACR_SERVER/norizon/$SERVICE_NAME:latest"
    BUILD_CONTEXT="$REPO_ROOT/$CONTEXT"

    echo "--- Building $SERVICE_NAME..."
    echo "    Context: $BUILD_CONTEXT"
    echo "    Image:   $FULL_IMAGE"

    BUILD_ARGS=""
    if [ "$SERVICE_NAME" = "frontend" ]; then
        # Require non-empty values
        : "${VITE_WORKFLOW_API_URL:?VITE_WORKFLOW_API_URL must be set in .env.azure}"
        : "${VITE_DEEPSEARCH_API_URL:?VITE_DEEPSEARCH_API_URL must be set in .env.azure}"
        : "${PUBLIC_AUTH0_DOMAIN:?PUBLIC_AUTH0_DOMAIN must be set in .env.azure}"
        : "${PUBLIC_AUTH0_CLIENT_ID:?PUBLIC_AUTH0_CLIENT_ID must be set in .env.azure}"
        : "${PUBLIC_AUTH0_AUDIENCE:?PUBLIC_AUTH0_AUDIENCE must be set in .env.azure}"

        # Write environment variables directly to .env to force SvelteKit Vite to load them
        cat > "$BUILD_CONTEXT/.env" <<EOF
VITE_WORKFLOW_API_URL=$VITE_WORKFLOW_API_URL
VITE_DEEPSEARCH_API_URL=$VITE_DEEPSEARCH_API_URL
VITE_API_BASE_URL=$VITE_DEEPSEARCH_API_URL/api/v1
VITE_SSR_API_BASE_URL=http://deepsearch:8000/api/v1
PUBLIC_AUTH0_DOMAIN=$PUBLIC_AUTH0_DOMAIN
PUBLIC_AUTH0_CLIENT_ID=$PUBLIC_AUTH0_CLIENT_ID
PUBLIC_AUTH0_AUDIENCE=$PUBLIC_AUTH0_AUDIENCE
EOF
        echo "    Wrote .env for SvelteKit build phase"
    fi

    DOCKERFILE="Dockerfile"
    if [ -f "$BUILD_CONTEXT/Dockerfile.prod" ]; then
        echo "    Using production Dockerfile: Dockerfile.prod"
        DOCKERFILE="Dockerfile.prod"
    fi

    # Force no-cache for frontend to ensure VITE_ env vars are always freshly baked in
    CACHE_FLAG=""
    if [ "$SERVICE_NAME" = "frontend" ]; then
        CACHE_FLAG="--no-cache"
    fi

    docker build --platform linux/amd64 $CACHE_FLAG -f "$BUILD_CONTEXT/$DOCKERFILE" -t "$FULL_IMAGE" -t "$LATEST_IMAGE" $BUILD_ARGS "$BUILD_CONTEXT"

    echo "--- Pushing $SERVICE_NAME..."
    docker push "$FULL_IMAGE"
    docker push "$LATEST_IMAGE"

    echo ""
done

# Get managed identity resource ID for ACR pull
IDENTITY_ID=$(az identity show -n norizon-internal-id -g "$AZURE_RESOURCE_GROUP" --query id -o tsv)

# Update Container Apps to use new images with ACR registry
echo "--- Updating Container Apps..."
UPDATE_SERVICES="$DEPLOY_SERVICES"
if [[ " $DEPLOY_SERVICES " == *" workflow-service "* ]] && [[ " $DEPLOY_SERVICES " != *" celery-worker "* ]]; then
    UPDATE_SERVICES="$UPDATE_SERVICES celery-worker"
fi

for SERVICE_NAME in $UPDATE_SERVICES; do
    IMAGE_NAME="$SERVICE_NAME"
    if [ "$SERVICE_NAME" = "celery-worker" ]; then
        IMAGE_NAME="workflow-service"
    fi

    echo "  Updating $SERVICE_NAME → norizon/$IMAGE_NAME:$IMAGE_TAG"
    az containerapp registry set \
        --name "$SERVICE_NAME" \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --server "$ACR_SERVER" \
        --identity "$IDENTITY_ID" \
        --output none 2>/dev/null || true
    az containerapp update \
        --name "$SERVICE_NAME" \
        --resource-group "$AZURE_RESOURCE_GROUP" \
        --image "$ACR_SERVER/norizon/$IMAGE_NAME:$IMAGE_TAG" \
        --output none &
done

# Wait for all background updates
wait

echo ""
echo "=== Deployment complete ==="
echo "Tag: $IMAGE_TAG"
echo ""
echo "Check status:"
echo "  az containerapp list -g $AZURE_RESOURCE_GROUP -o table"
echo ""
echo "View logs:"
echo "  az containerapp logs show -n deepsearch -g $AZURE_RESOURCE_GROUP --follow"
