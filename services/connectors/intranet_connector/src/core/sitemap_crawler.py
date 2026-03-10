#!/usr/bin/env python3
"""
Sitemap-based crawler for efficient and respectful web crawling.

This module provides functionality to:
1. Parse XML sitemaps (including sitemap indexes)
2. Discover subdomains from sitemaps
3. Crawl URLs directly without deep crawling
4. Handle rate limiting respectfully
"""

import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from typing import List, Set, Dict, Optional, Tuple, Any, AsyncGenerator
from urllib.parse import urlparse, urljoin
from datetime import datetime
import gzip
import random
from pathlib import Path
import json

from core.crawler import IntranetCrawler
from config.settings import CrawlerSettings
from publishing.publisher_base import PublisherBase
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


class SitemapParser:
    """
    Parses XML sitemaps and extracts URLs with metadata.
    
    Handles:
    - Standard sitemaps (sitemap.xml)
    - Sitemap indexes (links to multiple sitemaps)
    - Compressed sitemaps (.gz)
    - Nested sitemap structures
    """
    
    def __init__(self, base_url: str, include_subdomains: bool = True):
        """
        Initialize the sitemap parser.
        
        Args:
            base_url: The base URL of the website
            include_subdomains: Whether to include subdomains in results
        """
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.include_subdomains = include_subdomains
        self.discovered_urls: Set[str] = set()
        self.discovered_subdomains: Set[str] = set()
        self.sitemap_urls: List[str] = []
        self.processed_urls: Set[str] = set()  # Track all processed URLs globally
        self.duplicate_count = 0  # Count duplicates encountered
        
    async def find_sitemaps(self) -> List[str]:
        """
        Find all sitemaps for a website.
        
        Returns:
            List of sitemap URLs
        """
        sitemaps = []
        
        # Check robots.txt first
        robots_sitemaps = await self._check_robots_txt()
        sitemaps.extend(robots_sitemaps)
        
        # Check common sitemap locations if none found
        if not sitemaps:
            common_paths = [
                "/sitemap.xml",
                "/sitemap_index.xml",
                "/sitemap.xml.gz",
                "/sitemaps/sitemap.xml",
                "/sitemap1.xml",
                "/de/sitemap.xml",  # German sites often have language-specific sitemaps
                "/en/sitemap.xml"
            ]
            
            for path in common_paths:
                sitemap_url = urljoin(self.base_url, path)
                if await self._url_exists(sitemap_url):
                    sitemaps.append(sitemap_url)
                    print(f"✓ Found sitemap: {sitemap_url}")
        
        self.sitemap_urls = sitemaps
        return sitemaps
    
    async def parse_all_sitemaps(self, sitemap_urls: Optional[List[str]] = None) -> Dict[str, any]:
        """
        Parse all sitemaps and extract URLs.
        
        Args:
            sitemap_urls: List of sitemap URLs to parse (uses found sitemaps if None)
            
        Returns:
            Dictionary with parsed data and statistics
        """
        if sitemap_urls is None:
            sitemap_urls = self.sitemap_urls or await self.find_sitemaps()
        
        if not sitemap_urls:
            print("No sitemaps found!")
            return {"urls": [], "subdomains": set(), "statistics": {}}
        
        all_urls = []
        processed_sitemaps = set()
        
        # Process each sitemap (handles nesting)
        for sitemap_url in sitemap_urls:
            if sitemap_url not in processed_sitemaps:
                urls = await self._parse_sitemap_recursive(sitemap_url, processed_sitemaps)
                all_urls.extend(urls)
        
        # Analyze discovered URLs
        self._analyze_urls(all_urls)
        
        return {
            "urls": all_urls,
            "subdomains": self.discovered_subdomains,
            "statistics": self._generate_statistics(all_urls)
        }
    
    async def _check_robots_txt(self) -> List[str]:
        """Check robots.txt for sitemap declarations."""
        robots_url = urljoin(self.base_url, "/robots.txt")
        sitemaps = []
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(robots_url, timeout=10) as response:
                    if response.status == 200:
                        content = await response.text()
                        for line in content.split('\n'):
                            if line.lower().startswith('sitemap:'):
                                sitemap_url = line.split(':', 1)[1].strip()
                                sitemaps.append(sitemap_url)
                                print(f"✓ Found sitemap in robots.txt: {sitemap_url}")
                    else:
                        print(f"ℹ️ robots.txt returned status {response.status}")
        except aiohttp.ClientError as e:
            print(f"⚠️ Network error fetching robots.txt: {e}")
        except asyncio.TimeoutError:
            print(f"⚠️ Timeout fetching robots.txt (10s)")
        except Exception as e:
            print(f"⚠️ Unexpected error fetching robots.txt: {e}")
        
        return sitemaps
    
    async def _url_exists(self, url: str) -> bool:
        """Check if a URL exists (returns 200 status)."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.head(url, timeout=5, allow_redirects=True) as response:
                    return response.status == 200
        except:
            return False
    
    async def _parse_sitemap_recursive(self, sitemap_url: str, processed: Set[str]) -> List[Dict]:
        """
        Recursively parse a sitemap, handling sitemap indexes.
        
        Args:
            sitemap_url: URL of the sitemap to parse
            processed: Set of already processed sitemap URLs
            
        Returns:
            List of URL entries with metadata
        """
        if sitemap_url in processed:
            return []
        
        processed.add(sitemap_url)
        print(f"📄 Parsing sitemap: {sitemap_url}")
        
        try:
            content = await self._fetch_sitemap(sitemap_url)
            if not content:
                print(f"  ⚠️ No content received from {sitemap_url}")
                return []
            
            # Debug: Show first 200 chars of content
            if content.startswith('<?xml'):
                print(f"  ✓ Valid XML content received ({len(content)} bytes)")
            
            root = ET.fromstring(content)
            
            # Check if this is a sitemap index
            if 'sitemapindex' in root.tag:
                # This is a sitemap index - parse all child sitemaps
                print(f"  📚 Found sitemap index")
                urls = []
                for sitemap in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'):
                    loc = sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc is not None and loc.text:
                        print(f"    → Found child sitemap: {loc.text}")
                        child_urls = await self._parse_sitemap_recursive(loc.text.strip(), processed)
                        urls.extend(child_urls)
                return urls
            else:
                # Regular sitemap - extract URLs
                urls = []
                skipped_duplicates = 0
                # Try both with and without namespace
                url_elements = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url')
                if not url_elements:
                    # Try without namespace
                    url_elements = root.findall('.//url')
                    if url_elements:
                        print(f"  ℹ️ Found URLs without namespace declaration")
                
                for url_elem in url_elements:
                    url_data = self._extract_url_data(url_elem)
                    if url_data and self._should_include_url(url_data['loc']):
                        # Check for duplicates
                        if url_data['loc'] in self.processed_urls:
                            skipped_duplicates += 1
                            self.duplicate_count += 1
                            continue
                        
                        urls.append(url_data)
                        self.discovered_urls.add(url_data['loc'])
                        self.processed_urls.add(url_data['loc'])
                
                if skipped_duplicates > 0:
                    print(f"  ⚡ Skipped {skipped_duplicates} duplicate URLs")
                
                print(f"  ✓ Found {len(urls)} unique URLs in {sitemap_url}")
                return urls
                
        except ET.ParseError as e:
            print(f"  ⚠️ XML parsing error for {sitemap_url}: {e}")
            print(f"     First 100 chars of content: {content[:100] if content else 'None'}")
            return []
        except Exception as e:
            print(f"  ⚠️ Error parsing {sitemap_url}: {e}")
            return []
    
    async def _fetch_sitemap(self, url: str) -> Optional[str]:
        """Fetch sitemap content, handling compression."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=30) as response:
                    if response.status != 200:
                        return None
                    
                    content = await response.read()
                    
                    # Try to decode as text first
                    try:
                        return content.decode('utf-8')
                    except UnicodeDecodeError:
                        # If decode fails, might be gzipped
                        try:
                            decompressed = gzip.decompress(content)
                            return decompressed.decode('utf-8')
                        except:
                            # Not gzipped either, return as is
                            return content.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"  ⚠️ Error fetching {url}: {e}")
            return None
    
    def _extract_url_data(self, url_elem) -> Optional[Dict]:
        """Extract URL and metadata from sitemap URL element."""
        # Try with namespace first
        loc = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is None:
            # Try without namespace
            loc = url_elem.find('loc')
        
        if loc is None or not loc.text:
            return None
        
        data = {'loc': loc.text.strip()}
        
        # Extract optional metadata (try both with and without namespace)
        lastmod = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
        if lastmod is None:
            lastmod = url_elem.find('lastmod')
        if lastmod is not None and lastmod.text:
            data['lastmod'] = lastmod.text
        
        changefreq = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq')
        if changefreq is None:
            changefreq = url_elem.find('changefreq')
        if changefreq is not None and changefreq.text:
            data['changefreq'] = changefreq.text
        
        priority = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
        if priority is None:
            priority = url_elem.find('priority')
        if priority is not None and priority.text:
            try:
                data['priority'] = float(priority.text)
            except ValueError:
                pass  # Invalid priority value, skip
        
        return data
    
    def _should_include_url(self, url: str) -> bool:
        """Check if URL should be included based on domain settings."""
        parsed = urlparse(url)
        domain = parsed.netloc
        
        if not self.include_subdomains:
            # Only include exact domain match
            return domain == self.base_domain
        else:
            # Include subdomains of base domain
            return domain == self.base_domain or domain.endswith(f'.{self.base_domain}')
    
    def _analyze_urls(self, urls: List[Dict]) -> None:
        """Analyze URLs to discover subdomains and patterns."""
        for url_data in urls:
            url = url_data['loc']
            parsed = urlparse(url)
            domain = parsed.netloc
            
            # Track subdomains
            if domain != self.base_domain and domain.endswith(f'.{self.base_domain}'):
                subdomain = domain.replace(f'.{self.base_domain}', '')
                self.discovered_subdomains.add(subdomain)
    
    def _generate_statistics(self, urls: List[Dict]) -> Dict:
        """Generate statistics about the discovered URLs."""
        stats = {
            "total_urls": len(urls),
            "unique_domains": len(set(urlparse(u['loc']).netloc for u in urls)),
            "subdomains": list(self.discovered_subdomains),
            "subdomain_count": len(self.discovered_subdomains),
            "urls_by_domain": {}
        }
        
        # Count URLs per domain
        for url_data in urls:
            domain = urlparse(url_data['loc']).netloc
            stats["urls_by_domain"][domain] = stats["urls_by_domain"].get(domain, 0) + 1
        
        # Sort domains by URL count
        stats["urls_by_domain"] = dict(sorted(
            stats["urls_by_domain"].items(),
            key=lambda x: x[1],
            reverse=True
        ))
        
        return stats


