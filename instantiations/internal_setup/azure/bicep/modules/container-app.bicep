// Reusable Container App module — called once per service
// Supports: public/internal ingress, Key Vault secret refs, volume mounts, health probes

param name string
param location string
param environmentId string
param identityId string
param acrLoginServer string

// Container config
param imageName string
param containerPort int
param cpu string = '0.25'
param memory string = '0.5Gi'

// Set to true for public Docker Hub images (e.g., redis:7-alpine)
param usePublicImage bool = false

// Scaling
param minReplicas int = 0
param maxReplicas int = 2

// Ingress
param external bool = false
param customDomains array = []
param transport string = 'http'

// Custom startup command (empty array = use Dockerfile CMD)
param command array = []

// Environment variables (non-secret)
param envVars array = []

// Key Vault secret references: [{name: 'ENV_VAR_NAME', kvSecretUri: 'https://vault.../secrets/name'}]
param kvSecretRefs array = []

// Volume mounts: [{volumeName: 'x', mountPath: '/y'}]
param volumeMounts array = []

// Health probe path (empty string to skip)
param healthProbePath string = ''

// Build secret references for Key Vault
var secretDefs = [for ref in kvSecretRefs: {
  name: toLower(replace(ref.name, '_', '-'))
  keyVaultUrl: ref.kvSecretUri
  identity: identityId
}]

// Map KV secrets to env vars
var kvEnvVars = [for ref in kvSecretRefs: {
  name: ref.name
  secretRef: toLower(replace(ref.name, '_', '-'))
}]

// In placeholder mode, skip KV secrets (KV isn't seeded yet)
var effectiveSecretDefs = usePlaceholderImage ? [] : secretDefs
var effectiveKvEnvVars = usePlaceholderImage ? [] : kvEnvVars

// Combine plain env vars + secret env vars
var allEnvVars = usePlaceholderImage ? envVars : concat(envVars, effectiveKvEnvVars)

// Use placeholder image for initial deployment (ACR is empty until deploy-services.sh runs)
param usePlaceholderImage bool = false

// Image reference: placeholder, public Docker Hub, or ACR-prefixed
var fullImageName = usePlaceholderImage ? 'mcr.microsoft.com/k8se/quickstart:latest' : (usePublicImage ? imageName : '${acrLoginServer}/${imageName}')

// Volume definitions
var volumes = !empty(volumeMounts) ? [
  {
    name: 'workflow-uploads'
    storageName: 'workflow-uploads'
    storageType: 'AzureFile'
  }
] : []

// Container volume mounts
var containerVolumeMounts = [for mount in volumeMounts: {
  volumeName: 'workflow-uploads'
  mountPath: mount.mountPath
}]

// Health probe (liveness)
var probes = !empty(healthProbePath) ? [
  {
    type: 'Liveness'
    httpGet: {
      path: healthProbePath
      port: containerPort
    }
    initialDelaySeconds: 15
    periodSeconds: 30
    timeoutSeconds: 10
    failureThreshold: 3
  }
  {
    type: 'Startup'
    httpGet: {
      path: healthProbePath
      port: containerPort
    }
    initialDelaySeconds: 5
    periodSeconds: 10
    timeoutSeconds: 10
    failureThreshold: 10
  }
] : []

resource app 'Microsoft.App/containerApps@2024-03-01' = {
  name: name
  location: location
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${identityId}': {}
    }
  }
  properties: {
    environmentId: environmentId
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: {
        external: external
        targetPort: containerPort
        transport: transport
        allowInsecure: false
        customDomains: !empty(customDomains) ? customDomains : null
      }
      registries: (usePublicImage || usePlaceholderImage) ? [] : [
        {
          server: acrLoginServer
          identity: identityId
        }
      ]
      secrets: !empty(effectiveSecretDefs) ? effectiveSecretDefs : []
    }
    template: {
      containers: [
        {
          name: name
          image: fullImageName
          command: !empty(command) ? command : null
          resources: {
            cpu: json(cpu)
            memory: memory
          }
          env: allEnvVars
          volumeMounts: (!usePlaceholderImage && !empty(containerVolumeMounts)) ? containerVolumeMounts : null
          probes: usePlaceholderImage ? [] : (!empty(probes) ? probes : [])
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
      }
      volumes: (!usePlaceholderImage && !empty(volumes)) ? volumes : null
    }
  }
}

output fqdn string = app.properties.configuration.ingress.fqdn
output name string = app.name
