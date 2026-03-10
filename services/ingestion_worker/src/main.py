import pika
import time
import sys
import json
import logging
from typing import List, Dict, Any

from . import config
from .models import CrawledContentMessage
from .chunking import create_chunker
from .elasticsearch_client import ElasticsearchClient
from .model_client import ModelServiceClient

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IngestionWorker:
    """
    Enhanced ingestion worker with smart chunking and Elasticsearch integration.
    """
    
    def __init__(self):
        """Initialize the ingestion worker with all required clients."""
        self.chunker = create_chunker(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )
        
        self.es_client = ElasticsearchClient(
            es_host=config.ELASTICSEARCH_HOST,
            es_port=config.ELASTICSEARCH_PORT,
            es_user=config.ELASTICSEARCH_USER,
            es_password=config.ELASTICSEARCH_PASSWORD
        )
        
        self.model_client = ModelServiceClient(
            model_service_url=config.MODEL_SERVICE_URL
        )
        
        # Health checks
        self._perform_health_checks()
    
    def _perform_health_checks(self):
        """Perform health checks on all external services."""
        logger.info("Performing health checks...")
        
        # Check Elasticsearch
        if not self.es_client.health_check():
            logger.warning("Elasticsearch health check failed - service may be unavailable")
        else:
            logger.info("Elasticsearch is healthy")
        
        # Check Model Service
        if not self.model_client.health_check():
            logger.warning("Model service health check failed - will use fallback embeddings")
        else:
            logger.info("Model service is healthy")
    
    def process_content(self, message: CrawledContentMessage) -> bool:
        """
        Process a single content message through the enhanced pipeline.
        
        Args:
            message: The crawled content message to process
            
        Returns:
            bool: True if processing was successful, False otherwise
        """
        try:
            logger.info(f"Processing content from {message.source_uri}")
            
            # Step 1: Smart chunking
            chunks, enhanced_metadata = self.chunker.chunk_content(
                content=message.content,
                source_uri=message.source_uri,
                existing_metadata=message.metadata
            )
            
            logger.info(f"Created {len(chunks)} chunks from {message.source_uri}")
            
            # Step 2: Generate embeddings
            chunk_texts = [chunk['content'] for chunk in chunks]
            embeddings = self._generate_embeddings(chunk_texts)
            
            if embeddings is None:
                logger.error(f"Failed to generate embeddings for {message.source_uri}")
                return False
            
            # Step 3: Store in Elasticsearch
            success = self.es_client.store_chunks(
                source_uri=message.source_uri,
                source_type=message.source_type,
                chunks=chunks,
                embeddings=embeddings,
                permissions=message.permissions,
                document_metadata=enhanced_metadata
            )
            
            if success:
                logger.info(f"Successfully processed and stored content from {message.source_uri}")
                return True
            else:
                logger.error(f"Failed to store content from {message.source_uri} in Elasticsearch")
                return False
                
        except Exception as e:
            logger.error(f"Error processing content from {message.source_uri}: {e}", exc_info=True)
            return False
    
    def _generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for text chunks with fallback to dummy embeddings.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        try:
            # Try to use the model service
            embeddings = self.model_client.generate_embedding_batch(
                texts=texts,
                batch_size=config.EMBEDDING_BATCH_SIZE,
                model_name=config.EMBEDDING_MODEL_NAME
            )
            
            if embeddings is not None:
                logger.info(f"Generated embeddings using model service for {len(texts)} chunks")
                return embeddings
            else:
                logger.warning("Model service failed, falling back to dummy embeddings")
                return self._generate_dummy_embeddings(texts)
                
        except Exception as e:
            logger.warning(f"Error generating embeddings: {e}, falling back to dummy embeddings")
            return self._generate_dummy_embeddings(texts)
    
    def _generate_dummy_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate dummy embeddings as fallback.
        
        Args:
            texts: List of text strings
            
        Returns:
            List of dummy embedding vectors
        """
        logger.warning(f"Generating dummy embeddings for {len(texts)} chunks")
        # Create deterministic dummy embeddings based on text hash
        import hashlib
        
        embeddings = []
        for text in texts:
            # Create a simple hash-based embedding
            text_hash = hashlib.md5(text.encode()).hexdigest()
            # Convert hex to numbers and normalize to create a 768-dim vector
            embedding = []
            for i in range(0, len(text_hash), 2):
                hex_pair = text_hash[i:i+2]
                value = int(hex_pair, 16) / 255.0  # Normalize to 0-1
                embedding.append(value)
            
            # Pad or truncate to 768 dimensions
            while len(embedding) < 768:
                embedding.extend(embedding[:min(len(embedding), 768 - len(embedding))])
            embedding = embedding[:768]
            
            embeddings.append(embedding)
        
        return embeddings


def process_message_callback(ch, method, properties, body):
    """
    Callback function executed when a message is received.
    Enhanced version with smart chunking and Elasticsearch.
    """
    try:
        # Parse the message
        message_data = json.loads(body)
        message = CrawledContentMessage(**message_data)
        
        logger.info(f"Received message for {message.source_uri}")
        
        # Create worker instance and process
        worker = IngestionWorker()
        success = worker.process_content(message)
        
        if success:
            # Acknowledge the message
            ch.basic_ack(delivery_tag=method.delivery_tag)
            logger.info(f"Successfully processed and acknowledged message for {message.source_uri}")
        else:
            # Reject the message and requeue for retry
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
            logger.error(f"Failed to process message for {message.source_uri}, requeuing")
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    except Exception as e:
        logger.error(f"Error in message callback: {e}", exc_info=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    finally:
        if es_client:
            es_client.close()


def main():
    """
    Main function to start the enhanced ingestion worker.
    """
    logger.info("Starting Enhanced Ingestion Worker...")
    
    # Connect to RabbitMQ with retry logic
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempting to connect to RabbitMQ (attempt {attempt + 1}/{max_retries})")
            connection = pika.BlockingConnection(pika.URLParameters(config.RABBITMQ_URL))
            channel = connection.channel()
            
            # Declare the queue (idempotent)
            channel.queue_declare(queue=config.RAW_CONTENT_QUEUE, durable=True)
            
            # Set up consumer
            channel.basic_qos(prefetch_count=1)  # Process one message at a time
            channel.basic_consume(
                queue=config.RAW_CONTENT_QUEUE,
                on_message_callback=process_message_callback
            )
            
            logger.info("Enhanced Ingestion Worker is ready. Waiting for messages...")
            logger.info("Features enabled:")
            logger.info("  - Smart chunking (HTML→Markdown, header-based)")
            logger.info("  - Elasticsearch storage")
            logger.info("  - Model service integration")
            logger.info("  - Fallback dummy embeddings")
            
            # Start consuming
            channel.start_consuming()
            
        except pika.exceptions.AMQPConnectionError as e:
            logger.error(f"Failed to connect to RabbitMQ: {e}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                logger.error("Max retries reached. Exiting.")
                sys.exit(1)
        except KeyboardInterrupt:
            logger.info("Received interrupt signal. Shutting down gracefully...")
            try:
                channel.stop_consuming()
                connection.close()
            except:
                pass
            sys.exit(0)
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            sys.exit(1)


if __name__ == "__main__":
    main()