#!/usr/bin/env python3
"""
Crawl estimator integrated with the existing crawler configuration.
Uses the actual crawler to get more accurate estimates.
"""

import asyncio
import time
from typing import Dict, List, Optional
from config.settings import CrawlerSettings
from core.crawler import IntranetCrawler
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, DomainFilter

class CrawlEstimator:
    """
    Estimates crawl time and scope using the actual crawler with limited depth/pages.
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None):
        """
        Initialize the estimator with crawler settings.
        
        Args:
            settings: Crawler settings (uses defaults if not provided)
        """
        self.settings = settings or CrawlerSettings()
        
    async def estimate(self, start_url: str, allowed_domains: List[str]) -> Dict:
        """
        Estimate crawl scope and time by doing a limited test crawl.
        
        Args:
            start_url: Starting URL for the crawl
            allowed_domains: List of allowed domains
            
        Returns:
            Dictionary with estimation results
        """
        print(f"\n🔬 Crawl Estimation for: {start_url}")
        print(f"   Allowed domains: {', '.join(allowed_domains)}")
        print("\n📊 Running test crawl (depth=1, max_pages=10)...")
        
        # Create a test configuration with limited scope
        test_settings = CrawlerSettings(
            STRATEGY="bfs",  # BFS gives better overview
            MAX_DEPTH=1,     # Only go 1 level deep
            MAX_PAGES=10,    # Sample up to 10 pages
            USE_PLAYWRIGHT=self.settings.USE_PLAYWRIGHT
        )
        
        # Run test crawl
        test_crawler = IntranetCrawler(settings=test_settings)
        
        crawled_pages = []
        page_times = []
        discovered_urls = set()
        
        start_time = time.time()
        
        try:
            async for page_data in test_crawler.crawl(start_url, allowed_domains):
                page_start = time.time()
                crawled_pages.append(page_data)
                
                # Extract URLs mentioned in content
                if page_data.content:
                    import re
                    # Simple URL extraction from markdown
                    url_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
                    matches = re.findall(url_pattern, page_data.content)
                    for _, url in matches:
                        if any(domain in url for domain in allowed_domains):
                            discovered_urls.add(url)
                
                page_time = time.time() - page_start
                page_times.append(page_time)
                
                print(f"   ✓ Crawled: {page_data.source.uri[:60]}... ({len(page_data.content)} chars, {page_time:.2f}s)")
        
        except Exception as e:
            print(f"   ⚠️ Error during test crawl: {e}")
        
        total_test_time = time.time() - start_time
        
        # Calculate estimates
        pages_crawled = len(crawled_pages)
        avg_page_time = sum(page_times) / len(page_times) if page_times else 1.0
        
        # Estimate total pages based on discovery rate
        # If we found N new URLs at depth 1, estimate exponential growth
        links_per_page = len(discovered_urls) / pages_crawled if pages_crawled > 0 else 0
        
        # Estimate based on configured max_depth
        estimated_pages = self._estimate_total_pages(
            pages_at_depth_1=pages_crawled,
            links_per_page=links_per_page,
            max_depth=self.settings.MAX_DEPTH
        )
        
        # Apply MAX_PAGES limit
        estimated_pages = min(estimated_pages, self.settings.MAX_PAGES)
        
        # Calculate time estimates
        estimated_total_time = estimated_pages * avg_page_time
        
        # Calculate data size estimates
        total_content_size = sum(len(p.content) for p in crawled_pages)
        avg_content_size = total_content_size / pages_crawled if pages_crawled > 0 else 0
        estimated_total_size = avg_content_size * estimated_pages
        
        results = {
            "start_url": start_url,
            "test_pages_crawled": pages_crawled,
            "test_time": total_test_time,
            "discovered_urls": len(discovered_urls),
            "average_page_time": avg_page_time,
            "average_content_size": avg_content_size,
            "estimated_total_pages": estimated_pages,
            "estimated_total_time": estimated_total_time,
            "estimated_total_size": estimated_total_size,
            "current_settings": {
                "MAX_DEPTH": self.settings.MAX_DEPTH,
                "MAX_PAGES": self.settings.MAX_PAGES,
                "STRATEGY": self.settings.STRATEGY,
                "USE_PLAYWRIGHT": self.settings.USE_PLAYWRIGHT
            }
        }
        
        # Print results
        self._print_results(results)
        
        return results
    
    def _estimate_total_pages(self, pages_at_depth_1: int, links_per_page: float, max_depth: int) -> int:
        """
        Estimate total pages based on branching factor and depth.
        
        Uses a dampened exponential model since not all links lead to new pages.
        """
        if pages_at_depth_1 == 0:
            return 0
        
        # Dampening factor for each level (pages overlap, external links, etc.)
        dampening = 0.5
        
        total = pages_at_depth_1
        current_level_pages = pages_at_depth_1
        
        for depth in range(2, max_depth + 1):
            # Estimate pages at this depth
            new_pages = current_level_pages * links_per_page * dampening
            total += new_pages
            current_level_pages = new_pages
            
            # Further dampen for deeper levels
            dampening *= 0.7
        
        return int(total)
    
    def _print_results(self, results: Dict):
        """Print formatted estimation results."""
        print("\n" + "="*60)
        print("📈 CRAWL ESTIMATION RESULTS")
        print("="*60)
        
        print(f"\n🔍 Test Crawl Results:")
        print(f"  • Pages crawled: {results['test_pages_crawled']}")
        print(f"  • Test duration: {results['test_time']:.2f} seconds")
        print(f"  • URLs discovered: {results['discovered_urls']}")
        print(f"  • Avg page time: {results['average_page_time']:.2f} seconds")
        print(f"  • Avg content size: {results['average_content_size']/1024:.1f} KB")
        
        print(f"\n📊 Full Crawl Estimates:")
        print(f"  • Estimated total pages: {results['estimated_total_pages']:,}")
        print(f"  • Estimated time: {self._format_time(results['estimated_total_time'])}")
        print(f"  • Estimated data size: {results['estimated_total_size']/(1024*1024):.1f} MB")
        
        print(f"\n⚙️ Current Settings:")
        for key, value in results['current_settings'].items():
            print(f"  • {key}: {value}")
        
        # Recommendations
        print(f"\n💡 Recommendations:")
        
        total_hours = results['estimated_total_time'] / 3600
        if total_hours > 24:
            print(f"  ⚠️ Very long crawl ({total_hours:.1f} hours)!")
            print(f"     - Consider reducing MAX_PAGES or MAX_DEPTH")
            print(f"     - Run in batches with checkpointing")
            print(f"     - Use multiple parallel crawlers")
        elif total_hours > 1:
            print(f"  ℹ️ Long crawl ({total_hours:.1f} hours)")
            print(f"     - Run during off-peak hours")
            print(f"     - Monitor progress with verbose=True")
        else:
            print(f"  ✅ Reasonable crawl time ({results['estimated_total_time']/60:.1f} minutes)")
        
        if results['average_page_time'] > 5:
            print(f"  🐌 Slow page loads detected")
            print(f"     - Consider increasing page_timeout")
            print(f"     - Check if site has rate limiting")
            print(f"     - Try USE_PLAYWRIGHT=False for faster crawling")
        
        if results['estimated_total_pages'] > 5000:
            print(f"  📚 Large number of pages")
            print(f"     - Use BFS strategy for breadth")
            print(f"     - Implement relevance scoring")
            print(f"     - Consider domain/path filtering")
    
    def _format_time(self, seconds: float) -> str:
        """Format seconds into human-readable time."""
        if seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        else:
            return f"{seconds/86400:.1f} days"


async def main():
    """Example usage of the CrawlEstimator."""
    import sys
    from config import settings
    
    # Get URL from command line or use default
    if len(sys.argv) > 1:
        start_url = sys.argv[1]
        # Extract domain from URL
        from urllib.parse import urlparse
        parsed = urlparse(start_url)
        allowed_domains = [parsed.netloc]
        
        # Add www variant if not present
        if not parsed.netloc.startswith('www.'):
            allowed_domains.append(f"www.{parsed.netloc}")
        else:
            allowed_domains.append(parsed.netloc.replace('www.', ''))
    else:
        start_url = "https://www.fau.de"
        allowed_domains = ["fau.de", "www.fau.de"]
    
    print(f"🌐 Estimating crawl for: {start_url}")
    print(f"🔒 Allowed domains: {allowed_domains}")
    
    # Create estimator with current settings
    estimator = CrawlEstimator(settings=settings)
    
    # Run estimation
    results = await estimator.estimate(start_url, allowed_domains)
    
    return results


if __name__ == "__main__":
    asyncio.run(main())