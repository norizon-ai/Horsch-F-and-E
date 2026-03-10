# HPC Knowledge Database: Immediate Action Items (Next 2 Weeks)

**Status:** URGENT - Critical infrastructure issues
**Owner:** DevOps/SRE Team
**Deadline:** Start Week 1, Complete by Week 2

---

## CRITICAL ACTIONS (Do First - 48 Hours)

### Action 1: Emergency Backup Policy (Fixes OPS-001)
**Risk:** Complete data loss in VM failure
**Timeline:** TODAY (by EOD)
**Owner:** DevOps Lead

#### Step 1: Create backup script
File: `/opt/hpc-kb/backup-elasticsearch.sh`

```bash
#!/bin/bash
# HPC KB Elasticsearch backup script
# Run daily via cron: 0 2 * * * /opt/hpc-kb/backup-elasticsearch.sh

set -euo pipefail

BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/mnt/backups"
S3_BUCKET="s3://hpc-kb-backups"
LOG_FILE="/var/log/hpc-kb-backup.log"

# Create backup directory
mkdir -p "$BACKUP_DIR"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

log "=== Starting Elasticsearch backup ==="

# Create Elasticsearch snapshot
curl -X PUT "localhost:9200/_snapshot/local" \
    -H 'Content-Type: application/json' \
    -d '{
        "type": "fs",
        "settings": {
            "location": "'$BACKUP_DIR'/elasticsearch"
        }
    }' 2>/dev/null || log "Snapshot repo already exists"

# Create snapshot
SNAPSHOT_NAME="snapshot-$BACKUP_DATE"
curl -X PUT "localhost:9200/_snapshot/local/$SNAPSHOT_NAME" \
    -H 'Content-Type: application/json' \
    -d '{}' \
    >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    log "Snapshot created: $SNAPSHOT_NAME"
else
    log "ERROR: Failed to create snapshot"
    exit 1
fi

# Wait for snapshot completion (max 5 minutes)
for i in {1..300}; do
    STATUS=$(curl -s "localhost:9200/_snapshot/local/$SNAPSHOT_NAME" | \
        grep -o '"state":"[^"]*"' | cut -d'"' -f4)

    if [ "$STATUS" = "SUCCESS" ]; then
        log "Snapshot completed successfully"
        break
    elif [ "$STATUS" = "FAILED" ]; then
        log "ERROR: Snapshot failed"
        exit 1
    fi

    if [ $((i % 30)) -eq 0 ]; then
        log "Snapshot in progress... (${i}s)"
    fi
    sleep 1
done

# Upload to S3 (if S3 endpoint available)
if command -v s3cmd &> /dev/null; then
    log "Uploading to S3..."
    tar -czf "$BACKUP_DIR/elasticsearch-$BACKUP_DATE.tar.gz" \
        "$BACKUP_DIR/elasticsearch" \
        >> "$LOG_FILE" 2>&1

    s3cmd put "$BACKUP_DIR/elasticsearch-$BACKUP_DATE.tar.gz" \
        "$S3_BUCKET/" >> "$LOG_FILE" 2>&1

    if [ $? -eq 0 ]; then
        log "Uploaded to S3 successfully"
        # Cleanup local tar
        rm "$BACKUP_DIR/elasticsearch-$BACKUP_DATE.tar.gz"
    else
        log "WARNING: S3 upload failed (keeping local backup)"
    fi
fi

# Cleanup old local backups (keep 7 days)
find "$BACKUP_DIR" -name "elasticsearch-*" -type d -mtime +7 -exec rm -rf {} \; \
    >> "$LOG_FILE" 2>&1

log "=== Backup completed ==="
```

#### Step 2: Setup cron job
```bash
# SSH to OpenStack VM
ssh -i ~/.ssh/fau_openstack_key ubuntu@<floating-ip>

# Make script executable
chmod +x /opt/hpc-kb/backup-elasticsearch.sh

# Add to crontab
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/hpc-kb/backup-elasticsearch.sh") | crontab -

# Verify
crontab -l
```

#### Step 3: Test backup NOW
```bash
# Run backup immediately
/opt/hpc-kb/backup-elasticsearch.sh

# Monitor
tail -f /var/log/hpc-kb-backup.log

# Verify in Elasticsearch
curl http://localhost:9200/_snapshot/local?pretty
```

**Completion Check:**
- [ ] Script created and executable
- [ ] Cron job installed
- [ ] First backup completed successfully
- [ ] Log file shows success message

---

### Action 2: Container Resource Limits (Fixes OPS-002)
**Risk:** OOM crashes, uncontrolled resource usage
**Timeline:** TODAY (by EOD)
**Owner:** DevOps Lead

