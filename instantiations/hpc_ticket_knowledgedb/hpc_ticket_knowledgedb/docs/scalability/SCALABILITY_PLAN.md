# HPC Ticket Knowledge Database - Scalability Improvement Plan

## Executive Summary

The HPC Ticket Knowledge Database API is a FastAPI-based Deep Research system processing complex HPC support queries. Current single-instance deployment suffers from security gaps, concurrency bottlenecks, and lack of observability. This plan delivers pragmatic improvements across 3-6 months with FastAPI-compatible technologies.

**Key Metrics:**
- Processing time: 10-120s per query (highly variable)
- Current concurrency: Single DRWorkflow instance (race conditions)
- No authentication, rate limiting, caching, or monitoring
- Single Docker Compose deployment (single-node)

---

## PHASE 1: QUICK WINS (1-2 Weeks) - 8-12 Days Implementation

### 1.1 Authentication Strategy (SEC-002, SEC-001 partial)

**Current Issue:** API completely open - no authentication or authorization checks.

**Solution:** Implement API key authentication with token-based access control using JWT. Simple, stateless, and fits FastAPI patterns.

**Technology:** `python-jose[cryptography]` + `fastapi.security.HTTPBearer`

**Implementation:**
- Generate and store API keys in environment/database
- Create middleware to validate keys on protected endpoints
- Add `/auth/generate-key` endpoint (admin only)
- Mark endpoints with `@protected_endpoint` decorator
- Public endpoints: `/health`, `/` root

**Effort:** 2 days

**Code Sample:**
```python
# api/auth.py
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import hashlib

security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthCredentials = Security(security)) -> str:
    token = credentials.credentials
    # Validate against stored keys
    if not validate_token(token):
        raise HTTPException(status_code=403, detail="Invalid API key")
    return token

# In main.py endpoints
@app.post("/query", dependencies=[Depends(verify_api_key)])
async def process_query(request: QueryRequest):
    ...
```

**CORS Hardening:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # Specific origins
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type", "Authorization"],
)
```

---

### 1.2 Rate Limiting (SEC-007)

**Current Issue:** No rate limiting allows DDoS or resource exhaustion attacks.

**Solution:** Implement token bucket rate limiting per API key using in-memory cache. Simple and effective for single-instance deployment.

**Technology:** `slowapi` (built on `limits`)

**Implementation:**
- 100 requests/minute per API key (configurable)
- Different limits for `/query` (10/min) vs `/search` (50/min)
- Return 429 with Retry-After header
- Log rate limit violations

**Effort:** 1.5 days

**Code Sample:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/query")
@limiter.limit("10/minute")
async def process_query(request: QueryRequest, _=Depends(verify_api_key)):
    return await dr_workflow.process_query(request.query)

@app.post("/search")
@limiter.limit("50/minute")
async def search(request: SearchRequest, _=Depends(verify_api_key)):
    ...
```

---

### 1.3 Input Validation & Sanitization

**Current Issue:** No validation on query input - risks prompt injection and resource exhaustion.

**Solution:** Strict input validation using Pydantic with length limits and sanitization.

**Technology:** Pydantic v2 with Field validators

**Implementation:**
- Query: max 500 chars, alphanumeric + spaces only
- max_iterations: 1-10 (default 3)
- Custom validator for prompt injection prevention
- Reject if confidence score or processing time in response would exceed limits

**Effort:** 1 day

**Code Sample:**
```python
from pydantic import BaseModel, Field, field_validator

class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="HPC support question"
    )
    max_iterations: int = Field(default=3, ge=1, le=10)

    @field_validator('query')
    @classmethod
    def validate_query(cls, v):
        # Reject common injection patterns
        dangerous_patterns = ['__', 'import ', 'exec(', 'eval(']
        if any(pattern in v for pattern in dangerous_patterns):
            raise ValueError("Query contains potentially dangerous patterns")
        # Limit special chars
        if not all(c.isalnum() or c in ' ?,!.' for c in v):
            raise ValueError("Query contains invalid characters")
        return v.strip()
```

---

### 1.4 Response Caching Layer

