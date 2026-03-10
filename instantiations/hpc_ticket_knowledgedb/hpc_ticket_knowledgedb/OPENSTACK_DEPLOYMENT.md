# OpenStack Deployment Guide - HPC Knowledge Database

This guide walks you through deploying the HPC Knowledge Database to OpenStack and connecting it to your existing OpenWebUI instance.

## Overview

**What You're Deploying:**
- Single Ubuntu 22.04 VM (4 vCPU, 16GB RAM, 100GB disk)
- Elasticsearch 8.11.0 (single-node, 4GB heap)
- DR API (FastAPI service on port 8001)
- 100GB persistent volume for Elasticsearch data
- Auto-configured via cloud-init on first boot

**What Already Exists:**
- OpenWebUI instance on OpenStack
- Root infrastructure (SLURM cluster, network)

**What You'll Create:**
- New VM with floating IP
- Custom network (10.240.60.0/24)
- Security groups for API access
- Elasticsearch volume storage

---

## Prerequisites

### 1. OpenStack Credentials
You need:
- Application credential ID
- Application credential secret
- SSH public key

These should already exist from your current OpenStack setup.

### 2. Docker Hub Access
Required to push images:
- Docker Hub account: `lisarebecca`
- Docker logged in locally

### 3. Local Tools
- Terraform >= 1.0
- Docker and Docker Compose
- SSH key pair
- `jq` (optional, for testing)

### 4. Network Access
- VPN connection to FAU network (for LLM access at lme49.cs.fau.de:30000)
- SSH access to OpenStack (api.cc.rrze.de)

---

## Deployment Workflow

### Phase 1: Build and Push Docker Images

**Why:** The VM will pull pre-built images from Docker Hub on first boot.

```bash
# Navigate to project directory
cd /Users/lisaschmidt/Documents/GitHub/rag-server/products/hpc_ticket_knowledgedb

# Build images (takes 2-3 minutes)
./scripts/build_images.sh

# Login to Docker Hub (one-time)
docker login

# Push images to registry (takes 5-10 minutes)
./scripts/push_images.sh
```

**Expected Output:**
```
Building DR API image: lisarebecca/hpc-kb-dr-api:latest
Building Indexer image: lisarebecca/hpc-kb-indexer:latest
...
Pushing lisarebecca/hpc-kb-dr-api:latest
Pushing lisarebecca/hpc-kb-indexer:latest
```

**Verify:**
```bash
docker images | grep hpc-kb
# Should show:
# lisarebecca/hpc-kb-dr-api     latest
# lisarebecca/hpc-kb-indexer    latest
```

---

### Phase 2: Configure Terraform

**Location:** `deploy/terraform/`

#### Step 2.1: Create `terraform.tfvars`

```bash
cd deploy/terraform
cp terraform.tfvars.example terraform.tfvars
```

#### Step 2.2: Edit `terraform.tfvars`

You need to fill in:

**OpenStack Authentication:**
```hcl
application_credential_id     = "your-credential-id"
application_credential_secret = "your-credential-secret"
```

**Get these from:**
- OpenStack Dashboard → Identity → Application Credentials
- Or from existing clouds.yaml file
- Or from your FAU OpenStack account

**SSH Configuration:**
```hcl
ssh_public_key       = "ssh-rsa AAAAB3NzaC1yc2E... your-key"
ssh_private_key_path = "~/.ssh/id_rsa"  # Path to your private key
```

**Get your public key:**
```bash
cat ~/.ssh/id_rsa.pub
# Copy the entire output
```

**Network Configuration (Default is fine):**
```hcl
network_name = "hpc_kb_net"
subnet_cidr  = "10.240.60.0/24"
vm_fixed_ip  = "10.240.60.10"
```

**Security Configuration:**
```hcl
ssh_allowed_cidr = "0.0.0.0/0"  # CHANGE THIS in production!
api_allowed_cidr = "0.0.0.0/0"  # Will restrict to OpenWebUI IP later
```

