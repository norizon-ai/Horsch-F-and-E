"""
Enhanced test publisher for the smart chunking ingestion worker.
Tests HTML content, Markdown content, and plain text with various structures.
"""
import pika
import json
import uuid

# Enhanced test messages with different content types
test_messages = [
    {
        "source_type": "intranet",
        "source_uri": "https://internal.company.com/news/quarterly-report.html",
        "content": """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Q3 2024 Quarterly Report</title>
            <meta name="author" content="Finance Team">
            <meta name="description" content="Comprehensive quarterly financial report">
        </head>
        <body>
            <h1>Q3 2024 Financial Results</h1>
            <p>We are pleased to announce strong financial performance for Q3 2024.</p>
            
            <h2>Revenue Overview</h2>
            <p>Total revenue increased by 15% compared to Q2 2024, reaching $2.5M.</p>
            <ul>
                <li>Product sales: $1.8M (+20%)</li>
                <li>Service revenue: $0.7M (+5%)</li>
            </ul>
            
            <h2>Key Metrics</h2>
            <p>Our key performance indicators show positive trends:</p>
            <h3>Customer Acquisition</h3>
            <p>New customers: 150 (+25% from last quarter)</p>
            <h3>Customer Retention</h3>
            <p>Retention rate: 92% (industry average: 85%)</p>
            
            <h2>Future Outlook</h2>
            <p>Based on current trends, we project continued growth in Q4 2024.</p>
            <p>Expected revenue range: $2.7M - $3.0M</p>
        </body>
        </html>
        """,
        "metadata": {
            "department": "Finance",
            "quarter": "Q3 2024",
            "tags": ["financial", "quarterly", "revenue"]
        },
        "permissions": ["role:employee", "role:finance"]
    },
    {
        "source_type": "documentation",
        "source_uri": "https://docs.company.com/api/authentication.md",
        "content": """# API Authentication Guide

## Overview
This guide explains how to authenticate with our REST API using various methods.

## Authentication Methods

### 1. API Key Authentication
The simplest method for server-to-server communication.

#### Setup
1. Generate an API key in the developer console
2. Include the key in the `X-API-Key` header
3. Make your request

```bash
curl -H "X-API-Key: your-api-key" https://api.company.com/v1/users
```

### 2. OAuth 2.0
Recommended for user-facing applications.

#### Authorization Code Flow
1. Redirect user to authorization endpoint
2. User grants permission
3. Exchange code for access token
4. Use token in Authorization header

### 3. JWT Tokens
For internal services and microservices communication.

#### Token Structure
- Header: Algorithm and token type
- Payload: Claims and user information  
- Signature: Verification signature

## Best Practices
- Always use HTTPS in production
- Rotate API keys regularly
- Implement proper token expiration
- Use appropriate scopes for OAuth

## Rate Limiting
All endpoints are subject to rate limiting:
- 1000 requests per hour for authenticated users
- 100 requests per hour for unauthenticated requests
""",
        "metadata": {
            "type": "documentation",
            "category": "API",
            "last_updated": "2024-01-15",
            "author": "dev-team"
        },
        "permissions": ["role:developer", "role:employee"]
    },
    {
        "source_type": "policy",
        "source_uri": "https://hr.company.com/policies/remote-work-2024",
        "content": "Remote Work Policy 2024\n\nEffective Date: January 1, 2024\n\nPurpose: This policy establishes guidelines for remote work arrangements to ensure productivity, collaboration, and work-life balance.\n\nEligibility: All full-time employees who have completed their probationary period are eligible for remote work arrangements. Part-time employees may be considered on a case-by-case basis.\n\nWork Schedule: Remote employees must maintain core business hours (9 AM - 3 PM local time) for collaboration and meetings. Flexible hours outside core time are permitted with manager approval.\n\nEquipment and Technology: The company will provide necessary equipment including laptop, monitor, and ergonomic accessories. Employees are responsible for maintaining a secure internet connection.\n\nCommunication Requirements: Daily check-ins with immediate supervisor, weekly team meetings via video conference, and monthly one-on-one meetings with manager.\n\nPerformance Expectations: Remote employees are held to the same performance standards as office-based employees. Regular performance reviews will assess productivity, quality of work, and collaboration effectiveness.\n\nData Security: All remote workers must comply with company data security policies, use VPN for accessing company systems, and ensure physical security of work materials.\n\nExpenses: The company will reimburse up to $500 annually for home office setup and $50 monthly for internet expenses with proper documentation.",
        "metadata": {
            "department": "HR",
            "policy_type": "remote_work",
            "effective_date": "2024-01-01",
            "version": "2.0"
        },
        "permissions": ["role:employee", "role:hr"]
    },
    {
        "source_type": "knowledge_base",
        "source_uri": "https://kb.company.com/troubleshooting/network-issues.html",
        "content": """
        <html>
        <head><title>Network Troubleshooting Guide</title></head>
        <body>
        <h1>Network Connectivity Issues</h1>
        <p>This guide helps resolve common network problems.</p>
        
        <h2>Quick Diagnostics</h2>
        <ol>
            <li><strong>Check Physical Connections</strong>
                <p>Ensure all cables are securely connected</p>
            </li>
            <li><strong>Restart Network Equipment</strong>
                <p>Power cycle modem and router (wait 30 seconds)</p>
            </li>
            <li><strong>Test Connectivity</strong>
                <p>Try accessing different websites</p>
            </li>
        </ol>
        
        <h2>Advanced Troubleshooting</h2>
        <h3>DNS Issues</h3>
        <p>If websites load slowly or not at all:</p>
        <ul>
            <li>Try using Google DNS (8.8.8.8)</li>
            <li>Flush DNS cache</li>
            <li>Check DNS settings</li>
        </ul>
        
        <h3>Bandwidth Problems</h3>
        <p>For slow internet speeds:</p>
        <ul>
            <li>Run speed test</li>
            <li>Check for background downloads</li>
            <li>Contact ISP if speeds are below plan</li>
        </ul>
        
        <h2>When to Escalate</h2>
        <p>Contact IT support if:</p>
        <ul>
            <li>Issues persist after basic troubleshooting</li>
            <li>Multiple users affected</li>
            <li>Security concerns identified</li>
        </ul>
        </body>
        </html>
        """,
        "metadata": {
            "category": "troubleshooting",
            "difficulty": "beginner",
            "last_reviewed": "2024-01-10"
        },
        "permissions": ["role:employee", "role:it-support"]
    }
]