**Current Issue:** Identical queries re-process entire DR pipeline (10-120s waste).

**Solution:** Add in-memory cache for query results with TTL. Cache hit rate expected 20-40%.

**Technology:** `aiocache` with Redis-compatible memory backend

**Implementation:**
- Cache responses for 24 hours
- Cache key: hash(query, max_iterations)
- Serve cached results if exists and valid
- Cache warming for common queries
- Include cache hit/miss in response headers

**Effort:** 1.5 days

**Code Sample:**
```python
from aiocache import cached, Cache
import hashlib

def get_cache_key(query: str, iterations: int) -> str:
    return hashlib.sha256(f"{query}:{iterations}".encode()).hexdigest()

@app.post("/query")
@cached(cache=Cache.MEMORY, ttl=86400)  # 24h TTL
async def process_query(request: QueryRequest):
    cache_key = get_cache_key(request.query, request.max_iterations)

    # Check cache
    cached_result = await cache.get(cache_key)
    if cached_result:
        return {**cached_result, "cached": True, "cache_age_seconds": ...}

    # Process and cache
    result = await dr_workflow.process_query(request.query)
    await cache.set(cache_key, result.dict(), ttl=86400)
    return {**result.dict(), "cached": False}
```

---

### 1.5 Health Check & Startup Validation

**Current Issue:** API starts even if Elasticsearch or LLM unavailable.

**Solution:** Fail fast on startup if critical services unavailable. Add detailed health checks.

**Technology:** FastAPI lifespan context manager

**Effort:** 0.5 days

**Code Sample:**
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting HPC DR API...")

    # Validate critical services
    es_ok = await search_service.initialize()
    if not es_ok:
        raise RuntimeError("Elasticsearch unavailable at startup")

    llm_ok = await test_llm_connection()
    if not llm_ok:
        raise RuntimeError("LLM endpoint unavailable")

    yield

    # Shutdown
    print("Shutting down HPC DR API...")

app = FastAPI(lifespan=lifespan)
```

**Phase 1 Timeline:**
- Days 1-2: Auth + API key generation
- Days 3-4: Rate limiting
- Days 5: Input validation
- Days 6-7: Caching layer
- Days 8: Health checks + testing

**Phase 1 Effort: 8-10 days**

---

## PHASE 2: MEDIUM-TERM (4-8 Weeks) - Async Processing & Observability

### 2.1 Concurrency Fix: DRWorkflow Instance Pool (REL-001)

**Current Issue:** Single shared `dr_workflow` instance causes race conditions on concurrent requests.

**Solution:** Create workflow pool with semaphore-controlled access. Each request gets dedicated workflow instance or queued safely.

**Technology:** `asyncio.Semaphore`, built-in contextvars

**Implementation:**
- Max 3 concurrent workflows (configurable)
- Queue additional requests (FIFO)
- Return job ID immediately with `/jobs/{job_id}` for async tracking
- Keep 24h job history in-memory

**Effort:** 3 days

---

### 2.2 Background Job Processing (RQ)

**Current Issue:** Long-running `/query` endpoint ties up API worker processes.

**Solution:** Offload query processing to background queue. FastAPI returns immediately with job tracking.

**Technology:** `rq` (Redis Queue) - simpler than Celery for this use case

**Implementation:**
- `/query` submits to Redis queue, returns job_id
- `/query` (blocking) still available for backward compatibility
- `/jobs/{job_id}` polls for results
- Job TTL: 24 hours
- Configurable worker count (2-4 workers initially)

**Effort:** 4 days

**Docker Compose Addition:**
```yaml
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - hpc-kb-network

  query-worker:
    build:
      context: .
      dockerfile: Dockerfile.worker
    environment:
      - REDIS_URL=redis://redis:6379/0
      - ELASTICSEARCH_URL=http://elasticsearch:9200
      - LLM_BASE_URL=${LLM_BASE_URL}
    depends_on:
      - redis
      - elasticsearch
    networks:
      - hpc-kb-network
    deploy:
      replicas: 2
