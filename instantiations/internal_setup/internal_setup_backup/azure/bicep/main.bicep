// =============================================================================
// Norizon Internal Setup — Azure Container Apps Deployment
// =============================================================================
// Deploys all infrastructure for internal dogfooding (~5-10 users).
// Run via: az deployment group create -g <rg> -f main.bicep -p parameters/internal.bicepparam
//
// Resources created:
//   1. User-Assigned Managed Identity
//   2. Container Registry (Basic)
//   3. Key Vault
//   4. Storage Account + File Share
//   5. Log Analytics Workspace
//   6. Container Apps Environment
//   7. 7x Container Apps (6 services + redis)

targetScope = 'resourceGroup'

// ---- Parameters ----
param location string
param envPrefix string

// ACR
param acrName string

// Key Vault
param kvName string

// Storage
param storageName string

// Container image tag (default: latest, overridden by deploy script with git SHA)
param imageTag string = 'latest'

// Use placeholder images for initial deploy (before images are pushed to ACR)
param usePlaceholderImage bool = true

// Custom domains (empty = use default ACA domains)
param frontendDomain string = ''
param apiDomain string = ''
param workflowDomain string = ''

// Database Administrator configuration
param pgAdminUser string = 'pgadmin'
@secure()
param pgAdminPassword string = 'NorizonPGAuth2026!${uniqueString(resourceGroup().id)}'

// ---- Managed Identity ----
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: '${envPrefix}-id'
  location: location
}

// ---- Container Registry ----
module acr 'modules/container-registry.bicep' = {
  name: 'acr'
  params: {
    name: acrName
    location: location
    identityPrincipalId: identity.properties.principalId
  }
}

// ---- Key Vault ----
module kv 'modules/key-vault.bicep' = {
  name: 'keyvault'
  params: {
    name: kvName
    location: location
    identityPrincipalId: identity.properties.principalId
  }
}

// ---- Storage ----
module storage 'modules/storage.bicep' = {
  name: 'storage'
  params: {
    name: storageName
    location: location
  }
}

// ---- Container Apps Environment ----
module env 'modules/container-apps-env.bicep' = {
  name: 'container-apps-env'
  params: {
    name: '${envPrefix}-env'
    location: location
    logAnalyticsName: '${envPrefix}-logs'
    storageName: storageName
    storageShareName: 'workflow-uploads'
  }
  dependsOn: [storage]
}

// ---- Helper variables ----
var kvUri = kv.outputs.uri
var envId = env.outputs.id
var acrServer = acr.outputs.loginServer
var idId = identity.id

// ---- Postgres Flexible Server ----
module postgres 'modules/postgres.bicep' = {
  name: 'postgres'
  params: {
    name: 'psql-${envPrefix}-${uniqueString(resourceGroup().id)}'
    location: location
    adminUser: pgAdminUser
    adminPassword: pgAdminPassword
  }
}

// ---- Minio (Temporary S3) ----
module minio 'modules/container-app.bicep' = {
  name: 'minio'
  params: {
    name: 'minio'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'minio/minio:latest'
    usePublicImage: true
    containerPort: 9000
    cpu: '0.5'
    memory: '1Gi'
    minReplicas: 1
    external: false
    command: [
      'server'
      '/data'
      '--console-address'
      ':9001'
    ]
    envVars: [
      { name: 'MINIO_ROOT_USER', value: 'minioadmin' }
      { name: 'MINIO_ROOT_PASSWORD', value: 'minioadmin' }
    ]
  }
}

// ---- Redis (infrastructure service) ----
module redis 'modules/container-app.bicep' = {
  name: 'redis'
  params: {
    name: 'redis'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'redis:7-alpine'
    usePublicImage: true
    containerPort: 6379
    cpu: '0.25'
    memory: '0.5Gi'
    minReplicas: 1 // Redis should always be running
    maxReplicas: 1
    external: false
    transport: 'tcp'  // Redis uses TCP protocol, not HTTP
    healthProbePath: ''
  }
}

// ---- Confluence MCP ----
module confluenceMcp 'modules/container-app.bicep' = {
  name: 'confluence-mcp'
  params: {
    name: 'confluence-mcp'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/confluence-mcp:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8005
    cpu: '0.25'
    memory: '0.5Gi'
    minReplicas: 1 // Must stay running — deepsearch calls it synchronously
    external: false
    kvSecretRefs: [
      { name: 'CONFLUENCE_URL', kvSecretUri: '${kvUri}secrets/confluence-url' }
      { name: 'CONFLUENCE_USERNAME', kvSecretUri: '${kvUri}secrets/confluence-username' }
      { name: 'CONFLUENCE_API_TOKEN', kvSecretUri: '${kvUri}secrets/confluence-api-token' }
    ]
  }
}

