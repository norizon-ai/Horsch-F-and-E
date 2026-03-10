#!/usr/bin/env python3
"""
Test script to demonstrate file-based crawling workflow.
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from config.settings import CrawlerSettings
from core.crawler import IntranetCrawler
from publishing.file_storage_publisher import FileStoragePublisher
from utils.processors import BatchProcessor


async def test_file_crawl():
    """
    Test crawling with file storage.
    """
    print("=" * 60)
    print("FILE-BASED CRAWL TEST")
    print("=" * 60)
    
    # Configure for file storage
    settings = CrawlerSettings(
        STORAGE_MODE="file",
        STORAGE_PATH="./test_crawl_data",
        MAX_PAGES=5,  # Small test
        MAX_DEPTH=1,
        STRATEGY="bfs"
    )
    
    # Test URL (using a small, fast site)
    start_url = "https://example.com"
    allowed_domains = ["example.com"]
    
    print(f"\n1. Starting crawl of {start_url}")
    print(f"   Max pages: {settings.MAX_PAGES}")
    print(f"   Storage: {settings.STORAGE_PATH}")
    
    # Create crawler and publisher
    crawler = IntranetCrawler(settings)
    publisher = FileStoragePublisher(
        storage_path=settings.STORAGE_PATH,
        batch_size=2  # Small batches for testing
    )
    
    try:
        # Connect and crawl
        await publisher.connect()
        
        published_count = await crawler.crawl_and_publish(
            start_url, allowed_domains, publisher
        )
        
        print(f"\n2. Crawl complete: {published_count} pages saved")
        
        # Get storage info
        storage_info = publisher.get_storage_info()
        print(f"\n3. Storage information:")
        for key, value in storage_info.items():
            print(f"   {key}: {value}")
        
    finally:
        await publisher.close()
    
    # Now process the data
    print(f"\n4. Processing crawled data...")
    processor = BatchProcessor(settings.STORAGE_PATH)
    
    # Get session info
    session_info = processor.get_session_info()
    print(f"\n5. Session information:")
    for key, value in session_info.items():
        if key != "statistics":
            print(f"   {key}: {value}")
    
    # Process and show some chunks
    print(f"\n6. Sample processed chunks:")
    chunk_count = 0
    for chunk in processor.process_session(chunk_size=500, chunk_overlap=100):
        chunk_count += 1
        if chunk_count <= 2:  # Show first 2 chunks
            print(f"\n   Chunk {chunk_count}:")
            print(f"   - ID: {chunk['chunk_id']}")
            print(f"   - URL: {chunk['url']}")
            print(f"   - Size: {len(chunk['content'])} chars")
            print(f"   - Preview: {chunk['content'][:100]}...")
    
    print(f"\n7. Total chunks created: {chunk_count}")
    
    # Export to JSONL
    export_file = "./test_export.jsonl"
    print(f"\n8. Exporting to {export_file}...")
    processor.export_to_jsonl(export_file)
    
    print(f"\n✅ Test complete!")
    print(f"   - Crawled data saved to: {settings.STORAGE_PATH}")
    print(f"   - Exported chunks to: {export_file}")
    print(f"\nYou can now:")
    print(f"   - View crawled data: ls -la {settings.STORAGE_PATH}/*/")
    print(f"   - Process with: python batch_processor.py --storage {settings.STORAGE_PATH}")
    print(f"   - Manage with: python crawl_manager.py list")


if __name__ == "__main__":
    asyncio.run(test_file_crawl())