```

---

### 2.3 Connection Pooling

**Current Issue:** Each request to Elasticsearch creates new connection (inefficient).

**Solution:** Connection pool for Elasticsearch client with configurable size.

**Technology:** AsyncElasticsearch with connection pooling

**Effort:** 1 day

---

### 2.4 Monitoring & Metrics (QUA-005)

**Current Issue:** No observability - can't diagnose performance issues or track SLOs.

**Solution:** Instrument API with Prometheus metrics. Export request latency, error rates, queue depth.

**Technology:** `prometheus-client` + Prometheus scrape endpoint

**Implementation:**
- Request latency histogram (p50, p95, p99)
- Request count by endpoint and status code
- Active job count
- Elasticsearch latency
- LLM response time
- Cache hit rate
- Error rate tracking

**Effort:** 3 days

---

### 2.5 Structured Logging

**Current Issue:** Print statements scattered throughout - hard to debug, no log levels.

**Solution:** Centralized structured logging with JSON output for log aggregation.

**Technology:** `structlog` + JSON formatter

**Effort:** 1.5 days

**Phase 2 Timeline:**
- Weeks 1-2: Concurrency fix + job pool
- Week 2-3: Background queue (RQ)
- Week 3: Connection pooling
- Week 4: Prometheus metrics + structured logging

**Phase 2 Effort: 4-6 weeks**

---

## PHASE 3: LONG-TERM (3-6 Months) - Horizontal Scaling & Advanced Features

### 3.1 Horizontal Scaling Architecture

**Current State:** Single Docker Compose instance. Can't scale beyond single machine.

**Target Architecture:**

```
┌─────────────────────────────────────────────────┐
│           Load Balancer (Nginx/HAProxy)          │
├─────────────────────────────────────────────────┤
│  API Pod 1  │  API Pod 2  │  API Pod 3          │
│ (FastAPI)   │ (FastAPI)   │ (FastAPI)           │
├─────────────────────────────────────────────────┤
│  Query Worker Pool (RQ Workers) - Scalable      │
├─────────────────────────────────────────────────┤
│  Redis (Cache + Queue)                          │
│  Elasticsearch Cluster (3 nodes)                │
│  PostgreSQL (Job history, API keys)             │
└─────────────────────────────────────────────────┘
```

**Technology:** Kubernetes (recommended for growth)

**Implementation Approach:**
1. Move to Kubernetes with StatefulSets for data services
2. Horizontal pod autoscaling based on CPU/memory
3. Scale worker pool independently (5-20 workers)
4. Job stealing if queue depth exceeds threshold

**Effort:** 4-5 weeks

---

### 3.2 API Versioning

**Solution:** Implement URI-based versioning (/v1/, /v2/) with deprecation support.

**Implementation:**
- V1: Current endpoints (frozen after migration)
- V2: New endpoints with breaking changes
- Sunset V1 after 6 months notice
- Migration docs and guides

**Effort:** 3 weeks

---

### 3.3 Advanced Caching Strategy

**Current:** Simple 24h TTL in-memory cache.

**Enhanced Strategy:**
- L1: In-memory (fast, small, 100 entries)
- L2: Redis (distributed, 10k entries, 24h TTL)
- L3: Elasticsearch aggregations (pre-computed results)

**Smart Invalidation:**
- Invalidate on new docs/tickets indexed
- Cache warming for popular queries
- Query fingerprinting to catch variants

**Effort:** 3 weeks

---

### 3.4 GraphQL API (Optional)

**Recommendation:** Build GraphQL as *alternative* (not replacement) for v2.

**Use Case:**
- Complex nested queries (iterations + research answers)
- Client controls exact fields returned (reduce payload)
- Batch queries for multiple jobs

**Technology:** `strawberry-graphql` or `graphene`

**Effort:** 4 weeks (only if business requires)

---

### 3.5 Disaster Recovery

**Solution:**
- Daily Elasticsearch snapshots (S3)
- Redis RDB backup (hourly)
- API key/config version control
- Point-in-time recovery testing

**Effort:** 2 weeks

---

## Implementation Priorities

### Minimum Viable Scaling (Weeks 1-8)
1. Authentication + API keys
2. Rate limiting
3. Input validation
4. Concurrency fix (workflow pool)
5. Background job queue (RQ)
6. Prometheus metrics

**Estimated Load:** 50-100 concurrent users, 500 queries/hour

### Production Ready (Weeks 9-16)
1. Everything above
2. Connection pooling
3. Multi-layer caching
4. Structured logging
5. Kubernetes deployment
6. Load balancing
7. API versioning

**Estimated Load:** 500+ concurrent users, 5000 queries/hour

---

## Deployment Progression

### Stage 1: Docker Compose (Current)
Limited to 1-2 servers, ~50 concurrent requests.

### Stage 2: Single-Server Enhanced (Phase 1-2)
Docker Compose with Redis, RQ workers, Prometheus. ~300 concurrent requests.

### Stage 3: Kubernetes Multi-Node (Phase 3)
Multi-server with HPA scaling workers 5-20. 1000+ concurrent requests.

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Queue overflow | Set max job TTL (24h), auto-prune old jobs |
| Cache poisoning | Validate responses before caching, sign cache entries |
| Key leakage | Rotate keys monthly, audit access logs |
| Elasticsearch downtime | Graceful degradation, return cached/error response |
| LLM latency | Request timeout (300s), queue backoff strategy |
| Worker starvation | Adaptive concurrency, priority queues |

---

## Success Metrics

**By end of Phase 1 (Week 2):**
- All requests require API key
- Rate limit enforcement active
- No obvious security vulnerabilities
- 20-40% of queries served from cache

**By end of Phase 2 (Week 8):**
- Concurrent request limit 10+ (from 1)
- Query latency p95: < 5s (cached), < 120s (uncached)
- 99.9% uptime SLO met
- Full observability (metrics, logs, traces)

**By end of Phase 3 (Month 6):**
- Horizontal scaling to 10+ API instances
- Support 1000+ concurrent users
- Query latency p95: < 2s (cached), < 90s (uncached)
- 99.95% uptime SLO met

---

## Technology Stack Summary

| Component | Current | Phase 1 | Phase 2 | Phase 3 |
|-----------|---------|---------|---------|---------|
| Framework | FastAPI | FastAPI | FastAPI | FastAPI |
| Auth | None | python-jose | python-jose | oauth2-proxy |
| Rate Limit | None | slowapi | slowapi | redis |
| Cache | None | aiocache | aiocache | redis |
| Queue | None | None | RQ | RQ |
| Monitoring | None | prometheus | prometheus | prometheus + grafana |
| Logging | print() | structlog | structlog | ELK stack |
| Orchestration | Docker | Docker | Kubernetes | Kubernetes |
| Storage | Elasticsearch | Elasticsearch | ES Cluster | ES Cluster |
| Redis | None | None | Redis | Redis Cluster |

---

## Effort Summary

| Phase | Duration | Dev Days | Resources |
|-------|----------|----------|-----------|
| Phase 1 | 1-2 weeks | 8-10 | 1 backend engineer |
| Phase 2 | 4-8 weeks | 15-20 | 2 backend engineers |
| Phase 3 | 3-6 months | 30-40 | 2-3 engineers (incl. DevOps) |
| **Total** | **3-6 months** | **53-70** | **2-3 FTE** |

---

## Next Steps

1. Week 1: Review and approve scalability plan
2. Week 1-2: Begin Phase 1 (auth, rate limiting)
3. Weekly: Track progress, adjust based on load patterns
4. Month 1: Complete Phase 1, start Phase 2 planning
5. Month 3: Phase 2 complete, evaluate Phase 3 business case

---

## FAQ

**Q: Why RQ instead of Celery?**
A: RQ is simpler - no broker config, built-in job tracking, easier local development.

**Q: When to move to Kubernetes?**
A: When hitting single-node limits (~500 req/min), typically Phase 3 around month 4.

**Q: Can we use GraphQL instead of REST?**
A: Not yet. REST covers current needs. GraphQL best added as alternative in Phase 3.

**Q: How to handle 10-120s query latency?**
A: Phase 3 focuses on optimization. For now, caching + background processing hide latency.
