
import pytest
from unittest.mock import patch, MagicMock
from ..crawler import IntranetCrawler
from ..config import CrawlerSettings
from .mock_publisher import MockPublisher

@pytest.mark.asyncio
@patch('src.crawler.AsyncWebCrawler')
async def test_crawler_publishes_data(mock_async_web_crawler):
    """
    Tests that the IntranetCrawler correctly crawls a page and publishes
    the extracted data to the publisher.
    """
    # 1. Setup
    # Mock the return value of crawl4ai's arun method
    mock_crawl_result = MagicMock()
    mock_crawl_result.success = True
    mock_crawl_result.url = "https://fake.intranet/page1"
    mock_crawl_result.markdown.fit_markdown = "This is the page content."
    mock_crawl_result.metadata = {"title": "Page 1"}
    mock_crawl_result.status_code = 200
    mock_crawl_result.redirected_url = None
    mock_crawl_result.tables = []

    async def mock_arun_gen(*args, **kwargs):
        yield mock_crawl_result

    # Configure the mock AsyncWebCrawler instance
    mock_crawler_instance = mock_async_web_crawler.return_value
    mock_crawler_instance.arun.return_value = mock_arun_gen()

    # Configure settings for the crawler
    settings = CrawlerSettings(MAX_PAGES=1)
    crawler = IntranetCrawler(settings=settings)

    # Use the mock publisher
    mock_publisher = MockPublisher("amqp://fake", "test_queue")
    await mock_publisher.connect()

    # 2. Execution
    # Replace the real publisher with our mock
    with patch('src.publisher.DataPublisher', return_value=mock_publisher):
        async for page_data in crawler.crawl("https://fake.intranet", ["fake.intranet"]):
            await mock_publisher.publish_message(page_data)

    # 3. Assertion
    published_messages = mock_publisher.get_published_messages()
    assert len(published_messages) == 1
    
    published_message = published_messages[0]
    assert published_message.source_document_id == "https://fake.intranet/page1"
    assert published_message.content == "This is the page content."
    assert published_message.metadata["title"] == "Page 1"
    assert "group:all-employees" in published_message.permissions

    await mock_publisher.close()
