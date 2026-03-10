# Phase 1 Implementation Guide - Quick Wins (1-2 Weeks)

This guide provides ready-to-implement code for all Phase 1 improvements.

## 1. Authentication & API Keys (2 days)

### Step 1.1: Create `api/auth.py`

```python
import os
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthCredentials

security = HTTPBearer()

# In-memory key storage (upgrade to DB in Phase 2)
# Format: {key_hash: {"name": str, "created": datetime, "active": bool}}
VALID_API_KEYS = {}

def hash_api_key(api_key: str) -> str:
    """Hash API key for secure storage"""
    return hashlib.sha256(api_key.encode()).hexdigest()

def generate_api_key(key_name: str = "default") -> str:
    """Generate a new API key"""
    # Format: hpc_XXXXXXXXXXXXXXXXXXXX (32 random chars)
    key = f"hpc_{secrets.token_hex(16)}"
    key_hash = hash_api_key(key)

    # Store hash
    VALID_API_KEYS[key_hash] = {
        "name": key_name,
        "created": datetime.utcnow(),
        "active": True,
        "last_used": None
    }

    return key

def validate_api_key(api_key: str) -> bool:
    """Validate provided API key"""
    key_hash = hash_api_key(api_key)
    if key_hash not in VALID_API_KEYS:
        return False

    key_info = VALID_API_KEYS[key_hash]
    if not key_info["active"]:
        return False

    # Update last used timestamp
    VALID_API_KEYS[key_hash]["last_used"] = datetime.utcnow()
    return True

async def verify_api_key(credentials: HTTPAuthCredentials = Security(security)) -> str:
    """FastAPI dependency to verify API key on protected endpoints"""
    token = credentials.credentials

    if not validate_api_key(token):
        raise HTTPException(
            status_code=403,
            detail="Invalid or inactive API key"
        )

    return token

def revoke_api_key(api_key: str) -> bool:
    """Revoke an API key"""
    key_hash = hash_api_key(api_key)
    if key_hash in VALID_API_KEYS:
        VALID_API_KEYS[key_hash]["active"] = False
        return True
    return False

def list_api_keys() -> list:
    """List all API keys (admin use)"""
    return [
        {
            "hash": key_hash[:8] + "...",
            "name": info["name"],
            "created": info["created"].isoformat(),
            "active": info["active"],
            "last_used": info["last_used"].isoformat() if info["last_used"] else None
        }
        for key_hash, info in VALID_API_KEYS.items()
    ]
```

### Step 1.2: Update `api/main.py` - Add Auth Endpoints

Add these imports at top:
```python
from api.auth import verify_api_key, generate_api_key, list_api_keys, revoke_api_key
from fastapi import Depends
```

Add these endpoints:
```python
@app.post("/auth/generate-key")
async def create_api_key(key_name: str = "api-key"):
    """Generate new API key (should be admin-protected in production)"""
    key = generate_api_key(key_name)
    return {
        "api_key": key,
        "message": "Store this key securely. It won't be shown again.",
        "usage": "Include in Authorization header: Authorization: Bearer YOUR_KEY"
    }

@app.get("/auth/keys")
async def get_api_keys(api_key: str = Depends(verify_api_key)):
    """List all API keys (admin-protected)"""
    return {"keys": list_api_keys()}

@app.post("/auth/revoke")
async def revoke_key(key_to_revoke: str, api_key: str = Depends(verify_api_key)):
    """Revoke an API key (admin-protected)"""
    if revoke_api_key(key_to_revoke):
        return {"message": "API key revoked"}
    raise HTTPException(status_code=404, detail="API key not found")
```

### Step 1.3: Update Existing Endpoints - Add `Depends(verify_api_key)`

```python
# Update query endpoint
@app.post("/query", response_model=QueryResponse)
async def process_query(
    request: QueryRequest,
    _: str = Depends(verify_api_key)  # Add this line
):
    """Process query with authentication"""
    # ... existing code ...

# Update search endpoint
@app.post("/search")
async def search(
    request: SearchRequest,
    _: str = Depends(verify_api_key)  # Add this line
):
    """Search with authentication"""
    # ... existing code ...

# Update stream endpoint
@app.post("/query/stream")
async def process_query_stream(
    request: QueryRequest,
    _: str = Depends(verify_api_key)  # Add this line
):
    """Stream query with authentication"""
    # ... existing code ...

# Health and root endpoints remain public (no Depends)
```

### Step 1.4: Update CORS Configuration

Replace existing CORS middleware in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend-domain.com",
        "https://admin-dashboard.example.com"
        # Remove "*" - specify only trusted domains
    ],
    allow_credentials=False,  # Don't send cookies
    allow_methods=["GET", "POST"],  # Only needed methods
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["X-RateLimit-Remaining", "X-RateLimit-Reset"],
    max_age=3600
)
```

---

## 2. Rate Limiting (1.5 days)

### Step 2.1: Install and Configure slowapi

Update `requirements.txt`:
```
slowapi>=0.1.9
```

### Step 2.2: Create `api/rate_limit.py`

```python
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