**Docker Configuration:**
```hcl
docker_registry = "lisarebecca"
dr_api_tag      = "latest"
indexer_tag     = "latest"
```

**LLM Configuration:**
```hcl
llm_base_url = "http://lme49.cs.fau.de:30000/v1"
llm_model    = "openai/gpt-oss-120b"
```

#### Step 2.3: Create `clouds.yaml` (if not exists)

**Location:** `deploy/terraform/clouds.yaml`

```yaml
clouds:
  openstack:
    auth:
      auth_url: https://api.cc.rrze.de:5000
      application_credential_id: "your-credential-id"
      application_credential_secret: "your-credential-secret"
    region_name: "DE-ERL"
    interface: "public"
    identity_api_version: 3
    auth_type: "v3applicationcredential"
```

**Note:** This file contains secrets - do NOT commit to git!

---

### Phase 3: Deploy Infrastructure

#### Step 3.1: Initialize Terraform

```bash
cd deploy/terraform
terraform init
```

**Expected Output:**
```
Initializing the backend...
Initializing provider plugins...
- Finding terraform-provider-openstack/openstack versions matching "~> 1.53.0"...
Terraform has been successfully initialized!
```

#### Step 3.2: Review Deployment Plan

```bash
terraform plan
```

**Review the plan carefully:**
- 1 VM will be created
- 1 network will be created
- 1 subnet will be created
- 1 router will be created
- 1 volume will be created (100GB)
- 1 floating IP will be allocated
- Multiple security groups will be created

**Expected Resources:** ~12 resources to be created

#### Step 3.3: Apply Infrastructure

```bash
terraform apply
```

**Prompts:**
- Type `yes` to confirm
- Deployment takes 5-10 minutes

**Expected Output:**
```
Apply complete! Resources: 12 added, 0 changed, 0 destroyed.

Outputs:

dr_api_url = "http://131.188.45.XXX:8001"
elasticsearch_url = "http://131.188.45.XXX:9200"
floating_ip = "131.188.45.XXX"
ssh_command = "ssh -i ~/.ssh/id_rsa ubuntu@131.188.45.XXX"
vm_name = "hpc-knowledge-database"
```

**IMPORTANT:** Save the floating IP address - you'll need it for OpenWebUI!

---

### Phase 4: Verify Services on VM

#### Step 4.1: SSH to VM

```bash
# Use the ssh_command from terraform output
ssh -i ~/.ssh/id_rsa ubuntu@131.188.45.XXX
```

**First login may take 2-3 minutes** as cloud-init is still running.

#### Step 4.2: Monitor Cloud-Init Progress

```bash
# Check cloud-init status
cloud-init status

# Expected: "status: done"
# If "status: running", wait 1-2 minutes
```

#### Step 4.3: Verify Docker Installation

```bash
docker --version
# Expected: Docker version 24.0.x

docker compose version
# Expected: Docker Compose version v2.x.x
```

#### Step 4.4: Check Running Services

```bash
docker ps
```

**Expected Output:**
```
CONTAINER ID   IMAGE                                    STATUS         PORTS
abc123...      lisarebecca/hpc-kb-dr-api:latest        Up 2 minutes   0.0.0.0:8001->8000/tcp
def456...      elasticsearch:8.11.0                     Up 2 minutes   0.0.0.0:9200->9200/tcp
```

**If containers are not running:**
```bash
# Check logs
sudo journalctl -u hpc-kb -n 50

# Or manually start
cd /opt/hpc-kb
sudo docker compose up -d
```

#### Step 4.5: Verify Elasticsearch

```bash
curl http://localhost:9200/_cluster/health | jq
```

**Expected:**
```json
{
  "cluster_name": "elasticsearch",
  "status": "yellow",
  "number_of_nodes": 1,
  "active_primary_shards": 0,
  "active_shards": 0
}
```

