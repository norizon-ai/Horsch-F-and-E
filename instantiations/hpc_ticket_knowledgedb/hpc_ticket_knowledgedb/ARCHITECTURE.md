# HPC API Scalability Architecture

## Current Architecture (Single Node)

```
┌─────────────────────────────────────────────────────────┐
│                  Docker Compose (Single Host)            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────────────────────────────────────────┐    │
│  │        FastAPI (Single Instance)                 │    │
│  │  - /query, /query/stream, /search, /health       │    │
│  │  - Global dr_workflow (RACE CONDITIONS)          │    │
│  │  - No auth, no rate limiting, no caching         │    │
│  │  - Blocks on 10-120s queries                      │    │
│  └──────────────────────┬──────────────────────────┘    │
│                         │                                │
│  ┌──────────────────────▼──────────────────────────┐    │
│  │    Elasticsearch (Single Node)                   │    │
│  │  - docs, tickets, knowledgebase indices          │    │
│  │  - No connection pooling                         │    │
│  │  - New connection per request                    │    │
│  └──────────────────────────────────────────────────┘    │
│                                                           │
│  ┌──────────────────────────────────────────────────┐    │
│  │  External LLM (lme49.cs.fau.de:30000)            │    │
│  │  - Single endpoint, no fallback                  │    │
│  │  - Blocks API on 10-120s responses               │    │
│  └──────────────────────────────────────────────────┘    │
│                                                           │
└─────────────────────────────────────────────────────────┘

BOTTLENECKS:
1. Single FastAPI instance
2. Shared mutable dr_workflow
3. Blocking on LLM calls
4. No caching or queue
5. No monitoring
```

---

## Phase 1 Architecture (Single Node, Enhanced)

```
┌─────────────────────────────────────────────────────────────┐
│              Docker Compose (Same Single Host)               │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           FastAPI (Same Instance)                     │   │
│  │ ┌────────────────────────────────────────────────┐   │   │
│  │ │ Auth Middleware                               │   │   │
│  │ │ - APIKeyDependency on /query, /search         │   │   │
│  │ └────────────────────────────────────────────────┘   │   │
│  │ ┌────────────────────────────────────────────────┐   │   │
│  │ │ Rate Limit Middleware                         │   │   │
│  │ │ - slowapi limiter                             │   │   │
│  │ │ - 10/min /query, 30/min /search               │   │   │
│  │ └────────────────────────────────────────────────┘   │   │
│  │ ┌────────────────────────────────────────────────┐   │   │
│  │ │ Input Validation                              │   │   │
│  │ │ - Pydantic validators                         │   │   │
│  │ │ - Reject injection patterns                   │   │   │
│  │ └────────────────────────────────────────────────┘   │   │
│  │ ┌────────────────────────────────────────────────┐   │   │
│  │ │ Response Cache                                │   │   │
│  │ │ - In-memory LRU cache                         │   │   │
│  │ │ - 24h TTL, hash(query:iterations) key         │   │   │
│  │ │ - 20-40% hit rate expected                    │   │   │
│  │ └────────────────────────────────────────────────┘   │   │
│  │                                                       │   │
│  │  Endpoints:                                           │   │
│  │  - GET  /health                        [Public]      │   │
│  │  - POST /query                        [Auth]         │   │
│  │  - POST /query/stream                 [Auth]         │   │
│  │  - POST /search                       [Auth]         │   │
│  │  - GET  /cache/stats                  [Auth]         │   │
│  │  - POST /auth/generate-key            [Admin]        │   │
│  │  - GET  /auth/keys                    [Admin]        │   │
│  └──────────────────────────────────────────────────────┘   │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐   │
│  │    Elasticsearch (Single Node)                       │   │
│  │  - Connection pooling (maxsize=25)                  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  External LLM                                        │   │
│  │  - Still blocks API calls                           │   │
│  │  - No queue/async yet                               │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘

IMPROVEMENTS:
+ Authentication (SEC-002)
+ Rate limiting (SEC-007)
+ Input validation & sanitization
+ Response caching (20-40% faster)
+ CORS hardening (SEC-001)
+ Startup validation

REMAINING BOTTLENECKS:
- Still blocks on LLM calls
- Single shared dr_workflow (REL-001)
- No async job processing
- No monitoring (QUA-005)
```