limiter = Limiter(key_func=get_remote_address)

def setup_rate_limiting(app: FastAPI):
    """Configure rate limiting on FastAPI app"""

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
        return JSONResponse(
            status_code=429,
            content={
                "detail": "Rate limit exceeded",
                "retry_after": exc.detail
            },
            headers={"Retry-After": exc.detail}
        )

    app.state.limiter = limiter
```

### Step 2.3: Update `api/main.py` - Apply Rate Limits

Add at imports:
```python
from api.rate_limit import limiter, setup_rate_limiting
```

In app initialization:
```python
app = FastAPI(
    title="HPC Deep Research API",
    description="Multi-agent deep research system for HPC support questions",
    version="1.0.0"
)

# Setup rate limiting
setup_rate_limiting(app)
```

Update endpoints with rate limits:

```python
@app.post("/query", response_model=QueryResponse)
@limiter.limit("10/minute")  # Add this decorator
async def process_query(
    request: Request,  # Add Request parameter
    query_request: QueryRequest,
    _: str = Depends(verify_api_key)
):
    """Process query - 10 requests per minute per IP"""
    # ... existing code ...

@app.post("/query/stream")
@limiter.limit("10/minute")  # Add this decorator
async def process_query_stream(
    request: Request,  # Add Request parameter
    query_request: QueryRequest,
    _: str = Depends(verify_api_key)
):
    """Stream query - 10 requests per minute per IP"""
    # ... existing code ...

@app.post("/search")
@limiter.limit("30/minute")  # Higher limit for search
async def search(
    request: Request,  # Add Request parameter
    search_request: SearchRequest,
    _: str = Depends(verify_api_key)
):
    """Search - 30 requests per minute per IP"""
    # ... existing code ...

