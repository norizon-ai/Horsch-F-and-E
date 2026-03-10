# HPC Knowledge Database: Architecture Diagrams & Quick Reference

---

## CURRENT STATE (CRITICAL ISSUES)

```
┌─────────────────────────────────────────────────┐
│            Single OpenStack VM                   │
│          4 vCPU, 16GB RAM, 100GB SSD            │
├─────────────────────────────────────────────────┤
│
│  ┌─────────────────────────────────────────┐
│  │   Docker Compose (all containers)       │
│  │                                         │
│  │  ┌──────────────────────────────────┐  │
│  │  │   Elasticsearch (Single Node)     │  │
│  │  │   - No HA                         │  │
│  │  │   - No clustering                 │  │
│  │  │   - Single disk = SPF             │  │
│  │  │   - No security (xpack off)       │  │
│  │  └──────────────────────────────────┘  │
│  │            ↑↓                            │
│  │  ┌──────────────────────────────────┐  │
│  │  │   FastAPI + Gunicorn             │  │
│  │  │   - Single instance              │  │
│  │  │   - No load balancer             │  │
│  │  │   - No horizontal scaling        │  │
│  │  │   - No resource limits (OPS-002) │  │
│  │  └──────────────────────────────────┘  │
│  │
│  │  ┌──────────────────────────────────┐  │
│  │  │   Indexer (Docker)               │  │
│  │  │   - On-demand only               │  │
│  │  │   - Manual invocation            │  │
│  │  └──────────────────────────────────┘  │
│  │
│  └─────────────────────────────────────────┘
│
│  NO: Caching, Monitoring, Backup, Clustering
│
└─────────────────────────────────────────────────┘

PROBLEMS:
- VM failure = 100% downtime (SPOF)
- No failover capability
- No backup (OPS-001) → Data loss risk
- No monitoring → Invisible failures
- No resource limits → Possible OOM crashes
- No API auth → Public access
```

---

## OPTION A: ENHANCED OPENSTACK (Recommended for Phase 1)

### Architecture (After 8 Weeks)

```
┌────────────────────────────────────────────────────────────┐
│                 OpenStack (DE-ERL Region)                  │
├────────────────────────────────────────────────────────────┤
│
│  ┌──────────────────────────────────────────────────────┐
│  │              Public/Internal Network                 │
│  │  (10.240.60.0/24 with floating IP pool)             │
│  └──────────────────────────────────────────────────────┘
│                        ↑ (Port 8001)
│  ┌──────────────────────────────────────────────────────┐
│  │                 HAProxy Load Balancer               │
│  │           (VM: 2 vCPU, 4GB, health checks)          │
│  └──────────────────────────────────────────────────────┘
│       ↓              ↓              ↓
│   Port 8000      Port 8000      Port 8000
│
│  ┌────────────┐  ┌────────────┐  ┌────────────┐
│  │   API-1    │  │   API-2    │  │   API-3    │
│  │ 2v/8GB RAM │  │ 2v/8GB RAM │  │ 2v/8GB RAM │
│  │  FastAPI   │  │  FastAPI   │  │  FastAPI   │
│  │ Gunicorn-4 │  │ Gunicorn-4 │  │ Gunicorn-4 │
│  │ workers    │  │ workers    │  │ workers    │
│  └────────────┘  └────────────┘  └────────────┘
│         ↓              ↓              ↓
│    localhost:9200 → Elasticsearch Cluster
│         ↓              ↓              ↓
│  ┌────────────┐  ┌────────────┐  ┌────────────┐
│  │ ES-Master  │  │ ES-Data-1  │  │ ES-Data-2  │
│  │ 2v/8GB RAM │  │ 4v/16GB    │  │ 4v/16GB    │
│  │   ACTIVE   │  │ 250GB vol  │  │ 250GB vol  │
│  │            │  │            │  │            │
│  │ No data    │  │ Shards     │  │ Shards     │
│  │ only coord │  │ & replicas │  │ & replicas │
│  └────────────┘  └────────────┘  └────────────┘
│         ↓ (Port 6379)
│  ┌────────────────────────────────────────────┐
│  │         Redis Cluster (3 nodes)            │
│  │   Redis-1    Redis-2    Redis-3            │
│  │   (leader)   (replica)  (replica)          │
│  │  1v/4GB      1v/4GB     1v/4GB             │
│  │  Caching, query result TTL, session store  │
│  └────────────────────────────────────────────┘
│
│  ┌──────────────────────────────────────────────┐
│  │   Monitoring Stack (monitoring-vm)           │
│  │   2 vCPU, 8GB RAM                           │
│  │                                              │
│  │  ┌──────────────────────────────────────┐  │
│  │  │  Prometheus (scrape every 15s)       │  │
│  │  │  - API metrics, ES health, cache     │  │
│  │  │  - Retention: 30 days                │  │
│  │  └──────────────────────────────────────┘  │
│  │
│  │  ┌──────────────────────────────────────┐  │
│  │  │  Grafana (dashboards)                │  │
│  │  │  - Request latency, error rates      │  │
│  │  │  - ES cluster health                 │  │
│  │  │  - Cache hit/miss rates              │  │
│  │  │  - Redis memory usage                │  │
│  │  └──────────────────────────────────────┘  │
│  │
│  │  ┌──────────────────────────────────────┐  │
│  │  │  AlertManager                        │  │
│  │  │  - Route alerts to email/Slack       │  │
│  │  │  - Critical: ES red, API down        │  │
│  │  │  - Warning: disk >80%, memory >85%   │  │
│  │  └──────────────────────────────────────┘  │
│  │
│  └──────────────────────────────────────────────┘
│
│  ┌──────────────────────────────────────────────┐
│  │   Backup Storage (Object Storage)            │
│  │                                              │
│  │  - Daily ES snapshots (100GB)               │
│  │  - Redis RDB backups (hourly)               │
│  │  - Retention: 30 days                       │
│  │  - €50/month storage cost                   │
│  │                                              │
│  └──────────────────────────────────────────────┘
│
└────────────────────────────────────────────────────────────┘

TOTAL INFRASTRUCTURE:
- 9 VMs (24 vCPUs total, 80GB RAM)
- 500GB block storage (ES data)
- 500GB object storage (backups)
- Cost: €3,950/month (production-ready)
```

