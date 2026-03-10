#!/usr/bin/env python3
"""
Test script for the Job Listener functionality.

This script demonstrates how to:
1. Send crawl job requests to the listener
2. Monitor the results
3. Verify end-to-end functionality

Usage:
1. Start Docker services: docker-compose up -d
2. Start job listener: python src/job_listener.py
3. In another terminal, run: python test_job_listener.py
"""

import asyncio
import json
import sys
import os
from datetime import datetime

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import aio_pika
from models.communication import CrawlJob

async def send_test_job(amqp_url: str, queue_name: str = "crawl.requested"):
    """Send a test crawl job to the job listener."""
    
    print("📤 Sending test crawl job...")
    
    # Create a test job
    test_job = CrawlJob(
        source_type="INTRANET",
        base_url="https://httpbin.org",  # Simple, fast test site
        start_urls=["https://httpbin.org/html"],
        config={
            "description": "Test crawl job from job listener test script",
            "max_pages": 3
        }
    )
    
    try:
        # Connect to RabbitMQ
        connection = await aio_pika.connect_robust(amqp_url)
        channel = await connection.channel()
        
        # Declare the queue
        queue = await channel.declare_queue(queue_name, durable=True)
        
        # Publish the job
        message_body = test_job.model_dump_json().encode()
        await channel.default_exchange.publish(
            aio_pika.Message(body=message_body),
            routing_key=queue_name
        )
        
        print(f"✅ Successfully sent job to queue '{queue_name}'")
        print(f"   Job details: {test_job.base_url}")
        
        await connection.close()
        
    except Exception as e:
        print(f"❌ Failed to send job: {e}")
        return False
        
    return True

async def monitor_output_queue(amqp_url: str, queue_name: str = "content.raw.received", timeout: int = 60):
    """Monitor the output queue for crawled content."""
    
    print(f"\n👀 Monitoring output queue '{queue_name}' for results...")
    print(f"   Waiting up to {timeout} seconds...")
    
    try:
        connection = await aio_pika.connect_robust(amqp_url)
        channel = await connection.channel()
        
        # Declare the output queue
        queue = await channel.declare_queue(queue_name, durable=True)
        
        results = []
        start_time = asyncio.get_event_loop().time()
        
        async def process_result(message):
            async with message.process():
                try:
                    data = json.loads(message.body.decode())
                    results.append(data)
                    
                    print(f"📨 Received result #{len(results)}:")
                    print(f"   URL: {data.get('source_document_id')}")
                    print(f"   Title: {data.get('metadata', {}).get('title', 'N/A')}")
                    print(f"   Content length: {len(data.get('content', ''))} chars")
                    
                    # Stop after getting some results or timeout
                    if len(results) >= 3:
                        await queue.cancel()
                        
                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON in result: {e}")
        
        # Start consuming
        await queue.consume(process_result)
        
        # Wait for results or timeout
        try:
            await asyncio.wait_for(
                asyncio.Future(),  # This will wait forever unless cancelled
                timeout=timeout
            )
        except asyncio.TimeoutError:
            print(f"⏰ Timeout after {timeout} seconds")
        except asyncio.CancelledError:
            pass  # Queue was cancelled, which is expected
        
        await connection.close()
        
        print(f"\n📊 Summary: Received {len(results)} results")
        return results
        
    except Exception as e:
        print(f"❌ Error monitoring output queue: {e}")
        return []

async def check_queue_status(amqp_url: str):
    """Check the status of both input and output queues."""
    
    print("\n📋 Checking queue status...")
    
    try:
        connection = await aio_pika.connect_robust(amqp_url)
        channel = await connection.channel()
        
        # Check input queue
        input_queue = await channel.declare_queue("crawl.requested", durable=True)
        input_count = input_queue.declaration_result.message_count
        
        # Check output queue  
        output_queue = await channel.declare_queue("content.raw.received", durable=True)
        output_count = output_queue.declaration_result.message_count
        
        print(f"   Input queue 'crawl.requested': {input_count} messages")
        print(f"   Output queue 'content.raw.received': {output_count} messages")
        
        await connection.close()
        
        return {"input": input_count, "output": output_count}
        
    except Exception as e:
        print(f"❌ Error checking queue status: {e}")
        return {"input": -1, "output": -1}

async def test_job_listener_integration():
    """Complete integration test of the job listener."""
    
    print("🧪 Testing Job Listener Integration")
    print("=" * 50)
    
    amqp_url = "amqp://test_user:test_pass@localhost:5672/"
    
    # 1. Check initial queue status
    print("\n1. Initial queue status:")
    initial_status = await check_queue_status(amqp_url)
    
    # 2. Send test job
    print("\n2. Sending test job:")
    job_sent = await send_test_job(amqp_url)
    if not job_sent:
        print("❌ Failed to send job. Exiting.")
        return
    
    # 3. Wait a moment for job to be picked up
    print("\n3. Waiting for job to be processed...")
    await asyncio.sleep(2)
    
    # 4. Monitor for results
    print("\n4. Monitoring for results:")
    results = await monitor_output_queue(amqp_url, timeout=30)
    
    # 5. Final queue status
    print("\n5. Final queue status:")
    final_status = await check_queue_status(amqp_url)
    
    # 6. Summary
    print("\n" + "=" * 50)
    print("🎯 Test Summary:")
    print(f"   Jobs processed: {initial_status['input'] - final_status['input'] + 1}")
    print(f"   Results received: {len(results)}")
    print(f"   Content items queued: {final_status['output'] - initial_status['output']}")
    
    if len(results) > 0:
        print("✅ Job listener integration test PASSED")
    else:
        print("❌ Job listener integration test FAILED - no results received")
        print("💡 Make sure the job listener is running: python src/job_listener.py")

if __name__ == "__main__":
    print("🔗 Job Listener Integration Test")
    print("💡 Make sure Docker services are running: docker-compose up -d")
    print("💡 Make sure job listener is running: python src/job_listener.py")
    print("")
    
    try:
        asyncio.run(test_job_listener_integration())
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()