# Implementation Checklist

## Pre-Implementation Review

### Phase 1 Approval
- [ ] Business stakeholder approval
- [ ] Security review (auth, CORS, rate limiting)
- [ ] Performance targets agreed
- [ ] Timeline approved (1-2 weeks)
- [ ] Resource commitment confirmed (1 engineer)

### Environment Setup
- [ ] Python 3.9+ available
- [ ] FastAPI project structure confirmed
- [ ] Docker Compose environment working
- [ ] Test framework (pytest) ready
- [ ] Git workflow established

### Dependencies Reviewed
- [ ] python-jose[cryptography] - API key hashing
- [ ] slowapi - Rate limiting
- [ ] aiocache - In-memory caching
- [ ] structlog - JSON logging (Phase 2)
- [ ] prometheus-client - Metrics (Phase 2)
- [ ] rq - Job queue (Phase 2)
- [ ] redis - Cache backend (Phase 2)

---

## Phase 1 Implementation (1-2 Weeks)

### Week 1: Core Security & Caching

#### Day 1-2: Authentication (2 days)
- [ ] Create `api/auth.py` with:
  - [ ] `generate_api_key()` function
  - [ ] `hash_api_key()` function
  - [ ] `validate_api_key()` function
  - [ ] `verify_api_key()` FastAPI dependency
  - [ ] In-memory key storage (dict)
  - [ ] Unit tests for auth module

- [ ] Update `api/main.py`:
  - [ ] Import auth module
  - [ ] Add `@app.post("/auth/generate-key")` endpoint
  - [ ] Add `@app.get("/auth/keys")` endpoint
  - [ ] Add `@app.post("/auth/revoke")` endpoint
  - [ ] Keep `/health` and `/` public
  - [ ] Keep other endpoints protected with `Depends(verify_api_key)`

- [ ] Test authentication:
  - [ ] `curl /health` works (no auth)
  - [ ] `curl /query` fails 403 (no auth)
  - [ ] `curl /query -H "Authorization: Bearer KEY"` works
  - [ ] Invalid key returns 403
  - [ ] Key generation works

- [ ] Update documentation:
  - [ ] Add API key generation instructions
  - [ ] Add example requests with headers
  - [ ] Document auth flow

#### Day 3-4: Rate Limiting (1.5 days)
- [ ] Create `api/rate_limit.py` with:
  - [ ] slowapi Limiter setup
  - [ ] Custom exception handler for 429
  - [ ] setup_rate_limiting() function

- [ ] Update `api/main.py`:
  - [ ] Import rate_limit module
  - [ ] Call setup_rate_limiting(app)
  - [ ] Add `@limiter.limit()` decorator to endpoints:
    - [ ] `/query` - "10/minute"
    - [ ] `/query/stream` - "10/minute"
    - [ ] `/search` - "30/minute"
    - [ ] Leave `/health` unlimited
  - [ ] Update endpoint signatures to include `request: Request`

- [ ] Test rate limiting:
  - [ ] Apache Bench: `ab -n 20 -c 1 http://localhost:8000/health`
  - [ ] Should get 429 after 10 requests in 60s
  - [ ] Check Retry-After header
  - [ ] Verify different limits per endpoint

- [ ] Update documentation:
  - [ ] Document rate limits
  - [ ] Show 429 error response format
  - [ ] Explain Retry-After header

#### Day 5: Input Validation (1 day)
- [ ] Update `api/main.py` request models:
  - [ ] QueryRequest:
    - [ ] query: 5-500 chars
    - [ ] max_iterations: 1-10
    - [ ] @field_validator for injection detection
    - [ ] @field_validator for character whitelist
  - [ ] SearchRequest:
    - [ ] query: 3-300 chars
    - [ ] index: regex validation
    - [ ] max_results: 1-100

- [ ] Test validation:
  - [ ] Too short query rejected (422)
  - [ ] Too long query rejected (422)
  - [ ] Injection patterns rejected (422)
  - [ ] Invalid characters rejected (422)
  - [ ] Valid queries accepted (200)

- [ ] Update documentation:
  - [ ] Document query constraints
  - [ ] Show validation error examples

#### Day 6-7: Response Caching (1.5 days)
- [ ] Create `api/cache.py` with:
  - [ ] CacheManager class
  - [ ] `_get_key()` method (SHA256 hash)
  - [ ] `get()` async method
  - [ ] `set()` async method
  - [ ] TTL expiration logic
  - [ ] Cache statistics
  - [ ] clear() method

