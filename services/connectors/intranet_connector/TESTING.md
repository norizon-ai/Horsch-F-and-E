# Testing Guide for Intranet Connector

This guide covers how to test the Intranet Connector with both mock and real message queue systems.

---

## 🔍 PR Reviewer Instructions

**⏱️ Total Review Time: ~15 minutes**

This section provides a step-by-step guide for PR reviewers to quickly validate the complete Intranet Connector implementation.

### Prerequisites
- **Docker & Docker Compose**: Installed and running
- **Python 3.13+**: With virtual environment support
- **Terminal Access**: To run test commands

### Step-by-Step Review Process

#### 1. Environment Setup (2 minutes)
```bash
# Navigate to the connector directory
cd services/connectors/intranet_connector

# Activate the virtual environment of your choice (virtualenv, conda, ...)
# requirements are needed to run the test scripts only, for production setup everything is in the container images
# make sure that the requirements are installed:
pip install -r requirements.txt

pip install -e .

# Verify environment is ready
python -c "import sys; print('✅ Python ready:', sys.version)"
```

#### 2. Start Infrastructure (3 minutes)
```bash
# Start RabbitMQ and Elasticsearch services
docker-compose up -d

# Wait for services to initialize
echo "⏳ Waiting for services to start..."
sleep 30

# Verify services are running
docker-compose ps

# Expected: Both rabbitmq and elasticsearch should show "Up" status
```

#### 3. Test Core Components (5 minutes)

**Test A: Mock Publisher Integration** *(Fastest - always works)*
```bash
# Test crawler with mock publisher
python src/crawler.py

# ✅ Expected output:
# - "=== Testing with Mock Publisher ==="
# - Shows ~5 crawled pages with content length > 5000 chars each
# - "Published a total of 5 pages"
# - Legacy crawler test also shows similar results
```

**Test B: Real RabbitMQ Integration**
```bash
# Test with actual RabbitMQ queue
python test_real_publisher.py

# ✅ Expected output:
# - "✅ Successfully connected to RabbitMQ"
# - Crawl4AI progress logs with URLs
# - "✅ Successfully published X pages to RabbitMQ"
# - Consumer shows valid JSON message structure
# - Queue statistics displayed
```

#### 4. Test End-to-End Job Processing (3 minutes)

**Terminal 1 - Start Job Listener:**
```bash
python src/job_listener.py

# ✅ Expected output:
# - "🎯 Intranet Connector Job Listener starting..."
# - "✅ Successfully connected to RabbitMQ and initialized publisher"
# - "🎧 Starting to listen for messages on queue 'crawl.requested'"
```

**Terminal 2 - Send Test Job:**
```bash
# In a new terminal (same directory, activate venv)
source venv/bin/activate
python test_job_listener.py

# ✅ Expected output:
# - "📤 Sending test crawl job..."
# - "✅ Successfully sent job to queue 'crawl.requested'"
# - "📨 Received result #1-3:" with crawled content
# - "🎉 All tests PASSED! Service is ready."
```

#### 5. Test Health & Service Endpoints (2 minutes)

**Stop job listener** (Ctrl+C) and **start full FastAPI service:**
```bash
python src/service.py

# ✅ Expected output:
# - "🚀 Starting Intranet Connector Service..."
# - "INFO: Uvicorn running on http://0.0.0.0:8000"
```

**Test Service Endpoints:**
```bash
# Test health endpoint
curl -s http://localhost:8000/health | python -m json.tool

# ✅ Expected: JSON with "status": "healthy" and detailed checks

# Test service info
curl -s http://localhost:8000/ | python -m json.tool

# ✅ Expected: Service info with available endpoints

# Test metrics
curl -s http://localhost:8000/metrics | python -m json.tool

# ✅ Expected: Queue metrics and uptime statistics
```

### 🎯 Success Criteria for PR Approval

**✅ Must Pass All Tests:**
1. **Mock Integration**: 5+ pages crawled with substantial content (>5KB each)
2. **RabbitMQ Integration**: Messages successfully queued and consumed
3. **Job Processing**: Complete end-to-end job execution
4. **Health Checks**: All endpoints return `"status": "healthy"`
5. **Service Endpoints**: All API endpoints respond correctly

**❌ Red Flags - Request Changes If:**
- Import errors or circular dependency issues
- Empty or minimal content in crawled pages (<1KB)
- RabbitMQ connection failures (when Docker is running)
- Health checks showing "unhealthy" status
- Unhandled exceptions or service crashes
- Test scripts failing to complete successfully