#### Step 1: Update docker-compose.yml
File: `/opt/hpc-kb/docker-compose.yml`

Add resource limits to existing services:

```yaml
services:
  elasticsearch:
    # ... existing config ...
    resources:
      limits:
        cpus: '2.0'        # Max 2 vCPU
        memory: 8G         # Max 8GB RAM
      reservations:
        cpus: '1.0'        # Guaranteed 1 vCPU
        memory: 4G         # Guaranteed 4GB RAM

  dr-api:
    # ... existing config ...
    resources:
      limits:
        cpus: '1.0'        # Max 1 vCPU per instance
        memory: 4G         # Max 4GB RAM
      reservations:
        cpus: '0.5'        # Guaranteed 0.5 vCPU
        memory: 2G         # Guaranteed 2GB RAM

  indexer:
    # ... existing config ...
    resources:
      limits:
        cpus: '2.0'
        memory: 8G
      reservations:
        cpus: '1.0'
        memory: 4G
```

#### Step 2: Apply changes
```bash
# Backup original
cp docker-compose.yml docker-compose.yml.backup.$(date +%Y%m%d)

# Apply new config (will restart containers)
docker-compose down
docker-compose up -d

# Monitor startup
docker-compose logs -f
```

#### Step 3: Verify limits
```bash
# Check container stats
docker stats

# Expected output:
# CONTAINER    MEM USAGE / LIMIT
# elasticsearch    4.2G / 8G     ✓
# dr-api          1.8G / 4G     ✓
```

**Completion Check:**
- [ ] docker-compose.yml updated with resource limits
- [ ] Containers restarted
- [ ] docker stats shows limits enforced
- [ ] All containers healthy (`docker-compose ps`)
- [ ] API responding to requests (`curl http://localhost:8001/health`)

---

## HIGH-PRIORITY ACTIONS (This Week)

### Action 3: Health Check Validation
**Risk:** Silent failures, unable to detect problems
**Timeline:** Day 2-3
**Owner:** DevOps Lead

#### Step 1: Verify health checks in docker-compose.yml
```yaml
services:
  elasticsearch:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9200/_cluster/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  dr-api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

#### Step 2: Monitor health
```bash
# Check current health
docker-compose ps

# Watch health status
watch -n 5 docker-compose ps

# View health check logs
docker logs hpc-kb-elasticsearch | grep -i health
docker logs hpc-kb-dr-api | grep -i health
```

**Completion Check:**
- [ ] All services show "healthy" status
- [ ] Health checks passing consistently

---

### Action 4: Create Emergency Runbook
**Risk:** Panic response to outages, missing procedures
**Timeline:** Day 3-4
**Owner:** DevOps Lead + SRE Team

File: `/opt/hpc-kb/RUNBOOK_EMERGENCY.md`

```markdown
# HPC KB Emergency Runbook

## Service Down - General Response

### Detection
- AlertManager notification received (email/Slack)
- OR: Manual monitoring alert triggered
- OR: Customer reports service unavailable