---

## Phase 2 Architecture (Medium-Term)

```
┌──────────────────────────────────────────────────────────────┐
│                  Docker Compose                              │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│ CLIENT                                                        │
│   │                                                           │
│   ├─ POST /query ──────────────────────────┐                │
│   │                                         ▼                │
│   │ ┌───────────────────────────────────────────────────┐   │
│   │ │      FastAPI (Single Instance, Stateless)        │   │
│   │ │                                                   │   │
│   │ │  + Auth/Rate Limit/Validation (Phase 1)          │   │
│   │ │  + Response Cache (Phase 1)                       │   │
│   │ │                                                   │   │
│   │ │  NEW:                                             │   │
│   │ │  - /query/async → returns job_id immediately    │   │
│   │ │  - /query (old) → still available (blocks)       │   │
│   │ │  - /jobs/{job_id} → poll for results             │   │
│   │ │  - Workflow pool with semaphore (max=3)          │   │
│   │ │  - Metrics endpoint /metrics (Prometheus)        │   │
│   │ │  - Structured JSON logging                       │   │
│   │ │                                                   │   │
│   └───────────────────────┬───────────────────────────┘   │
│                           │                                 │
│                    ┌──────▼──────┐                         │
│                    │ Check cache │                         │
│                    ├─────────────┤                         │
│                    │  Hit (60%)  │─────────┐              │
│                    └──────┬──────┘         │              │
│                    │ Miss (40%) │         │              │
│                    │            │         │              │
│                    ▼            │         │              │
│    ┌─────────────────────────┐  │         │              │
│    │  Redis Queue (RQ)       │  │         │              │
│    │                         │  │         │              │
│    │  - Query job submitted  │  │         │              │
│    │  - Returns job_id       │  │         │              │
│    │  - Status: pending      │  │         │              │
│    └─────────────┬───────────┘  │         │              │
│                  │              │         │              │
│    ┌─────────────▼───────────┐  │         │              │
│    │  Query Workers (RQ)     │  │         │              │
│    │                         │  │         │              │
│    │  - 2-4 workers          │  │         │              │
│    │  - Pull from queue      │  │         │              │
│    │  - Max timeout: 5 min   │  │         │              │
│    │  - Status: processing   │  │         │              │
│    │                         │  │         │              │
│    │  [Worker 1]             │  │         │              │
│    │  [Worker 2]             │  │         │              │
│    │  [Worker 3]             │  │         │              │
│    └─────────────┬───────────┘  │         │              │
│                  │              │         │              │
│    ┌─────────────▼───────────┐  │         │              │
│    │  Workflow Execution     │  │         │              │
│    │                         │  │         │              │
│    │  - Dedicated instance   │  │         │              │
│    │  - Max 10-120s latency  │  │         │              │
│    │  - Queries Elasticsearch│  │         │              │
│    │  - Calls LLM            │  │         │              │
│    │  - Returns result       │  │         │              │
│    │  - Status: completed    │  │         │              │
│    └─────────────┬───────────┘  │         │              │
│                  │              │         │              │
│    ┌─────────────▼───────────┐  │         │              │
│    │  Redis (Cache + Queue)  │  │         │              │
│    │                         │  │         │              │
│    │  - Jobs by ID           │  │         │              │
│    │  - Result cache (24h)   │  │         │              │
│    │  - TTL: 24h             │  │         │              │
│    │  - Max items: ~10k      │  │         │              │
│    └────────────────────────┘   │         │              │
│                                  │         │              │
│    ┌──────────────────────────┐  │         │              │
│    │  Elasticsearch           │  │         │              │
│    │  - Connection pool       │  │         │              │
│    │  - Maxsize: 25           │  │         │              │
│    └──────────────────────────┘  │         │              │
│                                  │         │              │
│    ┌──────────────────────────┐  │         │              │
│    │  Prometheus Metrics      │  │         │              │
│    │  - Request latency       │  │         │              │
│    │  - Error rates           │  │         │              │
│    │  - Job queue depth       │  │         │              │
│    │  - Cache hit rate        │  │         │              │
│    │  - Elasticsearch latency │  │         │              │
│    │  - LLM response time     │  │         │              │
│    └──────────────────────────┘  │         │              │
│                                  │         │              │
│    ┌──────────────────────────┐  │         │              │
│    │  Structured Logging      │  │         │              │
│    │  - JSON format           │  │         │              │
│    │  - Log aggregation ready │  │         │              │
│    └──────────────────────────┘  │         │              │
│                                  │         │              │
│   GET /jobs/{job_id} ◄───────────┴─────────┘              │
│   - Returns cached result if available                     │
│   - Returns pending/processing if not ready                │
│                                                             │
│   GET /cache/stats ◄──────────────────────────────────┐   │
│   - Hit rate: 45.2%                                   │   │
│   - Items cached: 523                                 │   │
│                                                         │   │
└──────────────────────────────────────────────────────────┘

IMPROVEMENTS:
+ Async job processing (no more blocking)
+ Query workers scale independently
+ Connection pooling to Elasticsearch
+ Full observability (Prometheus + structured logs)
+ Handles 10+ concurrent requests

REMAINING BOTTLENECKS:
- Single host (all services on one machine)
- Single API instance
- Redis not replicated
- No horizontal scaling yet
```

