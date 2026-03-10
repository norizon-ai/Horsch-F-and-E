import pika
import json
import uuid

# --- Realistic Test Messages ---
# These are dictionaries that match the structure of your CrawledContentMessage model.
test_messages = [
    {
        "source_type": "intranet",
        "source_uri": "https://internal.company.com/news/article-1",
        "content": "This is the full text of the first news article. It discusses the quarterly earnings and future projections.",
        "metadata": {"author": "john.doe", "title": "Q3 Earnings Report", "tags": ["finance", "news"]},
        "permissions": ["role:employee"]
    },
    {
        "source_type": "intranet",
        "source_uri": "https://internal.company.com/hr/policy-update-2025",
        "content": "The updated HR policy includes new guidelines for remote work and benefits. All employees are required to read and acknowledge this document.",
        "metadata": {"author": "jane.smith", "title": "HR Policy Update 2025", "department": "HR"},
        "permissions": ["role:employee"]
    },
    {
        "source_type": "intranet",
        "source_uri": "https://internal.company.com/it/security-best-practices",
        "content": "IT security is everyone's responsibility. This document outlines best practices for password management, phishing detection, and data protection.",
        "metadata": {"author": "security.team", "title": "IT Security Guide"},
        "permissions": ["role:it-admin", "role:employee"]
    }
]

# --- RabbitMQ Connection ---
try:
    # Connect to the RabbitMQ container on localhost
    connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:5672/'))
    channel = connection.channel()

    # Declare the same queue the worker is listening to
    # This is idempotent, so it's safe to run even if the queue already exists
    queue_name = 'content.raw.received'
    channel.queue_declare(queue=queue_name, durable=True)

    # --- Publish Messages ---
    for message_body in test_messages:
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(message_body),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
                correlation_id=str(uuid.uuid4()) # unique id for tracing
            ))
        print(f" [x] Sent message for: '{message_body['metadata']['title']}'")

    connection.close()
    print("\nSuccessfully sent all test messages.")

except pika.exceptions.AMQPConnectionError as e:
    print(f"Error: Could not connect to RabbitMQ at localhost:5672.")
    print("Please ensure the docker-compose services are running.")