### Immediate Steps (First 5 minutes)
1. Check service status:
   \`\`\`bash
   docker-compose ps
   \`\`\`
   - All containers should show "Up" and "healthy"
   - If any red: Go to specific runbook below

2. Check logs for obvious errors:
   \`\`\`bash
   docker-compose logs --tail=50 | grep -i error
   \`\`\`

3. Check if services are responding:
   \`\`\`bash
   curl http://localhost:8001/health   # API
   curl http://localhost:9200/_cluster/health?pretty  # ES
   \`\`\`

### Communication
- Notify team in #ops Slack channel
- Incident severity: [Critical/High/Medium/Low]
- Est. impact: [All users/Some features/Performance only]
- ETA for fix: [TBD, investigating]

---

## Elasticsearch Node Down

### Symptoms
- ES cluster status yellow/red
- \`curl http://localhost:9200/_cluster/health\` shows unassigned shards
- API searches timing out or failing

### Response (5 min)
1. Check cluster status:
   \`\`\`bash
   curl http://localhost:9200/_cat/nodes?v
   curl http://localhost:9200/_cat/shards | grep UNASSIGNED
   \`\`\`

2. Check container status:
   \`\`\`bash
   docker-compose ps elasticsearch
   \`\`\`

3. If container crashed:
   \`\`\`bash
   docker-compose restart elasticsearch
   docker-compose logs elasticsearch --tail=50
   \`\`\`

4. Check disk space (common cause):
   \`\`\`bash
   df -h
   du -sh /var/lib/docker/volumes/es-data/*
   \`\`\`
   If >90% full → Alert DevOps immediately

5. Wait for recovery (max 2 minutes):
   \`\`\`bash
   # Monitor cluster status
   while true; do \
     curl http://localhost:9200/_cluster/health?pretty; \
     sleep 5; \
   done
   \`\`\`

### If still red after 5 min
- Check logs: \`docker-compose logs elasticsearch\`
- If data volume corrupted → Restore from backup (see section below)
- If network issue → Check network connectivity to other services

---

## API Down

### Symptoms
- \`curl http://localhost:8001/health\` returns error
- HTTP 502/503 responses
- Requests timeout

### Response (5 min)
1. Check container:
   \`\`\`bash
   docker-compose ps dr-api
   \`\`\`

2. Check logs:
   \`\`\`bash
   docker-compose logs dr-api --tail=50
   \`\`\`

3. Common issues and fixes:

   **Out of memory:**
   \`\`\`bash
   # Check memory
   docker stats dr-api | grep dr-api

   # If >4GB: restart
   docker-compose restart dr-api
   \`\`\`

   **Elasticsearch connection failed:**
   \`\`\`bash
   # Verify ES is up
   curl http://localhost:9200/_cluster/health

   # Restart API
   docker-compose restart dr-api
   \`\`\`

   **LLM endpoint unreachable:**
   \`\`\`bash
   # Check env var
   docker-compose exec dr-api env | grep LLM

   # Test connectivity
   curl http://lme49.cs.fau.de:30000/v1/models
   \`\`\`
   If LLM is down → API will fail on /query but /health should pass

---

## Restore from Backup

### When to trigger
- Data corruption detected
- Accidental deletion of indices
- Security incident (malicious data inserted)

### Steps
1. Check available backups:
   \`\`\`bash
   ls -lah /mnt/backups/elasticsearch/
   curl http://localhost:9200/_snapshot/local?pretty
   \`\`\`

2. STOP the API immediately:
   \`\`\`bash
   docker-compose stop dr-api
   \`\`\`

3. List available snapshots:
   \`\`\`bash
   curl http://localhost:9200/_snapshot/local?pretty
   \`\`\`

4. Restore specific snapshot:
   \`\`\`bash
   curl -X POST "localhost:9200/_snapshot/local/snapshot-20251206_020000/_restore" \
     -H 'Content-Type: application/json' \
     -d '{
       "indices": "docs,tickets,knowledgebase",
       "ignore_unavailable": true,
       "include_global_state": false
     }'
   \`\`\`

5. Monitor restore progress:
   \`\`\`bash
   # Wait for restore to complete (may take 5-30 min)
   curl http://localhost:9200/_cluster/health?pretty

   # Check restore status
   curl http://localhost:9200/_snapshot/local/snapshot-20251206_020000/_status?pretty
   \`\`\`

6. Restart API once ES is green:
   \`\`\`bash
   docker-compose start dr-api
   docker-compose logs dr-api
   \`\`\`

7. Validate data:
   \`\`\`bash
   # Check index counts
   curl http://localhost:9200/_cat/indices?v

   # Test search
   curl -X POST http://localhost:9200/docs/_search -H 'Content-Type: application/json' \
     -d '{"query": {"match_all": {}}, "size": 1}'
   \`\`\`

---

## Complete Service Restart (Last Resort)

Use only if individual service restarts fail.

```bash
# Shutdown all services
docker-compose down

# Wait 10 seconds
sleep 10

# Bring everything back up
docker-compose up -d

# Monitor
docker-compose logs -f

# Verify all healthy
while ! docker-compose ps | grep -q "healthy"; do
  sleep 2
done

echo "All services healthy!"
```

---

## Escalation

If you cannot resolve within 15 minutes:

1. Page on-call engineer:
   - Slack: @devops-oncall
   - Phone: [On-call number]

2. Create incident ticket:
   - Jira: Create ticket in OPS project
   - Title: "HPC KB Service Down - [Root Cause Unknown]"
   - Add runbook output and logs

3. Update status page (if external):
   - Status: "Investigating - Performance Degradation"
   - ETA: [Time]
```

#### Step 2: Test runbook procedures
```bash
# Create test scenario - temporary restart ES
docker-compose restart elasticsearch

# Time the recovery
time docker-compose logs elasticsearch | tail -20

# Should recover within 2-3 minutes
```

**Completion Check:**
- [ ] Runbook document created and accessible
- [ ] All team members know location
- [ ] Test procedures validated (not in production)
- [ ] Contact info for on-call updated

---

### Action 5: Create Monitoring Dashboard (Minimal)
**Risk:** No visibility into system state
**Timeline:** Day 4-5
**Owner:** DevOps Lead

