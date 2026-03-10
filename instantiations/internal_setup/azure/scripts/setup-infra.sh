#!/usr/bin/env bash
# =============================================================================
# setup-infra.sh — One-time Azure infrastructure provisioning
# =============================================================================
# Creates all Azure resources for Norizon internal deployment:
#   Resource Group, Managed Identity, ACR, Key Vault, Storage,
#   Log Analytics, Container Apps Environment, 7 Container Apps
#
# Prerequisites:
#   - Azure CLI installed and logged in (az login)
#   - Bicep CLI installed (az bicep install)
#   - .env.azure sourced or AZURE_SUBSCRIPTION_ID set
#
# Usage:
#   cd instantiations/internal_setup/azure
#   ./scripts/setup-infra.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AZURE_DIR="$(dirname "$SCRIPT_DIR")"

# Load Azure config
if [ -f "$AZURE_DIR/.env.azure" ]; then
    set -a
    source "$AZURE_DIR/.env.azure"
    set +a
fi

# Required config
: "${AZURE_SUBSCRIPTION_ID:?Set AZURE_SUBSCRIPTION_ID in .env.azure}"
: "${AZURE_RESOURCE_GROUP:=norizon-internal-rg}"
: "${AZURE_LOCATION:=swedencentral}"

echo "=== Norizon Internal — Azure Infrastructure Setup ==="
echo "Subscription: $AZURE_SUBSCRIPTION_ID"
echo "Resource Group: $AZURE_RESOURCE_GROUP"
echo "Location: $AZURE_LOCATION"
echo ""

# Set subscription
az account set --subscription "$AZURE_SUBSCRIPTION_ID"

# Create resource group
echo "--- Creating resource group..."
az group create \
    --name "$AZURE_RESOURCE_GROUP" \
    --location "$AZURE_LOCATION" \
    --output none

# Deploy Bicep template
echo "--- Deploying infrastructure (this takes 3-5 minutes)..."
DEPLOY_NAME="norizon-infra-$(date +%Y%m%d-%H%M%S)"
az deployment group create \
    --resource-group "$AZURE_RESOURCE_GROUP" \
    --template-file "$AZURE_DIR/bicep/main.bicep" \
    --parameters "$AZURE_DIR/bicep/parameters/internal.bicepparam" \
    --name "$DEPLOY_NAME"

# Extract outputs from deployment
ACR_SERVER=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.acrLoginServer.value' -o tsv)
KV_NAME=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.kvName.value' -o tsv)
ENV_DOMAIN=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.envDefaultDomain.value' -o tsv)
FRONTEND_FQDN=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.frontendFqdn.value' -o tsv)
DEEPSEARCH_FQDN=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.deepsearchFqdn.value' -o tsv)
WORKFLOW_FQDN=$(az deployment group show -g "$AZURE_RESOURCE_GROUP" -n "$DEPLOY_NAME" --query 'properties.outputs.workflowFqdn.value' -o tsv)

echo ""
echo "=== Infrastructure deployed ==="
echo "ACR:            $ACR_SERVER"
echo "Key Vault:      $KV_NAME"
echo "Env domain:     $ENV_DOMAIN"
echo ""
echo "Service URLs (default ACA domains):"
echo "  Frontend:     https://$FRONTEND_FQDN"
echo "  DeepSearch:   https://$DEEPSEARCH_FQDN"
echo "  Workflow:     https://$WORKFLOW_FQDN"
echo ""
echo "Next steps:"
echo "  1. Run ./scripts/seed-keyvault.sh to populate secrets"
echo "  2. Run ./scripts/deploy-services.sh to build and deploy containers"
echo ""
echo "Deployment output saved to /tmp/norizon-deploy-output.json"
