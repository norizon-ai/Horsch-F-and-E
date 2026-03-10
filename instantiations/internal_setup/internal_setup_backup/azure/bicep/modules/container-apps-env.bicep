// Container Apps Environment — shared runtime for all services
// Consumption plan: scale-to-zero, pay-per-use
// Includes storage mount for workflow uploads volume

param name string
param location string
param logAnalyticsName string
param storageName string
param storageShareName string

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: logAnalyticsName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {
  name: storageName
}

resource env 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: name
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
    workloadProfiles: [
      {
        name: 'Consumption'
        workloadProfileType: 'Consumption'
      }
    ]
  }
}

// Azure Files storage mount — used by services needing shared volume
resource storageMount 'Microsoft.App/managedEnvironments/storages@2024-03-01' = {
  parent: env
  name: 'workflow-uploads'
  properties: {
    azureFile: {
      accountName: storageName
      accountKey: storage.listKeys().keys[0].value
      shareName: storageShareName
      accessMode: 'ReadWrite'
    }
  }
}

output id string = env.id
output name string = env.name
output defaultDomain string = env.properties.defaultDomain
