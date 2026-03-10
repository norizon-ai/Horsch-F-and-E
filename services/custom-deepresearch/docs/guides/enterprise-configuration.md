# Enterprise Configuration Management

This guide covers production-ready approaches for managing DeepSearch configurations across multiple client deployments.

## Overview of Options

| Approach | Complexity | Best For | Hot Reload |
|----------|------------|----------|------------|
| Volume Mounts | Low | Single-tenant, dev | Restart required |
| Environment Variables | Low | Simple overrides | Restart required |
| ConfigMaps (K8s) | Medium | Kubernetes deployments | Restart required |
| Config Server | Medium | Multi-environment | ✅ Yes |
| Database-backed | High | Multi-tenant SaaS | ✅ Yes |
| GitOps + ArgoCD | Medium | Enterprise CI/CD | Auto-sync |

---

## Option 1: Kubernetes ConfigMaps & Secrets

**Best for:** Kubernetes deployments with proper CI/CD

```yaml
# k8s/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: deepsearch-config-techmech
  namespace: deepsearch
data:
  agents.yaml: |
    agents:
      confluence:
        type: elasticsearch
        enabled: true
        description: "Search TechMech Confluence"
        backend:
          url: "http://elasticsearch:9200"
          index: "confluence_techmech"
          search_fields:
            - "title^3"
            - "content"
---
apiVersion: v1
kind: Secret
metadata:
  name: deepsearch-secrets-techmech
  namespace: deepsearch
type: Opaque
stringData:
  DR_LLM_API_KEY: "sk-xxx"
  ES_PASSWORD: "xxx"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deepsearch-techmech
spec:
  template:
    spec:
      containers:
        - name: deepsearch
          image: norizon/deepsearch:latest
          envFrom:
            - secretRef:
                name: deepsearch-secrets-techmech
          volumeMounts:
            - name: config
              mountPath: /app/config
              readOnly: true
            - name: prompts
              mountPath: /app/prompts
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: deepsearch-config-techmech
        - name: prompts
          configMap:
            name: deepsearch-prompts-techmech
```

**Update without rebuild:**
```bash
kubectl apply -f k8s/configmap.yaml
kubectl rollout restart deployment/deepsearch-techmech
```

---

## Option 2: GitOps with ArgoCD

**Best for:** Enterprise with multiple environments and audit requirements

```
infrastructure/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    ├── techmech-prod/
    │   ├── agents.yaml
    │   ├── prompts/
    │   ├── secrets.yaml (sealed)
    │   └── kustomization.yaml
    ├── techmech-staging/
    │   └── ...
    └── fau-prod/
        └── ...
```

```yaml
# overlays/techmech-prod/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: deepsearch-techmech

resources:
  - ../../base

configMapGenerator:
  - name: deepsearch-agents
    files:
      - agents.yaml
  - name: deepsearch-prompts
    files:
      - prompts/supervisor.yaml
      - prompts/elasticsearch_agent.yaml

patchesStrategicMerge:
  - deployment-patch.yaml
```

ArgoCD automatically syncs changes when you push to Git.

---

## Option 3: Centralized Config Server

**Best for:** Dynamic configuration without restarts

### 3a. HashiCorp Consul

```python
# deepsearch/config/consul_loader.py
import consul
import yaml
from typing import Optional

class ConsulConfigLoader:
    def __init__(self, host: str = "localhost", port: int = 8500):
        self.client = consul.Consul(host=host, port=port)

    def get_agents_config(self, tenant_id: str) -> dict:
        """Load agents.yaml from Consul KV store."""
        key = f"deepsearch/{tenant_id}/agents"
        _, data = self.client.kv.get(key)
        if data:
            return yaml.safe_load(data["Value"].decode())
        return {}

    def watch_config(self, tenant_id: str, callback):
        """Watch for config changes and trigger reload."""
        key = f"deepsearch/{tenant_id}/agents"
        index = None
        while True:
            index, data = self.client.kv.get(key, index=index, wait="30s")
            if data:
                callback(yaml.safe_load(data["Value"].decode()))
```

```bash
# Store config in Consul
consul kv put deepsearch/techmech/agents @agents.yaml
```

### 3b. AWS AppConfig / Azure App Configuration

```python
# deepsearch/config/azure_loader.py
from azure.appconfiguration import AzureAppConfigurationClient

class AzureConfigLoader:
    def __init__(self, connection_string: str):
        self.client = AzureAppConfigurationClient.from_connection_string(
            connection_string
        )

    def get_agents_config(self, tenant_id: str) -> dict:
        """Load config from Azure App Configuration."""
        setting = self.client.get_configuration_setting(
            key=f"deepsearch/{tenant_id}/agents",
            label="production"
        )
        return yaml.safe_load(setting.value)
```

---

## Option 4: Database-Backed Configuration (Multi-Tenant SaaS)

**Best for:** True multi-tenant SaaS with per-customer configs

### Database Schema

