# Nora Proxy Setup Guide

## Overview

The Nora FastAPI proxy now successfully integrates with your DeepResearch backend! The proxy sits between your frontend and DeepResearch, providing:
- Request/response logging and monitoring
- Centralized error handling
- Connection pooling for efficient HTTP requests
- Future extensibility for authentication, rate limiting, and caching

## Current Architecture

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   Frontend   │─────▶│  Nora Proxy  │─────▶│ DeepResearch │
│  (SvelteKit) │◀─────│   (FastAPI)  │◀─────│     API      │
│  localhost:  │ SSE  │    Docker    │ SSE  │    Docker    │
│    5173      │      │    :5002     │      │    :5001     │
└──────────────┘      └──────────────┘      └──────────────┘
                             │
                             ▼
                      ┌─────────────┐
                      │   Ollama    │
                      │  SearxNG    │
                      │   (Docker)  │
                      └─────────────┘
```

## Your Current Hybrid Setup

You're running:
- **Frontend**: Locally on `localhost:5173` (for hot reload during development)
- **Proxy**: Docker container on `localhost:5002` ✓ **NEW**
- **DeepResearch**: Docker container on `localhost:5001`
- **Ollama**: Docker container on `localhost:11434`
- **SearxNG**: Docker container on `localhost:8080`

## Quick Start

### 1. Start Docker Services (Backend + Proxy)

```bash
cd /Users/omariko/Documents/GitHub/tier-zero/services/norizon-research

# Start all backend services including the new proxy
docker-compose -f docker-compose.dev.yml up -d proxy deepresearch ollama searxng

# Check that proxy is healthy
curl http://localhost:5002/health
```

Expected output:
```json
{
  "status": "healthy",
  "deepresearch_connected": true,
  "deepresearch_url": "http://deepresearch:5000"
}
```

### 2. Start Frontend Locally

```bash
cd /Users/omariko/Documents/GitHub/tier-zero/services/norizon-research/frontend

# Install dependencies (first time only)
npm install

# Start dev server
npm run dev
```

The frontend will automatically connect to the proxy at `http://localhost:5002` (configured in `.env`)

### 3. Access the Application

Open your browser to: **http://localhost:5173**

The request flow will be:
```
Browser → Frontend (5173) → Proxy (5002) → DeepResearch (5001) → Ollama/SearxNG
```

## Verification

### Check All Services

```bash
# Proxy
curl http://localhost:5002/health

# DeepResearch (should redirect to /auth/login)
curl -I http://localhost:5001/

# Ollama
curl http://localhost:11434/api/tags

# SearxNG
curl http://localhost:8080/
```

### View Logs

```bash
# Proxy logs (watch for requests)
docker logs -f norizon-proxy-dev

# DeepResearch logs
docker logs -f norizon-deepresearch-dev

# Ollama logs
docker logs -f norizon-ollama-dev

# SearxNG logs
docker logs -f norizon-searxng-dev
```

## Common Issues & Solutions

### Issue: Frontend can't connect to proxy

**Symptoms**: CORS errors, connection refused in browser console

**Solution**:
```bash
# 1. Verify proxy is running
docker ps | grep proxy

# 2. Check proxy logs
docker logs norizon-proxy-dev

# 3. Verify frontend .env
cat frontend/.env | grep VITE_DEEPRESEARCH_API_URL
# Should output: VITE_DEEPRESEARCH_API_URL=http://localhost:5002

# 4. Restart frontend dev server
cd frontend
npm run dev
```

### Issue: Proxy can't connect to DeepResearch

**Symptoms**: Health check shows `deepresearch_connected: false`

**Solution**:
```bash
# 1. Check if DeepResearch is running
docker ps | grep deepresearch

# 2. Restart DeepResearch
docker-compose -f docker-compose.dev.yml restart deepresearch

# 3. Wait for Ollama to be ready (DeepResearch depends on it)
docker logs norizon-ollama-dev | grep "successfully"

# 4. Check network connectivity
docker network inspect norizon-network | grep -A 3 "norizon-proxy"
```

### Issue: Research queries timeout

**Symptoms**: Queries hang or timeout after 5 minutes

**Solution**:
The proxy has a 5-minute timeout (300 seconds) for research queries. If you need longer:

```bash
# Edit docker-compose.dev.yml
# Under proxy service, change:
environment:
  - REQUEST_TIMEOUT=600  # 10 minutes

# Restart proxy
docker-compose -f docker-compose.dev.yml restart proxy
```

