param name string
param location string
param adminUser string
@secure()
param adminPassword string
param databaseName string = 'workflows'

resource postgresServer 'Microsoft.DBforPostgreSQL/flexibleServers@2023-03-01-preview' = {
  name: name
  location: location
  sku: {
    name: 'Standard_B1ms'
    tier: 'Burstable'
  }
  properties: {
    version: '15'
    administratorLogin: adminUser
    administratorLoginPassword: adminPassword
    storage: {
      storageSizeGB: 32
    }
    highAvailability: {
      mode: 'Disabled'
    }
  }

  // Allow Azure services to access the database
  resource firewall 'firewallRules@2023-03-01-preview' = {
    name: 'AllowAllAzureServicesAndIPs'
    properties: {
      startIpAddress: '0.0.0.0'
      endIpAddress: '255.255.255.255'
    }
  }

  resource database 'databases@2023-03-01-preview' = {
    name: databaseName
  }
}

output fqdn string = postgresServer.properties.fullyQualifiedDomainName
output databaseName string = databaseName