### Scalability Path

```
LOAD INCREASE RESPONSE:

100 req/s (Month 1)
    ↓
Current setup: 3 API instances, 2 ES data nodes
CPU: 40%, Memory: 60%, Disk: 20%
Status: Comfortable headroom
    ↓ Add monitoring & caching
    ↓
300 req/s (Month 3)
    ↓
Decision point: Scale or accept limits?
Option 1: Add 2 API instances (€500/month)
Option 2: Optimize queries, increase cache hit rate
Option 3: Migrate to AWS (Option B)
    ↓
500 req/s (Month 6)
    ↓
Add ES data node 3 (€250/month)
Add API instances 4-5 (€500/month)
Total scale: 3 API + 3 ES nodes, 5-node Redis
    ↓
1000+ req/s (Outgrow OpenStack)
    ↓
Migrate to AWS or Kubernetes option
```

---

## OPTION B: AWS ARCHITECTURE (Recommended Long-term)

### Architecture (After 7 Weeks)

```
┌──────────────────────────────────────────────────────────────┐
│                      AWS Region (eu-west-1)                  │
├──────────────────────────────────────────────────────────────┤
│
│                    INTERNET (CloudFront CDN)
│                           ↓
│  ┌────────────────────────────────────────────────────────┐
│  │              Application Load Balancer (ALB)           │
│  │  - Health checks every 5s                             │
│  │  - Sticky sessions (optional)                         │
│  │  - TLS termination                                    │
│  └────────────────────────────────────────────────────────┘
│                    ↓        ↓        ↓        ↓
│            (Auto-scaling between 2-20 tasks)
│
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
│  │Fargate │  │Fargate │  │Fargate │  │Fargate │  ...
│  │Task 1  │  │Task 2  │  │Task 3  │  │Task N  │
│  │0.5 vCPU│  │0.5 vCPU│  │0.5 vCPU│  │0.5 vCPU│
│  │2GB RAM │  │2GB RAM │  │2GB RAM │  │2GB RAM │
│  │FastAPI │  │FastAPI │  │FastAPI │  │FastAPI │
│  │        │  │        │  │        │  │        │
│  │Triggers:  │        │  │        │  │        │
│  │CPU >70%   │        │  │        │  │        │
│  │Memory >85%│        │  │        │  │        │
│  └────────┘  └────────┘  └────────┘  └────────┘
│         ↓                       ↓
│  ┌──────────────────────────────────────┐
│  │      OpenSearch (Managed)            │
│  │   3 nodes (multi-AZ enabled)         │
│  │                                      │
│  │  ┌─────────┐  ┌─────────┐          │
│  │  │ Node 1  │  │ Node 2  │  Node 3  │
│  │  │ r5.xl   │  │ r5.xl   │ r5.xl    │
│  │  │ AZ: a   │  │ AZ: b   │ AZ: c    │
│  │  └─────────┘  └─────────┘          │
│  │                                      │
│  │  - Warm/cold tier (auto lifecycle)   │
│  │  - Snapshots every 5 min to S3       │
│  │  - Automatic failover                │
│  │  - Scaling: storage auto-grows       │
│  └──────────────────────────────────────┘
│         ↓
│  ┌──────────────────────────────────────┐
│  │    ElastiCache Redis (Managed)       │
│  │                                      │
│  │  ┌─────────┐  ┌─────────┐          │
│  │  │ Primary │  │ Replica │          │
│  │  │ r6g.xl  │  │ r6g.xl  │          │
│  │  │ AZ: a   │  │ AZ: b   │          │
│  │  └─────────┘  └─────────┘          │
│  │                                      │
│  │  - Multi-AZ replication              │
│  │  - Auto-failover <30s                │
│  │  - 256GB max memory                  │
│  │  - Encryption in transit/rest        │
│  └──────────────────────────────────────┘
│         ↓
│  ┌──────────────────────────────────────┐
│  │      RDS Aurora PostgreSQL (opt)     │
│  │  (For API keys, job history, state)  │
│  │                                      │
│  │  - Serverless v2 (pay per second)    │
│  │  - Auto-scaling 0.5-1 ACU            │
│  │  - Automatic backups (7 days)        │
│  │  - Read replicas in other AZs        │
│  └──────────────────────────────────────┘
│         ↓
│  ┌──────────────────────────────────────┐
│  │      S3 (Data & Backups)             │
│  │                                      │
│  │  - Versioning enabled                │
│  │  - Lifecycle: 30 days → Glacier      │
│  │  - Encryption: SSE-S3                │
│  │  - Cost: €150/month @ 500GB          │
│  └──────────────────────────────────────┘
│
│  ┌──────────────────────────────────────┐
│  │    CloudWatch (Monitoring)           │
│  │                                      │
│  │  - Metrics: automatic collection    │
│  │  - Logs: application logs auto      │
│  │  - Alarms: cost, performance        │
│  │  - Dashboards: pre-built templates  │
│  │  - Cost: ~€100/month                │
│  └──────────────────────────────────────┘
│
│  ┌──────────────────────────────────────┐
│  │    Route53 (Multi-region DR)         │
│  │                                      │
│  │  - Primary: eu-west-1 (Ireland)     │
│  │  - Failover: eu-central-1 (Frankfurt)
│  │  - Health-based routing              │
│  │  - RPO: 5 minutes (sync replication) │
│  │  - RTO: 30 seconds (auto failover)  │
│  │  - Cost: +€1,500/month (standby)    │
│  └──────────────────────────────────────┘
│
└──────────────────────────────────────────────────────────────┘

TOTAL INFRASTRUCTURE:
- Fargate tasks: 2-20 (auto-scales)
- OpenSearch: 3 nodes (r5.xlarge)
- ElastiCache: 2 nodes (r6g.xlarge)
- RDS Aurora: 0.5-1 ACU serverless
- S3: 500GB baseline
- Cost: €2,530/month baseline (single region)
- Cost: €4,030/month with multi-region DR
```