- [ ] Update `api/main.py`:
  - [ ] Import cache manager
  - [ ] Instantiate global cache_manager
  - [ ] Update `/query` endpoint:
    - [ ] Check cache on entry
    - [ ] Return cached result if hit
    - [ ] Cache result after processing
    - [ ] Add "cached": True/False to response
  - [ ] Add `/cache/stats` endpoint
  - [ ] Add `/cache/clear` endpoint

- [ ] Update QueryResponse model:
  - [ ] Add `cached: bool` field
  - [ ] Add `cache_age_seconds: Optional[int]` field

- [ ] Test caching:
  - [ ] First query: cached=false
  - [ ] Second identical query: cached=true
  - [ ] Cache stats show hit/miss counts
  - [ ] Cache expires after 24h
  - [ ] Cache clears on /cache/clear

- [ ] Update documentation:
  - [ ] Document cache behavior
  - [ ] Show cache stats endpoint

#### Day 8: CORS & Health Checks (1 day)
- [ ] Update CORS configuration:
  - [ ] Change `allow_origins=["*"]` to specific domain
  - [ ] Set `allow_methods=["GET", "POST"]`
  - [ ] Set `allow_headers=["Content-Type", "Authorization"]`
  - [ ] Add `expose_headers` for rate limit info

- [ ] Add startup validation:
  - [ ] Create `test_llm_connection()` async function
  - [ ] Update `@app.on_event("startup")` or use lifespan:
    - [ ] Test Elasticsearch connection
    - [ ] Test LLM connection
    - [ ] Fail startup if critical services unavailable
  - [ ] Add clear startup logging

- [ ] Test startup:
  - [ ] With ES/LLM running: starts successfully
  - [ ] With ES down: fails with clear error
  - [ ] With LLM down: fails with clear error

### Week 2: Testing & Deployment

#### Day 9: Unit Tests
- [ ] Create `tests/test_auth.py`:
  - [ ] test_generate_api_key()
  - [ ] test_validate_api_key_valid()
  - [ ] test_validate_api_key_invalid()
  - [ ] test_hash_consistency()
  - [ ] test_revoke_api_key()

- [ ] Create `tests/test_rate_limit.py`:
  - [ ] test_rate_limit_enforced()
  - [ ] test_429_response_format()
  - [ ] test_retry_after_header()
  - [ ] test_different_limits_per_endpoint()

- [ ] Create `tests/test_validation.py`:
  - [ ] test_query_too_short_rejected()
  - [ ] test_query_too_long_rejected()
  - [ ] test_injection_patterns_rejected()
  - [ ] test_invalid_characters_rejected()
  - [ ] test_valid_query_accepted()

- [ ] Create `tests/test_cache.py`:
  - [ ] test_cache_hit()
  - [ ] test_cache_miss()
  - [ ] test_cache_expiration()
  - [ ] test_cache_key_generation()
  - [ ] test_cache_stats()
  - [ ] test_cache_clear()

- [ ] Create `tests/test_endpoints.py`:
  - [ ] test_health_public()
  - [ ] test_query_requires_auth()
  - [ ] test_query_with_auth()
  - [ ] test_search_with_auth()

- [ ] Run all tests:
  ```bash
  pytest tests/ -v --cov=api
  ```

- [ ] Achieve > 80% code coverage

#### Day 10: Integration Testing
- [ ] Full workflow test:
  ```python
  # 1. Generate key
  # 2. Make query without key (expect 403)
  # 3. Make query with key (expect 200)
  # 4. Make second identical query (expect cached=true)
  # 5. Check rate limit (11+ requests fail)
  # 6. Test invalid input (expect 422)
  ```

- [ ] Load testing:
  ```bash
  # Test rate limiting
  ab -n 100 -c 10 -H "Authorization: Bearer KEY" \
    -p query.json http://localhost:8000/query
  ```

- [ ] Documentation testing:
  - [ ] All code examples runnable
  - [ ] All endpoints documented
  - [ ] Error responses documented

#### Day 11: Documentation & Migration Guide
- [ ] Update README:
  - [ ] Add authentication section
  - [ ] Add rate limiting section
  - [ ] Add example requests with keys

- [ ] Create MIGRATION.md:
  - [ ] How to generate API keys
  - [ ] How to update client code
  - [ ] Migration timeline for existing clients
  - [ ] FAQ and troubleshooting

- [ ] Update OpenAPI/Swagger:
  - [ ] Add security definition
  - [ ] Mark endpoints with auth requirement
  - [ ] Update response models with new fields

