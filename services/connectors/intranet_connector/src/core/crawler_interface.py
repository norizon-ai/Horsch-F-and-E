"""
Unified crawler interface for all crawler implementations.

This module provides a common interface and shared functionality for all crawlers,
eliminating code duplication between different crawler types.
"""

import logging
from abc import ABC, abstractmethod
from typing import AsyncIterator, Dict, Any, List, Optional
from datetime import datetime
import hashlib

from models.articles import RawArticle, RawArticleSource

logger = logging.getLogger(__name__)


class CrawlerInterface(ABC):
    """
    Abstract base class for all crawler implementations.
    
    This interface defines the common contract for crawlers and provides
    shared functionality to eliminate duplication.
    """
    
    def __init__(self, settings):
        """
        Initialize the crawler interface.
        
        Args:
            settings: Crawler settings configuration
        """
        self.settings = settings
        self.crawled_urls = set()
        self.error_count = 0
        self.success_count = 0
        
    @abstractmethod
    async def crawl_urls(
        self,
        urls: List[str],
        allowed_domains: List[str],
        max_pages: Optional[int] = None,
        max_depth: Optional[int] = None
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Crawl a list of URLs.
        
        This is the main method that each crawler must implement.
        
        Args:
            urls: List of URLs to crawl
            allowed_domains: List of allowed domains
            max_pages: Maximum number of pages to crawl
            max_depth: Maximum crawl depth
            
        Yields:
            Crawl results as dictionaries
        """
        pass
    
    def process_crawl_result(
        self,
        url: str,
        content: str,
        metadata: Dict[str, Any],
        html: Optional[str] = None,
        links: Optional[Any] = None,
        success: bool = True,
        error: Optional[Exception] = None
    ) -> Dict[str, Any]:
        """
        Process a crawl result into a standardized format.
        
        This method eliminates the duplicate result processing logic
        that was present in multiple crawlers.
        
        Args:
            url: The URL that was crawled
            content: The extracted content (markdown or text)
            metadata: Metadata extracted from the page
            html: Raw HTML content (optional)
            links: Extracted links (optional)
            success: Whether the crawl was successful
            error: Exception if crawl failed
            
        Returns:
            Standardized crawl result dictionary
        """
        if success:
            self.success_count += 1
            
            # Create RawArticle
            article = self._create_raw_article(url, content, metadata)
            
            return {
                'success': True,
                'url': url,
                'data': article,
                'html': html,
                'links': links,
                'metadata': metadata
            }
        else:
            self.error_count += 1
            
            return {
                'success': False,
                'url': url,
                'error': error,
                'error_message': str(error) if error else 'Unknown error'
            }
    
    def _create_raw_article(
        self,
        url: str,
        content: str,
        metadata: Dict[str, Any]
    ) -> RawArticle:
        """
        Create a RawArticle from crawled data.
        
        This consolidates the duplicate RawArticle creation logic.
        
        Args:
            url: The URL of the article
            content: The article content
            metadata: Article metadata
            
        Returns:
            RawArticle instance
        """
        # Generate document ID
        doc_id = self._generate_document_id(url)
        
        # Create source
        source = RawArticleSource(
            uri=url,
            module="Intranet Connector",
            retrieved_at=datetime.utcnow()
        )
        
        # Build metadata
        article_metadata = {
            'url': url,
            'title': metadata.get('title', ''),
            'description': metadata.get('description', ''),
            'crawled_at': datetime.utcnow().isoformat(),
            'crawler': self.__class__.__name__
        }
        
        # Add OpenGraph metadata if present
        for key, value in metadata.items():
            if key.startswith('og:') or key.startswith('twitter:'):
                article_metadata[key] = value
        
        # Add technical metadata
        if 'status_code' in metadata:
            article_metadata['status_code'] = metadata['status_code']
        if 'content_type' in metadata:
            article_metadata['content_type'] = metadata['content_type']
        if 'depth' in metadata:
            article_metadata['depth'] = metadata['depth']
        
        # Create article
        article = RawArticle(
            source_document_id=doc_id,
            content=content,
            source=source,
            metadata=article_metadata,
            tags=[],
            permissions=[]
        )
        
        return article
    
    def _generate_document_id(self, url: str) -> str:
        """
        Generate a unique document ID for a URL.
        
        Args:
            url: The URL to generate ID for
            
        Returns:
            Unique document ID
        """
        # Use URL hash for consistent IDs
        url_hash = hashlib.sha256(url.encode()).hexdigest()[:12]
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{url_hash}_{timestamp}"
    
    def should_crawl_url(self, url: str, force_recrawl: bool = False) -> bool:
        """
        Check if a URL should be crawled.
        
        Args:
            url: The URL to check
            force_recrawl: If True, ignore duplicate checks
            
        Returns:
            True if the URL should be crawled
        """
        if force_recrawl:
            return True
        
        if url in self.crawled_urls:
            logger.debug(f"Skipping duplicate URL: {url}")
            return False
        
        return True
    
    def mark_url_crawled(self, url: str) -> None:
        """
        Mark a URL as crawled.
        
        Args:
            url: The URL that was crawled
        """
        self.crawled_urls.add(url)
    
    def is_domain_allowed(self, url: str, allowed_domains: List[str]) -> bool:
        """
        Check if a URL's domain is in the allowed list.
        
        Args:
            url: The URL to check
            allowed_domains: List of allowed domains
            
        Returns:
            True if the domain is allowed
        """
        from urllib.parse import urlparse
        
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        for allowed in allowed_domains:
            if domain == allowed.lower() or domain.endswith(f".{allowed.lower()}"):
                return True
        
        return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get crawler statistics.
        
        Returns:
            Dictionary with crawler statistics
        """
        total = self.success_count + self.error_count
        success_rate = self.success_count / total if total > 0 else 0
        
        return {
            'total_crawled': total,
            'successful': self.success_count,
            'failed': self.error_count,
            'success_rate': success_rate,
            'unique_urls': len(self.crawled_urls)
        }
    
    def reset_statistics(self) -> None:
        """Reset crawler statistics."""
        self.crawled_urls.clear()
        self.error_count = 0
        self.success_count = 0
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        # Cleanup if needed
        pass