### Auto-scaling Behavior

```
FARGATE AUTO-SCALING (ECS):

Time: 09:00 - Quiet morning
Metrics: CPU 15%, Memory 20%
Active tasks: 2 (minimum)
Cost: €32/month

Time: 12:00 - Lunch rush
Metrics: CPU 72%, Memory 78%
Auto-scaling triggered (>70% threshold)
Tasks: 2 → 5 (30 seconds)
Cost: €80/month

Time: 13:00 - Heavy usage
Metrics: CPU 85%, Memory 92%
Auto-scaling triggered again
Tasks: 5 → 12 (60 seconds)
Cost: €192/month

Time: 14:00 - Peak usage
Metrics: CPU 78%, Memory 85%
Stable at 12 tasks
Cost: €192/month
Queue depth: 0 (no backlog)

Time: 18:00 - Evening taper
Metrics: CPU 30%, Memory 35%
Auto-scaling down
Tasks: 12 → 8 → 4 → 2
Cost: ~€64/month

TIME-BASED PATTERN (Weekly):
- Mon-Fri 08:00-18:00: 8-15 tasks (peak hours)
- Evenings: 2-4 tasks
- Weekends: 2 tasks
- Overnight: 2 tasks (minimum)

MONTHLY VARIATION:
- Beginning of month: 12-15 tasks (billing questions)
- Mid-month: 8-10 tasks
- End of month: 5-8 tasks
- Avg: 8 tasks

Cost scales with actual usage (no over-provisioning needed)
```