**Status "yellow" is OK** for single-node cluster (no replicas).

#### Step 4.6: Verify DR API

```bash
curl http://localhost:8001/health | jq
```

**Expected:**
```json
{
  "status": "healthy",
  "elasticsearch_connected": true,
  "llm_configured": true,
  "indices": {
    "docs": 0,
    "tickets": 0
  }
}
```

**Note:** Index counts are 0 because data isn't indexed yet.

---

### Phase 5: Index Data

#### Step 5.1: Check Data Volume

```bash
ls -lh /opt/hpc-kb/ticketknowledgedb/
```

**Expected:**
- `docsmd/` - Documentation files
- `knowledgebase/` - Support ticket markdown files

#### Step 5.2: Run Indexer

```bash
cd /opt/hpc-kb
docker compose --profile indexing up indexer
```

**Expected Output:**
```
Indexing documentation...
Indexed 114 documents
Indexing tickets...
Indexed 7780 tickets
✓ Indexing complete
```

**Duration:** 2-5 minutes

#### Step 5.3: Verify Indices

```bash
curl http://localhost:9200/_cat/indices?v
```

**Expected:**
```
health status index   pri rep docs.count
yellow open   docs      1   1        114
yellow open   tickets   1   1       7780
```

#### Step 5.4: Test Search

```bash
curl -X POST http://localhost:9200/docs/_search \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"title": "SLURM"}}, "size": 1}' | jq
```

Should return SLURM-related documentation.

---

### Phase 6: Test DR API

#### Step 6.1: Test Synchronous Query

```bash
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How do I submit a SLURM job?",
    "brief": true
  }' | jq
```

**Expected (30-60 seconds):**
```json
{
  "concise_answer": "To submit a SLURM job...",
  "confidence_score": 0.85,
  "total_iterations": 1,
  "processing_time": 45.2
}
```

#### Step 6.2: Test Streaming Query

```bash
curl -N -X POST http://localhost:8001/query/stream \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What GPUs are available?"
  }'
```

**Expected (streaming output):**
```
data: {"type": "started"}
data: {"type": "iteration", "number": 1, "total": 3}
data: {"type": "completed", "answer": "...", "confidence": 0.8}
```

#### Step 6.3: Test from Local Machine

Exit SSH and test from your local machine:

```bash
# Replace XXX with your floating IP
curl http://131.188.45.XXX:8001/health | jq

curl -X POST http://131.188.45.XXX:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I load modules?", "brief": true}' | jq
```

---

### Phase 7: Connect OpenWebUI

#### Option A: Using OpenWebUI Functions

**Steps:**
1. Access your OpenWebUI instance
2. Go to Workspace → Functions
3. Click "Create New Function"
4. Copy code from `/Users/lisaschmidt/Documents/GitHub/rag-server/products/hpc_ticket_knowledgedb/hpc_dr_function.py`
5. Update the `DR_API_URL` in the Valves configuration:
   ```python
   DR_API_URL: str = Field(
       default="http://131.188.45.XXX:8001",  # Your floating IP
       description="URL of the DR API server"
   )
   ```
6. Save and enable the function
7. Select "HPC Deep Research" model in chat

#### Option B: Using OpenWebUI Pipelines

**Steps:**
1. Deploy pipelines server (if not already running)
2. Update `pipelines/openwebui_pipeline.py`:
   ```python
   DR_API_URL: str = "http://131.188.45.XXX:8001"
   ```
3. Configure OpenWebUI to connect to pipelines server
4. Enable "HPC Deep Research" pipeline

#### Step 7.1: Update Security Groups (Production)

Once you know OpenWebUI's IP address, restrict API access:

**Edit `terraform.tfvars`:**
```hcl
api_allowed_cidr = "10.x.x.x/32"  # OpenWebUI's IP
ssh_allowed_cidr = "131.188.x.x/24"  # Your office network
```

