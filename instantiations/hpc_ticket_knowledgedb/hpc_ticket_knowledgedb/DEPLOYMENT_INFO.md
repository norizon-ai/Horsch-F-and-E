# HPC Knowledge Database - Deployment Information

## Production Deployment on OpenStack (Dec 7, 2025)

### Instance Details

- **VM Name:** hpc-knowledge-database
- **Flavor:** SCS-4V-16-100s (4 vCPU, 16GB RAM, 100GB disk)
- **OS:** Ubuntu 22.04 LTS
- **Region:** DE-ERL (Erlangen)
- **Internal IP:** 10.240.60.10
- **Public IP (Floating):** **172.17.70.18**

### Service Endpoints

- **DR API (External):** http://172.17.70.18:8001
- **DR API Health:** http://172.17.70.18:8001/health
- **DR API Docs:** http://172.17.70.18:8001/docs
- **Elasticsearch (Internal Only):** http://172.17.70.18:9200

### SSH Access

```bash
ssh -i ~/.ssh/fau_openstack_key ubuntu@172.17.70.18
```

### Docker Images Deployed

- **DR API:** lisarebecca/hpc-kb-dr-api:latest
- **Indexer:** lisarebecca/hpc-kb-indexer:latest
- **Elasticsearch:** elasticsearch:8.11.0

### Network Configuration

- **Network:** hpc_kb_net (10.240.60.0/24)
- **Subnet:** hpc_kb_sub
- **Router:** hpc_kb_router (connected to FAU-Intern)
- **Security Group:** hpc_kb_secgroup

**Open Ports:**
- 22 (SSH) - from 0.0.0.0/0 ⚠️
- 8001 (DR API) - from 0.0.0.0/0 ⚠️
- 9200 (Elasticsearch) - from 10.240.60.0/24 only ✓
- 80, 443 (HTTP/HTTPS for updates)

⚠️ **Security Warning:** SSH and API are open to all IPs. Restrict after OpenWebUI connection is configured!

### Storage

- **Volume ID:** 6a596bcb-5a17-4488-afb1-1afa4d6434b7
- **Volume Size:** 100GB
- **Volume Mount:** /opt/hpc-kb/elasticsearch-data (on VM)
- **Purpose:** Elasticsearch data persistence

### LLM Configuration

- **Endpoint:** http://lme49.cs.fau.de:30000/v1
- **Model:** openai/gpt-oss-120b
- **Temperature:** 0.2
- **Max Tokens:** 2000

### Next Steps

1. ✅ Infrastructure deployed (Terraform)
2. ⏳ Cloud-init completing (Docker install, service startup)
3. ⏳ Index data (7,780 tickets + 114 docs)
4. ⏳ Connect OpenWebUI to DR API
5. ⏳ Test end-to-end integration
6. ⏳ Restrict security groups (production hardening)

### OpenWebUI Integration

Update your OpenWebUI function with:

```python
DR_API_URL: str = Field(
    default="http://172.17.70.18:8001",
    description="URL of the DR API server"
)
```

**Or** if using internal network between OpenWebUI and DR API, use: `http://10.240.60.10:8001`

### Common Commands

**Check service status:**
```bash
ssh ubuntu@172.17.70.18 "docker ps"
```

**View API logs:**
```bash
ssh ubuntu@172.17.70.18 "docker logs -f dr-api"
```

**Check Elasticsearch health:**
```bash
curl http://172.17.70.18:9200/_cluster/health | jq
```

**Test DR API:**
```bash
curl http://172.17.70.18:8001/health | jq
```

**Run indexer:**
```bash
ssh ubuntu@172.17.70.18 "cd /opt/hpc-kb && docker compose --profile indexing up indexer"
```

**Restart services:**
```bash
ssh ubuntu@172.17.70.18 "sudo systemctl restart hpc-kb"
```

### Troubleshooting

**Services not running?**
```bash
ssh ubuntu@172.17.70.18 "sudo journalctl -u hpc-kb -n 50"
```

**Cloud-init issues?**
```bash
ssh ubuntu@172.17.70.18 "sudo tail -100 /var/log/cloud-init-output.log"
```

**Elasticsearch not starting?**
```bash
ssh ubuntu@172.17.70.18 "docker logs elasticsearch"
```

### Terraform State

- **State File:** deploy/terraform/terraform.tfstate
- **Lock File:** deploy/terraform/.terraform.lock.hcl
- **Destroy:** `terraform destroy` (from deploy/terraform/)

### Backup & Recovery

**Backup Elasticsearch data:**
```bash
ssh ubuntu@172.17.70.18 "docker exec elasticsearch curl -X PUT localhost:9200/_snapshot/backup_repo -H 'Content-Type: application/json' -d '{\"type\": \"fs\", \"settings\": {\"location\": \"/usr/share/elasticsearch/backup\"}}'"
```

**Create snapshot:**
```bash
ssh ubuntu@172.17.70.18 "docker exec elasticsearch curl -X PUT 'localhost:9200/_snapshot/backup_repo/snapshot_1?wait_for_completion=true'"
```

### Cost Estimate

**Monthly:**
- VM (SCS-4V-16-100s): ~€120/month
- Volume (100GB): ~€20/month
- Floating IP: Free (FAU internal)
- **Total:** ~€140/month

### Security Hardening (TODO before production)

1. **Restrict SSH access:**
   ```hcl
   ssh_allowed_cidr = "131.188.0.0/16"  # FAU network only
   ```

2. **Restrict API access:**
   ```hcl
   api_allowed_cidr = "10.x.x.x/32"  # OpenWebUI IP only
   ```

3. **Apply changes:**
   ```bash
   cd deploy/terraform
   terraform apply
   ```

4. **Enable Elasticsearch security:**
   - Set password for elasticsearch user
   - Update DR API .env with credentials

5. **Add API authentication:**
   - Implement API key in DR API
   - Configure in OpenWebUI function

### Monitoring & Alerts (Recommended)

- Set up Prometheus + Grafana
- Monitor disk usage (alert at 80%)
- Monitor API response times
- Monitor Elasticsearch cluster health

### Created Resources in OpenStack

| Resource Type | Name | ID |
|--------------|------|-----|
| VM Instance | hpc-knowledge-database | 932eb928-c493-4915-82e3-1bf2ade59a34 |
| Network | hpc_kb_net | 8f3ad02a-a02b-44e7-9ecd-bb2a65c2376f |
| Subnet | hpc_kb_sub | 316baecb-4352-4bef-ad6a-c5f284910bfc |
| Router | hpc_kb_router | ea26c1e4-79fc-4d35-a502-95411ec8a688 |
| Security Group | hpc_kb_secgroup | be82fc87-a483-4c3d-82dd-b8deff908f9a |
| Floating IP | 172.17.70.18 | bf7b605e-3761-44c8-ba62-934222bd9377 |
| Volume | elasticsearch-data | 6a596bcb-5a17-4488-afb1-1afa4d6434b7 |
| SSH Key | hpc-kb-key | hpc-kb-key |

---

**Deployment completed:** December 7, 2025, 14:17 UTC
**Terraform version:** 1.x
**OpenStack provider:** terraform-provider-openstack/openstack v1.53.0
