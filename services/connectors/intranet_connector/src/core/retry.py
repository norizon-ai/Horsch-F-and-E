#!/usr/bin/env python3
"""
Retry mechanism for failed crawl URLs.

This module provides intelligent retry logic for URLs that failed during crawling,
with different strategies based on error types.
"""

import asyncio
from typing import List, Dict, Any, Optional
from pathlib import Path
import json
from datetime import datetime, timezone
import random

from core.crawler import IntranetCrawler
from config.settings import CrawlerSettings
from core.error_tracker import ErrorTracker, ErrorType
from publishers.base import PublisherBase


class RetryStrategy:
    """Base class for retry strategies."""
    
    def get_delay(self, attempt: int) -> float:
        """
        Get delay in seconds for the given attempt number.
        
        Args:
            attempt: Attempt number (0-based)
            
        Returns:
            Delay in seconds
        """
        raise NotImplementedError


class ExponentialBackoff(RetryStrategy):
    """Exponential backoff retry strategy."""
    
    def __init__(self, base_delay: float = 1.0, max_delay: float = 60.0):
        self.base_delay = base_delay
        self.max_delay = max_delay
    
    def get_delay(self, attempt: int) -> float:
        """Calculate exponential backoff delay."""
        delay = self.base_delay * (2 ** attempt)
        # Add jitter to prevent thundering herd
        jitter = random.uniform(0, 0.1 * delay)
        return min(delay + jitter, self.max_delay)


class LinearBackoff(RetryStrategy):
    """Linear backoff retry strategy."""
    
    def __init__(self, increment: float = 5.0, max_delay: float = 30.0):
        self.increment = increment
        self.max_delay = max_delay
    
    def get_delay(self, attempt: int) -> float:
        """Calculate linear backoff delay."""
        return min(self.increment * (attempt + 1), self.max_delay)


