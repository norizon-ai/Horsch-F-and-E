import httpx
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_scraping_strategy import WebScrapingStrategy
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy, BFSDeepCrawlStrategy, DFSDeepCrawlStrategy
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai.deep_crawling.filters import FilterChain, DomainFilter, ContentTypeFilter, URLPatternFilter
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from typing import Dict, Any, Optional, List, AsyncGenerator
import asyncio
import sys
from datetime import datetime, timezone
from urllib.parse import urlparse

# Import the centralized settings
from config.settings import CrawlerSettings
from publishing.publisher_base import PublisherBase
from models.articles import RawArticle, RawArticleSource, RawArticleAuthor

class IntranetCrawler:
    """
    A crawler designed to fetch content and permissions from a company's intranet.

    This class is configured via a Pydantic settings object.
    """

    def __init__(self, settings: CrawlerSettings):
        """
        Initializes the IntranetCrawler with a configuration object.

        Args:
            settings (CrawlerSettings): The configuration object that dictates
                                        the crawler's behavior.
        """
        self.settings = settings
        # Enable Playwright mode directly in the crawler's constructor
        # based on the configuration settings.
        self.crawler = AsyncWebCrawler(playwright_mode=settings.USE_PLAYWRIGHT)

    async def _fetch_permissions(self, url: str, client: httpx.AsyncClient) -> List[str]:
        """
        Fetches access permissions for a given URL from the intranet's API.

        This method makes a direct, authenticated API call to a hypothetical
        permissions endpoint. It is separate from the main content crawl.

        Args:
            url (str): The URL of the page for which to fetch permissions.
            client (httpx.AsyncClient): An authenticated HTTP client.

        Returns:
            List[str]: A list of permission strings (e.g., "group:engineering").
                       Returns an empty list if permissions cannot be fetched.
        """
        # TODO: Implement as needed
        print(f"SIMULATING: Fetching permissions for {url}...")
        return ["group:all-employees"]

    def extract_base_domain(self, url: str) -> str:
        """Extract base domain from URL (e.g., 'fau.de' from 'www.fau.de')."""
        domain = urlparse(url).netloc if url.startswith('http') else url
        parts = domain.split('.')
        if len(parts) > 2 and parts[0] in ['www', 'mail', 'ftp']:
            return '.'.join(parts[1:])
        elif len(parts) > 2:
            # Likely a subdomain, return last two parts
            return '.'.join(parts[-2:])
        return domain
    
    def _create_crawler_config(self, allowed_domains: List[str]) -> CrawlerRunConfig:
        """
        Creates a dynamic CrawlerRunConfig based on the injected settings.

        This configuration uses the selected crawling strategy and applies
        strict filters to keep the crawl within the specified intranet domains.

        Args:
            allowed_domains (List[str]): A list of domains the crawler is
                                         permitted to access.

        Returns:
            CrawlerRunConfig: A fully configured object for the crawl job.
        """
        # For comprehensive crawling, use base domain and allow subdomains
        if self.settings.UNLIMITED_CRAWL or getattr(self.settings, 'COMPREHENSIVE_CRAWL', False):
            # Extract base domain and allow all subdomains
            base_domain = self.extract_base_domain(allowed_domains[0])
            filter_list = [
                DomainFilter(allowed_domains=[base_domain]),
            ]
        else:
            # Standard filtering for specific domains
            filter_list = [
                DomainFilter(allowed_domains=allowed_domains),
            ]
        
        #if self.settings.URL_INCLUDE_PATTERNS:
        #    filter_list.append(URLPatternFilter(patterns=self.settings.URL_INCLUDE_PATTERNS))
        filter_chain = FilterChain(filter_list)

        # Configure crawling limits
        if self.settings.UNLIMITED_CRAWL:
            max_depth = sys.maxsize
            max_pages = sys.maxsize
            include_external = True  # Allow following links to subdomains
        else:
            max_depth = self.settings.MAX_DEPTH
            max_pages = self.settings.MAX_PAGES
            include_external = False
        
        strategy_args = {
            "max_depth": max_depth,
            "max_pages": max_pages,
            "include_external": include_external,
            "filter_chain": filter_chain,
        }

        if self.settings.STRATEGY == "best_first":
            scorer = KeywordRelevanceScorer(keywords=self.settings.RELEVANCE_KEYWORDS)
            strategy_args["url_scorer"] = scorer
            strategy = BestFirstCrawlingStrategy(**strategy_args)
        elif self.settings.STRATEGY == "bfs":
            strategy = BFSDeepCrawlStrategy(**strategy_args)
        else: # dfs
            strategy = DFSDeepCrawlStrategy(**strategy_args)

        return CrawlerRunConfig(
            deep_crawl_strategy=strategy,
            scraping_strategy=LXMLWebScrapingStrategy(),
            markdown_generator=DefaultMarkdownGenerator(),
            excluded_tags=self.settings.EXCLUDED_TAGS,
            exclude_external_links=self.settings.EXCLUDE_EXTERNAL_LINKS,
            exclude_social_media_links=self.settings.EXCLUDE_SOCIAL_MEDIA_LINKS,
            page_timeout=120000,  # Increase timeout to 120 seconds (120000ms)
            wait_until="networkidle",  # More robust wait condition
            stream=self.settings.USE_STREAMING,  # Enable streaming mode for memory efficiency
            verbose=True
        )

    async def crawl_and_publish(self, start_url: str, allowed_domains: List[str], publisher: PublisherBase) -> Dict[str, Any]:
        """
        Initializes and runs the intranet crawl, publishing processed data for each page.

        Args:
            start_url (str): The initial URL to begin crawling from.
            allowed_domains (List[str]): The list of domains to confine the crawl to.
            publisher (PublisherBase): The publisher to send crawled data to.

        Returns:
            Dict[str, Any]: Statistics including successful and failed crawls.
        """
        published_count = 0
        failed_urls = []
        
        async for result in self._crawl_generator_with_errors(start_url, allowed_domains):
            if result.get("success"):
                try:
                    await publisher.publish_message(result["data"])
                    published_count += 1
                    print(f"Published page: {result['data'].source.uri}")
                except Exception as e:
                    print(f"Failed to publish page {result['data'].source.uri}: {e}")
                    failed_urls.append({
                        "url": result['data'].source.uri,
                        "error": str(e),
                        "type": "publish_error"
                    })
            else:
                # Track failed URL
                failed_urls.append(result)
                
                # If publisher has error tracking, report it
                if hasattr(publisher, 'report_error'):
                    await publisher.report_error(result['url'], result['error'])
        
        return {
            "published_count": published_count,
            "failed_count": len(failed_urls),
            "failed_urls": failed_urls
        }

    async def crawl(self, start_url: str, allowed_domains: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Initializes and runs the intranet crawl, yielding processed data for each page.
        
        DEPRECATED: Use crawl_and_publish() for production. This method is kept for backward compatibility and testing.

        Args:
            start_url (str): The initial URL to begin crawling from.
            allowed_domains (List[str]): The list of domains to confine the crawl to.

        Yields:
            An asynchronous generator of dictionaries, each representing a page.
        """
        async for page_data in self._crawl_generator(start_url, allowed_domains):
            yield page_data

    async def _crawl_generator_with_errors(self, start_url: str, allowed_domains: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Internal method that performs crawling and yields both successful and failed results.
        
        Args:
            start_url (str): The initial URL to begin crawling from.
            allowed_domains (List[str]): The list of domains to confine the crawl to.
        
        Yields:
            Dictionary with either successful data or error information.
        """
        config = self._create_crawler_config(allowed_domains)
        headers = {}
        if self.settings.AUTH_TOKEN:
            headers["Authorization"] = f"Bearer {self.settings.AUTH_TOKEN}"

        async with self.crawler as crawler:
            if self.settings.USE_STREAMING:
                # Streaming mode: Process results as they arrive
                print("🚀 Using streaming mode - processing pages as they arrive...")
                async for result in await crawler.arun(start_url, config=config):
                    # Process each result immediately
                    yield await self._process_crawl_result(result)
            else:
                # Batch mode: Wait for all results then process
                print("📦 Using batch mode - waiting for all pages...")
                results = await crawler.arun(start_url, config=config)
                for result in results:
                    yield await self._process_crawl_result(result)
    
    async def _process_crawl_result(self, result) -> Dict[str, Any]:
        """
        Process a single crawl result and return formatted data or error.
        
        Args:
            result: Crawl result from crawl4ai
            
        Returns:
            Dictionary with either successful data or error information.
        """
        # Check if crawl was successful
        if not result.success:
            # Return error information
            print(f"[ERROR] Failed to crawl {result.url}: {result.error_message or 'Unknown'}")
            return {
                "success": False,
                "url": result.url,
                "error": result.error_message or 'Unknown error',
                "type": "crawl_error"
            }

        # Process successful result
        try:
            # Start with the metadata extracted by the crawler
            final_metadata = result.metadata or {}
            
            # Enrich metadata
            final_metadata["title"] = final_metadata.get("title", result.url)
            final_metadata["status_code"] = result.status_code
            final_metadata["redirected_from"] = result.redirected_url
            
            if hasattr(result, 'tables') and result.tables:
                final_metadata["tables"] = result.tables

            # Create RawArticle object
            author_name = final_metadata.get('author')
            author = RawArticleAuthor(name=author_name) if author_name else None

            page_data = RawArticle(
                source_document_id=result.url,
                content=result.markdown or "",
                source=RawArticleSource(
                    uri=result.url,
                    module="Intranet Connector",
                    retrieved_at=datetime.now(timezone.utc)
                ),
                author=author,
                tags=[],
                permissions=[],
                metadata=final_metadata
            )
            
            return {
                "success": True,
                "data": page_data,
                "html": result.html,  # Include raw HTML for subdomain extraction
                "url": result.url,
                "links": result.links  # Include crawl4ai's extracted links
            }
            
        except Exception as e:
            # Return processing error
            print(f"[ERROR] Failed to process {result.url}: {e}")
            return {
                "success": False,
                "url": result.url,
                "error": f"Processing error: {str(e)}",
                "type": "processing_error"
            }
    
    async def _crawl_generator(self, start_url: str, allowed_domains: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Internal method that performs the actual crawling and yields RawArticle objects.

        Args:
            start_url (str): The initial URL to begin crawling from.
            allowed_domains (List[str]): The list of domains to confine the crawl to.

        Yields:
            An asynchronous generator of RawArticle objects.
        """
        config = self._create_crawler_config(allowed_domains)
        headers = {}
        if self.settings.AUTH_TOKEN:
            headers["Authorization"] = f"Bearer {self.settings.AUTH_TOKEN}"

        async with self.crawler as crawler:
            if self.settings.USE_STREAMING:
                # Streaming mode: Process results as they arrive
                async for result in await crawler.arun(start_url, config=config):
                    # Process each result immediately
                    if result.success:
                        yield await self._process_successful_result(result)
                    else:
                        print(f"Skipping failed crawl for {result.url}. Error: {result.error_message or 'Unknown'}")
            else:
                # Batch mode: Wait for all results then process
                results = await crawler.arun(start_url, config=config)
                for result in results:
                    if result.success:
                        yield await self._process_successful_result(result)
                    else:
                        print(f"Skipping failed crawl for {result.url}. Error: {result.error_message or 'Unknown'}")
    
    async def _process_successful_result(self, result) -> RawArticle:
        """
        Process a successful crawl result into RawArticle.
        
        Args:
            result: Successful crawl result from crawl4ai
            
        Returns:
            RawArticle object.
        """
        # Start with the metadata extracted by the crawler (e.g., from meta tags)
        final_metadata = result.metadata or {}

        # Enrich the metadata with key fields from the CrawlResult object itself
        # to provide a more complete picture of the crawl.
        final_metadata["title"] = final_metadata.get("title", result.url) # Ensure title exists, fallback to URL
        final_metadata["status_code"] = result.status_code
        
        final_metadata["redirected_from"] = result.redirected_url

        # Safely check for the 'tables' attribute for backward compatibility with older crawl4ai versions.
        if hasattr(result, 'tables') and result.tables:
            final_metadata["tables"] = result.tables

        # Create the RawArticle object
        # Extract author information if available
        author_name = final_metadata.get('author')
        author = RawArticleAuthor(name=author_name) if author_name else None

        page_data = RawArticle(
            source_document_id=result.url, # Using URL as the unique ID from source
            content=result.markdown or "",
            source=RawArticleSource(
                uri=result.url,
                module="Intranet Connector",
                retrieved_at=datetime.now(timezone.utc)
            ),
            author=author,
            tags=[], # Placeholder for now
            permissions=[],
            metadata=final_metadata
        )
        return page_data

if __name__ == '__main__':
    async def main():
        
        from config import settings
        from publisher_factory import PublisherFactory

        print(f"Loaded settings: STRATEGY={settings.STRATEGY}, MAX_PAGES={settings.MAX_PAGES}")
        
        # Get publisher info
        publisher_info = PublisherFactory.get_publisher_info(settings)
        print(f"Storage mode: {publisher_info['storage_mode']}")
        print(f"Publisher: {publisher_info['description']}")

        crawler = IntranetCrawler(settings=settings)

        # Define the crawl target. The DomainFilter will handle subdomains automatically.
        start_url = "https://fau.de"
        allowed_domains = ["fau.de", "www.fau.de"]

        # Create publisher based on configuration
        print(f"\n=== Starting Crawl with {publisher_info['storage_mode'].upper()} Publisher ===")
        publisher = PublisherFactory.create_publisher(settings)
        await publisher.connect()
        
        results = await crawler.crawl_and_publish(start_url, allowed_domains, publisher)
        
        print(f"\n--- Finished Crawl ---")
        print(f"Successfully published: {results['published_count']} pages")
        print(f"Failed URLs: {results['failed_count']}")
        
        # Show failed URLs if any
        if results['failed_urls']:
            print("\nFailed URLs:")
            for failed in results['failed_urls'][:10]:  # Show first 10
                print(f"  - {failed['url']}: {failed['error'][:80]}...")
        
        # Show storage info if using file storage
        if hasattr(publisher, 'get_storage_info'):
            storage_info = publisher.get_storage_info()
            print(f"\nStorage Information:")
            for key, value in storage_info.items():
                print(f"  {key}: {value}")
        
        await publisher.close()

    asyncio.run(main())