#### Step 1: Install basic monitoring
```bash
# SSH to VM
ssh -i ~/.ssh/fau_openstack_key ubuntu@<floating-ip>

# Install monitoring scripts
mkdir -p /opt/hpc-kb/monitoring

# Create daily health check script
cat > /opt/hpc-kb/monitoring/daily-healthcheck.sh << 'EOF'
#!/bin/bash
# Daily HPC KB health check
# Run: 0 8 * * * /opt/hpc-kb/monitoring/daily-healthcheck.sh

DATE=$(date '+%Y-%m-%d %H:%M:%S')
REPORT="/var/log/hpc-kb-daily-report.log"

echo "=== HPC KB Daily Health Check - $DATE ===" >> $REPORT

# Check services
echo "Service Status:" >> $REPORT
docker-compose ps >> $REPORT 2>&1

# Check Elasticsearch
echo "Elasticsearch Health:" >> $REPORT
curl -s http://localhost:9200/_cluster/health?pretty >> $REPORT 2>&1

# Check disk space
echo "Disk Space:" >> $REPORT
df -h >> $REPORT

# Check memory
echo "Memory Usage:" >> $REPORT
free -h >> $REPORT

# Check backup
echo "Latest Backup:" >> $REPORT
ls -lah /mnt/backups/elasticsearch/ | tail -5 >> $REPORT

# Summary
CLUSTER_STATUS=$(curl -s http://localhost:9200/_cluster/health | grep -o '"status":"[^"]*"')
if [[ $CLUSTER_STATUS == *"green"* ]]; then
    OVERALL="HEALTHY"
else
    OVERALL="DEGRADED"
fi

echo "Overall Status: $OVERALL" >> $REPORT
echo "" >> $REPORT

# Email report if degraded
if [ "$OVERALL" = "DEGRADED" ]; then
    echo "Sending alert email..."
    mail -s "HPC KB Health Alert - $OVERALL" devops@example.com < $REPORT
fi
EOF

chmod +x /opt/hpc-kb/monitoring/daily-healthcheck.sh

# Schedule it
(crontab -l 2>/dev/null; echo "0 8 * * * /opt/hpc-kb/monitoring/daily-healthcheck.sh") | crontab -
```

#### Step 2: Create simple status page
File: `/opt/hpc-kb/STATUS.txt`

```
HPC Knowledge Database - Status

Last Updated: [Auto-updated every minute]

SERVICES:
- Elasticsearch: [Run curl -s http://localhost:9200/_cluster/health | grep status]
- API: [Run curl -s http://localhost:8001/health | grep status]
- Disk: [Run df -h | grep elasticsearch]

RECENT BACKUPS:
[List last 3 backups]

INCIDENTS:
- [Auto-populate from /var/log/hpc-kb-backup.log]
```

**Completion Check:**
- [ ] Daily health check script created
- [ ] Cron job installed
- [ ] Test run completed
- [ ] Status report generated

---

## CHECKLIST: Complete in Next 2 Weeks

```
WEEK 1:
Day 1:
  [ ] Backup script created and tested (Action 1)
  [ ] Docker resource limits applied (Action 2)
  [ ] Backup cron job running
  [ ] First backup completed successfully

Day 2-3:
  [ ] Health checks verified (Action 3)
  [ ] All services showing "healthy"
  [ ] Created emergency runbook (Action 4)
  [ ] Team reviewed runbook

Day 4-5:
  [ ] Monitoring script installed (Action 5)
  [ ] Daily health check running
  [ ] Team has runbook bookmarked

WEEK 2:
Day 6-7:
  [ ] Schedule Phase 1 kickoff meeting
  [ ] Assign team members to Phase 1 tasks
  [ ] Provision VMs for ES cluster (if doing Option A)
  [ ] Prepare docker-compose-cluster.yml configuration

Day 8-10:
  [ ] Begin ES cluster deployment
  [ ] Start monitoring metrics collection
  [ ] Document baseline performance
  [ ] Plan Phase 1 timeline with team

Post-Week 2:
  [ ] Schedule decision meeting for Week 4 (Option A vs B)
  [ ] Begin Phase 1 technical work
  [ ] Weekly sync on progress
```

---

## SIGN-OFF

**Implementation Team Lead:** ________________  Date: _____

**Stakeholder Approval:** ________________  Date: _____

**Expected Completion:** [2 weeks from start]

---

## NEXT DOCUMENT TO READ

After completing these immediate actions:
1. **SCALABILITY_PLAN.md** - Detailed 3-phase implementation plan
2. **IMPLEMENTATION_GUIDE.md** - Week-by-week technical steps
3. **ARCHITECTURE_DIAGRAMS.md** - Visual reference for both options

---

**Questions?** Contact DevOps Lead or review EXECUTIVE_SUMMARY.md for context.
