# Intranet Connector - Clean Architecture

## Overview

The Intranet Connector has been refactored to follow a **hexagonal architecture** (ports and adapters pattern), providing a clean separation between business logic, input triggers, and output publishers. This design makes the system highly modular, testable, and extensible.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      Input Triggers                          │
├──────────┬──────────┬──────────┬──────────────────────────┤
│   CLI    │  Queue   │   Cron   │          API              │
└──────┬───┴────┬─────┴────┬─────┴──────┬───────────────────┘
       │        │          │            │
       └────────┴──────────┴────────────┘
                          │
                    ┌─────▼─────┐
                    │   Core    │
                    │  Business │
                    │   Logic   │
                    └─────┬─────┘
                          │
       ┌────────┬─────────┴────────┬────────┐
       │        │                  │        │
┌──────▼───┬────▼─────┬──────────▼──┬─────▼────┐
│   File   │  Queue   │   Database  │   Mock   │
└──────────┴──────────┴─────────────┴──────────┘
                 Output Publishers
```

## Directory Structure

```
src/
├── main.py                 # Unified entry point
│
├── core/                   # Business Logic (Domain)
│   ├── crawler.py         # Core crawler logic
│   ├── sitemap_crawler.py # Sitemap-specific crawler
│   └── crawler_factory.py # Factory for creating crawlers
│
├── triggers/              # Input Adapters (Ports)
│   ├── __init__.py
│   ├── base.py           # Abstract trigger interface
│   ├── cli.py            # CLI trigger
│   ├── queue.py          # Message queue trigger
│   └── cron.py           # Scheduled crawl trigger
│
├── publishers/            # Output Adapters (Ports)
│   ├── __init__.py
│   ├── base.py           # Abstract publisher interface
│   ├── factory.py        # Publisher factory
│   └── (implementations in publishing/)
│
├── config/               # Configuration Management
│   ├── __init__.py
│   ├── settings.py       # Main settings with Pydantic
│   └── profiles/         # Environment-specific configs
│       ├── dev.py        # Development settings
│       ├── prod.py       # Production settings
│       └── test.py       # Test settings
│
├── models/               # Domain Models
│   ├── articles.py       # Data models
│   └── communication.py  # Message models
│
└── utils/                # Utilities
    ├── estimators.py     # Crawl estimators
    └── processors.py     # Data processors
```

## Components

### 1. Triggers (Input Adapters)

Triggers determine **when** and **how** crawls are initiated:

- **CLITrigger**: Command-line interface for manual execution
- **QueueTrigger**: Listens to RabbitMQ for crawl requests
- **CronTrigger**: Executes crawls on a schedule
- **APITrigger**: REST API for remote triggering (planned)

All triggers inherit from `TriggerBase` and implement:
- `start()`: Begin listening for trigger events
- `stop()`: Clean shutdown
- `execute_crawl()`: Common crawl execution logic

### 2. Publishers (Output Adapters)

Publishers determine **where** crawled data is sent:

- **FileStoragePublisher**: Saves to JSON files on disk
- **DataPublisher**: Sends to RabbitMQ queue
- **ParquetStoragePublisher**: Saves in Parquet format
- **MockPublisher**: In-memory storage for testing

All publishers inherit from `PublisherBase` and implement:
- `connect()`: Establish connection to destination
- `publish_message()`: Send a crawled article
- `close()`: Clean up resources

### 3. Core Business Logic

The core contains the actual crawling logic, independent of triggers and publishers:

- **IntranetCrawler**: Deep crawling with link discovery
- **SitemapCrawler**: Efficient sitemap-based crawling
- **ErrorTracker**: Centralized error management

### 4. Configuration Profiles

Environment-specific settings are managed through profiles:

- **dev.py**: Local development (CLI trigger, file output)
- **prod.py**: Production (queue trigger, queue output)
- **test.py**: Testing (mock publishers, minimal crawling)

## Usage Examples

### 1. CLI Mode (Development)

```bash
# Using default (dev) profile
python main.py crawl https://example.com --max-pages 100

# With specific output
python main.py crawl https://example.com --output file
```

### 2. Queue Mode (Production)

```bash
# Set environment for production
export CRAWLER_PROFILE=prod
export CRAWLER_TRIGGER_TYPE=queue
python main.py
```

### 3. Cron Mode (Scheduled)

```bash
# Simple cron configuration
export CRAWLER_TRIGGER_TYPE=cron
export CRON_SCHEDULE="0 2 * * *"  # 2 AM daily
export CRON_URL="https://www.fau.de"
export CRON_MAX_PAGES=1000
python main.py

