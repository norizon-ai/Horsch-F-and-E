#!/usr/bin/env python3
"""
Test script to verify streaming mode for memory-efficient crawling.
"""

import asyncio
import time
import psutil
import os
from config.settings import CrawlerSettings
from core.crawler import IntranetCrawler
from publishing.file_storage_publisher import FileStoragePublisher

def get_memory_usage():
    """Get current memory usage in MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

async def test_streaming_mode():
    """Test crawling with streaming mode enabled."""
    
    print("=" * 60)
    print("TESTING STREAMING MODE")
    print("=" * 60)
    
    # Configure for streaming
    settings = CrawlerSettings(
        USE_STREAMING=True,  # Enable streaming
        STORAGE_MODE="file",
        STORAGE_PATH="./test_streaming_data",
        MAX_PAGES=20,  # Moderate test
        MAX_DEPTH=2,
        STRATEGY="bfs",
        BATCH_SIZE=5  # Small batches to see streaming effect
    )
    
    # Test URL
    start_url = "https://example.com"
    allowed_domains = ["example.com"]
    
    print(f"\nConfiguration:")
    print(f"  Streaming: {settings.USE_STREAMING}")
    print(f"  Max pages: {settings.MAX_PAGES}")
    print(f"  Max depth: {settings.MAX_DEPTH}")
    print(f"  Batch size: {settings.BATCH_SIZE}")
    print(f"  Storage: {settings.STORAGE_PATH}")
    
    # Track memory usage
    initial_memory = get_memory_usage()
    print(f"\nInitial memory usage: {initial_memory:.2f} MB")
    
    # Create crawler and publisher
    crawler = IntranetCrawler(settings)
    publisher = FileStoragePublisher(
        storage_path=settings.STORAGE_PATH,
        batch_size=settings.BATCH_SIZE
    )
    
    try:
        await publisher.connect()
        
        # Track timing and progress
        start_time = time.time()
        page_count = 0
        first_page_time = None
        memory_samples = []
        
        print("\n--- Starting streaming crawl ---")
        print("Pages will be processed as they arrive...\n")
        
        # Use the generator directly to see streaming
        async for result in crawler._crawl_generator_with_errors(start_url, allowed_domains):
            page_count += 1
            current_time = time.time() - start_time
            current_memory = get_memory_usage()
            memory_samples.append(current_memory)
            
            if page_count == 1:
                first_page_time = current_time
                print(f"✓ First page received after {first_page_time:.2f}s")
            
            if result.get("success"):
                # Publish the page
                await publisher.publish_message(result["data"])
                print(f"  [{page_count:3}] {current_time:6.2f}s - {result['data'].source.uri[:60]}... "
                      f"(Memory: {current_memory:.1f} MB)")
            else:
                print(f"  [{page_count:3}] {current_time:6.2f}s - ERROR: {result['url'][:60]}...")
            
            # Show batch saves
            if page_count % settings.BATCH_SIZE == 0:
                print(f"       → Batch saved to disk")
        
        elapsed = time.time() - start_time
        
        # Calculate statistics
        max_memory = max(memory_samples) if memory_samples else initial_memory
        avg_memory = sum(memory_samples) / len(memory_samples) if memory_samples else initial_memory
        memory_increase = max_memory - initial_memory
        
        print("\n" + "=" * 60)
        print("STREAMING TEST RESULTS")
        print("=" * 60)
        print(f"Pages processed: {page_count}")
        print(f"Total time: {elapsed:.2f} seconds")
        print(f"Time to first page: {first_page_time:.2f} seconds" if first_page_time else "N/A")
        print(f"Average time per page: {elapsed/page_count:.2f} seconds" if page_count > 0 else "N/A")
        print(f"\nMemory usage:")
        print(f"  Initial: {initial_memory:.2f} MB")
        print(f"  Maximum: {max_memory:.2f} MB")
        print(f"  Average: {avg_memory:.2f} MB")
        print(f"  Peak increase: {memory_increase:.2f} MB")
        
        # Show storage info
        if hasattr(publisher, 'get_storage_info'):
            storage_info = publisher.get_storage_info()
            print(f"\nStorage info:")
            for key, value in storage_info.items():
                print(f"  {key}: {value}")
        
    finally:
        await publisher.close()
    
    print("\n✅ Streaming test complete!")

async def compare_modes():
    """Compare streaming vs batch mode."""
    
    print("\n" + "=" * 60)
    print("COMPARING STREAMING VS BATCH MODE")
    print("=" * 60)
    
    test_settings = {
        "MAX_PAGES": 10,
        "MAX_DEPTH": 1,
        "STRATEGY": "bfs"
    }
    
    results = {}
    
    for use_streaming in [False, True]:
        mode = "Streaming" if use_streaming else "Batch"
        print(f"\n--- Testing {mode} Mode ---")
        
        settings = CrawlerSettings(
            USE_STREAMING=use_streaming,
            STORAGE_MODE="file",
            STORAGE_PATH=f"./test_{mode.lower()}_data",
            **test_settings
        )
        
        crawler = IntranetCrawler(settings)
        publisher = FileStoragePublisher(settings.STORAGE_PATH, batch_size=5)
        
        initial_memory = get_memory_usage()
        start_time = time.time()
        first_page_time = None
        
        try:
            await publisher.connect()
            
            page_count = 0
            memory_samples = []
            
            async for result in crawler._crawl_generator_with_errors("https://example.com", ["example.com"]):
                page_count += 1
                current_memory = get_memory_usage()
                memory_samples.append(current_memory)
                
                if page_count == 1 and first_page_time is None:
                    first_page_time = time.time() - start_time
                
                if result.get("success"):
                    await publisher.publish_message(result["data"])
            
            elapsed = time.time() - start_time
            max_memory = max(memory_samples) if memory_samples else initial_memory
            
            results[mode] = {
                "pages": page_count,
                "total_time": elapsed,
                "first_page_time": first_page_time,
                "max_memory": max_memory - initial_memory
            }
            
        finally:
            await publisher.close()
    
    # Print comparison
    print("\n" + "=" * 60)
    print("COMPARISON RESULTS")
    print("=" * 60)
    print(f"{'Metric':<25} {'Batch':>15} {'Streaming':>15}")
    print("-" * 55)
    
    if "Batch" in results and "Streaming" in results:
        batch = results["Batch"]
        stream = results["Streaming"]
        
        print(f"{'Pages processed':<25} {batch['pages']:>15} {stream['pages']:>15}")
        print(f"{'Total time (s)':<25} {batch['total_time']:>15.2f} {stream['total_time']:>15.2f}")
        print(f"{'Time to first page (s)':<25} {batch['first_page_time']:>15.2f} {stream['first_page_time']:>15.2f}")
        print(f"{'Memory increase (MB)':<25} {batch['max_memory']:>15.2f} {stream['max_memory']:>15.2f}")
        
        # Calculate improvements
        if batch['first_page_time'] > 0:
            first_page_improvement = (batch['first_page_time'] - stream['first_page_time']) / batch['first_page_time'] * 100
            print(f"\n✨ Streaming mode delivers first page {first_page_improvement:.1f}% faster!")
        
        if batch['max_memory'] > 0:
            memory_improvement = (batch['max_memory'] - stream['max_memory']) / batch['max_memory'] * 100
            if memory_improvement > 0:
                print(f"✨ Streaming mode uses {memory_improvement:.1f}% less memory!")

if __name__ == "__main__":
    # Check if psutil is installed
    try:
        import psutil
    except ImportError:
        print("Please install psutil for memory monitoring: pip install psutil")
        print("Running basic test without memory monitoring...")
        asyncio.run(test_streaming_mode())
    else:
        # Run tests
        asyncio.run(test_streaming_mode())
        # Optionally compare modes
        # asyncio.run(compare_modes())