class CrawlerRetry:
    """
    Manages retry logic for failed crawl URLs.
    
    Features:
    - Intelligent retry based on error type
    - Configurable retry strategies
    - Progress tracking
    - Final failure handling
    """
    
    def __init__(self, crawler: IntranetCrawler, publisher: PublisherBase,
                 max_retries: int = 3):
        """
        Initialize the retry manager.
        
        Args:
            crawler: The crawler instance
            publisher: The publisher for successful crawls
            max_retries: Maximum number of retry attempts
        """
        self.crawler = crawler
        self.publisher = publisher
        self.max_retries = max_retries
        
        # Define retry strategies for different error types
        self.strategies = {
            ErrorType.TIMEOUT: ExponentialBackoff(base_delay=2.0, max_delay=60.0),
            ErrorType.NETWORK: ExponentialBackoff(base_delay=1.0, max_delay=30.0),
            ErrorType.CONNECTION: LinearBackoff(increment=5.0, max_delay=30.0),
            ErrorType.DNS: LinearBackoff(increment=10.0, max_delay=60.0),
            # Don't retry HTTP errors (404, 403, etc.) or parsing errors
            ErrorType.HTTP_ERROR: None,
            ErrorType.PARSING: None,
            ErrorType.UNKNOWN: ExponentialBackoff(base_delay=1.0, max_delay=30.0)
        }
        
        self.retry_stats = {
            "total_retries": 0,
            "successful_retries": 0,
            "final_failures": 0,
            "by_type": {}
        }
    
    async def retry_failed_urls(self, failed_urls: List[Dict[str, Any]],
                               allowed_domains: List[str]) -> Dict[str, Any]:
        """
        Retry failed URLs with appropriate strategies.
        
        Args:
            failed_urls: List of failed URL information
            allowed_domains: Allowed domains for crawling
            
        Returns:
            Dictionary with retry results
        """
        print(f"\n{'='*60}")
        print(f"STARTING RETRY PROCESS")
        print(f"{'='*60}")
        print(f"Failed URLs to retry: {len(failed_urls)}")
        print(f"Max retries per URL: {self.max_retries}")
        
        results = {
            "recovered": [],
            "permanent_failures": [],
            "statistics": {}
        }
        
        # Group URLs by error type for batch processing
        urls_by_type = self._group_by_error_type(failed_urls)
        
        for error_type, urls in urls_by_type.items():
            print(f"\n--- Retrying {error_type.value} errors ({len(urls)} URLs) ---")
            
            strategy = self.strategies.get(error_type)
            if strategy is None:
                # No retry for this error type
                print(f"  Skipping {error_type.value} errors (no retry strategy)")
                results["permanent_failures"].extend(urls)
                continue
            
            for url_info in urls:
                url = url_info["url"]
                retry_count = url_info.get("retry_count", 0)
                
                if retry_count >= self.max_retries:
                    print(f"  {url}: Max retries exceeded")
                    results["permanent_failures"].append(url_info)
                    self.retry_stats["final_failures"] += 1
                    continue
                
                # Calculate delay
                delay = strategy.get_delay(retry_count)
                print(f"  Retrying {url} (attempt {retry_count + 1}/{self.max_retries})")
                print(f"    Waiting {delay:.1f} seconds...")
                await asyncio.sleep(delay)
                
                # Retry the URL
                success = await self._retry_single_url(url, allowed_domains)
                
                self.retry_stats["total_retries"] += 1
                
                if success:
                    print(f"    ✓ Successfully recovered")
                    results["recovered"].append(url)
                    self.retry_stats["successful_retries"] += 1
                else:
                    # Update retry count
                    url_info["retry_count"] = retry_count + 1
                    
                    if url_info["retry_count"] >= self.max_retries:
                        print(f"    ✗ Failed after {self.max_retries} attempts")
                        results["permanent_failures"].append(url_info)
                        self.retry_stats["final_failures"] += 1
                    else:
                        # Will be retried in next round
                        print(f"    ✗ Failed, will retry again")
        
        # Generate summary
        results["statistics"] = self.retry_stats
        self._print_retry_summary(results)
        
        return results
    
    async def _retry_single_url(self, url: str, allowed_domains: List[str]) -> bool:
        """
        Retry crawling a single URL.
        
        Args:
            url: URL to retry
            allowed_domains: Allowed domains
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Use the crawler's internal method directly
            config = self.crawler._create_crawler_config(allowed_domains)
            
            async with self.crawler.crawler as crawler:
                result = await crawler.arun(url, config=config)
                
                if result and result.success:
                    # Process and publish
                    from models.articles import RawArticle, RawArticleSource, RawArticleAuthor
                    from datetime import datetime, timezone
                    
                    # Create article from result
                    metadata = result.metadata or {}
                    metadata["title"] = metadata.get("title", url)
                    metadata["status_code"] = result.status_code
                    metadata["retry_recovered"] = True  # Mark as recovered
                    
                    author_name = metadata.get('author')
                    author = RawArticleAuthor(name=author_name) if author_name else None
                    
                    page_data = RawArticle(
                        source_document_id=url,
                        content=result.markdown or "",
                        source=RawArticleSource(
                            uri=url,
                            module="Intranet Connector",
                            retrieved_at=datetime.now(timezone.utc)
                        ),
                        author=author,
                        tags=[],
                        permissions=[],
                        metadata=metadata
                    )
                    
                    # Publish the recovered page
                    await self.publisher.publish_message(page_data)
                    return True
                    
        except Exception as e:
            print(f"      Error during retry: {str(e)[:100]}")
        
        return False
    
    def _group_by_error_type(self, failed_urls: List[Dict[str, Any]]) -> Dict[ErrorType, List[Dict]]:
        """
        Group failed URLs by error type.
        
        Args:
            failed_urls: List of failed URL information
            
        Returns:
            Dictionary mapping error types to URL lists
        """
        from collections import defaultdict
        grouped = defaultdict(list)
        
        for url_info in failed_urls:
            error_msg = url_info.get("error", "")
            # Detect error type from message
            error_type = self._detect_error_type(error_msg)
            grouped[error_type].append(url_info)
        
        return dict(grouped)
    
    def _detect_error_type(self, error_message: str) -> ErrorType:
        """Detect error type from message."""
        error_lower = error_message.lower()
        
        if any(x in error_lower for x in ['timeout', 'timed out']):
            return ErrorType.TIMEOUT
        elif any(x in error_lower for x in ['dns', 'nxdomain']):
            return ErrorType.DNS
        elif any(x in error_lower for x in ['connection', 'refused']):
            return ErrorType.CONNECTION
        elif any(x in error_lower for x in ['network', 'net::']):
            return ErrorType.NETWORK
        elif any(x in error_lower for x in ['404', '403', '500']):
            return ErrorType.HTTP_ERROR
        else:
            return ErrorType.UNKNOWN
    
    def _print_retry_summary(self, results: Dict[str, Any]) -> None:
        """Print a summary of retry results."""
        print(f"\n{'='*60}")
        print("RETRY SUMMARY")
        print(f"{'='*60}")
        print(f"Total retry attempts: {self.retry_stats['total_retries']}")
        print(f"Successfully recovered: {self.retry_stats['successful_retries']}")
        print(f"Permanent failures: {self.retry_stats['final_failures']}")
        
        if self.retry_stats['successful_retries'] > 0:
            success_rate = (self.retry_stats['successful_retries'] / 
                          self.retry_stats['total_retries'] * 100)
            print(f"Recovery rate: {success_rate:.1f}%")
        
        if results['permanent_failures']:
            print(f"\nPermanently failed URLs ({len(results['permanent_failures'])}):")
            for url_info in results['permanent_failures'][:5]:  # Show first 5
                print(f"  - {url_info['url']}")
            if len(results['permanent_failures']) > 5:
                print(f"  ... and {len(results['permanent_failures']) - 5} more")
        
        print(f"{'='*60}")


async def retry_from_error_log(storage_path: str, session_id: str,
                               crawler_settings: Optional[CrawlerSettings] = None) -> None:
    """
    Retry failed URLs from a previous crawl session.
    
    Args:
        storage_path: Path to crawl data storage
        session_id: Session ID to retry from
        crawler_settings: Crawler settings (uses defaults if None)
    """
    from publisher_factory import PublisherFactory
    
    # Load error log
    error_log_path = Path(storage_path) / session_id / "failed_urls.jsonl"
    if not error_log_path.exists():
        print(f"No error log found for session {session_id}")
        return
    
    failed_urls = []
    with open(error_log_path, "r") as f:
        for line in f:
            try:
                error_data = json.loads(line)
                failed_urls.append({
                    "url": error_data["url"],
                    "error": error_data["error_message"],
                    "retry_count": error_data.get("retry_count", 0)
                })
            except json.JSONDecodeError:
                continue
    
    if not failed_urls:
        print("No failed URLs to retry")
        return
    
    print(f"Found {len(failed_urls)} failed URLs to retry")
    
    # Create crawler and publisher
    settings = crawler_settings or CrawlerSettings()
    crawler = IntranetCrawler(settings)
    publisher = PublisherFactory.create_publisher(settings)
    
    # TODO: Extract allowed_domains from the session
    # For now, we'll need to pass them
    allowed_domains = ["example.com"]  # This should be loaded from session data
    
    try:
        await publisher.connect()
        
        # Create retry manager
        retry_manager = CrawlerRetry(crawler, publisher)
        
        # Retry failed URLs
        results = await retry_manager.retry_failed_urls(failed_urls, allowed_domains)
        
    finally:
        await publisher.close()


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python crawler_retry.py <storage_path> <session_id>")
        sys.exit(1)
    
    storage_path = sys.argv[1]
    session_id = sys.argv[2]
    
    asyncio.run(retry_from_error_log(storage_path, session_id))