# HPC API Scalability - Quick Reference

## Current State (Critical Issues)

| Issue ID | Severity | Problem | Impact |
|----------|----------|---------|--------|
| SEC-002 | CRITICAL | No authentication | Anyone can query API |
| SEC-001 | HIGH | CORS=* | Vulnerable to XSS attacks |
| SEC-007 | HIGH | No rate limiting | DDoS/resource exhaustion |
| REL-001 | CRITICAL | Race conditions | Data corruption, crashes |
| QUA-005 | HIGH | No monitoring | Can't track performance |

## Phase 1: Quick Wins (Days 1-10)

### 1. API Key Authentication
- Time: 2 days
- Complexity: LOW
- Security: Makes API usable in production
- Code: `api/auth.py` (120 LOC)

```bash
# Test after implementation
curl -X GET http://localhost:8000/health  # Works (public)
curl -X POST http://localhost:8000/query \
  -H "Authorization: Bearer <api_key>" \
  -d '{"query": "HPC question"}'  # Works
curl -X POST http://localhost:8000/query \
  -d '{"query": "HPC question"}'  # Fails 403
```

### 2. Rate Limiting
- Time: 1.5 days
- Complexity: LOW
- Limits: `/query` = 10/min, `/search` = 30/min
- Code: `api/rate_limit.py` (50 LOC)

```bash
# After 10 requests in 60s, returns 429
for i in {1..15}; do
  curl -X GET http://localhost:8000/health
done
```

### 3. Input Validation
- Time: 1 day
- Complexity: LOW
- Prevents: Prompt injection, XSS, buffer overflow
- Code: Update Pydantic models (50 LOC)

```python
# Now rejects:
# - Queries < 5 chars: "HPC"
# - Injection patterns: "import os"
# - Invalid chars: "<script>"
# - Iterations outside 1-10
```

### 4. Query Caching
- Time: 1.5 days
- Complexity: LOW
- Expected improvement: 20-40% faster (cache hits)
- Code: `api/cache.py` (100 LOC)

```bash
# Check cache stats
curl -X GET http://localhost:8000/cache/stats \
  -H "Authorization: Bearer <api_key>"
# Response: {"hits": 25, "misses": 30, "hit_rate": "45.5%"}
```

### 5. Health Checks
- Time: 0.5 days
- Complexity: LOW
- Tests: Elasticsearch, LLM availability
- Fails on startup if critical service down

**Phase 1 Total: 8-10 days for 1 engineer**

---

## Phase 2: Medium-Term (Weeks 4-8)

### 1. Concurrency Fix (REL-001)
- Time: 3 days
- Current: Single shared workflow (race conditions)
- Solution: Workflow pool + semaphore
- Max concurrent: 3 (configurable)

### 2. Background Job Queue
- Time: 4 days
- Technology: Redis + RQ (Python)
- Returns: Job ID immediately
- Status: Poll `/jobs/{job_id}` for result

### 3. Connection Pooling
- Time: 1 day
- For: Elasticsearch client
- Max connections: 25 (configurable)

### 4. Prometheus Metrics
- Time: 3 days
- Metrics: Request latency, error rates, cache hits
- Endpoint: `/metrics` (protected)
- Scrape: Every 15 seconds

### 5. Structured Logging
- Time: 1.5 days
- Format: JSON (easier log aggregation)
- Replaces: print() statements

**Phase 2 Total: 4-6 weeks for 2 engineers**

---

## Phase 3: Long-Term (Months 3-6)

### 1. Horizontal Scaling
- Kubernetes with 3-10 API replicas
- Worker pool scales 5-20
- Load balancer (Nginx/HAProxy)

### 2. API Versioning
- `/v1/` - Current (frozen)
- `/v2/` - New with breaking changes
- Sunset: 6 months notice

### 3. Advanced Caching
- L1: In-memory (100 items)
- L2: Redis (10k items)
- L3: Elasticsearch aggregations

### 4. GraphQL API (Optional)
- Alternative to REST (not replacement)
- Better for nested queries
- Add in `/graphql` endpoint

**Phase 3 Total: 3-6 months for 2-3 engineers**

---

## Load Progression

| Milestone | Concurrent Users | Queries/Hour | Latency p95 | Uptime SLO |
|-----------|-----------------|--------------|-------------|-----------|
| Current | 1 | 10 | 120s | - |
| Phase 1 end | 50 | 500 | 60s | - |
| Phase 2 end | 300 | 3k | 45s | 99.9% |
| Phase 3 end | 1000+ | 10k+ | 20s | 99.95% |

---

## Technology Decisions

### Why RQ over Celery?
- Simpler setup (no separate broker)
- Built-in job tracking
- Easier local development
- Sufficient for current scale

### Why Kubernetes in Phase 3?
- Horizontal scaling of stateless API
- Auto-scaling based on load
- Cost-efficient for variable traffic
- Industry standard for HPC environments

