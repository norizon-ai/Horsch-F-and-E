"""
Integration tests for the complete Intranet Connector pipeline.

These tests cover:
1. Crawler → RabbitMQ Publisher integration
2. End-to-end pipeline testing (when services are available)
3. Error handling and resilience
"""

import pytest
import asyncio
import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crawler import IntranetCrawler
from publisher import DataPublisher
from testing.mock_publisher import MockPublisher
from config import CrawlerSettings

class TestCrawlerPublisherIntegration:
    """Test the integration between crawler and publisher components."""

    @pytest.mark.asyncio
    async def test_crawl_and_publish_with_mock(self):
        """Test the crawl_and_publish method with MockPublisher."""
        
        # Setup
        settings = CrawlerSettings(MAX_PAGES=2, MAX_DEPTH=1, STRATEGY="bfs")
        crawler = IntranetCrawler(settings=settings)
        mock_publisher = MockPublisher("amqp://fake", "test_queue")
        
        await mock_publisher.connect()
        
        # Test with a controlled URL (using mock for deterministic testing)
        with patch('crawler.AsyncWebCrawler') as mock_crawler_class:
            # Mock crawl results
            mock_result1 = MagicMock()
            mock_result1.success = True
            mock_result1.url = "https://test.example/page1"
            mock_result1.markdown = "# Test Page 1\n\nContent for page 1"
            mock_result1.metadata = {"title": "Test Page 1"}
            mock_result1.status_code = 200
            mock_result1.redirected_url = None
            mock_result1.tables = []
            
            mock_result2 = MagicMock()
            mock_result2.success = True
            mock_result2.url = "https://test.example/page2"
            mock_result2.markdown = "# Test Page 2\n\nContent for page 2"
            mock_result2.metadata = {"title": "Test Page 2"}
            mock_result2.status_code = 200
            mock_result2.redirected_url = None
            mock_result2.tables = []
            
            # Configure mock crawler
            mock_crawler_instance = mock_crawler_class.return_value
            mock_crawler_instance.__aenter__.return_value = mock_crawler_instance
            mock_crawler_instance.__aexit__.return_value = None
            mock_crawler_instance.arun.return_value = [mock_result1, mock_result2]
            
            # Execute
            published_count = await crawler.crawl_and_publish(
                "https://test.example", 
                ["test.example"], 
                mock_publisher
            )
            
            # Verify
            assert published_count == 2
            published_messages = mock_publisher.get_published_messages()
            assert len(published_messages) == 2
            
            # Check first message
            msg1 = published_messages[0]
            assert msg1.source_document_id == "https://test.example/page1"
            assert msg1.content == "# Test Page 1\n\nContent for page 1"
            assert msg1.metadata["title"] == "Test Page 1"
            assert msg1.source.module == "Intranet Connector"
            
            # Check second message
            msg2 = published_messages[1]
            assert msg2.source_document_id == "https://test.example/page2"
            assert msg2.content == "# Test Page 2\n\nContent for page 2"
            assert msg2.metadata["title"] == "Test Page 2"
            
        await mock_publisher.close()

    @pytest.mark.asyncio
    async def test_crawl_and_publish_error_handling(self):
        """Test error handling when publisher fails."""
        
        # Setup
        settings = CrawlerSettings(MAX_PAGES=1, MAX_DEPTH=1)
        crawler = IntranetCrawler(settings=settings)
        
        # Create a mock publisher that fails
        class FailingPublisher(MockPublisher):
            async def publish_message(self, message):
                raise Exception("Simulated publisher failure")
        
        failing_publisher = FailingPublisher("amqp://fake", "test_queue")
        await failing_publisher.connect()
        
        with patch('crawler.AsyncWebCrawler') as mock_crawler_class:
            # Mock a single successful crawl result
            mock_result = MagicMock()
            mock_result.success = True
            mock_result.url = "https://test.example/page"
            mock_result.markdown = "# Test Page\n\nContent"
            mock_result.metadata = {"title": "Test Page"}
            mock_result.status_code = 200
            mock_result.redirected_url = None
            mock_result.tables = []
            
            mock_crawler_instance = mock_crawler_class.return_value
            mock_crawler_instance.__aenter__.return_value = mock_crawler_instance
            mock_crawler_instance.__aexit__.return_value = None
            mock_crawler_instance.arun.return_value = [mock_result]
            
            # Execute - should handle the error gracefully
            published_count = await crawler.crawl_and_publish(
                "https://test.example", 
                ["test.example"], 
                failing_publisher
            )
            
            # Verify - no pages should be successfully published due to publisher failure
            assert published_count == 0
            
        await failing_publisher.close()

    @pytest.mark.asyncio
    async def test_crawl_and_publish_partial_failure(self):
        """Test behavior when some crawl results fail."""
        
        # Setup
        settings = CrawlerSettings(MAX_PAGES=3, MAX_DEPTH=1)
        crawler = IntranetCrawler(settings=settings)
        mock_publisher = MockPublisher("amqp://fake", "test_queue")
        
        await mock_publisher.connect()
        
        with patch('crawler.AsyncWebCrawler') as mock_crawler_class:
            # Mix of successful and failed results
            mock_result1 = MagicMock()
            mock_result1.success = True
            mock_result1.url = "https://test.example/page1"
            mock_result1.markdown = "# Success Page"
            mock_result1.metadata = {"title": "Success"}
            mock_result1.status_code = 200
            mock_result1.redirected_url = None
            mock_result1.tables = []
            
            mock_result2 = MagicMock()
            mock_result2.success = False  # Failed result
            mock_result2.url = "https://test.example/page2"
            mock_result2.error_message = "404 Not Found"
            
            mock_result3 = MagicMock()
            mock_result3.success = True
            mock_result3.url = "https://test.example/page3"
            mock_result3.markdown = "# Another Success"
            mock_result3.metadata = {"title": "Success 2"}
            mock_result3.status_code = 200
            mock_result3.redirected_url = None
            mock_result3.tables = []
            
            mock_crawler_instance = mock_crawler_class.return_value
            mock_crawler_instance.__aenter__.return_value = mock_crawler_instance
            mock_crawler_instance.__aexit__.return_value = None
            mock_crawler_instance.arun.return_value = [mock_result1, mock_result2, mock_result3]
            
            # Execute
            published_count = await crawler.crawl_and_publish(
                "https://test.example", 
                ["test.example"], 
                mock_publisher
            )
            
            # Verify - only successful results should be published
            assert published_count == 2  # 2 successful, 1 failed
            published_messages = mock_publisher.get_published_messages()
            assert len(published_messages) == 2
            
            # Check that only successful pages were published
            published_urls = [msg.source_document_id for msg in published_messages]
            assert "https://test.example/page1" in published_urls
            assert "https://test.example/page3" in published_urls
            assert "https://test.example/page2" not in published_urls  # Failed page
            
        await mock_publisher.close()

