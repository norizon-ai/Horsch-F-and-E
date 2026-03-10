# Nora API Proxy

Production-ready FastAPI proxy server that forwards requests to DeepResearch API with SSE streaming support.

## Purpose

This proxy sits between the Nora frontend and DeepResearch backend, providing:
- Request/response logging and monitoring
- Centralized error handling
- Connection pooling and timeout management
- Future extensibility for authentication, rate limiting, and caching

## Features

- **HTTP Streaming Proxy**: Forwards SSE streams from DeepResearch to frontend
- **Production-Ready**: Proper error handling, timeouts, and health checks
- **Configurable**: Environment-based configuration for all endpoints
- **Connection Pooling**: Efficient HTTP client with connection reuse
- **CORS Support**: Configurable CORS for frontend integration
- **Health Checks**: Monitors DeepResearch connectivity

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running

### Development Mode

```bash
# Run locally with auto-reload
python main.py

# Or using uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 5002 --reload --log-level info
```

### Docker Development

```bash
# Start all services including proxy
cd /path/to/norizon-research
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker logs -f norizon-proxy-dev
```

### Production Docker

```bash
# Build and run
docker-compose up -d proxy

# Or manually
docker build -t norizon-proxy:latest -f Dockerfile .
docker run -d -p 5002:5002 \
  -e DEEPRESEARCH_URL=http://deepresearch:5000 \
  norizon-proxy:latest
```

### Kubernetes

```bash
# Deploy to K8s
kubectl apply -f k8s/proxy-deployment.yaml

# Check status
kubectl get pods -n norizon-research | grep proxy
kubectl logs -n norizon-research deployment/norizon-proxy
```

The proxy will run on `http://localhost:5002` (dev) or via Kubernetes service (prod)

## API Endpoints

### POST /query

Send a research query and receive streaming SSE results.

**Request:**
```json
{
  "query": "What is quantum computing?",
  "session_id": "session-abc-123",
  "include_web": true,
  "max_sources": 5
}
```

**Response:** Server-Sent Events stream (forwarded from DeepResearch)

```
data: {"type": "content", "data": "Quantum computing is..."}
data: {"type": "source", "data": {"id": "src-1", "title": "...", "url": "..."}}
data: {"type": "done", "data": null}
```

### GET /health

Health check endpoint - returns proxy status and DeepResearch connectivity.

**Response:**
```json
{
  "status": "healthy",
  "deepresearch_connected": true,
  "deepresearch_url": "http://deepresearch:5000"
}
```

### GET /

Root endpoint - returns service info.

**Response:**
```json
{
  "service": "Nora API Proxy",
  "version": "2.0.0",
  "status": "running",
  "deepresearch_url": "http://deepresearch:5000"
}
```

## Configuration

Environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DEEPRESEARCH_URL` | `http://deepresearch:5000` | DeepResearch API endpoint |
| `PROXY_PORT` | `5002` | Port to run the proxy on |
| `REQUEST_TIMEOUT` | `300` | Request timeout in seconds (5 min for research) |
| `CORS_ORIGINS` | `*` | Comma-separated allowed CORS origins |

## Architecture

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   Frontend   │─────▶│  Nora Proxy  │─────▶│ DeepResearch │
│  (SvelteKit) │◀─────│   (FastAPI)  │◀─────│     API      │
│    :5173     │ SSE  │    :5002     │ SSE  │    :5000     │
└──────────────┘      └──────────────┘      └──────────────┘
                             │
                             ▼
                      ┌─────────────┐
                      │   Logging   │
                      │   Metrics   │
                      │   Errors    │
                      └─────────────┘
```

The proxy:
1. Receives POST requests from frontend with query parameters
2. Forwards the request to DeepResearch API with proper headers
3. Streams SSE responses back to frontend in real-time
4. Handles errors and timeouts gracefully
5. Provides connection pooling and request logging

## Development Setup

For local development with frontend on localhost:5173:

1. Start Docker services (DeepResearch, Ollama, SearxNG, Proxy):
   ```bash
   cd services/norizon-research
   docker-compose -f docker-compose.dev.yml up -d proxy deepresearch ollama searxng
   ```

2. Configure frontend `.env`:
   ```bash
   echo "VITE_DEEPRESEARCH_API_URL=http://localhost:5002" > frontend/.env
   ```

3. Start frontend locally:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. Access:
   - Frontend: http://localhost:5173
   - Proxy: http://localhost:5002
   - Proxy Health: http://localhost:5002/health

## Production Deployment

### Docker Compose
```bash
docker-compose up -d
```

### Kubernetes
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/proxy-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/deepresearch-deployment.yaml
```

## Monitoring

Monitor proxy health and logs:

```bash
# Health check
curl http://localhost:5002/health

# Docker logs
docker logs -f norizon-proxy-dev

# Kubernetes logs
kubectl logs -f -n norizon-research deployment/norizon-proxy
```

## Troubleshooting

**Proxy can't connect to DeepResearch:**
- Check `DEEPRESEARCH_URL` environment variable
- Verify DeepResearch is running: `curl http://localhost:5001/health`
- Check Docker network: `docker network inspect norizon-network`

**Frontend can't connect to Proxy:**
- Verify proxy is running: `curl http://localhost:5002/health`
- Check frontend `.env` has correct `VITE_DEEPRESEARCH_API_URL`
- Check CORS settings if seeing CORS errors in browser console

**Streaming fails:**
- Check `REQUEST_TIMEOUT` is sufficient (default 5 minutes)
- Verify DeepResearch is responding: check proxy logs
- Test direct DeepResearch connection