---

## Phase 3 Architecture (Long-Term Scaling)

```
                        CLIENT REQUESTS
                              │
                    ┌─────────┴─────────┐
                    │                   │
            ┌───────▼────────────────────────────────┐
            │  Load Balancer (Nginx/HAProxy)         │
            │  - Round-robin across API pods         │
            │  - Health checks every 30s             │
            │  - TLS termination                     │
            │  - Session affinity (if needed)        │
            └───────┬────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
    ┌───▼──┐    ┌───▼──┐    ┌───▼──┐
    │ API  │    │ API  │    │ API  │   (Kubernetes Deployment)
    │ Pod1 │    │ Pod2 │    │ Pod3 │   - Replicas: 3-10
    │      │    │      │    │      │   - HPA on CPU/Memory
    └───┬──┘    └───┬──┘    └───┬──┘   - Rolling updates
        │           │           │
        └───────────┴───────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
    ┌───▼──────────┐       ┌───▼──────────┐
    │ Redis Cluster│       │PostgreSQL    │
    │              │       │              │
    │ - Cache      │       │ - API keys   │
    │ - Queue      │       │ - Job history│
    │ - Sessions   │       │ - Config     │
    │              │       │              │
    │ (3+ nodes)   │       │ (HA replica) │
    └───┬──────────┘       └──────────────┘
        │
    ┌───▼──────────────────────────┐
    │ Elasticsearch Cluster         │
    │                              │
    │ - 3+ nodes                   │
    │ - Sharded indices            │
    │ - Replicas for HA            │
    │ - Snapshot to S3             │
    └──────────────────────────────┘
        │
    ┌───▼──────────────────────────┐
    │ RQ Worker Pool (Autoscaling)  │
    │                              │
    │ - 5-20 workers (HPA)         │
    │ - Priority queues            │
    │ - Job stealing               │
    │ - Resource limits            │
    └──────────────────────────────┘
        │
    ┌───▼──────────────────────────┐
    │ External LLM Service          │
    │                              │
    │ - With retry logic           │
    │ - Circuit breaker           │
    │ - Fallback models           │
    └──────────────────────────────┘
        │
    ┌───┴──────────────────────────┐
    │ Observability Stack           │
    │                              │
    │ - Prometheus (metrics)       │
    │ - Grafana (dashboards)       │
    │ - ELK Stack (logging)        │
    │ - Jaeger (tracing)          │
    └──────────────────────────────┘

KUBERNETES RESOURCES:
- Deployment: hpc-api (3-10 replicas)
- Deployment: rq-worker (5-20 workers)
- StatefulSet: elasticsearch (3 nodes)
- StatefulSet: redis (3 nodes)
- Deployment: prometheus
- Deployment: grafana
- Service: hpc-api-service (load balanced)
- Service: elasticsearch-service
- Service: redis-service
- Ingress: TLS frontend
- HPA: API and workers autoscale

IMPROVEMENTS:
+ Horizontal scaling (10+ instances)
+ High availability (multi-node)
+ Auto-scaling based on load
+ Load balancing
+ Rolling updates (zero downtime)
+ Persistent storage for data services
+ Full observability
+ Disaster recovery (backups)

SUPPORTS:
- 1000+ concurrent users
- 10k+ queries/hour
- 99.95% uptime SLO
```