**Apply changes:**
```bash
terraform apply
```

---

## Verification Checklist

After deployment, verify:

- [ ] Terraform apply completed successfully
- [ ] VM is accessible via SSH
- [ ] Docker containers are running (dr-api, elasticsearch)
- [ ] Elasticsearch cluster health is yellow/green
- [ ] DR API health check returns `"status": "healthy"`
- [ ] Data is indexed (docs: 114, tickets: 7780)
- [ ] Local query test returns valid answer
- [ ] Remote query test (from local machine) works
- [ ] OpenWebUI can connect to DR API
- [ ] End-to-end query in OpenWebUI succeeds

---

## Troubleshooting

### Issue: Cloud-init still running after 5 minutes

**Check logs:**
```bash
sudo tail -f /var/log/cloud-init-output.log
```

**Common causes:**
- Slow Docker image pulls (normal, wait)
- Network connectivity issues
- Invalid environment variables

### Issue: Elasticsearch won't start

**Check logs:**
```bash
docker logs elasticsearch
```

**Common fixes:**
```bash
# Check volume mount
df -h | grep elastic

# Check memory
free -h
# Elasticsearch needs 4GB+ available

# Restart container
docker compose restart elasticsearch
```

### Issue: DR API returns "LLM connection failed"

**Check:**
1. VPN connection to FAU network
2. LLM endpoint is accessible:
   ```bash
   curl http://lme49.cs.fau.de:30000/v1/models
   ```
3. Environment variables in docker-compose.yml

### Issue: No data indexed

**Verify data exists:**
```bash
ls /opt/hpc-kb/ticketknowledgedb/docsmd/
ls /opt/hpc-kb/ticketknowledgedb/knowledgebase/
```

**Re-run indexer:**
```bash
docker compose --profile indexing up indexer --force-recreate
```

### Issue: OpenWebUI can't connect

**Check security groups:**
```bash
# From OpenWebUI server, test connectivity
curl http://131.188.45.XXX:8001/health
```

**If timeout:**
- Check `api_allowed_cidr` in terraform.tfvars
- Verify floating IP is correct
- Check OpenStack security groups in dashboard

### Issue: Queries timeout

**Increase timeout in OpenWebUI:**
- Functions: Edit `DR_API_TIMEOUT` valve (default 180s)
- Pipelines: Update environment variable

**Check LLM latency:**
```bash
time curl -X POST http://lme49.cs.fau.de:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-oss-120b", "messages": [{"role": "user", "content": "test"}]}'
```

---

## Monitoring

### Check Service Status

```bash
# VM service status
sudo systemctl status hpc-kb

# Container health
docker ps
docker stats

# API logs
docker logs -f dr-api

# Elasticsearch logs
docker logs -f elasticsearch
```

### Monitor Resource Usage

```bash
# Disk usage
df -h

# Memory usage
free -h

# Docker usage
docker system df
```

### View Recent API Queries

```bash
docker logs --since 1h dr-api | grep "Processing HPC query"
```

---

## Updating the Deployment

### Update Code Only

```bash
# Local machine
cd /Users/lisaschmidt/Documents/GitHub/rag-server/products/hpc_ticket_knowledgedb
./scripts/build_images.sh
./scripts/push_images.sh

# On VM
ssh ubuntu@131.188.45.XXX
cd /opt/hpc-kb
docker compose pull
docker compose up -d
```

### Update Infrastructure

```bash
# Edit terraform.tfvars as needed
terraform plan
terraform apply
```

### Reindex Data

```bash
# If data source files change
ssh ubuntu@131.188.45.XXX
cd /opt/hpc-kb
docker compose --profile indexing up indexer --force-recreate
```

---

## Backup and Recovery

### Backup Elasticsearch Data

