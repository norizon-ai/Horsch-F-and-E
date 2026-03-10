"""
Test environment configuration.

Settings optimized for automated testing.
"""

# Trigger settings
TRIGGER_TYPE = "cli"

# Publisher settings
PUBLISHER_TYPE = "mock"  # Use mock publisher for tests
STORAGE_PATH = "./test_data"

# Crawler settings - minimal for fast tests
MAX_PAGES = 10
MAX_DEPTH = 1
USE_STREAMING = False  # Simpler for testing
USE_SITEMAP = False

# No delays for fast testing
CRAWL_DELAY = 0
RANDOM_DELAY = False

# Logging
LOG_LEVEL = "WARNING"  # Less verbose for tests

# Test message queue
RABBITMQ_URL = "amqp://test:test@localhost:5672/"
INPUT_QUEUE = "test.crawl.requested"
OUTPUT_QUEUE = "test.content.raw.received"