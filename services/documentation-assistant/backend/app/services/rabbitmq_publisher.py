"""RabbitMQ publisher for sending documents to the knowledge base"""
import pika
import json
from app.config import settings
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class RabbitMQPublisher:
    """Publish documents to RabbitMQ queue"""

    @staticmethod
    def publish_document(document: Dict[str, Any]) -> bool:
        """
        Publish a document to the RabbitMQ queue

        Args:
            document: Document data to publish

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create connection parameters
            credentials = pika.PlainCredentials(
                settings.rabbitmq_user,
                settings.rabbitmq_password
            )

            parameters = pika.ConnectionParameters(
                host=settings.rabbitmq_host,
                port=settings.rabbitmq_port,
                credentials=credentials,
                # Add connection timeout and heartbeat
                connection_attempts=3,
                retry_delay=2,
                socket_timeout=10,
                heartbeat=600
            )

            # Establish connection
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # Declare queue (idempotent - will create if doesn't exist)
            channel.queue_declare(
                queue=settings.rabbitmq_queue,
                durable=True  # Survive broker restarts
            )

            # Prepare message
            message = {
                "document_id": document.get("id"),
                "title": document.get("title"),
                "content": document.get("content"),
                "metadata": document.get("metadata", {}),
                "source": "documentation-assistant",
                "type": "documentation"
            }

            # Publish message
            channel.basic_publish(
                exchange='',
                routing_key=settings.rabbitmq_queue,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Make message persistent
                    content_type='application/json'
                )
            )

            logger.info(f"Published document {document.get('id')} to RabbitMQ queue '{settings.rabbitmq_queue}'")

            # Close connection
            connection.close()

            return True

        except pika.exceptions.AMQPConnectionError as e:
            logger.error(f"Failed to connect to RabbitMQ: {e}")
            return False
        except Exception as e:
            logger.error(f"Error publishing to RabbitMQ: {e}")
            return False