### Issue: Auto-reload not working for proxy code

**Symptoms**: Changes to `proxy/main.py` don't take effect

**Solution**:
The proxy runs with `--reload` flag and has volume mount. Changes should auto-reload:

```bash
# If it doesn't, manually restart:
docker-compose -f docker-compose.dev.yml restart proxy

# Watch logs to see reload:
docker logs -f norizon-proxy-dev
```

## Development Workflow

### Making Changes to Proxy Code

1. Edit `services/norizon-research/proxy/main.py`
2. Save the file
3. Watch logs: `docker logs -f norizon-proxy-dev`
4. You should see: `WatchFiles detected changes in 'main.py'. Reloading...`
5. Changes are live immediately (no restart needed)

### Adding New Dependencies

1. Add to `services/norizon-research/proxy/requirements.txt`
2. Rebuild the proxy container:
   ```bash
   docker-compose -f docker-compose.dev.yml up -d --build proxy
   ```

### Testing the Proxy API Directly

```bash
# Test query endpoint (will need a valid session_id)
curl -X POST http://localhost:5002/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is quantum computing?",
    "session_id": "test-session-123",
    "include_web": true,
    "max_sources": 5
  }'
```

## Production Deployment

### Docker Compose Production

```bash
# Build and start all services
docker-compose up -d

# Check status
docker ps
```

The proxy will be accessible at `http://localhost:5002` or via your ingress/load balancer.

### Kubernetes Deployment

```bash
# Deploy proxy
kubectl apply -f k8s/proxy-deployment.yaml

# Verify
kubectl get pods -n norizon-research | grep proxy
kubectl logs -n norizon-research deployment/norizon-proxy

# Check service
kubectl get svc -n norizon-research | grep proxy
```

The frontend will connect to the proxy via the service URL: `http://norizon-proxy-service:5002`

## Monitoring

### Health Checks

The proxy exposes a health endpoint that checks:
- Proxy status
- DeepResearch connectivity

```bash
# Local
curl http://localhost:5002/health

# Kubernetes
kubectl exec -n norizon-research deployment/norizon-proxy -- \
  curl http://localhost:5002/health
```

### Logs

Proxy logs include:
- Startup information
- Connection tests to DeepResearch
- Each query request (with first 50 chars)
- Streaming progress
- Errors and exceptions

```bash
# Docker
docker logs -f norizon-proxy-dev

# Kubernetes
kubectl logs -f -n norizon-research deployment/norizon-proxy
```

### Metrics to Watch

Look for these log patterns:

**Healthy:**
```
✓ Successfully connected to DeepResearch
Proxying query: 'What is...' (session: abc-123)
Query completed successfully (session: abc-123)
```

**Issues:**
```
Failed to connect to DeepResearch: [error]
DeepResearch returned 500: [error]
Streaming error: [error]
```

## Configuration Reference

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEEPRESEARCH_URL` | `http://deepresearch:5000` | DeepResearch API URL (use service name in Docker) |
| `PROXY_PORT` | `5002` | Port the proxy listens on |
| `REQUEST_TIMEOUT` | `300` | Timeout for research queries (seconds) |
| `CORS_ORIGINS` | `*` | Allowed CORS origins (comma-separated) |

### Frontend Configuration

Edit `frontend/.env`:
```bash
VITE_DEEPRESEARCH_API_URL=http://localhost:5002
```

For production, this should point to your proxy's public URL.

## Next Steps

Now that the proxy is integrated:

1. **Test end-to-end**: Submit a query via the frontend and verify it flows through the proxy
2. **Monitor logs**: Watch the proxy logs to see requests being proxied
3. **Add features**: Enhance the proxy with:
   - Request rate limiting
   - Authentication/authorization
   - Request/response caching
   - Custom logging/metrics
   - Request retry logic

## Additional Resources

- Proxy source code: `services/norizon-research/proxy/main.py`
- Proxy README: `services/norizon-research/proxy/README.md`
- Docker configs: `services/norizon-research/docker-compose.dev.yml`
- Kubernetes configs: `services/norizon-research/k8s/proxy-deployment.yaml`

## Need Help?

If you encounter issues:
1. Check the logs: `docker logs norizon-proxy-dev`
2. Verify health: `curl http://localhost:5002/health`
3. Check network: `docker network inspect norizon-network`
4. Restart services: `docker-compose -f docker-compose.dev.yml restart proxy`
