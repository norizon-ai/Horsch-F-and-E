#!/usr/bin/env bash
# =============================================================================
# teardown.sh — Delete all Azure resources
# =============================================================================
# Deletes the entire resource group and all resources within it.
# This is irreversible — all data, secrets, and container images will be lost.
#
# Usage:
#   cd instantiations/internal_setup/azure
#   ./scripts/teardown.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AZURE_DIR="$(dirname "$SCRIPT_DIR")"

# Load Azure config
if [ -f "$AZURE_DIR/.env.azure" ]; then
    set -a
    source "$AZURE_DIR/.env.azure"
    set +a
fi

: "${AZURE_SUBSCRIPTION_ID:?Set AZURE_SUBSCRIPTION_ID in .env.azure}"
: "${AZURE_RESOURCE_GROUP:=norizon-internal-rg}"

echo "=== Norizon Internal — Teardown ==="
echo ""
echo "This will PERMANENTLY DELETE all resources in:"
echo "  Resource Group: $AZURE_RESOURCE_GROUP"
echo "  Subscription:   $AZURE_SUBSCRIPTION_ID"
echo ""
echo "Including: Container Apps, ACR (all images), Key Vault, Storage, Logs"
echo ""
read -rp "Type 'yes' to confirm: " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

az account set --subscription "$AZURE_SUBSCRIPTION_ID"

echo ""
echo "--- Deleting resource group (this takes 1-2 minutes)..."
az group delete \
    --name "$AZURE_RESOURCE_GROUP" \
    --yes \
    --no-wait

echo ""
echo "=== Teardown initiated ==="
echo "Resource group deletion is running in the background."
echo "Monitor: az group show -n $AZURE_RESOURCE_GROUP 2>/dev/null || echo 'Deleted'"