---

## COMPARISON: INFRASTRUCTURE PATTERNS

### Load Balancing

```
OPTION A (OpenStack):
┌─────────┐
│ HAProxy │  Manual LB, health checks every 3s
│  (VM)   │  No auto-scaling, requires config changes
└─────────┘
     ↓
┌─────────┐  ┌─────────┐  ┌─────────┐
│  API-1  │  │  API-2  │  │  API-3  │
└─────────┘  └─────────┘  └─────────┘

OPTION B (AWS):
┌─────────┐
│   ALB   │  Managed LB, health checks every 5s
│ (AWS)   │  Auto-scaling: 2-20 tasks automatically
└─────────┘
     ↓
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│Task 1   │  │Task 2   │  │Task 3   │  │Task N   │
│(Fargate)│  │(Fargate)│  │(Fargate)│  │(Fargate)│
└─────────┘  └─────────┘  └─────────┘  └─────────┘

Advantage Option B: Auto-scaling saves 73% ops time
```

### Storage Management

```
OPTION A (OpenStack):
- Manual volume management (500GB allocated)
- Manual snapshot creation (cron job)
- Manual restoration (SSH + rsync + import)
- Snapshot cost: €50/month fixed
- Disk runs full? Manual cleanup required
- Time to restore: 30-60 minutes

OPTION B (AWS):
- Automatic storage scaling (grows as needed, pay per GB)
- Automatic snapshots (every 5 minutes)
- 1-click restoration
- Snapshot cost: Included in OpenSearch pricing
- Disk runs full? Automatically expands
- Time to restore: <5 minutes
```

### Disaster Recovery

```
OPTION A (OpenStack):
Week 1:
├─ Snapshot created
├─ Stored to object storage
└─ Manual testing (2 hours, scheduled)

Week 2: Full DR test
├─ Provision new VMs (20 min)
├─ Restore Elasticsearch (60 min)
├─ Validate data (20 min)
├─ Update DNS (5 min)
└─ TOTAL RTO: 105 minutes

Data loss: Up to 1 hour (last snapshot)
Testing: Quarterly (manual)


OPTION B (AWS):
Continuous (automatic):
├─ Snapshots every 5 minutes
├─ Replication to backup region (async)
└─ Auto-test of restore capability

RTO: 30 seconds (automatic failover)
RPO: 5 minutes (latest snapshot)
Testing: Continuous (chaos engineering)
```

---

## COST BREAKDOWN EXAMPLES

### Scenario 1: 100 req/s Load (Month 6)

**OPTION A:**
```
Infrastructure:
├─ 9 VMs (24 vCPU @ €150/vCPU): €3,600
├─ Block storage (500GB @ €0.50/GB): €250
├─ Object storage (backups): €50
└─ Bandwidth: €50
Total: €3,950/month

Operations (estimated):
├─ Monitoring/alerts: 8h/week
├─ Performance tuning: 6h/month
├─ Backup verification: 2h/week
├─ Incident response: 20h/month (avg 2 incidents)
└─ Total: ~80h/month = €6,400
Monthly Total: €10,350
```