// ---- Confluence Publisher ----
module confluencePublisher 'modules/container-app.bicep' = {
  name: 'confluence-publisher'
  params: {
    name: 'confluence-publisher'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/confluence-publisher:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8003
    cpu: '0.25'
    memory: '0.5Gi'
    external: false
    healthProbePath: '/health'
    envVars: [
      { name: 'PUBLISHER_MCP_SERVER_URL', value: 'http://confluence-mcp' }
    ]
  }
}

// ---- DeepSearch ----
module deepsearch 'modules/container-app.bicep' = {
  name: 'deepsearch'
  params: {
    name: 'deepsearch'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/deepsearch:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8000
    cpu: '0.5'
    memory: '1Gi'
    external: true
    healthProbePath: '/api/v1/health'
    customDomains: !empty(apiDomain) ? [
      { name: apiDomain, bindingType: 'SniEnabled' }
    ] : []
    envVars: [
      { name: 'DR_PROMPTS_DIR', value: '/app/prompts' }
      { name: 'DR_LOG_FORMAT', value: 'text' }
      { name: 'DR_ENABLE_TRACING', value: 'false' }
      { name: 'CONFLUENCE_MCP_URL', value: 'http://confluence-mcp' }
      { name: 'DR_LLM_PROVIDER', value: 'openai' }
      { name: 'DR_LLM_BASE_URL', value: 'https://api.openai.com/v1' }
      { name: 'DR_LLM_MODEL', value: 'gpt-4o-mini' }
      { name: 'DR_LLM_TEMPERATURE', value: '0.2' }
      { name: 'DR_LLM_MAX_TOKENS', value: '2000' }
      { name: 'DR_LLM_TIMEOUT', value: '120' }
      { name: 'DR_EXECUTION_STRATEGY', value: 'iterative' }
      { name: 'DR_MAX_ITERATIONS', value: '3' }
      { name: 'DR_QUALITY_THRESHOLD', value: '0.7' }
      { name: 'DR_LOG_LEVEL', value: 'INFO' }
    ]
    kvSecretRefs: [
      { name: 'DR_LLM_API_KEY', kvSecretUri: '${kvUri}secrets/openai-api-key' }
    ]
  }
}

// ---- Deepgram Service ----
module deepgramService 'modules/container-app.bicep' = {
  name: 'deepgram-service'
  params: {
    name: 'deepgram-service'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/deepgram-service:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8002
    cpu: '0.25'
    memory: '0.5Gi'
    minReplicas: 1 // Must stay running — workflow-service calls it synchronously
    external: false
    envVars: [
      { name: 'REDIS_URL', value: 'redis://${redis.outputs.fqdn}:6379/0' }
      { name: 'UPLOAD_DIR', value: '/tmp/workflow-uploads' }
      { name: 'DATA_DIR', value: '/tmp/workflow-uploads' }
      { name: 'S3_ENDPOINT', value: 'http://minio:9000' }
      { name: 'S3_ACCESS_KEY', value: 'minioadmin' }
      { name: 'S3_SECRET_KEY', value: 'minioadmin' }
      { name: 'S3_BUCKET', value: 'nora-meeting-data' }
    ]
    kvSecretRefs: [
      { name: 'DEEPGRAM_API_KEY', kvSecretUri: '${kvUri}secrets/deepgram-api-key' }
      { name: 'OPENAI_API_KEY', kvSecretUri: '${kvUri}secrets/openai-api-key' }
    ]
    volumeMounts: [
      { mountPath: '/tmp/workflow-uploads' }
    ]
  }
}

