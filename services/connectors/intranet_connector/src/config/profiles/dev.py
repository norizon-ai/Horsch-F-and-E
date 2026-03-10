"""
Development environment configuration.

Settings optimized for local development and testing.
"""

# Trigger settings
TRIGGER_TYPE = "cli"

# Publisher settings  
PUBLISHER_TYPE = "file"
STORAGE_PATH = "./dev_crawled_data"

# Crawler settings
MAX_PAGES = 2000
MAX_DEPTH = 2
USE_STREAMING = True
USE_SITEMAP = True
BATCH_SIZE = 20  # Larger batches for efficiency

# Delays for respectful crawling
CRAWL_DELAY = 0.5  # Shorter delay for dev
RANDOM_DELAY = False

# Logging
LOG_LEVEL = "DEBUG"

# API settings
API_HOST = "localhost"
API_PORT = 8000

# Message queue (for testing)
RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"