def publish_test_messages():
    """Publish enhanced test messages to the ingestion worker queue."""
    try:
        # Connect to RabbitMQ
        print("Connecting to RabbitMQ...")
        connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:5672/'))
        channel = connection.channel()

        # Declare the queue (should match the worker's queue)
        queue_name = 'content.raw.received'
        channel.queue_declare(queue=queue_name, durable=True)

        print(f"Publishing {len(test_messages)} enhanced test messages...")
        
        # Publish each message
        for i, message_body in enumerate(test_messages, 1):
            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=json.dumps(message_body, indent=2),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Make message persistent
                    correlation_id=str(uuid.uuid4()),  # Unique ID for tracing
                    content_type='application/json'
                )
            )
            
            print(f"✓ Published message {i}/{len(test_messages)}: {message_body['source_uri']}")
            print(f"  Content type: {message_body.get('source_type', 'unknown')}")
            print(f"  Content length: {len(message_body['content'])} characters")
            
        print(f"\n🎉 Successfully published all {len(test_messages)} test messages!")
        print("\nTest message types:")
        print("1. HTML content with headers and metadata")
        print("2. Markdown documentation with code blocks")
        print("3. Plain text policy document")
        print("4. HTML troubleshooting guide with nested structure")
        
        print("\nThe enhanced ingestion worker should:")
        print("- Convert HTML to Markdown")
        print("- Chunk content by headers where possible")
        print("- Extract metadata from HTML")
        print("- Generate embeddings (real or fallback)")
        print("- Store everything in Elasticsearch")
        
        connection.close()
        
    except pika.exceptions.AMQPConnectionError as e:
        print(f"❌ Failed to connect to RabbitMQ: {e}")
        print("Make sure RabbitMQ is running on localhost:5672")
    except Exception as e:
        print(f"❌ Error publishing messages: {e}")

if __name__ == "__main__":
    publish_test_messages()