# Health check unlimited
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check - unlimited"""
    # ... existing code ...
```

---

## 3. Input Validation (1 day)

### Step 3.1: Update `api/main.py` - Pydantic Models

Replace existing models with enhanced validation:

```python
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List

class QueryRequest(BaseModel):
    """Request model for DR query with validation"""
    model_config = ConfigDict(examples=[{
        "query": "How do I optimize GPU job performance?",
        "max_iterations": 3,
        "brief": False
    }])

    query: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="HPC support question (5-500 chars)"
    )
    max_iterations: Optional[int] = Field(
        default=3,
        ge=1,
        le=10,
        description="Override max iterations (1-10)"
    )
    brief: Optional[bool] = Field(
        default=False,
        description="Return only concise answer"
    )

    @field_validator('query')
    @classmethod
    def validate_query(cls, v: str) -> str:
        """Validate and sanitize query"""
        v = v.strip()

        # Reject common injection patterns
        dangerous_patterns = [
            '__',
            'import ',
            'exec(',
            'eval(',
            'lambda ',
            'subprocess',
            'os.system'
        ]
        for pattern in dangerous_patterns:
            if pattern in v.lower():
                raise ValueError(f"Query contains potentially dangerous pattern: {pattern}")

        # Only allow alphanumeric, spaces, and basic punctuation
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,?!.-')
        invalid_chars = set(c for c in v if c not in allowed_chars)

        if invalid_chars:
            raise ValueError(f"Query contains invalid characters: {invalid_chars}")

        # Check for excessive repetition
        words = v.split()
        if len(words) < 2:
            raise ValueError("Query must contain at least 2 words")

        return v

class SearchRequest(BaseModel):
    """Request model for search with validation"""

    query: str = Field(
        ...,
        min_length=3,
        max_length=300,
        description="Search query (3-300 chars)"
    )
    index: str = Field(
        "docs",
        regex="^(docs|tickets|knowledgebase)$",
        description="Index to search"
    )
    max_results: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Results to return (1-100)"
    )

    @field_validator('query')
    @classmethod
    def validate_search_query(cls, v: str) -> str:
        """Validate search query"""
        v = v.strip()
        if len(v) < 3:
            raise ValueError("Search query too short")
        return v
```

---

## 4. Response Caching (1.5 days)

### Step 4.1: Create `api/cache.py`

```python
import hashlib
import json
from typing import Optional, Any
from datetime import datetime, timedelta

class CacheManager:
    """Simple in-memory cache with TTL"""

    def __init__(self):
        self.cache = {}  # {key: {"value": any, "expires": datetime}}
        self.hit_count = 0
        self.miss_count = 0

    def _get_key(self, query: str, max_iterations: int) -> str:
        """Generate cache key from query parameters"""
        key_str = f"{query}:{max_iterations}"
        return hashlib.sha256(key_str.encode()).hexdigest()

    async def get(self, query: str, max_iterations: int) -> Optional[dict]:
        """Get cached result if exists and not expired"""
        key = self._get_key(query, max_iterations)

        if key not in self.cache:
            self.miss_count += 1
            return None

        entry = self.cache[key]
        if datetime.utcnow() > entry["expires"]:
            # Expired, remove and return None
            del self.cache[key]
            self.miss_count += 1
            return None

        self.hit_count += 1
        return entry["value"]

    async def set(self, query: str, max_iterations: int, value: dict, ttl_seconds: int = 86400):
        """Cache a result with TTL"""
        key = self._get_key(query, max_iterations)
        self.cache[key] = {
            "value": value,
            "expires": datetime.utcnow() + timedelta(seconds=ttl_seconds),
            "created": datetime.utcnow()
        }

    def get_stats(self) -> dict:
        """Get cache statistics"""
        total = self.hit_count + self.miss_count
        hit_rate = (self.hit_count / total * 100) if total > 0 else 0

        return {
            "hits": self.hit_count,
            "misses": self.miss_count,
            "hit_rate": f"{hit_rate:.1f}%",
            "cached_items": len(self.cache),
            "total_requests": total
        }

    def clear(self):
        """Clear all cache"""
        self.cache.clear()

# Global cache instance
cache_manager = CacheManager()
```

### Step 4.2: Update `api/main.py` - Add Caching

Add import:
```python
from api.cache import cache_manager
```

Update query endpoint:

```python
@app.post("/query", response_model=QueryResponse)
@limiter.limit("10/minute")
async def process_query(
    request: Request,
    query_request: QueryRequest,
    _: str = Depends(verify_api_key)
):
    """Process query with caching"""
    try:
        # Check cache first
        cached_result = await cache_manager.get(
            query_request.query,
            query_request.max_iterations or 3
        )

        if cached_result:
            # Return with cache hit indicator
            return QueryResponse(
                **cached_result,
                cached=True,
                cache_age_seconds=0
            )

        # Override config if requested
        if query_request.max_iterations:
            config.max_iterations = query_request.max_iterations

        # Process query
        result = await dr_workflow.process_query(query_request.query)

        # Serialize iterations
        iterations_dict = None
        if not query_request.brief:
            iterations_dict = [
                {
                    "iteration_number": it.iteration_number,
                    "research_answers": [
                        {
                            "research_type": ans.research_type.value,
                            "answer": ans.answer,
                            "confidence": ans.confidence,
                            "sources": ans.sources[:5]
                        }
                        for ans in it.research_answers
                    ],
                    "assumptions": [
                        {
                            "assumption": assump.assumption,
                            "reformulated": assump.reformulated
                        }
                        for assump in it.user_assumptions
                    ]
                }
                for it in result.iterations
            ]

        response = QueryResponse(
            query=result.user_query,
            concise_answer=result.concise_answer,
            confidence_score=result.confidence_score,
            total_iterations=result.total_iterations,
            processing_time=result.processing_time,
            final_report=result.final_report if not query_request.brief else None,
            iterations=iterations_dict,
            cached=False
        )

        # Cache the result
        await cache_manager.set(
            query_request.query,
            query_request.max_iterations or 3,
            response.dict(),
            ttl_seconds=86400  # 24 hours
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")
```

Add cache stats endpoint:

```python
@app.get("/cache/stats")
async def get_cache_stats(_: str = Depends(verify_api_key)):
    """Get cache statistics (admin endpoint)"""
    return cache_manager.get_stats()

@app.post("/cache/clear")
async def clear_cache(_: str = Depends(verify_api_key)):
    """Clear all cached results (admin endpoint)"""
    cache_manager.clear()
    return {"message": "Cache cleared"}
```

---

## 5. Health Check & Startup Validation (0.5 days)

### Step 5.1: Update `api/main.py` - Add Lifespan

Replace the current `@app.on_event` decorators with:

```python
from contextlib import asynccontextmanager

async def test_llm_connection() -> bool:
    """Test LLM endpoint connectivity"""
    try:
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{config.llm_base_url}/chat/completions",
                json={
                    "model": config.llm_model,
                    "messages": [{"role": "user", "content": "test"}],
                    "max_tokens": 10
                },
                headers={"Authorization": f"Bearer {config.llm_api_key}"},
                timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                return resp.status < 500
    except Exception as e:
        print(f"LLM connection test failed: {e}")
        return False

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app startup and shutdown"""
    # Startup
    print("=" * 80)
    print("Starting HPC Deep Research API...")
    print(f"LLM Model: {config.llm_model}")
    print(f"LLM URL: {config.llm_base_url}")
    print(f"Elasticsearch: {config.elastic_url}")
    print("=" * 80)

    # Test critical services
    print("\nValidating critical services...")

    # Test Elasticsearch
    es_ok = False
    try:
        await search_service.initialize()
        es_ok = True
        print("✓ Elasticsearch connection OK")
    except Exception as e:
        print(f"✗ Elasticsearch connection FAILED: {e}")

    # Test LLM
    llm_ok = await test_llm_connection()
    if llm_ok:
        print("✓ LLM endpoint OK")
    else:
        print("✗ LLM endpoint FAILED")

    if not (es_ok and llm_ok):
        print("\nCritical services unavailable. Cannot start.")
        raise RuntimeError("Critical services unavailable at startup")

    print("\nAll services healthy. API is ready.\n")

    yield

    # Shutdown
    print("\n" + "=" * 80)
    print("Shutting down HPC Deep Research API...")
    print("=" * 80)