---

## Data Flow Comparison

### Phase 1: Query Processing (Blocking)

```
Client
  │
  ├─ POST /query
  │    │
  │    ├─ Auth check [50ms]
  │    ├─ Rate limit check [10ms]
  │    ├─ Input validation [20ms]
  │    ├─ Cache lookup [5ms] ─ HIT
  │    │
  │    ├─ Cache MISS
  │    │
  │    ├─ Elasticsearch search [200ms]
  │    ├─ LLM call [10-120s]
  │    ├─ Process result [500ms]
  │    ├─ Cache result [10ms]
  │    │
  │    └─ Return result [10-120s total]
  │
  └─ (Client blocked entire time)
```

### Phase 2: Async Query Processing

```
Client
  │
  ├─ POST /query/async
  │    │
  │    ├─ Auth check [50ms]
  │    ├─ Rate limit check [10ms]
  │    ├─ Input validation [20ms]
  │    ├─ Cache lookup [5ms] ─ HIT ─ Return immediately [100ms]
  │    │
  │    ├─ Cache MISS
  │    │
  │    ├─ Queue to Redis [20ms]
  │    │
  │    └─ Return job_id [100ms total]
  │
  │ (Client continues, polls for result)
  │
  ├─ GET /jobs/{job_id}
  │    │
  │    ├─ Check Redis [10ms]
  │    │
  │    ├─ If pending: return {status: "processing"} [20ms]
  │    ├─ If done: return cached result [30ms]
  │    │
  │    └─ Return result [30ms]
  │
  ├─ Meanwhile in background:
  │    │
  │    ├─ RQ Worker picks up job
  │    ├─ Elasticsearch search [200ms]
  │    ├─ LLM call [10-120s]
  │    ├─ Process result [500ms]
  │    ├─ Store in Redis [10ms]
  │    │
  │    └─ Client polls /jobs/{job_id} until done
  │
  └─ Total perceived latency: 100ms + polling interval
```

### Phase 3: Distributed with Multiple Caches

```
Client
  │
  ├─ POST /query/async (hits API pod via LB)
  │    │
  │    ├─ Local L1 cache [5ms] ─ HIT ─ Return [100ms]
  │    │
  │    ├─ L1 MISS
  │    │
  │    ├─ Redis L2 cache [15ms] ─ HIT ─ Return [100ms]
  │    │
  │    ├─ L2 MISS
  │    │
  │    ├─ Queue to Redis cluster [20ms]
  │    │
  │    └─ Return job_id [100ms]
  │
  │ (Client polls)
  │
  ├─ GET /jobs/{job_id} (may hit different API pod)
  │    │
  │    ├─ Check Redis cluster [10ms] ─ HIT ─ Return [30ms]
  │    │
  │    └─ Fast even with different pod
  │
  ├─ Meanwhile in background:
  │    │
  │    ├─ RQ worker from pool
  │    ├─ Elasticsearch cluster query [300ms]
  │    ├─ LLM call with retry [10-120s]
  │    ├─ Result stored in Redis cluster
  │    │
  │    └─ Next poll hits cache, returns result
  │
  └─ Total: 100ms initial + 30ms per poll
```

