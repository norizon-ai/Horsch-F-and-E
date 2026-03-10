# Norizon Internal — Azure Deployment Runbook

Step-by-step guide to deploy (or redeploy) Norizon internal setup to Azure Container Apps.

## Architecture

```
Internet
  │
  ├── internal.norizon.de ─────────► frontend (3000)
  ├── api.internal.norizon.de ──────► deepsearch (8000)
  └── workflow.internal.norizon.de ─► workflow-service (8001)
                                        │
                    ┌───────────────────┼───────────────────┐
                    │ ACA Environment   │                   │
                    │                   │                   │
                    │   confluence-mcp (8005)               │
                    │   confluence-publisher (8003)         │
                    │   deepgram-service (8002)             │
                    │   redis (6379)                        │
                    └───────────────────────────────────────┘
```

- **7 Container Apps** on Consumption plan (scale-to-zero)
- **3 public** (frontend, deepsearch, workflow-service) — browser needs direct access
- **4 internal** (confluence-mcp, confluence-publisher, deepgram-service, redis)
- Services communicate by name via ACA built-in DNS (e.g., `http://confluence-mcp`)

## Prerequisites

- Azure CLI: `brew install azure-cli` (or see https://aka.ms/installazurecli)
- Bicep: `az bicep install`
- Docker Desktop **running** (required for image builds — verify with `docker info`)
- `jq` installed: `brew install jq`
- Access to the MS for Startups subscription
- Local env files exist in the **parent directory** (`instantiations/internal_setup/`):
  - `atlassian.env` — Confluence credentials
  - `deepsearch.env` — LLM provider key (must contain `DR_LLM_API_KEY=...`)
  - `workflow.env` — Workflow service + Microsoft Teams OAuth

## Fresh Deployment (All Steps)

Run all 5 steps in order. Total time: ~15-20 minutes.

### Step 0: Azure Login

```bash
az login
az account list -o table
# Verify you see the MS for Startups subscription
```

### Step 1: Configure

```bash
cd instantiations/internal_setup/azure
cp .env.azure.example .env.azure
# Edit .env.azure — set AZURE_SUBSCRIPTION_ID and DEEPGRAM_API_KEY
```

### Step 2: Deploy Infrastructure

```bash
./scripts/setup-infra.sh
```

This creates (~3-5 min):
- Resource group `norizon-internal-rg` in Sweden Central
- User-Assigned Managed Identity
- Container Registry (Basic, ~EUR 5/mo)
- Key Vault with RBAC
- Storage Account + 5 GiB file share
- Log Analytics Workspace
- Container Apps Environment (Consumption plan)
- 7 Container Apps with **placeholder images** (not your code yet)

**Important:** Save the output — it shows the ACA default domain and service FQDNs. The domain follows the pattern `<service>.<random-id>.swedencentral.azurecontainerapps.io`.

After this step, all Container Apps will show `provisioningState: Failed` — this is expected because they're running a placeholder image that doesn't match the configured health probes.

### Step 3: Populate Secrets

```bash
./scripts/seed-keyvault.sh
```

Reads secrets from local `.env` files and stores them in Key Vault:
- `confluence-url`, `confluence-username`, `confluence-api-token` (from `atlassian.env`)
- `openai-api-key` (from `deepsearch.env` — reads the `DR_LLM_API_KEY` value)
- `ms-tenant-id`, `ms-client-id`, `ms-client-secret` (from `workflow.env`)
- `deepgram-api-key` (from `DEEPGRAM_API_KEY` in `.env.azure`)

The script auto-grants your user the "Key Vault Secrets Officer" role and waits 10s for propagation.

Verify:
```bash
az keyvault secret list --vault-name norizon-internal-kv -o table
# Should show 8 secrets
```

### Step 4: Build & Deploy Services

**Critical:** Update `.env.azure` with the ACA domain FQDNs from Step 2 output **before** deploying:
```bash
# These are baked into the SvelteKit frontend at Docker build time (via ARG in Dockerfile).
# Without these, the frontend falls back to http://localhost:8001 which breaks the workflow!
VITE_DEEPSEARCH_API_URL=https://deepsearch.<random-id>.swedencentral.azurecontainerapps.io
VITE_WORKFLOW_API_URL=https://workflow-service.<random-id>.swedencentral.azurecontainerapps.io
```

**Why this matters:** The search API uses SSR (server-side rendering) so it works via ACA internal DNS (`http://deepsearch:8000`). But the workflow API is called **client-side from the browser**, so it needs the public URL baked into the frontend build.

Then deploy:
```bash
./scripts/deploy-services.sh
```

This builds 6 Docker images (linux/amd64), pushes to ACR, and updates all Container Apps (~5-10 min). Images are tagged with the current git short SHA.

**Note:** The first build takes longer because Docker caches are cold. Subsequent builds reuse layers.

Verify all services are running:
```bash
az containerapp list -g norizon-internal-rg -o table
```

Check that all show real images (not `mcr.microsoft.com/k8se/quickstart`):
```bash
for svc in frontend deepsearch workflow-service redis confluence-mcp confluence-publisher deepgram-service; do
  echo "$svc: $(az containerapp show -n $svc -g norizon-internal-rg --query properties.template.containers[0].image -o tsv)"
done
```

### Step 5: Verify

Services with `minReplicas: 0` scale to zero when idle. The **first request after idle triggers a cold start (15-30s)**. Be patient or use `--max-time 60` with curl.

```bash
# Health checks (use actual FQDNs from Step 2 output)
curl --max-time 60 https://<deepsearch-fqdn>/api/v1/health
# Expected: {"status":"healthy","version":"1.0.0","components":{"agents":true,"tools":false,"llm":true}}
# Note: "tools":false is normal — it means the elasticsearch agent is disabled (expected)

curl --max-time 60 https://<workflow-fqdn>/health
# Expected: {"status":"ok","service":"workflow-service","use_mocks":false}

# Open frontend in browser
open https://<frontend-fqdn>

# Test a search query
curl --max-time 60 -X POST https://<deepsearch-fqdn>/api/v1/search/sync \
  -H "Content-Type: application/json" \
  -d '{"query": "test search"}'
```

## Custom Domains (Optional)

After verifying with default ACA domains, set up custom domains:

1. Get the ACA environment's default domain:
   ```bash
   az containerapp env show -n norizon-internal-env -g norizon-internal-rg --query defaultDomain -o tsv
   ```

2. At your DNS registrar, add CNAME records:
   ```
   internal.norizon.de          → frontend.<default-domain>
   api.internal.norizon.de      → deepsearch.<default-domain>
   workflow.internal.norizon.de  → workflow-service.<default-domain>
   ```

3. Add custom domains to Container Apps:
   ```bash
   az containerapp hostname add -n frontend -g norizon-internal-rg --hostname internal.norizon.de
   az containerapp hostname add -n deepsearch -g norizon-internal-rg --hostname api.internal.norizon.de
   az containerapp hostname add -n workflow-service -g norizon-internal-rg --hostname workflow.internal.norizon.de
   ```

4. Bind managed certificates (ACA handles Let's Encrypt automatically):
   ```bash
   az containerapp hostname bind -n frontend -g norizon-internal-rg --hostname internal.norizon.de --environment norizon-internal-env --validation-method CNAME
   az containerapp hostname bind -n deepsearch -g norizon-internal-rg --hostname api.internal.norizon.de --environment norizon-internal-env --validation-method CNAME
   az containerapp hostname bind -n workflow-service -g norizon-internal-rg --hostname workflow.internal.norizon.de --environment norizon-internal-env --validation-method CNAME
   ```

5. Rebuild frontend with custom domain URLs:
   ```bash
   # Update .env.azure:
   VITE_DEEPSEARCH_API_URL=https://api.internal.norizon.de
   VITE_WORKFLOW_API_URL=https://workflow.internal.norizon.de

   ./scripts/deploy-services.sh frontend
   ```

6. Update MS Teams OAuth redirect URI in Azure Entra ID:
   - Go to App registrations → Norizon Meeting Import
   - Update redirect URI to: `https://workflow.internal.norizon.de/auth/microsoft/callback`

## Updating Services

After code changes, redeploy:

```bash
# All services
./scripts/deploy-services.sh

# Single service
./scripts/deploy-services.sh deepsearch
./scripts/deploy-services.sh frontend
```

## Viewing Logs

```bash
# Stream logs for a service
az containerapp logs show -n deepsearch -g norizon-internal-rg --follow

# View recent logs
az containerapp logs show -n workflow-service -g norizon-internal-rg --tail 100

# System-level logs (image pull, scaling events)
az containerapp logs show -n deepsearch -g norizon-internal-rg --type system --tail 20
```

## Troubleshooting

### Services unreachable / curl times out
Scale-to-zero services need a cold start (15-30s). Retry with `--max-time 60`. If still failing, check if replicas exist:
```bash
az containerapp replica list -n <service> -g norizon-internal-rg -o table
```
If no replicas, the service scaled to zero. Send a request to trigger scaling.

### Container App shows "provisioningState: Failed"
This happens when the placeholder image is still in use (before `deploy-services.sh` runs). After deploying real images, state should change to `Succeeded`. Check:
```bash
az containerapp show -n <service> -g norizon-internal-rg \
  --query '{image: properties.template.containers[0].image, state: properties.provisioningState}' -o json
```

### DeepSearch health returns "tools": false
This is **expected**. It means the elasticsearch agent is disabled in `agents.yaml` (no ES instance in this deployment). The confluence_mcp agent is the active search agent.

### Key Vault access denied
```bash
# Verify managed identity has Key Vault Secrets User role
az role assignment list --scope $(az keyvault show -n norizon-internal-kv -g norizon-internal-rg --query id -o tsv) -o table
```

### Image pull failures
```bash
# Verify ACR login server
az acr show -n norizonacr --query loginServer -o tsv

# Verify managed identity has AcrPull role
az role assignment list --scope $(az acr show -n norizonacr --query id -o tsv) -o table

# List images in ACR
az acr repository list -n norizonacr -o table
```

### Service-to-service communication fails
ACA uses internal DNS. Services should use `http://<service-name>` (not localhost, not port numbers in the URL — ACA routes to the container's target port automatically).

### Redis connection issues
Redis runs as an always-on Container App (minReplicas=1). Check it's running:
```bash
az containerapp show -n redis -g norizon-internal-rg --query properties.runningStatus -o tsv
```

### seed-keyvault.sh skips secrets
The script reads from `../atlassian.env`, `../deepsearch.env`, `../workflow.env` (one directory up from `azure/`). Make sure the env files exist in `instantiations/internal_setup/`.

## Quick Status Check

Run this to check all services at once:
```bash
for svc in frontend deepsearch workflow-service redis confluence-mcp confluence-publisher deepgram-service; do
  echo "$svc: $(az containerapp show -n $svc -g norizon-internal-rg --query '{image: properties.template.containers[0].image, provisioning: properties.provisioningState, running: properties.runningStatus}' -o json 2>/dev/null)"
done
```

## Teardown

To delete everything:
```bash
./scripts/teardown.sh
```

This deletes the entire resource group and all resources. Irreversible.

## Cost Monitoring

```bash
# Check current spend
az consumption usage list --start-date $(date -v-30d +%Y-%m-%d) --end-date $(date +%Y-%m-%d) -o table
```

Expected: ~$40-60/month Azure + $10-50/month external APIs (OpenAI, Deepgram).
With $1000 MS for Startups credits, this gives 16-25 months of Azure runway.
