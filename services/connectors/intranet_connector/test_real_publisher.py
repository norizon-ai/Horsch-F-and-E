#!/usr/bin/env python3
"""
Integration test script for testing the IntranetCrawler with real RabbitMQ.

Prerequisites:
1. Run: docker-compose up -d
2. Ensure RabbitMQ is running on localhost:5672
3. Run: python test_real_publisher.py

This script will:
- Connect to real RabbitMQ
- Crawl a small number of pages
- Publish them to the queue
- Show the results
"""

import asyncio
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.crawler import IntranetCrawler
from src.publisher import DataPublisher
from src.config import CrawlerSettings

async def test_real_queue_integration():
    """Test the crawler with real RabbitMQ integration."""
    
    print("=== Real RabbitMQ Integration Test ===")
    
    # Configure crawler for a quick test
    settings = CrawlerSettings(MAX_PAGES=3, MAX_DEPTH=1)
    print(f"Crawler settings: MAX_PAGES={settings.MAX_PAGES}, STRATEGY={settings.STRATEGY}")
    
    # Initialize crawler
    crawler = IntranetCrawler(settings=settings)
    
    # Initialize real publisher
    amqp_url = "amqp://test_user:test_pass@localhost:5672/"
    queue_name = "test_crawled_content"
    publisher = DataPublisher(amqp_url, queue_name)
    
    try:
        # Connect to RabbitMQ
        print("\n1. Connecting to RabbitMQ...")
        await publisher.connect()
        print("✅ Successfully connected to RabbitMQ")
        
        # Test crawling and publishing
        print("\n2. Starting crawl and publish...")
        start_url = "https://fau.de"
        allowed_domains = ["fau.de", "www.fau.de"]
        
        published_count = await crawler.crawl_and_publish(start_url, allowed_domains, publisher)
        
        print(f"\n✅ Successfully published {published_count} pages to RabbitMQ queue '{queue_name}'")
        print(f"🌐 RabbitMQ Management UI: http://localhost:15672")
        print(f"📝 Login: test_user / test_pass")
        print(f"📋 Check queue '{queue_name}' for messages")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Clean up
        print("\n3. Closing connections...")
        await publisher.close()
        print("✅ Publisher connection closed")

async def test_queue_consumer():
    """Simple consumer to verify messages are in the queue."""
    
    print("\n=== Queue Consumer Test ===")
    
    import aio_pika
    import json
    
    try:
        connection = await aio_pika.connect_robust("amqp://test_user:test_pass@localhost:5672/")
        channel = await connection.channel()
        
        queue = await channel.declare_queue("test_crawled_content", durable=True)
        message_count = queue.declaration_result.message_count
        
        print(f"📊 Queue 'test_crawled_content' has {message_count} messages")
        
        if message_count > 0:
            print("\n📨 Consuming first message to verify structure...")
            
            async def process_message(message):
                async with message.process():
                    try:
                        data = json.loads(message.body.decode())
                        print(f"✅ Message structure valid:")
                        print(f"   - source_document_id: {data.get('source_document_id')}")
                        print(f"   - content length: {len(data.get('content', ''))} chars")
                        print(f"   - title: {data.get('metadata', {}).get('title', 'N/A')}")
                        print(f"   - retrieved_at: {data.get('source', {}).get('retrieved_at', 'N/A')}")
                        
                        # Stop after first message
                        await queue.cancel()
                        
                    except json.JSONDecodeError as e:
                        print(f"❌ Invalid JSON in message: {e}")
            
            await queue.consume(process_message)
            
        await connection.close()
        
    except Exception as e:
        print(f"❌ Consumer test failed: {e}")

if __name__ == "__main__":
    
    # Check if Docker services are running
    print("🐳 Checking if Docker services are running...")
    print("💡 If not running, start with: docker-compose up -d")
    
    try:
        asyncio.run(test_real_queue_integration())
        asyncio.run(test_queue_consumer())
        
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
    except Exception as e:
        print(f"❌ Test suite failed: {e}")
        sys.exit(1)