```sql
-- Tenant configurations
CREATE TABLE tenant_configs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,

    -- LLM settings
    llm_provider VARCHAR(50) DEFAULT 'openai',
    llm_model VARCHAR(100) DEFAULT 'gpt-4o-mini',
    llm_api_key_encrypted BYTEA,  -- Encrypted with tenant key

    -- Search settings
    max_iterations INT DEFAULT 3,
    quality_threshold DECIMAL(3,2) DEFAULT 0.7,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Agent definitions per tenant
CREATE TABLE tenant_agents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR(100) REFERENCES tenant_configs(tenant_id),
    agent_name VARCHAR(100) NOT NULL,
    agent_type VARCHAR(50) NOT NULL,  -- elasticsearch, websearch, custom
    enabled BOOLEAN DEFAULT true,
    description TEXT,
    display_name VARCHAR(255),
    source_type VARCHAR(50),  -- confluence, jira, sharepoint
    max_iterations INT DEFAULT 3,
    backend_config JSONB NOT NULL,  -- Flexible backend settings
    preprocessors JSONB DEFAULT '[]',

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),

    UNIQUE(tenant_id, agent_name)
);

-- Prompts per tenant (optional overrides)
CREATE TABLE tenant_prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR(100) REFERENCES tenant_configs(tenant_id),
    category VARCHAR(100) NOT NULL,  -- supervisor, elasticsearch_agent, etc.
    prompt_name VARCHAR(100) NOT NULL,
    prompt_template TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),

    UNIQUE(tenant_id, category, prompt_name)
);

-- Audit log for config changes
CREATE TABLE config_audit_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR(100),
    changed_by VARCHAR(255),
    change_type VARCHAR(50),  -- CREATE, UPDATE, DELETE
    entity_type VARCHAR(50),  -- tenant_config, tenant_agent, tenant_prompt
    entity_id UUID,
    old_value JSONB,
    new_value JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Python Implementation

```python
# deepsearch/config/database_loader.py
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import TenantConfig, TenantAgent, TenantPrompt

class DatabaseConfigLoader:
    """Load tenant configurations from database."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self._cache: dict[str, dict] = {}

    async def get_tenant_config(self, tenant_id: str) -> Optional[dict]:
        """Load full tenant configuration."""
        # Check cache first
        if tenant_id in self._cache:
            return self._cache[tenant_id]

        # Load from database
        result = await self.session.execute(
            select(TenantConfig).where(TenantConfig.tenant_id == tenant_id)
        )
        config = result.scalar_one_or_none()

        if not config:
            return None

        # Load agents
        agents_result = await self.session.execute(
            select(TenantAgent)
            .where(TenantAgent.tenant_id == tenant_id)
            .where(TenantAgent.enabled == True)
        )
        agents = agents_result.scalars().all()

        # Build config dict
        tenant_config = {
            "llm": {
                "provider": config.llm_provider,
                "model": config.llm_model,
                "api_key": self._decrypt(config.llm_api_key_encrypted),
            },
            "supervisor": {
                "max_iterations": config.max_iterations,
                "quality_threshold": float(config.quality_threshold),
            },
            "agents": {
                agent.agent_name: {
                    "type": agent.agent_type,
                    "enabled": agent.enabled,
                    "description": agent.description,
                    "display_name": agent.display_name,
                    "source_type": agent.source_type,
                    "max_iterations": agent.max_iterations,
                    "backend": agent.backend_config,
                    "preprocessors": agent.preprocessors or [],
                }
                for agent in agents
            },
        }

        # Cache it
        self._cache[tenant_id] = tenant_config
        return tenant_config

    def invalidate_cache(self, tenant_id: str):
        """Invalidate cache when config changes."""
        self._cache.pop(tenant_id, None)

    def _decrypt(self, encrypted: bytes) -> str:
        """Decrypt API key using tenant-specific key."""
        # Use your encryption service (Vault, KMS, etc.)
        pass
```

### API for Config Management

```python
# deepsearch/api/admin/routes.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/admin/tenants", tags=["admin"])

class AgentCreate(BaseModel):
    agent_name: str
    agent_type: str  # elasticsearch, websearch, custom
    description: str
    display_name: str | None = None
    source_type: str | None = None
    max_iterations: int = 3
    backend: dict
    preprocessors: list[str] = []

class AgentUpdate(BaseModel):
    enabled: bool | None = None
    description: str | None = None
    max_iterations: int | None = None
    backend: dict | None = None

@router.post("/{tenant_id}/agents")
async def create_agent(
    tenant_id: str,
    agent: AgentCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(require_admin),
):
    """Add a new agent to a tenant's configuration."""
    # Create agent in database
    new_agent = TenantAgent(
        tenant_id=tenant_id,
        agent_name=agent.agent_name,
        agent_type=agent.agent_type,
        description=agent.description,
        display_name=agent.display_name,
        source_type=agent.source_type,
        max_iterations=agent.max_iterations,
        backend_config=agent.backend,
        preprocessors=agent.preprocessors,
    )
    db.add(new_agent)
    await db.commit()

    # Invalidate cache
    config_loader.invalidate_cache(tenant_id)

    # Audit log
    await log_config_change(
        tenant_id=tenant_id,
        changed_by=current_user.email,
        change_type="CREATE",
        entity_type="tenant_agent",
        new_value=agent.dict(),
    )

    return {"status": "created", "agent": agent.agent_name}