**OPTION B:**
```
Infrastructure:
├─ Fargate (8 tasks avg, 0.5vCPU, 2GB): €320
├─ OpenSearch (3 r5.xlarge nodes): €1,200
├─ ElastiCache (2 r6g.xlarge nodes): €400
├─ RDS Aurora serverless: €100
├─ S3 storage (500GB @ €0.023/GB): €150
├─ CloudWatch (logs + metrics): €100
├─ ALB (hourly + requests): €200
└─ Data egress (100GB @ €0.10/GB): €80
Total: €2,530/month

Operations (estimated):
├─ Cost optimization reviews: 4h/month
├─ CloudWatch dashboard review: 2h/week
├─ Security audits: 4h/quarter
└─ Total: ~15h/month = €1,200
Monthly Total: €3,730

Savings: €6,620/month (64% less expensive to operate)
```

### Scenario 2: 1000 req/s Load (Year 2)

**OPTION A:**
```
Infrastructure:
├─ 15 VMs (50 vCPU @ €150/vCPU): €7,500
├─ Block storage (1TB @ €0.50/GB): €500
├─ Object storage (multi-region): €200
└─ Bandwidth: €200
Total: €8,400/month = €100,800/year

Operations:
├─ Larger team (3-4 engineers)
├─ More incidents (3-5/month)
├─ Capacity planning, tuning
└─ Total: ~150h/month = €12,000
Annual: €144,000/year

3-Year Cost (assuming 50% growth/year):
Year 1: €60K infrastructure + €76K ops = €136K
Year 2: €100K infrastructure + €144K ops = €244K
Year 3: €150K infrastructure + €216K ops = €366K
TOTAL: €746K
```

**OPTION B:**
```
Infrastructure:
├─ Fargate (15 tasks avg, with RIs): €500/month
├─ OpenSearch (4 instances, with RIs): €1,200/month
├─ ElastiCache (3 nodes, with RIs): €500/month
├─ RDS Aurora (1-2 ACU): €200/month
├─ S3 + egress: €250/month
├─ Monitoring: €100/month
├─ Network + misc: €100/month
Total: €2,850/month = €34,200/year

Operations:
├─ 1-2 engineers (cloud-native tooling)
├─ Fewer incidents (automated ops)
├─ Mostly observability review
└─ Total: ~40h/month = €3,200
Annual: €38,400/year

3-Year Cost (with 1-year RIs purchased):
Year 1: €30K infrastructure + €20K ops + €10K RI = €60K
Year 2: €30K infrastructure (amortized RI) + €16K ops = €46K
Year 3: €30K infrastructure + €16K ops = €46K
TOTAL: €152K

Savings over 3 years: €594K (79% less expensive)
```

---

## METRICS & DASHBOARDS

### Key Metrics to Monitor (Both Options)

**API Performance:**
```
- Requests/sec (target: 500)
- Response latency (p50, p95, p99)
- Error rate (target: <0.1%)
- Cache hit rate (target: >50%)
- Queue depth (RQ jobs pending)
```

**Elasticsearch Health:**
```
- Cluster status (green/yellow/red)
- Disk usage (alert >80%)
- CPU usage (alert >80%)
- JVM memory (alert >85%)
- Query latency (p95, p99)
- Indexing rate (docs/sec)
```

**Infrastructure:**
```
- Container/instance CPU (alert >75%)
- Container/instance memory (alert >85%)
- Network latency (intra-service)
- Volume usage (alert >80%)
- Cost (monthly spend vs. budget)
```

---

## DECISION MATRIX: QUICK REFERENCE

| Decision Point | Option A | Option B |
|---|---|---|
| **Upfront effort** | 8 weeks | 7 weeks |
| **Monthly cost** | €3,950 | €2,530 |
| **Ops time/month** | 80 hours | 15 hours |
| **HA approach** | Manual | Automatic |
| **Scaling** | Manual (predictable) | Automatic (elastic) |
| **Disaster recovery** | Manual (4h RTO) | Automated (30s RTO) |
| **Team expertise needed** | Linux/ES ops | AWS cloud-native |
| **3-year TCO** | €216,200 | €84,080 |
| **Vendor lock-in** | None | AWS (medium) |

---

**For detailed implementation: See SCALABILITY_PLAN.md**
**For financial analysis: See OPTION_COMPARISON.md**
**For step-by-step deployment: See IMPLEMENTATION_GUIDE.md**