# Or use profile with predefined jobs
export CRAWLER_PROFILE=prod
export CRAWLER_TRIGGER_TYPE=cron
python main.py
```

### 4. Mixed Configurations

```bash
# Queue trigger with file output (for debugging)
export CRAWLER_TRIGGER_TYPE=queue
export CRAWLER_PUBLISHER_TYPE=file
python main.py

# CLI trigger with queue output
export CRAWLER_TRIGGER_TYPE=cli
export CRAWLER_PUBLISHER_TYPE=queue
python main.py crawl https://example.com
```

## Configuration

### Environment Variables

All settings can be configured via environment variables with the `CRAWLER_` prefix:

```bash
CRAWLER_TRIGGER_TYPE=queue        # Trigger type: cli, queue, cron, api
CRAWLER_PUBLISHER_TYPE=file       # Publisher: file, queue, mock
CRAWLER_MAX_PAGES=1000           # Maximum pages to crawl
CRAWLER_USE_SITEMAP=true         # Use sitemap for discovery
CRAWLER_CRAWL_DELAY=2.0          # Delay between requests
CRAWLER_STORAGE_PATH=./data      # File storage location
CRAWLER_RABBITMQ_URL=amqp://...  # RabbitMQ connection
CRAWLER_LOG_LEVEL=INFO           # Logging level
```

### Profile Selection

```bash
# Use a specific profile
export CRAWLER_PROFILE=prod
python main.py

# Profile overrides individual settings
# but environment variables override profile settings
export CRAWLER_PROFILE=prod
export CRAWLER_MAX_PAGES=100  # Overrides profile setting
python main.py
```

## Benefits of This Architecture

### 1. **Separation of Concerns**
- Core logic doesn't know about triggers or publishers
- Each component has a single responsibility
- Easy to understand and maintain

### 2. **Testability**
- Mock publishers for testing without external dependencies
- Each component can be tested in isolation
- Profile-based test configuration

### 3. **Extensibility**
- Add new triggers without changing core logic
- Add new publishers without changing triggers
- Mix and match components as needed

### 4. **Flexibility**
- Same crawler works with any trigger/publisher combination
- Environment-specific configuration through profiles
- Runtime configuration through environment variables

### 5. **Maintainability**
- Clear boundaries between components
- Consistent interfaces (base classes)
- Centralized configuration management

## Adding New Components

### Adding a New Trigger

1. Create `triggers/new_trigger.py`
2. Inherit from `TriggerBase`
3. Implement `start()`, `stop()`, and `get_publisher()`
4. Register in `main.py`

### Adding a New Publisher

1. Create `publishers/new_publisher.py`
2. Inherit from `PublisherBase`
3. Implement `connect()`, `publish_message()`, and `close()`
4. Register in `publishers/factory.py`

### Adding a New Profile

1. Create `config/profiles/new_profile.py`
2. Define settings as module-level constants
3. Use with `CRAWLER_PROFILE=new_profile`

## Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/

# Default to production profile
ENV CRAWLER_PROFILE=prod

# Entry point
CMD ["python", "src/main.py"]
```

## Docker Compose Example

```yaml
version: '3.8'

services:
  # Queue listener
  crawler-queue:
    build: .
    environment:
      CRAWLER_PROFILE: prod
      CRAWLER_TRIGGER_TYPE: queue
      CRAWLER_RABBITMQ_URL: amqp://rabbitmq:5672
    depends_on:
      - rabbitmq
  
  # Cron scheduler
  crawler-cron:
    build: .
    environment:
      CRAWLER_PROFILE: prod
      CRAWLER_TRIGGER_TYPE: cron
      CRON_SCHEDULE: "0 3 * * *"
      CRON_URL: https://www.fau.de
  
  # API service
  crawler-api:
    build: .
    environment:
      CRAWLER_PROFILE: prod
      CRAWLER_TRIGGER_TYPE: api
    ports:
      - "8000:8000"
  
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"
```

## Monitoring and Logging

The system provides comprehensive logging at different levels:

- **DEBUG**: Detailed crawl progress (dev profile)
- **INFO**: Normal operation logs (prod profile)
- **WARNING**: Issues that don't stop execution
- **ERROR**: Failures that need attention

Logs include:
- Trigger events (start, stop, job received)
- Crawl progress (pages processed, errors)
- Publisher events (connections, saves)
- Performance metrics (time per page, memory usage)

## Conclusion

This clean architecture provides a robust, scalable, and maintainable foundation for the Intranet Connector. The separation of triggers and publishers from core logic ensures the system can adapt to changing requirements without major refactoring.