"""
Crawl Orchestrator for comprehensive domain crawling.

This module provides orchestration for crawling entire domains including
all subdomains, using an iterative discovery approach.
"""

import sys
from typing import Dict, Optional, Any, List
from urllib.parse import urlparse
from datetime import datetime
import logging

from config.settings import CrawlerSettings
from core.subdomain_extractor import SubdomainExtractor
from core.sitemap_crawler import SitemapCrawler, SitemapParser
from core.crawler import IntranetCrawler
from publishers.base import PublisherBase

logger = logging.getLogger(__name__)


class CrawlStatistics:
    """Track statistics for the orchestrated crawl."""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.domains_discovered = set()
        self.domains_crawled = set()
        self.domains_with_sitemap = set()
        self.total_pages = 0
        self.failed_pages = 0
        self.pages_per_domain = {}
        self.errors_per_domain = {}
        
    def add_domain_discovered(self, domain: str):
        """Record a newly discovered domain."""
        self.domains_discovered.add(domain)
        
    def add_domain_crawled(self, domain: str):
        """Record a domain as crawled."""
        self.domains_crawled.add(domain)
        
    def add_page_crawled(self, domain: str, success: bool = True):
        """Record a page crawl."""
        self.total_pages += 1
        if not success:
            self.failed_pages += 1
        
        if domain not in self.pages_per_domain:
            self.pages_per_domain[domain] = 0
        self.pages_per_domain[domain] += 1
        
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of crawl statistics."""
        duration = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "duration_seconds": duration,
            "domains_discovered": len(self.domains_discovered),
            "domains_crawled": len(self.domains_crawled),
            "domains_with_sitemap": len(self.domains_with_sitemap),
            "total_pages": self.total_pages,
            "failed_pages": self.failed_pages,
            "success_rate": (self.total_pages - self.failed_pages) / self.total_pages if self.total_pages > 0 else 0,
            "pages_per_second": self.total_pages / duration if duration > 0 else 0,
            "pages_per_domain": self.pages_per_domain
        }


class CrawlOrchestrator:
    """
    Orchestrator that manages comprehensive domain crawling using crawl4ai.
    
    Features:
    - Iterative subdomain discovery
    - Intelligent strategy selection (sitemap vs deep crawl)
    - Progress tracking and statistics
    - Memory-efficient streaming
    """
    
    def __init__(self, settings: CrawlerSettings, base_url: str):
        """
        Initialize the orchestrator.
        
        Args:
            settings: Crawler configuration settings
            base_url: Starting URL for the crawl
        """
        self.settings = settings
        self.base_url = base_url
        
        # Extract base domain (remove www. and any subdomains)
        parsed = urlparse(base_url)
        domain_parts = parsed.netloc.split('.')
        if len(domain_parts) > 2:
            # Handle cases like www.fau.de or subdomain.fau.de
            self.base_domain = '.'.join(domain_parts[-2:])
        else:
            self.base_domain = parsed.netloc
        
        # Initialize components
        self.extractor = SubdomainExtractor(self.base_domain)
        self.stats = CrawlStatistics()
        
        # Track crawl state
        self.discovered_subdomains = set()
        self.crawled_subdomains = set()
        self.pending_subdomains = set()
        self.failed_subdomains = set()
        
        # Add the starting domain
        start_domain = parsed.netloc
        if start_domain.replace('www.', '') != self.base_domain:
            # Starting from a subdomain
            subdomain = start_domain.replace(f'.{self.base_domain}', '').replace('www.', '')
            if subdomain:
                self.discovered_subdomains.add(subdomain)
                self.pending_subdomains.add(subdomain)
        else:
            # Starting from base domain
            self.pending_subdomains.add('__base__')  # Special marker for base domain
    
    async def orchestrate_comprehensive_crawl(
        self, 
        publisher: PublisherBase,
        max_subdomains: Optional[int] = None,
        resume: bool = False,
        force_recrawl: bool = False
    ) -> Dict[str, Any]:
        """
        Orchestrate a comprehensive crawl of the domain and all subdomains.
        
        Args:
            publisher: Publisher for storing crawled data
            max_subdomains: Maximum number of subdomains to crawl (None for unlimited)
            resume: If True, skip initial crawl if base domain already crawled
            force_recrawl: If True, recrawl previously visited URLs
            
        Returns:
            Dictionary with crawl statistics and results
        """
        print("\n" + "=" * 60)
        print("COMPREHENSIVE DOMAIN CRAWL")
        print("=" * 60)
        print(f"Base domain: {self.base_domain}")
        print(f"Starting URL: {self.base_url}")
        print(f"Max subdomains: {max_subdomains or 'unlimited'}")
        print(f"Unlimited crawl: {self.settings.UNLIMITED_CRAWL}")
        print("=" * 60)
        
        try:
            # Store publisher reference for state saving
            self.current_publisher = publisher
            
            # Connect publisher
            await publisher.connect()
            
            # Load existing subdomain state if publisher supports it
            if hasattr(publisher, 'get_subdomain_state'):
                prev_state = publisher.get_subdomain_state()
                if prev_state.get('base_domain') == self.base_domain:
                    # Merge with existing state
                    self.discovered_subdomains.update(prev_state.get('discovered_subdomains', set()))
                    self.crawled_subdomains.update(prev_state.get('crawled_subdomains', set()))
                    
                    # Add uncrawled discovered subdomains to pending
                    for subdomain in prev_state.get('discovered_subdomains', set()):
                        if subdomain not in self.crawled_subdomains:
                            self.pending_subdomains.add(subdomain)
                    
                    if self.discovered_subdomains:
                        print(f"\n📚 Loaded previous subdomain state:")
                        print(f"  Previously discovered: {len(self.discovered_subdomains)} subdomains")
                        print(f"  Previously crawled: {len(self.crawled_subdomains)} subdomains")
                        print(f"  Resuming with: {len(self.pending_subdomains)} pending subdomains")
            
            # Save initial state
            if hasattr(publisher, 'save_subdomain_state'):
                await publisher.save_subdomain_state(
                    base_domain=self.base_domain,
                    discovered=self.discovered_subdomains,
                    crawled=self.crawled_subdomains,
                    pending=self.pending_subdomains,
                    failed=self.failed_subdomains
                )
            
            # Phase 1: Crawl starting point
            print("\n📍 Phase 1: Initial crawl")
            print("-" * 40)
            
            # Always crawl initial domain - individual URLs will be skipped as needed
            # When resume=True, the sitemap crawler will skip already processed URLs
            # When resume=True, the deep crawler will check against processed URLs
            if resume:
                print(f"  📌 Resume mode: will skip already processed URLs")
            
            await self._crawl_initial_domain(publisher, force_recrawl)
            
            # Phase 2+: Iteratively crawl discovered subdomains
            phase = 2
            subdomains_crawled = 0
            
            while self.pending_subdomains and (max_subdomains is None or subdomains_crawled < max_subdomains):
                pending_list = list(self.pending_subdomains)
                print(f"\n📍 Phase {phase}: Found {len(pending_list)} new subdomain(s)")
                print("-" * 40)
                
                for subdomain in pending_list:
                    if max_subdomains and subdomains_crawled >= max_subdomains:
                        print(f"\n⚠️ Reached maximum subdomain limit ({max_subdomains})")
                        break
                    
                    # Remove from pending
                    self.pending_subdomains.discard(subdomain)
                    
                    # Build subdomain URL
                    if subdomain == '__base__':
                        domain_url = f"https://{self.base_domain}"
                        domain_name = self.base_domain
                    else:
                        domain_url = f"https://{subdomain}.{self.base_domain}"
                        domain_name = f"{subdomain}.{self.base_domain}"
                    
                    print(f"\n🌐 Crawling: {domain_name}")
                    
                    try:
                        # Skip if already crawled and not force recrawl
                        if subdomain in self.crawled_subdomains and not force_recrawl:
                            print(f"  ⏭ Skipping (already crawled)")
                            continue
                        
                        # Crawl this subdomain
                        await self._crawl_domain(domain_url, domain_name, publisher, force_recrawl)
                        
                        # Mark as crawled
                        self.crawled_subdomains.add(subdomain)
                        self.stats.add_domain_crawled(domain_name)
                        
                        # Save updated state
                        if hasattr(self, 'current_publisher'):
                            await self._save_subdomain_state_async()
                        subdomains_crawled += 1
                        
                    except Exception as e:
                        logger.error(f"Failed to crawl {domain_name}: {e}")
                        self.failed_subdomains.add(subdomain)
                        print(f"  ❌ Failed: {e}")
                
                phase += 1
                
                # Check if we discovered any new subdomains
                if not self.pending_subdomains:
                    print("\n✅ No new subdomains discovered")
            
            # Final statistics
            print("\n" + "=" * 60)
            print("CRAWL COMPLETE")
            print("=" * 60)
            
            stats = self.stats.get_summary()
            print(f"Duration: {stats['duration_seconds']:.1f} seconds")
            print(f"Domains discovered: {stats['domains_discovered']}")
            print(f"Domains crawled: {stats['domains_crawled']}")
            print(f"Total pages: {stats['total_pages']}")
            print(f"Failed pages: {stats['failed_pages']}")
            print(f"Success rate: {stats['success_rate']*100:.1f}%")
            print(f"Average speed: {stats['pages_per_second']:.1f} pages/second")
            
            if stats['pages_per_domain']:
                print("\nPages per domain:")
                for domain, count in sorted(stats['pages_per_domain'].items(), key=lambda x: x[1], reverse=True)[:10]:
                    print(f"  {domain}: {count} pages")
            
            return stats
            
        finally:
            await publisher.close()
    
    async def _crawl_initial_domain(self, publisher: PublisherBase, force_recrawl: bool = False):
        """Crawl the initial domain from the starting URL."""
        parsed = urlparse(self.base_url)
        domain_name = parsed.netloc
        
        print(f"\n🌐 Crawling initial domain: {domain_name}")
        await self._crawl_domain(self.base_url, domain_name, publisher, force_recrawl)
        
        # Mark the initial domain as crawled
        # Handle www.domain.com and domain.com consistently
        if domain_name == self.base_domain or domain_name == f"www.{self.base_domain}":
            # Mark both __base__ and www to handle different scenarios
            self.crawled_subdomains.add('__base__')
            self.pending_subdomains.discard('__base__')
            if domain_name.startswith('www.'):
                self.crawled_subdomains.add('www')
                self.pending_subdomains.discard('www')
        else:
            # It's a subdomain
            subdomain = domain_name.replace(f'.{self.base_domain}', '').replace('www.', '')
            if subdomain:
                self.crawled_subdomains.add(subdomain)
                self.pending_subdomains.discard(subdomain)
        
        # Save state after marking initial domain as crawled
        if hasattr(self, 'current_publisher'):
            await self._save_subdomain_state_async()
    
    async def _crawl_domain(self, domain_url: str, domain_name: str, publisher: PublisherBase, force_recrawl: bool = False):
        """
        Crawl a single domain, extracting subdomains from each page.
        
        Args:
            domain_url: URL of the domain to crawl
            domain_name: Name of the domain (for logging)
            publisher: Publisher for storing crawled data
            force_recrawl: If True, recrawl previously visited URLs
        """
        # Check if domain has a sitemap
        has_sitemap = await self._check_for_sitemap(domain_url)
        
        if has_sitemap:
            print(f"  ✓ Found sitemap, using sitemap crawler")
            self.stats.domains_with_sitemap.add(domain_name)
            await self._crawl_with_sitemap(domain_url, domain_name, publisher, force_recrawl)
        else:
            print(f"  ℹ No sitemap found, using deep crawler")
            await self._crawl_with_deep_crawler(domain_url, domain_name, publisher, force_recrawl)
    
    async def _check_for_sitemap(self, domain_url: str) -> bool:
        """Check if a domain has a sitemap."""
        try:
            parser = SitemapParser(domain_url, include_subdomains=self.settings.INCLUDE_SUBDOMAINS)
            sitemaps = await parser.find_sitemaps()
            return len(sitemaps) > 0
        except Exception as e:
            logger.debug(f"Error checking for sitemap at {domain_url}: {e}")
            return False
    
    async def _crawl_with_sitemap(self, domain_url: str, domain_name: str, publisher: PublisherBase, force_recrawl: bool = False):
        """Crawl a domain using its sitemap."""
        # Note: force_recrawl handling would need to be implemented in the crawler
        # For now, we pass the flag but don't modify settings  
        crawler = SitemapCrawler(self.settings)
        
        # Parse sitemap to get URLs
        parser = SitemapParser(domain_url, include_subdomains=False)
        sitemap_data = await parser.parse_all_sitemaps()
        
        if not sitemap_data['urls']:
            print(f"  ⚠ Sitemap empty, falling back to deep crawler")
            await self._crawl_with_deep_crawler(domain_url, domain_name, publisher)
            return
        
        print(f"  📄 Found {len(sitemap_data['urls'])} URLs in sitemap")
        
        # Limit URLs if not unlimited crawl
        urls_to_crawl = sitemap_data['urls']
        if not self.settings.UNLIMITED_CRAWL and self.settings.MAX_PAGES:
            urls_to_crawl = urls_to_crawl[:self.settings.MAX_PAGES]
            print(f"  ⚠ Limited to {len(urls_to_crawl)} URLs")
        
        # Get already processed URLs from publisher if available
        already_processed = set()
        if hasattr(publisher, 'processed_urls'):
            already_processed = publisher.processed_urls.copy()
            if already_processed:
                print(f"  📌 Found {len(already_processed)} previously processed URLs to skip")
        
        # Filter out already processed URLs BEFORE crawling
        filtered_urls = []
        skipped_count = 0
        for url_data in urls_to_crawl:
            url = url_data['loc'] if isinstance(url_data, dict) else url_data
            if url in already_processed:
                skipped_count += 1
            else:
                filtered_urls.append(url_data)
        
        if skipped_count > 0:
            print(f"  ⚡ Filtering out {skipped_count} already processed URLs")
            print(f"  📊 Will crawl {len(filtered_urls)} new URLs")
        
        # Check if there are any URLs left to crawl
        if not filtered_urls:
            print(f"  ✅ All URLs from {domain_name} have already been processed")
            return
        
        # Crawl only the filtered URLs
        pages_crawled = 0
        async for result in crawler.crawl_urls(filtered_urls, [domain_name]):
            if result.get('success'):
                # Publish the page (result['data'] is already a RawArticle)
                await publisher.publish_message(result['data'])
                
                # Extract subdomains using crawl4ai's extracted links
                if result.get('links'):
                    await self._extract_and_queue_subdomains(result.get('html', ''), result['url'], result['links'])
                elif result.get('html'):
                    # Fallback to HTML parsing if no links available
                    await self._extract_and_queue_subdomains(result['html'], result['url'])
                
                pages_crawled += 1
                self.stats.add_page_crawled(domain_name, success=True)
                
                # Progress indicator
                if pages_crawled % 10 == 0:
                    print(f"    Progress: {pages_crawled}/{len(urls_to_crawl)} pages")
            else:
                self.stats.add_page_crawled(domain_name, success=False)
        
        if skipped_count > 0:
            print(f"  ⚡ Total skipped: {skipped_count} already processed URLs")
        print(f"  ✓ Crawled {pages_crawled} new pages from {domain_name}")
        
        # Save state after crawling domain
        if hasattr(self, 'current_publisher'):
            await self._save_subdomain_state_async()
    
    async def _crawl_with_deep_crawler(self, domain_url: str, domain_name: str, publisher: PublisherBase, force_recrawl: bool = False):
        """Crawl a domain using deep crawling."""
        # Configure crawler for comprehensive crawling
        settings = self.settings.model_copy()
        if self.settings.UNLIMITED_CRAWL:
            settings.MAX_DEPTH = sys.maxsize
            settings.MAX_PAGES = sys.maxsize
        # Note: force_recrawl handling would need to be implemented in the crawler
        # For now, we pass the flag but don't modify settings
        
        crawler = IntranetCrawler(settings)
        
        # Get already processed URLs from publisher if available
        already_processed = set()
        if hasattr(publisher, 'processed_urls'):
            already_processed = publisher.processed_urls.copy()
            if already_processed:
                print(f"  📌 Found {len(already_processed)} previously processed URLs to skip")
        
        # Check if the starting URL has already been processed
        if domain_url in already_processed:
            print(f"  ✅ Starting URL {domain_url} already processed, checking for new pages only")
        
        # Crawl and extract subdomains
        pages_crawled = 0
        skipped_count = 0
        async for result in crawler._crawl_generator_with_errors(domain_url, [domain_name]):
            if result.get('success'):
                # Skip if already processed
                url = result['url']
                if url in already_processed:
                    skipped_count += 1
                    if skipped_count % 10 == 0:
                        print(f"  ⚡ Skipped {skipped_count} already processed URLs")
                    continue
                
                # Publish the page (result['data'] is already a RawArticle)
                await publisher.publish_message(result['data'])
                
                # Extract subdomains using crawl4ai's extracted links
                if result.get('links'):
                    await self._extract_and_queue_subdomains(result.get('html', ''), result['url'], result['links'])
                elif result.get('html'):
                    # Fallback to HTML parsing if no links available
                    await self._extract_and_queue_subdomains(result['html'], result['url'])
                
                pages_crawled += 1
                self.stats.add_page_crawled(domain_name, success=True)
                
                # Progress indicator
                if pages_crawled % 10 == 0:
                    print(f"    Progress: {pages_crawled} pages crawled")
                    
                # Check if we should stop (for non-unlimited crawls)
                if not self.settings.UNLIMITED_CRAWL and pages_crawled >= self.settings.MAX_PAGES:
                    print(f"    ⚠ Reached page limit ({self.settings.MAX_PAGES})")
                    break
            else:
                self.stats.add_page_crawled(domain_name, success=False)
        
        if skipped_count > 0:
            print(f"  ⚡ Total skipped: {skipped_count} already processed URLs")
        print(f"  ✓ Crawled {pages_crawled} new pages from {domain_name}")
        
        # Save state after crawling domain
        if hasattr(self, 'current_publisher'):
            await self._save_subdomain_state_async()
    
    async def _extract_and_queue_subdomains(self, html_content: str, page_url: str, links_data: Optional[Any] = None):
        """
        Extract subdomains from page content and add to queue.
        
        Args:
            html_content: HTML content of the page
            page_url: URL of the page
            links_data: Optional Links object from crawl4ai with pre-extracted links
        """
        # Extract subdomains (prefer crawl4ai's links if available)
        new_subdomains = self.extractor.extract_from_page(html_content, page_url, links_data)
        
        # Track if we found any new subdomains
        found_new = False
        
        # Add newly discovered subdomains to queue
        for subdomain in new_subdomains:
            if subdomain not in self.discovered_subdomains:
                self.discovered_subdomains.add(subdomain)
                self.stats.add_domain_discovered(f"{subdomain}.{self.base_domain}")
                found_new = True
                
                # Add to pending if not already crawled
                if subdomain not in self.crawled_subdomains and subdomain not in self.failed_subdomains:
                    self.pending_subdomains.add(subdomain)
                    print(f"    → Discovered: {subdomain}.{self.base_domain}")
        
        # Save subdomain state immediately if we found new ones
        if found_new and hasattr(self, 'current_publisher'):
            await self._save_subdomain_state_async()
    
    async def _save_subdomain_state_async(self):
        """
        Save subdomain state asynchronously if publisher supports it.
        """
        if hasattr(self.current_publisher, 'save_subdomain_state'):
            await self.current_publisher.save_subdomain_state(
                base_domain=self.base_domain,
                discovered=self.discovered_subdomains,
                crawled=self.crawled_subdomains,
                pending=self.pending_subdomains,
                failed=self.failed_subdomains
            )
    
    def get_discovered_subdomains(self) -> List[str]:
        """
        Get list of all discovered subdomains.
        
        Returns:
            List of full subdomain names
        """
        return [f"{s}.{self.base_domain}" for s in self.discovered_subdomains if s != '__base__']