- [ ] Create CHANGELOG:
  - [ ] List Phase 1 improvements
  - [ ] Breaking changes (auth required)
  - [ ] New endpoints (/auth/*)
  - [ ] Deprecation notes (if any)

#### Day 12: Final Testing & Deployment
- [ ] Pre-deployment checklist:
  - [ ] All tests passing
  - [ ] Code review completed
  - [ ] Security audit passed
  - [ ] Performance targets met
  - [ ] Documentation complete

- [ ] Staging deployment:
  - [ ] Build Docker image
  - [ ] Deploy to staging environment
  - [ ] Run full test suite against staging
  - [ ] Performance validation

- [ ] Production deployment:
  - [ ] Generate production API keys
  - [ ] Deploy to production
  - [ ] Monitor error rates (should be < 1%)
  - [ ] Monitor latency (should be similar)
  - [ ] Monitor cache hit rate (should be 20-40%)
  - [ ] Verify all endpoints working

- [ ] Post-deployment:
  - [ ] Monitor logs for errors
  - [ ] Verify metrics being generated
  - [ ] Document any issues found
  - [ ] Plan Phase 2 start

---

## Phase 2 Implementation (4-8 Weeks)

### Pre-Phase 2: Planning
- [ ] Review Phase 1 metrics:
  - [ ] Cache hit rate
  - [ ] Query latency distribution
  - [ ] Error rates
  - [ ] Concurrent user count

- [ ] Decide on implementation approach:
  - [ ] Option A: Continue with same single server
  - [ ] Option B: Split workers to separate server
  - [ ] Option C: Start Kubernetes planning

- [ ] Resource allocation:
  - [ ] Assign 2 engineers to Phase 2
  - [ ] Reserve DevOps time for Redis setup
  - [ ] Plan deployment windows

### Week 1-2: Background Job Queue

#### Concurrency Fix (REL-001)
- [ ] Update `api/main.py`:
  - [ ] Remove global `dr_workflow` instance
  - [ ] Create WorkflowManager class with:
    - [ ] asyncio.Semaphore(max_concurrent=3)
    - [ ] Job tracking dict
    - [ ] Job ID generation
    - [ ] Job status management

- [ ] Implement `/query/async`:
  - [ ] Returns job_id immediately
  - [ ] Queues work in background
  - [ ] Returns < 200ms response

- [ ] Add RQ integration:
  - [ ] Install redis and rq
  - [ ] Create `jobs/worker.py`:
    - [ ] Job definition
    - [ ] Error handling
    - [ ] Result serialization

- [ ] Add Redis to docker-compose.yml:
  - [ ] Redis service definition
  - [ ] Health check
  - [ ] Volume for persistence

- [ ] Deploy Phase 2 workers:
  - [ ] Start 2-4 RQ workers
  - [ ] Monitor queue depth
  - [ ] Log worker status

### Week 2-3: Connection Pooling & Monitoring

#### Connection Pooling
- [ ] Update Elasticsearch client:
  - [ ] Enable connection pooling
  - [ ] Set maxsize=25
  - [ ] Set timeout=10s

#### Prometheus Metrics
- [ ] Create `api/metrics.py`:
  - [ ] REQUEST_COUNT (by endpoint, method, status)
  - [ ] REQUEST_DURATION (histogram)
  - [ ] ACTIVE_JOBS (gauge)
  - [ ] CACHE_HITS (counter)
  - [ ] ES_LATENCY (histogram)
  - [ ] LLM_LATENCY (histogram)

- [ ] Add middleware:
  - [ ] Track request timing
  - [ ] Track error rates
  - [ ] Track active jobs

- [ ] Expose /metrics endpoint:
  - [ ] Protected with auth
  - [ ] Returns Prometheus format

- [ ] Add docker-compose service:
  - [ ] Prometheus container
  - [ ] Scrape config for API
  - [ ] Data volume for persistence

- [ ] Create Grafana dashboard:
  - [ ] Request latency (p50, p95, p99)
  - [ ] Error rate
  - [ ] Cache hit rate
  - [ ] Active jobs
  - [ ] Queue depth

### Week 3-4: Structured Logging

- [ ] Update logging throughout:
  - [ ] Replace all print() with logger calls
  - [ ] Use structlog for JSON output
  - [ ] Include request IDs for tracing
  - [ ] Log all critical operations

---

## Phase 3 Implementation (3-6 Months)

### Pre-Kubernetes Planning
- [ ] Evaluate Kubernetes needs
- [ ] Choose platform (K8s self-hosted, managed service, etc.)
- [ ] Infrastructure budget approval
- [ ] DevOps team onboarding

### Kubernetes Migration
- [ ] Create manifests:
  - [ ] Deployment (API)
  - [ ] Deployment (RQ workers)
  - [ ] StatefulSet (Elasticsearch)
  - [ ] StatefulSet (Redis)
  - [ ] Services
  - [ ] Ingress
  - [ ] ConfigMap (configuration)
  - [ ] Secret (API keys, credentials)

- [ ] Set up CI/CD:
  - [ ] Docker image building
  - [ ] Automated testing
  - [ ] Automated deployment
  - [ ] Rollback procedures

- [ ] Production hardening:
  - [ ] TLS/HTTPS everywhere
  - [ ] Network policies
  - [ ] RBAC
  - [ ] Pod security policies
  - [ ] Resource limits/requests
  - [ ] Health checks
  - [ ] Liveness probes
  - [ ] Readiness probes

---

## Success Criteria Validation

### Phase 1 Complete When:
```bash
# All checks pass
[ ] Authentication endpoint returns 403 for missing API key
[ ] Rate limit endpoint returns 429 after limit
[ ] Invalid queries return 422
[ ] Cache hit rate > 0% (tracked via /cache/stats)
[ ] Startup aborts if ES/LLM unavailable
[ ] All tests pass: pytest tests/ -v
[ ] Code coverage > 80%
[ ] Security audit passed
[ ] Documentation complete
```

### Phase 2 Complete When:
```bash
# All checks pass
[ ] /query/async returns job_id in < 200ms
[ ] /jobs/{job_id} polls return proper status
[ ] 10+ concurrent queries processed
[ ] Prometheus metrics endpoint active
[ ] Grafana dashboard shows data
[ ] Cache hit rate 20-40%
[ ] Queue depth < 50 jobs
[ ] 99.9% uptime over 24h
[ ] All tests pass
[ ] Load test handles 100 concurrent
```

### Phase 3 Complete When:
```bash
# All checks pass
[ ] 10+ API replicas running
[ ] Workers autoscale (5-20)
[ ] Load balancer distributes traffic
[ ] Failover tested and working
[ ] Elasticsearch cluster healthy
[ ] Redis cluster healthy
[ ] 1000+ concurrent users supported
[ ] Cache hit rate 50%+
[ ] Query latency p95 < 20s
[ ] 99.95% uptime over 24h
[ ] All tests pass
```

---

## Risk Mitigation

### Phase 1 Risks
| Risk | Mitigation |
|------|-----------|
| Breaking change for clients | Gradual rollout, 2-week notice |
| Auth implementation bugs | Thorough unit tests, staged deployment |
| Performance regression | Benchmark before/after, have rollback ready |

### Phase 2 Risks
| Risk | Mitigation |
|------|-----------|
| Queue overflow | Set job TTL, max queue size |
| Redis unavailable | Graceful degradation to sync mode |
| Worker crashes | Restart policy, monitoring |

### Phase 3 Risks
| Risk | Mitigation |
|------|-----------|
| Kubernetes complexity | Proper training, professional support |
| Data loss | Backup/restore procedures tested |
| Network issues | Circuit breakers, retry logic |

---

## Rollback Procedures

### Phase 1 Rollback (< 1 hour)
```bash
# Remove auth dependency from endpoints
# Remove rate limiting decorators
# Revert Pydantic model changes
# Revert CORS config
# Restart API container
```

### Phase 2 Rollback (< 15 minutes)
```bash
# Stop RQ workers
# API continues with sync processing
# Delete Redis container (non-destructive)
# Restart API container
```

### Phase 3 Rollback (< 5 minutes)
```bash
# Scale Phase 2 deployment up
# Update load balancer to Phase 2
# Scale Phase 3 deployment down
```

---

## Communication Plan

### Stakeholder Updates
- Week 1: Phase 1 kickoff
- Week 2: Mid-phase progress
- Week 2: Phase 1 complete + Phase 2 planning
- Monthly: High-level updates
- After Phase 3: Final review

### Client Communication
- 2 weeks before: API key requirement announcement
- 1 week before: Migration guide release
- Go-live: API key requirement effective
- Ongoing: Support for migration questions

---

## Final Checklist Before Go-Live

- [ ] All code merged and tested
- [ ] Security audit completed
- [ ] Performance targets met
- [ ] Monitoring configured
- [ ] Alerting rules defined
- [ ] Runbook documentation written
- [ ] On-call rotation established
- [ ] Incident response plan ready
- [ ] Backup/restore tested
- [ ] Client communication sent
- [ ] Support team trained
- [ ] Deployment schedule set

