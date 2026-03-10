# Intranet Connector - Usage Examples

## Quick Start

### 1. Basic CLI Crawling

```bash
# Simple crawl with default settings
python src/main.py crawl https://www.fau.de

# With specific limits
python src/main.py crawl https://www.fau.de --max-pages 100 --sitemap

# Discover subdomains first
python src/main.py discover https://www.fau.de
```

### 2. Different Output Publishers

```bash
# Save to files (default)
python src/main.py crawl https://www.fau.de --output file

# Send to message queue
python src/main.py crawl https://www.fau.de --output queue

# Use mock publisher for testing
python src/main.py crawl https://www.fau.de --output mock
```

## Production Deployment

### 1. Queue Listener Mode

Listen for crawl jobs from RabbitMQ:

```bash
# Set up environment
export CRAWLER_TRIGGER_TYPE=queue
export CRAWLER_PUBLISHER_TYPE=queue
export CRAWLER_RABBITMQ_URL=amqp://user:pass@rabbitmq:5672
export CRAWLER_INPUT_QUEUE=crawl.requested
export CRAWLER_OUTPUT_QUEUE=content.raw.received

# Start listener
python src/main.py
```

Send a crawl job to the queue:

```python
import aio_pika
import json

async def send_crawl_job():
    connection = await aio_pika.connect("amqp://user:pass@rabbitmq:5672")
    channel = await connection.channel()
    
    job = {
        "job_id": "job-123",
        "target_url": "https://www.fau.de",
        "allowed_domains": ["fau.de", "www.fau.de"],
        "max_pages": 1000,
        "use_sitemap": True
    }
    
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps(job).encode()),
        routing_key="crawl.requested"
    )
```

### 2. Scheduled Crawling (Cron)

Set up daily crawls:

```bash
# Using environment variables
export CRAWLER_TRIGGER_TYPE=cron
export CRON_SCHEDULE="0 3 * * *"  # 3 AM daily
export CRON_URL="https://www.fau.de"
export CRON_MAX_PAGES=1000
export CRON_USE_SITEMAP=true

python src/main.py
```

Or define multiple jobs in configuration:

```python
# config/profiles/scheduled.py
TRIGGER_TYPE = "cron"
PUBLISHER_TYPE = "queue"

CRON_JOBS = [
    {
        "name": "daily_news",
        "schedule": "0 6 * * *",  # 6 AM daily
        "config": {
            "url": "https://www.fau.de/news",
            "max_pages": 100,
            "use_sitemap": True
        }
    },
    {
        "name": "weekly_full",
        "schedule": "0 2 * * 0",  # 2 AM Sunday
        "config": {
            "url": "https://www.fau.de",
            "max_pages": 5000,
            "use_sitemap": True,
            "include_subdomains": True
        }
    }
]
```

Run with profile:

```bash
export CRAWLER_PROFILE=scheduled
python src/main.py
```

## Development Workflow

### 1. Local Development

```bash
# Use dev profile (CLI trigger, file output, debug logging)
export CRAWLER_PROFILE=dev
python src/main.py crawl https://example.com

# View stored data
ls -la dev_crawled_data/
```

### 2. Testing

```bash
# Use test profile (mock publisher, minimal crawling)
export CRAWLER_PROFILE=test
python src/main.py crawl https://example.com

# Run with specific test settings
export CRAWLER_MAX_PAGES=5
export CRAWLER_MAX_DEPTH=1
export CRAWLER_PUBLISHER_TYPE=mock
python src/main.py crawl https://example.com
```

### 3. Debugging Production Issues

```bash
# Use queue trigger but save to files for debugging
export CRAWLER_TRIGGER_TYPE=queue
export CRAWLER_PUBLISHER_TYPE=file
export CRAWLER_STORAGE_PATH=./debug_output
export CRAWLER_LOG_LEVEL=DEBUG
python src/main.py
```

## Docker Examples

### 1. Single Service

```bash
# Build image
docker build -t intranet-connector .

# Run with CLI
docker run --rm intranet-connector \
  python src/main.py crawl https://www.fau.de

# Run as queue listener
docker run -d \
  --name crawler-queue \
  -e CRAWLER_TRIGGER_TYPE=queue \
  -e CRAWLER_RABBITMQ_URL=amqp://rabbitmq:5672 \
  --network mynetwork \
  intranet-connector

# Run as cron scheduler
docker run -d \
  --name crawler-cron \
  -e CRAWLER_TRIGGER_TYPE=cron \
  -e CRON_SCHEDULE="0 */6 * * *" \
  -e CRON_URL=https://www.fau.de \
  intranet-connector
```

### 2. Docker Compose Stack

