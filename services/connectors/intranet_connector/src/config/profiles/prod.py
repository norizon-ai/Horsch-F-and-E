"""
Production environment configuration.

Settings optimized for production deployment.
"""

import os

# Trigger settings
TRIGGER_TYPE = os.getenv("CRAWLER_TRIGGER_TYPE", "queue")

# Publisher settings
PUBLISHER_TYPE = "queue"  # Use message queue in production

# Crawler settings
MAX_PAGES = 5000
MAX_DEPTH = 10
USE_STREAMING = True
USE_SITEMAP = True

# Respectful crawling
CRAWL_DELAY = 2.0  # Longer delay for production
RANDOM_DELAY = True

# Storage for backups
STORAGE_PATH = "/data/crawled_data"
BATCH_SIZE = 50  # Larger batches for efficiency

# Message queue
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://prod_user:prod_pass@rabbitmq:5672/")
INPUT_QUEUE = "crawl.requested"
OUTPUT_QUEUE = "content.raw.received"

# Logging
LOG_LEVEL = "INFO"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000
API_KEY = os.getenv("API_KEY")  # Required in production

# Cron jobs for production
CRON_JOBS = [
    {
        "name": "daily_update",
        "schedule": "0 3 * * *",  # 3 AM daily
        "config": {
            "url": os.getenv("CRAWL_URL", "https://www.fau.de"),
            "max_pages": 1000,
            "use_sitemap": True
        }
    }
]