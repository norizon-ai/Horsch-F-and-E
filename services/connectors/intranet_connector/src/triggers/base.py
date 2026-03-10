"""
Base abstraction for all trigger types.

This module defines the interface that all triggers (CLI, Cron, Queue, API) must implement.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import logging

from publishers.base import PublisherBase
from config.settings import CrawlerSettings

logger = logging.getLogger(__name__)


class TriggerBase(ABC):
    """
    Abstract base class for all trigger implementations.
    
    A trigger is responsible for:
    1. Detecting when a crawl should start
    2. Configuring the crawl parameters
    3. Executing the crawl with appropriate crawler and publisher
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None):
        """
        Initialize the trigger.
        
        Args:
            settings: Crawler settings (uses defaults if None)
        """
        self.settings = settings or CrawlerSettings()
        self.publisher: Optional[PublisherBase] = None
        self.is_running = False
        
    @abstractmethod
    async def start(self) -> None:
        """
        Start the trigger and begin listening for events.
        
        This method should:
        1. Set up any necessary resources
        2. Begin listening for trigger events
        3. Call execute_crawl when triggered
        """
        pass
    
    @abstractmethod
    async def stop(self) -> None:
        """
        Stop the trigger and clean up resources.
        """
        pass
    
    @abstractmethod
    def get_publisher(self) -> PublisherBase:
        """
        Get the publisher instance for this trigger.
        
        Returns:
            Publisher instance configured for this trigger
        """
        pass
    
    async def execute_crawl(self, crawl_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a crawl with the given configuration.
        
        This is the common crawl execution logic used by all triggers.
        
        Args:
            crawl_config: Configuration for the crawl including:
                - url: Starting URL
                - allowed_domains: List of allowed domains
                - max_pages: Maximum pages to crawl
                - use_sitemap: Whether to use sitemap
                - other crawler-specific options
                
        Returns:
            Dictionary with crawl results and statistics
        """
        from core.crawler_factory import CrawlerFactory
        
        # Get crawler and publisher
        crawler = CrawlerFactory.create_crawler(self.settings, crawl_config)
        publisher = self.get_publisher()
        
        try:
            # Connect publisher
            await publisher.connect()
            
            # Execute crawl
            logger.info(f"Starting crawl: {crawl_config.get('url')}")
            
            if crawl_config.get('use_sitemap'):
                # Sitemap-based crawling
                results = await crawler.crawl_from_sitemap(
                    crawl_config['url'],
                    publisher,
                    include_subdomains=crawl_config.get('include_subdomains', True),
                    max_urls=crawl_config.get('max_pages')
                )
            else:
                # Deep crawling
                results = await crawler.crawl_and_publish(
                    crawl_config['url'],
                    crawl_config.get('allowed_domains', []),
                    publisher
                )
            
            logger.info(f"Crawl completed: {results}")
            return results
            
        except Exception as e:
            logger.error(f"Crawl failed: {e}")
            raise
        finally:
            # Always close publisher
            await publisher.close()
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate crawl configuration.
        
        Args:
            config: Configuration to validate
            
        Returns:
            True if valid, raises exception otherwise
        """
        if not config.get('url'):
            raise ValueError("URL is required for crawling")
        
        # Validate URL format
        from urllib.parse import urlparse
        parsed = urlparse(config['url'])
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(f"Invalid URL: {config['url']}")
        
        # Validate numeric parameters
        if 'max_pages' in config:
            if not isinstance(config['max_pages'], int) or config['max_pages'] <= 0:
                raise ValueError("max_pages must be a positive integer")
        
        return True