@router.patch("/{tenant_id}/agents/{agent_name}")
async def update_agent(
    tenant_id: str,
    agent_name: str,
    update: AgentUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update an existing agent configuration."""
    # ... implementation

@router.delete("/{tenant_id}/agents/{agent_name}")
async def delete_agent(tenant_id: str, agent_name: str):
    """Remove an agent from tenant configuration."""
    # ... implementation

@router.post("/{tenant_id}/agents/{agent_name}/toggle")
async def toggle_agent(tenant_id: str, agent_name: str, enabled: bool):
    """Enable or disable an agent without deleting it."""
    # ... implementation
```

---

## Option 5: Hot Reload with File Watcher

**Best for:** Development and simple deployments wanting live updates

```python
# deepsearch/config/hot_reload.py
import asyncio
from pathlib import Path
from watchfiles import awatch

class ConfigHotReloader:
    """Watch config files and reload agents on change."""

    def __init__(self, config_path: Path, agent_registry):
        self.config_path = config_path
        self.agent_registry = agent_registry
        self._running = False

    async def start(self):
        """Start watching for config changes."""
        self._running = True

        async for changes in awatch(self.config_path):
            if not self._running:
                break

            for change_type, path in changes:
                if path.endswith("agents.yaml"):
                    logger.info("agents.yaml changed, reloading...")
                    await self._reload_agents()
                elif path.endswith(".yaml") and "prompts" in path:
                    logger.info(f"Prompt changed: {path}, reloading...")
                    await self._reload_prompts()

    async def _reload_agents(self):
        """Reload agent configuration."""
        try:
            new_config = load_agents_yaml(self.config_path / "agents.yaml")
            await self.agent_registry.reload(new_config)
            logger.info("Agents reloaded successfully")
        except Exception as e:
            logger.error(f"Failed to reload agents: {e}")

    def stop(self):
        self._running = False
```

Enable in docker-compose:
```yaml
environment:
  - DR_ENABLE_HOT_RELOAD=true
```

---

## Option 6: Sidecar Pattern (Kubernetes)

**Best for:** Decoupled config management in K8s

```yaml
# ConfigMap watcher sidecar
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deepsearch
spec:
  template:
    spec:
      containers:
        - name: deepsearch
          image: norizon/deepsearch:latest
          volumeMounts:
            - name: config
              mountPath: /app/config

        # Sidecar that syncs config from Git/S3/Consul
        - name: config-sync
          image: norizon/config-sync:latest
          env:
            - name: CONFIG_SOURCE
              value: "s3://norizon-configs/techmech/"
            - name: SYNC_INTERVAL
              value: "60"
            - name: RELOAD_SIGNAL
              value: "SIGHUP"
          volumeMounts:
            - name: config
              mountPath: /config

      volumes:
        - name: config
          emptyDir: {}
```

---

## Recommended Architecture for Norizon SaaS

```
┌─────────────────────────────────────────────────────────────────┐
│                        Admin Portal                              │
│  (Manage tenants, agents, prompts, view audit logs)             │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Config API Service                          │
│  POST /tenants/{id}/agents                                      │
│  PATCH /tenants/{id}/agents/{name}                              │
│  POST /tenants/{id}/prompts                                     │
└─────────────────────────────────────────────────────────────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
         ┌──────────────────┐    ┌──────────────────┐
         │    PostgreSQL    │    │   Redis Cache    │
         │  (tenant configs)│    │ (hot config)     │
         └──────────────────┘    └──────────────────┘
                    │                       │
                    └───────────┬───────────┘
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DeepSearch Instances                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  Tenant A   │  │  Tenant B   │  │  Tenant C   │             │
│  │  (cached)   │  │  (cached)   │  │  (cached)   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

### Flow:
1. Admin updates config via Admin Portal
2. Config API writes to PostgreSQL + invalidates Redis cache
3. DeepSearch instances get updated config on next request (or via pub/sub)
4. No restart required, no rebuild required

---

## Quick Decision Guide

| Your Situation | Recommended Approach |
|----------------|---------------------|
| Single customer, simple | Volume mounts + restart |
| 2-5 customers, Kubernetes | ConfigMaps + Kustomize |
| Enterprise, audit required | GitOps + ArgoCD |
| Multi-tenant SaaS | Database-backed + Admin API |
| Need hot reload | File watcher or Redis pub/sub |
| AWS/Azure native | AppConfig / App Configuration |