### Why no GraphQL in Phase 1?
- REST covers current needs
- GraphQL adds complexity
- Better to add as optional in Phase 3
- Clients comfortable with REST

### Why cache before background jobs?
- Immediate 20-40% latency improvement
- No architectural changes
- Cheap to implement
- Reduces queue load

---

## Effort Estimates

### Quick Estimates for Your Team

Assuming 1 engineer:
- Phase 1: Start today, done in 2 weeks
- Phase 2: 4-6 weeks (overlaps with Phase 1 tweaks)
- Phase 3: 10-12 weeks (needs DevOps support)

Assuming 2 engineers:
- Phase 1: Start today, done in 1 week
- Phase 2: 2-3 weeks (run in parallel with Phase 1)
- Phase 3: 4-6 weeks (needs DevOps support)

---

## First Week Actions

### Day 1: Setup
- [ ] Create `api/auth.py`
- [ ] Create `api/cache.py`
- [ ] Install dependencies: `pip install python-jose slowapi`

### Days 2-3: Auth
- [ ] Implement API key generation
- [ ] Add `verify_api_key` dependency
- [ ] Protect all endpoints except `/health`
- [ ] Update CORS config

### Days 4-5: Rate Limiting
- [ ] Implement slowapi
- [ ] Configure limits by endpoint
- [ ] Test with `Apache Bench`: `ab -n 100 -c 10`

### Days 6-7: Caching + Validation
- [ ] Add Pydantic validation
- [ ] Implement cache layer
- [ ] Test cache hits

### Day 8+: Testing & Docs
- [ ] Write unit tests
- [ ] Update API documentation
- [ ] Test with real queries

---

## Monitoring Checklist

### What to Watch After Phase 1

```bash
# Cache hit rate (should be 20-40%)
curl http://localhost:8000/cache/stats

# Request latency (should see improvement)
# Elasticsearch status
curl http://localhost:9200/_cluster/health

# Error rates (should be < 1%)
grep ERROR logs/

# Rate limit hits (should be < 5%)
grep "429" logs/
```

---

## Cost Impact

### Infrastructure (Phase 1-2)
- Current: 1 server (no cost if using your HPC)
- Add: Redis (minimal - 512MB RAM)
- Add: Prometheus (minimal - 1GB disk)
- Phase 2: +1-2 more servers for workers

### Development
- Phase 1: 1 FTE x 2 weeks
- Phase 2: 2 FTE x 4-6 weeks
- Phase 3: 2-3 FTE x 8-12 weeks (with DevOps)

### ROI
- Eliminate security vulnerabilities: High
- Support 50x more users (Phase 3): Significant
- Reduce query latency 80% (cache): Immediate
- Enable async processing: Improves UX

---

## Rollback Plan

Each phase is independently deployable:

### Phase 1 Rollback (if issues)
- Remove `verify_api_key` decorators
- Remove rate limiting decorator
- Revert Pydantic changes
- Remove cache calls

Time: < 1 hour, no data loss

### Phase 2 Rollback (if issues)
- Stop RQ workers
- API still works with sync processing
- Delete Redis data (non-destructive)

Time: < 15 minutes, no data loss

### Phase 3 Rollback (if issues)
- Scale Kubernetes down
- Route to Phase 2 infrastructure
- No data loss

Time: < 5 minutes

---

## Success Criteria

### Phase 1 (Week 2)
- [ ] All endpoints require API key
- [ ] Rate limiting active
- [ ] No obvious vulnerabilities
- [ ] Cache stats show > 0 hits

### Phase 2 (Week 8)
- [ ] Can handle 10+ concurrent queries
- [ ] Elasticsearch latency < 200ms
- [ ] Queue depth < 50 jobs
- [ ] 99.9% uptime SLO met

### Phase 3 (Month 6)
- [ ] 10+ API replicas running
- [ ] Auto-scales based on load
- [ ] Cache hit rate > 50%
- [ ] 99.95% uptime SLO met

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| API key not working | Hash mismatch | Check auth.py hash function |
| Cache not working | TTL expired | Check datetime.utcnow() |
| Rate limit too strict | Wrong calculation | Verify slowapi limits |
| Elasticsearch slow | No connection pool | Implement pooling (Phase 2) |
| High error rate | LLM timeout | Increase timeout, add retry logic |

---

## Resources

- FastAPI docs: https://fastapi.tiangolo.com
- slowapi docs: https://slowapi.readthedocs.io
- RQ docs: https://python-rq.org
- Prometheus docs: https://prometheus.io
- Kubernetes docs: https://kubernetes.io

---

## Next Meeting Topics

1. **Approve Phase 1 plan** (30 min)
2. **Resource allocation** - How many engineers available?
3. **Timeline** - When to start Phase 2?
4. **Metrics** - What SLOs matter most?
5. **Deployment** - Dev/staging/prod environments?

---

Generated for HPC Ticket Knowledge Database API
Last Updated: 2025-12-06