### 🧹 Cleanup After Testing
```bash
# Stop all services
docker-compose down

# Stop FastAPI service (Ctrl+C)

# Deactivate virtual environment
deactivate
```

### 📊 Performance Expectations
- **Mock tests**: ~30 seconds
- **RabbitMQ integration**: ~60 seconds
- **End-to-end job processing**: ~90 seconds
- **Health endpoint responses**: <2 seconds each

### 🔗 Additional Verification
- **RabbitMQ UI**: http://localhost:15672 (`test_user` / `test_pass`)
- **Service Documentation**: All endpoints documented in `/` response
- **Configuration**: Check `src/config.py` for proper environment variable support

---

## 🧪 Detailed Testing Documentation

## Quick Start

### 1. Unit Testing with Mocks
```bash
# Run basic crawler test with mock publisher
source venv/bin/activate
python src/crawler.py
```

### 2. Integration Testing with Real RabbitMQ

#### Start Services
```bash
# Start RabbitMQ and Elasticsearch
docker-compose up -d

# Check services are running
docker-compose ps
```

#### Run Integration Test
```bash
# Test crawler → RabbitMQ integration
python test_real_publisher.py
```

#### Verify Results
- **RabbitMQ Management UI**: http://localhost:15672
- **Login**: `test_user` / `test_pass`
- **Queue**: Check `test_crawled_content` queue for messages

#### Test with Ingestion Worker
```bash
# Run the ingestion worker to consume messages
cd ../../ingestion_worker
python src/main.py
```

## Test Scenarios

### ✅ Completed Tests
- [x] **Mock Publisher Integration**: Crawler publishes to in-memory mock
- [x] **Real RabbitMQ Publishing**: Crawler publishes to actual RabbitMQ queue
- [x] **Message Structure Validation**: Verify `RawArticle` JSON format
- [x] **End-to-End Job Processing**: Complete crawl job workflow
- [x] **Job Listener Integration**: Service consumes `crawl.requested` messages
- [x] **Health Endpoints**: FastAPI health monitoring and metrics
- [x] **Service Integration**: Complete FastAPI service with lifecycle management
- [x] **Error Handling**: Graceful handling of failures and connection issues

### 🚧 Advanced Tests (Optional)
- [ ] **Performance Testing**: Large-scale crawling with high page limits
- [ ] **Load Testing**: Multiple concurrent crawl jobs
- [ ] **Ingestion Worker Integration**: Full pipeline to Elasticsearch

### 📋 Configuration Tests
- [x] **Environment Variables**: All `CRAWLER_*` settings work correctly
- [x] **Queue Configuration**: Custom queue names and RabbitMQ URLs
- [x] **Content Filtering**: Excluded tags, external links, social media filtering

## Docker Services

### RabbitMQ
- **Port**: 5672 (AMQP)
- **Management UI**: 15672
- **Credentials**: test_user / test_pass

### Elasticsearch
- **Port**: 9200 (HTTP)
- **Health**: http://localhost:9200/_cluster/health

### Cleanup
```bash
# Stop services
docker-compose down

# Remove volumes (reset data)
docker-compose down -v
```

## Test Structure

```
testing/
├── mock_publisher.py       # Mock implementation for unit tests
├── test_crawler.py        # Unit tests with mocks
└── __init__.py

# Integration test files
test_real_publisher.py     # Real RabbitMQ integration test
docker-compose.yml         # Local test environment
```

## Expected Results

### Successful Crawl Output
```
=== Testing with Mock Publisher ===
MockPublisher: Simulating connection.
[CRAWL OUTPUT FROM CRAWL4AI]
Published page: https://fau.de
Published a total of 5 pages.
```

### RabbitMQ Message Format
```json
{
  "source_document_id": "https://fau.de",
  "content": "# Page Title\n\nClean markdown content...",
  "source": {
    "uri": "https://fau.de",
    "module": "Intranet Connector",
    "retrieved_at": "2024-01-01T12:00:00Z"
  },
  "author": null,
  "tags": [],
  "permissions": [],
  "metadata": {
    "title": "Page Title",
    "status_code": 200
  }
}
```

## Troubleshooting

### RabbitMQ Connection Issues
```bash
# Check if RabbitMQ is running
docker-compose logs rabbitmq

# Restart RabbitMQ
docker-compose restart rabbitmq
```

### Import Issues
```bash
# Ensure you're in the right directory
cd services/connectors/intranet_connector

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

### Port Conflicts
```bash
# Check what's using port 5672
lsof -i :5672

# Use different ports in docker-compose.yml if needed
```
