using '../main.bicep'

// Norizon Internal Deployment — West Europe
// All resource names must be globally unique where required (ACR, storage, KV)

param location = 'swedencentral'
param envPrefix = 'norizon-internal'

// Container Registry (must be alphanumeric, globally unique)
param acrName = 'norizonacr'

// Key Vault (must be globally unique, 3-24 chars)
param kvName = 'norizon-internal-kv'

// Storage account (must be alphanumeric, lowercase, globally unique)
param storageName = 'norizonstorage'

// Image tag — overridden by deploy-services.sh with git SHA
param imageTag = 'latest'

// Set to false after first deploy (enables Key Vault refs, volume mounts, health probes)
param usePlaceholderImage = false

// Custom domains — set after DNS is configured
// Leave empty to use default *.azurecontainerapps.io domains first
param frontendDomain = ''
param apiDomain = ''
param workflowDomain = ''
