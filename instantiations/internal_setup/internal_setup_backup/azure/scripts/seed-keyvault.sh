#!/usr/bin/env bash
# =============================================================================
# seed-keyvault.sh — Populate Key Vault from local .env files
# =============================================================================
# Reads secrets from the local env files (atlassian.env, deepsearch.env,
# workflow.env) and stores them in Azure Key Vault.
#
# Prerequisites:
#   - Azure CLI logged in with Key Vault Secrets Officer role
#   - Local env files exist in instantiations/internal_setup/
#   - setup-infra.sh has been run
#
# Usage:
#   cd instantiations/internal_setup/azure
#   ./scripts/seed-keyvault.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AZURE_DIR="$(dirname "$SCRIPT_DIR")"
SETUP_DIR="$(dirname "$AZURE_DIR")"

# Load Azure config
if [ -f "$AZURE_DIR/.env.azure" ]; then
    set -a
    source "$AZURE_DIR/.env.azure"
    set +a
fi

: "${AZURE_SUBSCRIPTION_ID:?Set AZURE_SUBSCRIPTION_ID in .env.azure}"
: "${AZURE_RESOURCE_GROUP:=norizon-internal-rg}"
KV_NAME="${AZURE_KV_NAME:-norizon-internal-kv}"

az account set --subscription "$AZURE_SUBSCRIPTION_ID"

echo "=== Seeding Key Vault: $KV_NAME ==="

# Grant current user Key Vault Secrets Officer role (needed to set secrets)
CURRENT_USER=$(az ad signed-in-user show --query id -o tsv 2>/dev/null || true)
if [ -n "$CURRENT_USER" ]; then
    echo "--- Ensuring current user has Key Vault Secrets Officer role..."
    KV_ID=$(az keyvault show --name "$KV_NAME" --resource-group "$AZURE_RESOURCE_GROUP" --query id -o tsv)
    az role assignment create \
        --assignee "$CURRENT_USER" \
        --role "Key Vault Secrets Officer" \
        --scope "$KV_ID" \
        --output none 2>/dev/null || true
    echo "    (waiting 10s for role propagation...)"
    sleep 10
fi

# Helper: set a secret in Key Vault
set_secret() {
    local name="$1"
    local value="$2"
    if [ -z "$value" ]; then
        echo "  SKIP: $name (empty value)"
        return
    fi
    echo "  SET:  $name"
    az keyvault secret set \
        --vault-name "$KV_NAME" \
        --name "$name" \
        --value "$value" \
        --output none
}

# Helper: read a value from an env file
read_env() {
    local file="$1"
    local key="$2"
    grep "^${key}=" "$file" 2>/dev/null | head -1 | cut -d'=' -f2-
}

# --- Read from atlassian.env ---
ATLASSIAN_ENV="$SETUP_DIR/atlassian.env"
if [ -f "$ATLASSIAN_ENV" ]; then
    echo ""
    echo "--- Reading $ATLASSIAN_ENV"
    set_secret "confluence-url" "$(read_env "$ATLASSIAN_ENV" CONFLUENCE_URL)"
    set_secret "confluence-username" "$(read_env "$ATLASSIAN_ENV" CONFLUENCE_USERNAME)"
    set_secret "confluence-api-token" "$(read_env "$ATLASSIAN_ENV" CONFLUENCE_API_TOKEN)"
else
    echo "WARNING: $ATLASSIAN_ENV not found — skipping Confluence secrets"
fi

# --- Read from deepsearch.env ---
DEEPSEARCH_ENV="$SETUP_DIR/deepsearch.env"
if [ -f "$DEEPSEARCH_ENV" ]; then
    echo ""
    echo "--- Reading $DEEPSEARCH_ENV"
    set_secret "openai-api-key" "$(read_env "$DEEPSEARCH_ENV" DR_LLM_API_KEY)"
else
    echo "WARNING: $DEEPSEARCH_ENV not found — skipping OpenAI secret"
fi

# --- Read from workflow.env ---
WORKFLOW_ENV="$SETUP_DIR/workflow.env"
if [ -f "$WORKFLOW_ENV" ]; then
    echo ""
    echo "--- Reading $WORKFLOW_ENV"
    set_secret "ms-tenant-id" "$(read_env "$WORKFLOW_ENV" WORKFLOW_MS_TENANT_ID)"
    set_secret "ms-client-id" "$(read_env "$WORKFLOW_ENV" WORKFLOW_MS_CLIENT_ID)"
    set_secret "ms-client-secret" "$(read_env "$WORKFLOW_ENV" WORKFLOW_MS_CLIENT_SECRET)"
else
    echo "WARNING: $WORKFLOW_ENV not found — skipping MS Teams secrets"
fi

# --- Deepgram API key (from environment or prompt) ---
echo ""
if [ -n "${DEEPGRAM_API_KEY:-}" ]; then
    set_secret "deepgram-api-key" "$DEEPGRAM_API_KEY"
else
    echo "--- Deepgram API key"
    echo "  Set DEEPGRAM_API_KEY env var or run manually:"
    echo "  az keyvault secret set --vault-name $KV_NAME --name deepgram-api-key --value <key>"
fi

echo ""
echo "=== Key Vault seeded ==="
echo "Verify: az keyvault secret list --vault-name $KV_NAME --output table"
