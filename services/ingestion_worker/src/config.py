"""
Configuration loader for the Ingestion Worker.
Loads settings from environment variables.
"""
import os

# RabbitMQ Configuration
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
RAW_CONTENT_QUEUE = os.getenv("RAW_CONTENT_QUEUE", "content.raw.received")

# Database Configuration (kept for backward compatibility)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/tierzero")

# Elasticsearch Configuration
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")
ELASTICSEARCH_PORT = int(os.getenv("ELASTICSEARCH_PORT", "9200"))
ELASTICSEARCH_USER = os.getenv("ELASTICSEARCH_USER")
ELASTICSEARCH_PASSWORD = os.getenv("ELASTICSEARCH_PASSWORD")

# Model Service Configuration
MODEL_SERVICE_URL = os.getenv("MODEL_SERVICE_URL", "http://localhost:8000")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
EMBEDDING_BATCH_SIZE = int(os.getenv("EMBEDDING_BATCH_SIZE", "32"))

# Chunking Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