```bash
# On VM
docker exec elasticsearch \
  curl -X PUT "localhost:9200/_snapshot/backup_repo" \
  -H 'Content-Type: application/json' \
  -d '{"type": "fs", "settings": {"location": "/usr/share/elasticsearch/backup"}}'

# Create snapshot
docker exec elasticsearch \
  curl -X PUT "localhost:9200/_snapshot/backup_repo/snapshot_1?wait_for_completion=true"
```

### Restore from Backup

```bash
# List snapshots
docker exec elasticsearch \
  curl "localhost:9200/_snapshot/backup_repo/_all"

# Restore
docker exec elasticsearch \
  curl -X POST "localhost:9200/_snapshot/backup_repo/snapshot_1/_restore"
```

---

## Cost Monitoring

**Monthly costs (estimated):**
- VM (SCS-4V-16-100): ~€120/month
- Volume (100GB): ~€20/month
- Floating IP: Free (FAU internal)
- **Total: ~€140/month**

**Check usage:**
- OpenStack Dashboard → Compute → Instances
- OpenStack Dashboard → Volumes → Volumes

---

## Security Hardening (Production)

Before production use:

1. **Restrict Network Access:**
   ```hcl
   ssh_allowed_cidr = "131.188.x.x/24"  # Your network only
   api_allowed_cidr = "10.x.x.x/32"     # OpenWebUI IP only
   ```

2. **Add API Authentication:**
   - Implement API key authentication in DR API
   - Configure OpenWebUI function with API key

3. **Enable Elasticsearch Security:**
   - Enable X-Pack security
   - Set password for elasticsearch user
   - Update DR API configuration

4. **Set Up Monitoring:**
   - Deploy Prometheus + Grafana
   - Configure alerts for disk space, memory, API errors

5. **Regular Updates:**
   ```bash
   # Monthly security updates
   ssh ubuntu@131.188.45.XXX
   sudo apt update && sudo apt upgrade -y
   ```

---

## Next Steps

After successful deployment:

1. **Performance Testing:**
   - Test with 10-20 concurrent users
   - Monitor response times and resource usage
   - Adjust VM flavor if needed (scale up/down)

2. **Data Quality:**
   - Review answer quality
   - Update documentation sources
   - Refine confidence thresholds

3. **Scalability Planning:**
   - See `README_SCALABILITY.md` for Phase 1 implementation
   - Consider multi-node Elasticsearch for production
   - Implement caching layer

4. **User Training:**
   - Create user documentation
   - Provide example queries
   - Set up feedback mechanism

---

## Support and Documentation

**Related Documentation:**
- `README.md` - Project overview
- `CLAUDE.md` - Developer guide
- `IMPLEMENTATION_GUIDE.md` - Phase 1 scalability
- `ARCHITECTURE.md` - System architecture
- `OPTION_COMPARISON.md` - Cost analysis

**Need Help?**
- Check `docker logs dr-api` for API errors
- Check `docker logs elasticsearch` for indexing issues
- Review Terraform state: `terraform show`
- OpenStack dashboard for infrastructure issues

---

## Quick Reference

**Key URLs (replace XXX with your floating IP):**
- DR API: `http://131.188.45.XXX:8001`
- Health: `http://131.188.45.XXX:8001/health`
- Docs: `http://131.188.45.XXX:8001/docs`
- Elasticsearch: `http://131.188.45.XXX:9200` (internal only)

**Key Commands:**
```bash
# Deploy
terraform apply

# SSH
ssh -i ~/.ssh/id_rsa ubuntu@<floating_ip>

# Check services
docker ps
docker compose logs -f

# Reindex
docker compose --profile indexing up indexer

# Update
docker compose pull && docker compose up -d

# Destroy
terraform destroy
```

**Key Files:**
- `deploy/terraform/terraform.tfvars` - Your configuration
- `deploy/terraform/user_data.sh` - VM bootstrap script
- `.env` - Environment variables (local)
- `hpc_dr_function.py` - OpenWebUI function code