---

## Cost & Performance Summary

| Metric | Phase 1 | Phase 2 | Phase 3 |
|--------|---------|---------|---------|
| **Concurrency** | 1 user | 10+ users | 1000+ users |
| **Queries/Hour** | ~10 | ~500 | 10k+ |
| **Latency p95** | 120s | 60s | 20s |
| **Cache Hit %** | 0% | 25% | 50%+ |
| **Uptime SLO** | None | 99.9% | 99.95% |
| **Servers** | 1 | 1-2 | 10+ |
| **Redis** | None | 1 | 3 (cluster) |
| **ES Nodes** | 1 | 1 | 3+ |
| **Dev Cost** | 1 FTE x 2 wks | 2 FTE x 6 wks | 3 FTE x 12 wks |
| **Ops Cost** | Low | Medium | High |

---

## Migration Path

```
┌─────────────────────────────────────────────────────┐
│ Current: Single Docker, No Auth, Race Conditions    │
└──────────────────┬──────────────────────────────────┘
                   │ (Week 1-2: Phase 1)
                   │ + Auth + Rate Limit + Cache
                   │
┌──────────────────▼──────────────────────────────────┐
│ Phase 1: Single Node, Enhanced Security             │
│ - Still blocking on queries                         │
│ - 50-100 concurrent users                           │
└──────────────────┬──────────────────────────────────┘
                   │ (Week 3-8: Phase 2)
                   │ + RQ Queue + Workers + Monitoring
                   │
┌──────────────────▼──────────────────────────────────┐
│ Phase 2: Single Node, Async Processing              │
│ - Background job execution                          │
│ - 300+ concurrent users                             │
│ - Full observability                                │
└──────────────────┬──────────────────────────────────┘
                   │ (Month 3-6: Phase 3)
                   │ + Kubernetes + Autoscaling + HA
                   │
┌──────────────────▼──────────────────────────────────┐
│ Phase 3: Kubernetes, Distributed                    │
│ - Horizontal scaling                                │
│ - 1000+ concurrent users                            │
│ - High availability & DR                            │
└─────────────────────────────────────────────────────┘

NO BREAKING CHANGES:
- /query endpoint stays (backward compatible)
- /query/async added (optional)
- Existing clients continue working
```

---

## Infrastructure Requirements

### Phase 1 (Add to current)
- Redis: 512MB RAM container
- Prometheus: 1GB disk
- No additional servers needed
- Same Docker Compose host

### Phase 2 (Add to Phase 1)
- RQ workers: 2-4 containers
- Additional 1-2GB RAM for worker processes
- Same Docker Compose host (or split workers to separate host)

### Phase 3 (New deployment)
- Kubernetes cluster (3+ nodes recommended)
- Load balancer (Nginx Ingress or external LB)
- Redis cluster (3 nodes minimum)
- Elasticsearch cluster (3 nodes minimum)
- PostgreSQL (1 primary + 1 replica)
- Prometheus + Grafana
- Total: 15-20 containers across 3-5 nodes

---

## Validation Checklist

### Phase 1 Done When:
- [ ] All endpoints require API key
- [ ] Rate limiting returns 429 after limit
- [ ] Invalid queries rejected at validation
- [ ] Cache stats show > 0 hits
- [ ] Startup fails if ES/LLM unavailable

### Phase 2 Done When:
- [ ] /query/async returns job_id in < 200ms
- [ ] /jobs/{job_id} polls return status
- [ ] Workers process 10+ jobs in parallel
- [ ] Prometheus scrape target active
- [ ] JSON logs in elasticsearch format

### Phase 3 Done When:
- [ ] Kubernetes deployment healthy
- [ ] 5+ API replicas running
- [ ] HPA scales workers 5-20
- [ ] Load balancer distributes traffic
- [ ] 99.95% uptime over 24h window