# Update app initialization
app = FastAPI(
    title="HPC Deep Research API",
    description="Multi-agent deep research system for HPC support questions",
    version="1.0.0",
    lifespan=lifespan  # Add this
)
```

---

## 6. Testing Phase 1 Changes

### Step 6.1: Create `tests/test_phase1.py`

```python
import pytest
from fastapi.testclient import TestClient
from api.main import app
from api.auth import generate_api_key, hash_api_key
from api.cache import cache_manager

client = TestClient(app)

@pytest.fixture
def api_key():
    """Generate test API key"""
    return generate_api_key("test-key")

def test_health_no_auth():
    """Health check should work without auth"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] in ["healthy", "degraded"]

def test_query_requires_auth():
    """Query without auth should fail"""
    response = client.post(
        "/query",
        json={"query": "How do I use the HPC?"}
    )
    assert response.status_code == 403

def test_query_with_valid_auth(api_key):
    """Query with valid auth should work"""
    response = client.post(
        "/query",
        json={"query": "How do I use the HPC?"},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    # May fail due to missing LLM, but auth should pass
    assert response.status_code in [200, 500]

def test_query_validation():
    """Query validation should reject invalid input"""
    api_key = generate_api_key("test")

    # Too short
    response = client.post(
        "/query",
        json={"query": "HPC"},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    assert response.status_code == 422

    # Dangerous pattern
    response = client.post(
        "/query",
        json={"query": "import os; os.system('rm -rf /')"},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    assert response.status_code == 422

    # Invalid characters
    response = client.post(
        "/query",
        json={"query": "How to use HPC<script>alert('xss')</script>"},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    assert response.status_code == 422

def test_cache_hit(api_key, monkeypatch):
    """Identical queries should be cached"""
    # Mock the workflow to return quick result
    async def mock_process(*args, **kwargs):
        class Result:
            user_query = "Test query"
            concise_answer = "Test answer"
            confidence_score = 0.8
            total_iterations = 1
            processing_time = 0.1
            final_report = "Test report"
            iterations = []
        return Result()

    # First request (cache miss)
    response1 = client.post(
        "/query",
        json={"query": "How to optimize HPC?", "brief": True},
        headers={"Authorization": f"Bearer {api_key}"}
    )

    # Second request (cache hit)
    response2 = client.post(
        "/query",
        json={"query": "How to optimize HPC?", "brief": True},
        headers={"Authorization": f"Bearer {api_key}"}
    )

    # Both should succeed
    assert response1.status_code == 200
    assert response2.status_code == 200

    # Cache stats should show hits
    response = client.get(
        "/cache/stats",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    stats = response.json()
    assert stats["hits"] > 0

def test_rate_limiting(api_key):
    """Rate limiting should block excessive requests"""
    # Make 15 requests (limit is 10/minute)
    for i in range(15):
        response = client.get(
            "/health",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        if response.status_code == 429:
            assert "Rate limit exceeded" in response.json()["detail"]
            break
```

---

## 7. Deployment Checklist

Before deploying Phase 1:

- [ ] All code changes implemented
- [ ] Tests passing (`pytest tests/test_phase1.py`)
- [ ] API key generated and stored securely
- [ ] CORS configuration updated for your frontend
- [ ] Rate limits appropriate for your load
- [ ] Cache working (verify with `/cache/stats`)
- [ ] Health check passing on startup
- [ ] Documentation updated
- [ ] Example requests prepared for clients

## 8. Updated Requirements.txt

Add to `requirements.txt`:

```
python-jose[cryptography]>=3.3.0
slowapi>=0.1.9
structlog>=23.1.0
```

---

## Next Steps

After Phase 1 deployment:
1. Monitor metrics: error rates, latency, cache hit rate
2. Adjust rate limits based on actual usage
3. Collect user feedback on API key process
4. Plan Phase 2: Background job queue and Prometheus metrics