@pytest.mark.skipif(
    "INTEGRATION_TESTS" not in os.environ,
    reason="Integration tests require INTEGRATION_TESTS=1 environment variable"
)
class TestRealRabbitMQIntegration:
    """Tests that require real RabbitMQ service running."""
    
    @pytest.mark.asyncio
    async def test_real_rabbitmq_publishing(self):
        """Test publishing to real RabbitMQ (requires docker-compose up)."""
        
        import aio_pika
        
        # Test RabbitMQ connection first
        try:
            connection = await aio_pika.connect_robust("amqp://test_user:test_pass@localhost:5672/")
            await connection.close()
        except Exception as e:
            pytest.skip(f"RabbitMQ not available: {e}")
        
        # Setup
        settings = CrawlerSettings(MAX_PAGES=1, MAX_DEPTH=1)
        crawler = IntranetCrawler(settings=settings)
        
        amqp_url = "amqp://test_user:test_pass@localhost:5672/"
        queue_name = "test_integration_queue"
        publisher = DataPublisher(amqp_url, queue_name)
        
        try:
            await publisher.connect()
            
            # Use a simple, fast URL for testing
            published_count = await crawler.crawl_and_publish(
                "https://httpbin.org/html", 
                ["httpbin.org"], 
                publisher
            )
            
            assert published_count >= 1
            
            # Verify message was queued
            connection = await aio_pika.connect_robust(amqp_url)
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)
            
            # Check queue has messages
            assert queue.declaration_result.message_count >= 1
            
            await connection.close()
            
        finally:
            await publisher.close()

if __name__ == "__main__":
    # Run the tests
    import subprocess
    import sys
    
    # Add current directory to Python path
    os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))
    
    # Run pytest with verbose output
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        __file__, 
        "-v", 
        "--tb=short"
    ], cwd=os.path.dirname(os.path.abspath(__file__)))
    
    sys.exit(result.returncode)