class SitemapCrawler(IntranetCrawler):
    """
    Extended crawler that supports sitemap-based crawling.
    
    Features:
    - Parse and use sitemaps for URL discovery
    - Crawl URLs directly without deep crawling
    - Automatic subdomain discovery
    - Rate limiting and respectful crawling
    """
    
    def __init__(self, settings: CrawlerSettings):
        """Initialize the sitemap crawler."""
        super().__init__(settings)
        self.sitemap_parser = None
        self.crawl_delay = getattr(settings, 'CRAWL_DELAY', 1.0)
        self.random_delay = getattr(settings, 'RANDOM_DELAY', True)
        self.duplicate_count = 0  # Track duplicates across the crawl
        
    async def crawl_from_sitemap(
        self,
        base_url: str,
        publisher: PublisherBase,
        include_subdomains: bool = True,
        max_urls: Optional[int] = None,
        subdomain_filter: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Crawl a website using its sitemap.
        
        Args:
            base_url: Base URL of the website
            publisher: Publisher for storing crawled data
            include_subdomains: Whether to include subdomains
            max_urls: Maximum number of URLs to crawl (None for all)
            subdomain_filter: List of specific subdomains to include (None for all)
            
        Returns:
            Dictionary with crawl statistics
        """
        print("=" * 60)
        print("SITEMAP-BASED CRAWLING")
        print("=" * 60)
        print(f"Base URL: {base_url}")
        print(f"Include subdomains: {include_subdomains}")
        print(f"Max URLs: {max_urls or 'unlimited'}")
        print(f"Crawl delay: {self.crawl_delay}s")
        
        # Parse sitemaps
        self.sitemap_parser = SitemapParser(base_url, include_subdomains)
        sitemap_data = await self.sitemap_parser.parse_all_sitemaps()
        
        # Transfer duplicate count from parser
        self.duplicate_count = self.sitemap_parser.duplicate_count
        
        if not sitemap_data['urls']:
            print("No URLs found in sitemaps!")
            return {"error": "No URLs found"}
        
        # Display discovered subdomains
        if sitemap_data['subdomains']:
            print(f"\n📍 Discovered {len(sitemap_data['subdomains'])} subdomains:")
            for subdomain in sorted(sitemap_data['subdomains'])[:10]:
                count = sitemap_data['statistics']['urls_by_domain'].get(
                    f"{subdomain}.{urlparse(base_url).netloc}", 0
                )
                print(f"  • {subdomain}.{urlparse(base_url).netloc} ({count} URLs)")
            if len(sitemap_data['subdomains']) > 10:
                print(f"  ... and {len(sitemap_data['subdomains']) - 10} more")
        
        # Filter URLs if needed
        urls_to_crawl = sitemap_data['urls']
        
        if subdomain_filter:
            # Filter to specific subdomains
            base_domain = urlparse(base_url).netloc
            allowed_domains = [base_domain] + [f"{sd}.{base_domain}" for sd in subdomain_filter]
            urls_to_crawl = [
                u for u in urls_to_crawl
                if urlparse(u['loc']).netloc in allowed_domains
            ]
            print(f"\nFiltered to {len(urls_to_crawl)} URLs from specified subdomains")
        
        # Apply max_urls limit
        if max_urls and len(urls_to_crawl) > max_urls:
            urls_to_crawl = urls_to_crawl[:max_urls]
            print(f"\nLimited to first {max_urls} URLs")
        
        print(f"\n🚀 Starting crawl of {len(urls_to_crawl)} URLs...")
        print("=" * 60)
        
        # Crawl URLs directly
        results = await self._crawl_url_list(urls_to_crawl, publisher)
        
        # Add sitemap statistics to results
        results['sitemap_stats'] = sitemap_data['statistics']
        
        return results
    
    async def _crawl_url_list(
        self,
        url_list: List[Dict],
        publisher: PublisherBase
    ) -> Dict[str, any]:
        """
        Crawl a list of URLs directly.
        
        Args:
            url_list: List of URL dictionaries from sitemap
            publisher: Publisher for storing results
            
        Returns:
            Crawl statistics
        """
        stats = {
            "total_urls": len(url_list),
            "successful": 0,
            "failed": 0,
            "skipped": 0,
            "errors": [],
            "start_time": datetime.now(),
            "subdomains_crawled": set()
        }
        
        # Create crawler config for single-page crawling
        config = CrawlerRunConfig(
            scraping_strategy=LXMLWebScrapingStrategy(),
            markdown_generator=DefaultMarkdownGenerator(),
            excluded_tags=self.settings.EXCLUDED_TAGS,
            exclude_external_links=self.settings.EXCLUDE_EXTERNAL_LINKS,
            exclude_social_media_links=self.settings.EXCLUDE_SOCIAL_MEDIA_LINKS,
            page_timeout=120000,
            wait_until="domcontentloaded",  # Faster than networkidle for single pages
            verbose=False
        )
        
        # Track already seen URLs in this session
        session_seen_urls = set()
        duplicates_in_batch = 0
        
        # Get already processed URLs from publisher if available
        already_processed = set()
        if hasattr(publisher, 'processed_urls'):
            already_processed = publisher.processed_urls.copy()
            if already_processed:
                print(f"📌 Found {len(already_processed)} previously processed URLs to skip")
        
        async with self.crawler as crawler:
            actual_processed = 0
            for i, url_data in enumerate(url_list, 1):
                url = url_data['loc']
                
                # Skip if already processed in previous sessions
                if url in already_processed:
                    stats["skipped"] += 1
                    duplicates_in_batch += 1
                    self.duplicate_count += 1
                    continue
                
                # Skip if we've already seen this URL in this session
                if url in session_seen_urls:
                    stats["skipped"] += 1
                    duplicates_in_batch += 1
                    self.duplicate_count += 1  # Update crawler's duplicate count
                    continue
                
                session_seen_urls.add(url)
                actual_processed += 1
                
                # Track subdomain
                domain = urlparse(url).netloc
                stats['subdomains_crawled'].add(domain)
                
                # Progress indicator - show actual processed count
                if (actual_processed > 0 and actual_processed % 10 == 0) or (actual_processed == 1) or (i % 50 == 0):
                    if duplicates_in_batch > 0:
                        print(f"  ⚡ Skipped {duplicates_in_batch} duplicate URLs")
                        duplicates_in_batch = 0
                    if actual_processed > 0:
                        print(f"\n[{actual_processed} new / {i} total] Progress: {i/len(url_list)*100:.1f}%")
                
                try:
                    # Add delay to be respectful
                    if i > 1:  # No delay before first request
                        delay = self.crawl_delay
                        if self.random_delay:
                            delay += random.uniform(0, self.crawl_delay)
                        await asyncio.sleep(delay)
                    
                    # Crawl single URL
                    result = await crawler.arun(url, config=config)
                    
                    if result and result.success:
                        # Process successful result
                        processed = await self._process_crawl_result(result)
                        
                        if processed.get("success"):
                            await publisher.publish_message(processed["data"])
                            stats["successful"] += 1
                            print(f"  ✓ {url[:80]}...")
                        else:
                            stats["failed"] += 1
                            stats["errors"].append({
                                "url": url,
                                "error": processed.get("error", "Processing failed")
                            })
                            print(f"  ✗ {url[:80]}... (processing error)")
                    else:
                        # Crawl failed
                        error_msg = result.error_message if result else "Unknown error"
                        stats["failed"] += 1
                        stats["errors"].append({"url": url, "error": error_msg})
                        
                        # Report to publisher if it has error tracking
                        if hasattr(publisher, 'report_error'):
                            await publisher.report_error(url, error_msg)
                        
                        print(f"  ✗ {url[:80]}... ({error_msg[:50]})")
                        
                except asyncio.TimeoutError:
                    stats["failed"] += 1
                    error_msg = "Timeout - page took too long to load"
                    stats["errors"].append({"url": url, "error": error_msg})
                    if hasattr(publisher, 'report_error'):
                        await publisher.report_error(url, error_msg)
                    print(f"  ⏱️ {url[:80]}... (timeout)")
                    
                except Exception as e:
                    stats["failed"] += 1
                    error_type = type(e).__name__
                    error_msg = f"{error_type}: {str(e)}"
                    stats["errors"].append({"url": url, "error": error_msg})
                    if hasattr(publisher, 'report_error'):
                        await publisher.report_error(url, error_msg)
                    print(f"  ❌ {url[:80]}... ({error_type}: {str(e)[:30]})")
        
        # Report any remaining duplicates
        if duplicates_in_batch > 0:
            print(f"  ⚡ Skipped {duplicates_in_batch} duplicate URLs in final batch")
        
        # Calculate final statistics
        stats["end_time"] = datetime.now()
        stats["duration"] = (stats["end_time"] - stats["start_time"]).total_seconds()
        stats["subdomains_crawled"] = list(stats["subdomains_crawled"])
        
        # Add duplicate info to stats
        stats["duplicates_skipped"] = self.duplicate_count
        
        # Print summary
        print("\n" + "=" * 60)
        print("CRAWL COMPLETE")
        print("=" * 60)
        print(f"Total URLs in list: {stats['total_urls']}")
        if stats['skipped'] > 0:
            print(f"Skipped (already processed): {stats['skipped']}")
            print(f"New URLs crawled: {stats['successful'] + stats['failed']}")
        print(f"Successful: {stats['successful']}")
        print(f"Failed: {stats['failed']}")
        print(f"Duration: {stats['duration']:.1f} seconds")
        if stats['successful'] > 0:
            print(f"Average time per new URL: {stats['duration']/max(1, stats['successful']):.2f} seconds")
        print(f"Unique domains crawled: {len(stats['subdomains_crawled'])}")
        
        # Print error summary if there are errors
        if stats['failed'] > 0:
            print("\n📊 Error Summary:")
            error_types = {}
            for error in stats['errors']:
                error_type = error['error'].split(':')[0] if ':' in error['error'] else 'Unknown'
                error_types[error_type] = error_types.get(error_type, 0) + 1
            
            for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {error_type}: {count}")
        
        return stats
    
    async def crawl_urls(self, urls: List[Dict], allowed_domains: List[str]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Crawl a list of URLs and yield results.
        
        This method is used by the orchestrator to crawl URLs from sitemaps.
        
        Args:
            urls: List of URL dictionaries from sitemap parsing
            allowed_domains: List of allowed domains
            
        Yields:
            Dictionary with crawl results including HTML for subdomain extraction
        """
        # Create crawler config for single-page crawling
        config = CrawlerRunConfig(
            scraping_strategy=LXMLWebScrapingStrategy(),
            markdown_generator=DefaultMarkdownGenerator(),
            wait_until="networkidle",
            page_timeout=120000,  # 2 minutes timeout
            stream=False  # Single page crawl
        )
        
        async with self.crawler as crawler:
            for url_data in urls:
                url = url_data['loc'] if isinstance(url_data, dict) else url_data
                
                try:
                    # Add delay for respectful crawling
                    if self.crawl_delay > 0:
                        await asyncio.sleep(self.crawl_delay)
                    
                    # Crawl single URL
                    result = await crawler.arun(url, config=config)
                    
                    if result and result.success:
                        # Process and yield result with HTML
                        processed = await self._process_crawl_result(result)
                        yield processed
                    else:
                        # Yield error result
                        yield {
                            "success": False,
                            "url": url,
                            "error": result.error_message if result else "Unknown error"
                        }
                        
                except asyncio.TimeoutError:
                    # Yield timeout error
                    yield {
                        "success": False,
                        "url": url,
                        "error": "Timeout - page took too long to load"
                    }
                    
                except Exception as e:
                    # Yield exception as error with type information
                    error_type = type(e).__name__
                    yield {
                        "success": False,
                        "url": url,
                        "error": f"{error_type}: {str(e)}"
                    }


async def discover_subdomains(base_url: str) -> Dict[str, any]:
    """
    Discover all subdomains from a website's sitemaps.
    
    Args:
        base_url: Base URL of the website
        
    Returns:
        Dictionary with subdomain information
    """
    print(f"\n🔍 Discovering subdomains for {base_url}...")
    
    parser = SitemapParser(base_url, include_subdomains=True)
    sitemap_data = await parser.parse_all_sitemaps()
    
    if not sitemap_data['urls']:
        print("No sitemaps found or no URLs in sitemaps")
        return {"subdomains": [], "error": "No sitemaps found"}
    
    # Create detailed subdomain report
    base_domain = urlparse(base_url).netloc
    subdomain_info = {}
    
    for subdomain in sitemap_data['subdomains']:
        full_domain = f"{subdomain}.{base_domain}"
        subdomain_info[subdomain] = {
            "full_domain": full_domain,
            "url_count": sitemap_data['statistics']['urls_by_domain'].get(full_domain, 0),
            "sample_urls": []
        }
        
        # Get sample URLs for this subdomain
        for url_data in sitemap_data['urls'][:1000]:  # Check first 1000 for samples
            if urlparse(url_data['loc']).netloc == full_domain:
                subdomain_info[subdomain]["sample_urls"].append(url_data['loc'])
                if len(subdomain_info[subdomain]["sample_urls"]) >= 3:
                    break
    
    # Print report
    print("\n" + "=" * 60)
    print("SUBDOMAIN DISCOVERY REPORT")
    print("=" * 60)
    print(f"Base domain: {base_domain}")
    print(f"Total subdomains found: {len(subdomain_info)}")
    print(f"Total URLs across all domains: {sitemap_data['statistics']['total_urls']}")
    
    print("\n📍 Subdomains by URL count:")
    sorted_subdomains = sorted(
        subdomain_info.items(),
        key=lambda x: x[1]['url_count'],
        reverse=True
    )
    
    for subdomain, info in sorted_subdomains[:20]:
        print(f"\n• {info['full_domain']} ({info['url_count']} URLs)")
        for sample_url in info['sample_urls'][:2]:
            print(f"  - {sample_url[:100]}...")
    
    if len(sorted_subdomains) > 20:
        print(f"\n... and {len(sorted_subdomains) - 20} more subdomains")
    
    return {
        "base_domain": base_domain,
        "subdomains": subdomain_info,
        "total_subdomains": len(subdomain_info),
        "total_urls": sitemap_data['statistics']['total_urls'],
        "sitemap_urls": parser.sitemap_urls
    }


if __name__ == "__main__":
    import sys
    from publishers.factory import PublisherFactory
    from config.settings import settings
    
    async def main():
        if len(sys.argv) < 2:
            print("Usage:")
            print("  python sitemap_crawler.py discover <url>  # Discover subdomains")
            print("  python sitemap_crawler.py crawl <url> [max_urls]  # Crawl from sitemap")
            print("  python sitemap_crawler.py crawl-subdomain <url> <subdomain> [max_urls]")
            return
        
        command = sys.argv[1]
        base_url = sys.argv[2] if len(sys.argv) > 2 else "https://www.fau.de"
        
        if command == "discover":
            # Discover subdomains
            await discover_subdomains(base_url)
            
        elif command == "crawl":
            # Crawl from sitemap
            max_urls = int(sys.argv[3]) if len(sys.argv) > 3 else 100
            
            # Setup crawler and publisher
            crawler = SitemapCrawler(settings)
            publisher = PublisherFactory.create_publisher(settings)
            
            try:
                await publisher.connect()
                results = await crawler.crawl_from_sitemap(
                    base_url,
                    publisher,
                    include_subdomains=True,
                    max_urls=max_urls
                )
                print(f"\nResults saved to: {settings.STORAGE_PATH}")
            finally:
                await publisher.close()
                
        elif command == "crawl-subdomain":
            # Crawl specific subdomain
            subdomain = sys.argv[3] if len(sys.argv) > 3 else None
            max_urls = int(sys.argv[4]) if len(sys.argv) > 4 else 100
            
            if not subdomain:
                print("Please specify a subdomain")
                return
            
            crawler = SitemapCrawler(settings)
            publisher = PublisherFactory.create_publisher(settings)
            
            try:
                await publisher.connect()
                results = await crawler.crawl_from_sitemap(
                    base_url,
                    publisher,
                    include_subdomains=True,
                    max_urls=max_urls,
                    subdomain_filter=[subdomain]
                )
            finally:
                await publisher.close()
    
    asyncio.run(main())