```yaml
# docker-compose.yml
version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:3-management
    environment:
      RABBITMQ_DEFAULT_USER: crawler
      RABBITMQ_DEFAULT_PASS: secret
    ports:
      - "5672:5672"
      - "15672:15672"
  
  crawler-queue:
    build: .
    environment:
      CRAWLER_TRIGGER_TYPE: queue
      CRAWLER_PUBLISHER_TYPE: queue
      CRAWLER_RABBITMQ_URL: amqp://crawler:secret@rabbitmq:5672
    depends_on:
      - rabbitmq
    restart: unless-stopped
  
  crawler-cron:
    build: .
    environment:
      CRAWLER_TRIGGER_TYPE: cron
      CRAWLER_PUBLISHER_TYPE: file
      CRON_SCHEDULE: "0 */4 * * *"
      CRON_URL: https://www.fau.de
      CRON_MAX_PAGES: 500
    volumes:
      - ./crawled_data:/app/crawled_data
    restart: unless-stopped
```

Run the stack:

```bash
docker-compose up -d
docker-compose logs -f crawler-queue
```

## Mixed Mode Examples

### 1. File Storage with Queue Trigger

Useful for debugging production issues:

```bash
export CRAWLER_TRIGGER_TYPE=queue
export CRAWLER_PUBLISHER_TYPE=file
export CRAWLER_STORAGE_PATH=/mnt/debug_crawls
python src/main.py
```

### 2. CLI with Queue Output

Manual crawl that sends to production queue:

```bash
export CRAWLER_TRIGGER_TYPE=cli
export CRAWLER_PUBLISHER_TYPE=queue
export CRAWLER_RABBITMQ_URL=amqp://prod-server:5672
python src/main.py crawl https://www.fau.de --max-pages 100
```

### 3. Cron with Multiple Publishers

Use custom code to publish to multiple destinations:

```python
# custom_trigger.py
from triggers.cron import CronTrigger
from publishers.factory import PublisherFactory

class MultiPublisherCronTrigger(CronTrigger):
    def get_publisher(self):
        # Create composite publisher
        return CompositePublisher([
            PublisherFactory.create_publisher(self.settings, "file"),
            PublisherFactory.create_publisher(self.settings, "queue")
        ])
```

## Monitoring and Operations

### 1. View Crawl Sessions

```bash
# List all sessions
python src/main.py list

# Process specific session
python src/main.py process --session 20241211_143022 --export jsonl --output data.jsonl
```

### 2. Estimate Before Crawling

```bash
# Estimate crawl scope
python src/main.py estimate https://www.fau.de

# Discover subdomains
python src/main.py discover https://www.fau.de
```

### 3. Error Recovery

```bash
# View errors from latest crawl
python src/crawl_manager.py errors

# Export failed URLs
python src/crawl_manager.py export-errors --output failed.txt

# Retry failed URLs
python src/crawler_retry.py ./crawled_data 20241211_143022
```

## Environment Variable Reference

```bash
# Trigger configuration
CRAWLER_TRIGGER_TYPE=cli|queue|cron|api

# Publisher configuration  
CRAWLER_PUBLISHER_TYPE=file|queue|mock|parquet

# Crawler settings
CRAWLER_MAX_PAGES=1000
CRAWLER_MAX_DEPTH=5
CRAWLER_USE_SITEMAP=true
CRAWLER_CRAWL_DELAY=2.0
CRAWLER_USE_STREAMING=true

# Storage settings
CRAWLER_STORAGE_PATH=./crawled_data
CRAWLER_BATCH_SIZE=10

# Queue settings
CRAWLER_RABBITMQ_URL=amqp://user:pass@host:5672
CRAWLER_INPUT_QUEUE=crawl.requested
CRAWLER_OUTPUT_QUEUE=content.raw.received

# Cron settings
CRON_SCHEDULE="0 3 * * *"
CRON_URL=https://example.com
CRON_MAX_PAGES=1000

# Profile selection
CRAWLER_PROFILE=dev|prod|test

# Logging
CRAWLER_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR
```

## Tips and Best Practices

1. **Start with estimates**: Always run `estimate` before large crawls
2. **Use sitemaps**: Much faster and more respectful than deep crawling
3. **Monitor errors**: Check error reports regularly
4. **Test locally**: Use dev profile before deploying to production
5. **Batch processing**: Use larger batch sizes for better performance
6. **Respectful crawling**: Always use delays in production
7. **Profile separation**: Keep dev, test, and prod configurations separate
8. **Resource limits**: Set appropriate MAX_PAGES limits
9. **Error recovery**: Implement retry logic for transient failures
10. **Monitoring**: Set up logging aggregation in production