// ---- Workflow Service ----
module workflowService 'modules/container-app.bicep' = {
  name: 'workflow-service'
  params: {
    name: 'workflow-service'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/workflow-service:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8001
    cpu: '0.25'
    memory: '0.5Gi'
    external: true
    healthProbePath: '/health'
    customDomains: !empty(workflowDomain) ? [
      { name: workflowDomain, bindingType: 'SniEnabled' }
    ] : []
    envVars: [
      { name: 'DATABASE_URL', value: 'postgresql+asyncpg://${pgAdminUser}:${pgAdminPassword}@${postgres.outputs.fqdn}:5432/${postgres.outputs.databaseName}' }
      { name: 'WORKFLOW_USE_MOCKS', value: 'false' }
      { name: 'WORKFLOW_UPLOAD_DIR', value: '/tmp/workflow-uploads' }
      { name: 'WORKFLOW_KSTUDIO_URL', value: 'http://deepgram-service' }
      { name: 'WORKFLOW_DEEPSEARCH_URL', value: 'http://deepsearch' }
      { name: 'WORKFLOW_CONFLUENCE_PUBLISHER_URL', value: 'http://confluence-publisher' }
      { name: 'WORKFLOW_MS_REDIRECT_URI', value: 'https://workflow-service.${env.outputs.defaultDomain}/auth/microsoft/callback' }
      { name: 'WORKFLOW_CORS_ORIGINS', value: 'https://internal.norizon.de,https://frontend.${env.outputs.defaultDomain},http://localhost:5173,http://localhost:3000' }
      { name: 'AUTH0_DOMAIN', value: 'dev-u3sa781qevzl1yxr.us.auth0.com' }
      { name: 'AUTH0_AUDIENCE', value: 'https://api.nora-platform.com' }
    ]
    kvSecretRefs: [
      { name: 'WORKFLOW_MS_TENANT_ID', kvSecretUri: '${kvUri}secrets/ms-tenant-id' }
      { name: 'WORKFLOW_MS_CLIENT_ID', kvSecretUri: '${kvUri}secrets/ms-client-id' }
      { name: 'WORKFLOW_MS_CLIENT_SECRET', kvSecretUri: '${kvUri}secrets/ms-client-secret' }
      { name: 'OPENAI_API_KEY', kvSecretUri: '${kvUri}secrets/openai-api-key' }
      { name: 'KEYGEN_ACCOUNT_ID', kvSecretUri: '${kvUri}secrets/keygen-account-id' }
      { name: 'KEYGEN_LICENSE_KEY', kvSecretUri: '${kvUri}secrets/keygen-license-key' }
    ]
    volumeMounts: [
      { mountPath: '/tmp/workflow-uploads' }
    ]
  }
}

// ---- Celery Worker ----
module celeryWorker 'modules/container-app.bicep' = {
  name: 'celery-worker'
  params: {
    name: 'celery-worker'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    // Celery is part of deepgram-service, not workflow-service
    imageName: 'norizon/deepgram-service:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 8002
    enableIngress: false
    cpu: '0.25'
    memory: '0.5Gi'
    minReplicas: 1
    external: false
    command: [
      'celery'
      '-A'
      'src.celery_app.celery_app'
      'worker'
      '--loglevel=info'
      '--concurrency=2'
    ]
    envVars: [
      { name: 'REDIS_URL', value: 'redis://${redis.outputs.fqdn}:6379/0' }
      { name: 'UPLOAD_DIR', value: '/tmp/workflow-uploads' }
      { name: 'DATA_DIR', value: '/tmp/workflow-uploads' }
      { name: 'S3_ENDPOINT', value: 'http://minio:9000' }
      { name: 'S3_ACCESS_KEY', value: 'minioadmin' }
      { name: 'S3_SECRET_KEY', value: 'minioadmin' }
      { name: 'S3_BUCKET', value: 'nora-meeting-data' }
    ]
    kvSecretRefs: [
      { name: 'OPENAI_API_KEY', kvSecretUri: '${kvUri}secrets/openai-api-key' }
      { name: 'DEEPGRAM_API_KEY', kvSecretUri: '${kvUri}secrets/deepgram-api-key' }
    ]
    volumeMounts: [
      { mountPath: '/tmp/workflow-uploads' }
    ]
  }
}

// ---- Frontend ----
module frontend 'modules/container-app.bicep' = {
  name: 'frontend'
  params: {
    name: 'frontend'
    location: location
    environmentId: envId
    identityId: idId
    acrLoginServer: acrServer
    imageName: 'norizon/frontend:${imageTag}'
    usePlaceholderImage: usePlaceholderImage
    containerPort: 3000
    cpu: '0.25'
    memory: '0.5Gi'
    external: true
    customDomains: !empty(frontendDomain) ? [
      { name: frontendDomain, bindingType: 'SniEnabled' }
    ] : []
    envVars: [
      { name: 'NODE_ENV', value: 'production' }
      { name: 'PORT', value: '3000' }
    ]
  }
}

// ---- Outputs ----
output acrLoginServer string = acr.outputs.loginServer
output kvName string = kv.outputs.name
output envDefaultDomain string = env.outputs.defaultDomain
output frontendFqdn string = frontend.outputs.fqdn
output deepsearchFqdn string = deepsearch.outputs.fqdn
output workflowFqdn string = workflowService.outputs.fqdn
output identityClientId string = identity.properties.clientId
