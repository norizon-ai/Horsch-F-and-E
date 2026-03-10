import asyncio
import time
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse, urljoin
import httpx
import xml.etree.ElementTree as ET
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from bs4 import BeautifulSoup
import re
from collections import deque
import random

class SiteAnalyzer:
    """
    Analyzes a website to estimate crawl time and discover number of pages
    without performing a full crawl.
    """
    
    def __init__(self, max_sample_pages: int = 10, timeout: int = 30):
        """
        Initialize the site analyzer.
        
        Args:
            max_sample_pages: Maximum number of pages to sample for time estimation
            timeout: Timeout in seconds for each page request
        """
        self.max_sample_pages = max_sample_pages
        self.timeout = timeout
        self.discovered_urls: Set[str] = set()
        self.sitemap_urls: Set[str] = set()
        
    async def analyze(self, start_url: str, allowed_domains: Optional[List[str]] = None) -> Dict:
        """
        Analyze a website to estimate crawl scope and time.
        
        Args:
            start_url: The starting URL to analyze
            allowed_domains: List of domains to restrict analysis to
            
        Returns:
            Dictionary containing analysis results
        """
        print(f"🔍 Analyzing site: {start_url}")
        
        if allowed_domains is None:
            parsed = urlparse(start_url)
            allowed_domains = [parsed.netloc]
        
        results = {
            "start_url": start_url,
            "allowed_domains": allowed_domains,
            "sitemap_found": False,
            "sitemap_url_count": 0,
            "discovered_url_count": 0,
            "estimated_total_pages": 0,
            "sample_crawl_times": [],
            "average_page_time": 0,
            "estimated_total_time": 0,
            "page_size_stats": {
                "min": 0,
                "max": 0,
                "average": 0
            },
            "recommendations": []
        }
        
        # Step 1: Try to find and parse sitemap
        print("\n📋 Step 1: Checking for sitemap...")
        sitemap_urls = await self._find_sitemap_urls(start_url)
        if sitemap_urls:
            results["sitemap_found"] = True
            results["sitemap_url_count"] = len(sitemap_urls)
            self.sitemap_urls = sitemap_urls
            print(f"  ✓ Found {len(sitemap_urls)} URLs in sitemap")
        else:
            print("  ✗ No sitemap found")
        
        # Step 2: Quick BFS discovery to estimate page count
        print("\n🌐 Step 2: Quick page discovery...")
        discovered_urls = await self._quick_discovery(start_url, allowed_domains, max_pages=50)
        self.discovered_urls = discovered_urls
        results["discovered_url_count"] = len(discovered_urls)
        print(f"  ✓ Discovered {len(discovered_urls)} unique URLs through crawling")
        
        # Step 3: Estimate total pages
        print("\n📊 Step 3: Estimating total pages...")
        results["estimated_total_pages"] = self._estimate_total_pages()
        print(f"  ✓ Estimated total pages: {results['estimated_total_pages']}")
        
        # Step 4: Sample crawl for time estimation
        print("\n⏱️  Step 4: Sampling pages for time estimation...")
        sample_results = await self._sample_crawl(list(discovered_urls)[:self.max_sample_pages])
        
        if sample_results["times"]:
            results["sample_crawl_times"] = sample_results["times"]
            results["average_page_time"] = sum(sample_results["times"]) / len(sample_results["times"])
            results["estimated_total_time"] = results["average_page_time"] * results["estimated_total_pages"]
            results["page_size_stats"] = sample_results["size_stats"]
            
            print(f"  ✓ Average page crawl time: {results['average_page_time']:.2f} seconds")
            print(f"  ✓ Average page size: {results['page_size_stats']['average'] / 1024:.1f} KB")
        
        # Step 5: Generate recommendations
        results["recommendations"] = self._generate_recommendations(results)
        
        return results
    
    async def _find_sitemap_urls(self, base_url: str) -> Set[str]:
        """
        Try to find and parse sitemap.xml to get all URLs.
        """
        sitemap_urls = set()
        possible_paths = [
            "/sitemap.xml",
            "/sitemap_index.xml",
            "/sitemap.xml.gz",
            "/sitemap",
            "/sitemap.txt"
        ]
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            # Try robots.txt first
            try:
                robots_url = urljoin(base_url, "/robots.txt")
                response = await client.get(robots_url)
                if response.status_code == 200:
                    for line in response.text.split('\n'):
                        if line.lower().startswith('sitemap:'):
                            sitemap_url = line.split(':', 1)[1].strip()
                            sitemap_urls.update(await self._parse_sitemap(sitemap_url, client))
            except Exception as e:
                print(f"    Could not fetch robots.txt: {e}")
            
            # Try common sitemap paths
            if not sitemap_urls:
                for path in possible_paths:
                    try:
                        sitemap_url = urljoin(base_url, path)
                        response = await client.get(sitemap_url)
                        if response.status_code == 200:
                            sitemap_urls.update(await self._parse_sitemap(sitemap_url, client))
                            if sitemap_urls:
                                break
                    except Exception:
                        continue
        
        return sitemap_urls
    
    async def _parse_sitemap(self, sitemap_url: str, client: httpx.AsyncClient) -> Set[str]:
        """
        Parse a sitemap XML file to extract URLs.
        """
        urls = set()
        try:
            response = await client.get(sitemap_url)
            if response.status_code != 200:
                return urls
            
            # Parse XML
            root = ET.fromstring(response.content)
            
            # Handle sitemap index
            if 'sitemapindex' in root.tag:
                for sitemap in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'):
                    loc = sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc is not None:
                        child_urls = await self._parse_sitemap(loc.text, client)
                        urls.update(child_urls)
            else:
                # Regular sitemap
                for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc is not None:
                        urls.add(loc.text)
        except Exception as e:
            print(f"    Error parsing sitemap {sitemap_url}: {e}")
        
        return urls
    
    async def _quick_discovery(self, start_url: str, allowed_domains: List[str], 
                              max_pages: int = 50) -> Set[str]:
        """
        Perform a quick BFS crawl to discover URLs without full content extraction.
        """
        discovered = set()
        to_visit = deque([start_url])
        visited = set()
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            while to_visit and len(discovered) < max_pages:
                url = to_visit.popleft()
                if url in visited:
                    continue
                
                visited.add(url)
                
                try:
                    response = await client.get(url, follow_redirects=True)
                    if response.status_code != 200:
                        continue
                    
                    discovered.add(url)
                    
                    # Parse for more URLs
                    soup = BeautifulSoup(response.text, 'html.parser')
                    for link in soup.find_all('a', href=True):
                        full_url = urljoin(url, link['href'])
                        parsed = urlparse(full_url)
                        
                        # Check if URL is in allowed domains
                        if parsed.netloc in allowed_domains:
                            # Remove fragment and normalize
                            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                            if parsed.query:
                                clean_url += f"?{parsed.query}"
                            
                            if clean_url not in visited and clean_url not in discovered:
                                to_visit.append(clean_url)
                    
                except Exception as e:
                    print(f"    Error discovering {url}: {e}")
        
        return discovered
    
    async def _sample_crawl(self, sample_urls: List[str]) -> Dict:
        """
        Crawl a sample of pages to estimate average crawl time and page sizes.
        """
        times = []
        sizes = []
        
        # Use crawl4ai for more accurate time estimation
        crawler = AsyncWebCrawler(playwright_mode=False)
        config = CrawlerRunConfig(
            scraping_strategy=LXMLWebScrapingStrategy(),
            page_timeout=self.timeout * 1000,  # Convert to milliseconds
            verbose=False
        )
        
        async with crawler:
            for url in sample_urls:
                try:
                    start_time = time.time()
                    result = await crawler.arun(url, config=config)
                    elapsed = time.time() - start_time
                    
                    if result.success:
                        times.append(elapsed)
                        # Estimate content size
                        content_size = len(result.html.encode('utf-8')) if result.html else 0
                        sizes.append(content_size)
                        print(f"    Sampled {url}: {elapsed:.2f}s, {content_size/1024:.1f}KB")
                except Exception as e:
                    print(f"    Error sampling {url}: {e}")
        
        size_stats = {
            "min": min(sizes) if sizes else 0,
            "max": max(sizes) if sizes else 0,
            "average": sum(sizes) / len(sizes) if sizes else 0
        }
        
        return {
            "times": times,
            "size_stats": size_stats
        }
    
    def _estimate_total_pages(self) -> int:
        """
        Estimate total number of pages based on sitemap and discovery.
        """
        if self.sitemap_urls:
            # If we have a sitemap, use it as the primary source
            return len(self.sitemap_urls)
        elif self.discovered_urls:
            # Estimate based on discovery pattern
            # This is a heuristic: if we found N pages in quick discovery,
            # the total might be 2-10x more depending on site structure
            discovered_count = len(self.discovered_urls)
            
            # Conservative estimate: 3x the discovered pages
            return discovered_count * 3
        else:
            return 0
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """
        Generate recommendations based on the analysis.
        """
        recommendations = []
        
        # Time-based recommendations
        total_hours = results["estimated_total_time"] / 3600
        if total_hours > 24:
            recommendations.append(
                f"⚠️ Large crawl: Estimated {total_hours:.1f} hours. Consider:"
                f"\n     - Breaking into smaller batches"
                f"\n     - Using multiple parallel crawlers"
                f"\n     - Implementing checkpointing for resume capability"
            )
        elif total_hours > 1:
            recommendations.append(
                f"ℹ️ Medium crawl: Estimated {total_hours:.1f} hours. "
                f"Consider running during off-peak hours."
            )
        
        # Page count recommendations
        if results["estimated_total_pages"] > 10000:
            recommendations.append(
                "📚 Very large site (>10k pages). Recommendations:"
                "\n     - Use database storage instead of memory"
                "\n     - Implement rate limiting to avoid overloading server"
                "\n     - Consider using BFS strategy for breadth coverage"
            )
        elif results["estimated_total_pages"] > 1000:
            recommendations.append(
                "📄 Large site (>1k pages). Consider:"
                "\n     - Setting appropriate MAX_PAGES limit"
                "\n     - Using relevance scoring for priority crawling"
            )
        
        # Performance recommendations
        avg_time = results.get("average_page_time", 0)
        if avg_time > 5:
            recommendations.append(
                f"🐌 Slow page loads ({avg_time:.1f}s average). Consider:"
                f"\n     - Increasing page timeout"
                f"\n     - Using simpler scraping strategy"
                f"\n     - Checking if site has rate limiting"
            )
        
        # Sitemap recommendations
        if not results["sitemap_found"]:
            recommendations.append(
                "🗺️ No sitemap found. The estimate may be less accurate. "
                "Consider manual URL list if available."
            )
        
        return recommendations

def format_time(seconds: float) -> str:
    """
    Format seconds into human-readable time.
    """
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.1f} minutes"
    else:
        hours = seconds / 3600
        if hours < 24:
            return f"{hours:.1f} hours"
        else:
            return f"{hours/24:.1f} days"

async def main():
    """
    Example usage of the SiteAnalyzer.
    """
    # Example: Analyze FAU website
    analyzer = SiteAnalyzer(max_sample_pages=5)
    
    start_url = "https://www.fau.de"
    allowed_domains = ["fau.de", "www.fau.de"]
    
    print("=" * 60)
    print("WEBSITE CRAWL ANALYZER")
    print("=" * 60)
    
    results = await analyzer.analyze(start_url, allowed_domains)
    
    # Print formatted results
    print("\n" + "=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)
    
    print(f"\n📊 Site Statistics:")
    print(f"  • Sitemap found: {'Yes' if results['sitemap_found'] else 'No'}")
    if results['sitemap_found']:
        print(f"  • URLs in sitemap: {results['sitemap_url_count']}")
    print(f"  • URLs discovered (sample): {results['discovered_url_count']}")
    print(f"  • Estimated total pages: {results['estimated_total_pages']}")
    
    print(f"\n⏱️ Time Estimates:")
    print(f"  • Average page crawl time: {results['average_page_time']:.2f} seconds")
    print(f"  • Estimated total time: {format_time(results['estimated_total_time'])}")
    
    print(f"\n💾 Page Size Statistics:")
    stats = results['page_size_stats']
    print(f"  • Min: {stats['min']/1024:.1f} KB")
    print(f"  • Max: {stats['max']/1024:.1f} KB")
    print(f"  • Average: {stats['average']/1024:.1f} KB")
    print(f"  • Estimated total data: {(stats['average'] * results['estimated_total_pages']) / (1024*1024):.1f} MB")
    
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"\n{rec}")
    
    print("\n" + "=" * 60)
    
    # Calculate crawler settings
    print("\n🔧 Suggested Crawler Settings:")
    print(f"  MAX_PAGES = {min(results['estimated_total_pages'], 10000)}")
    if results['average_page_time'] > 3:
        print(f"  PAGE_TIMEOUT = {int((results['average_page_time'] + 10) * 1000)}")
    if results['estimated_total_pages'] > 1000:
        print(f"  STRATEGY = 'bfs'  # For large sites")
    else:
        print(f"  STRATEGY = 'best_first'  # For focused crawling")
    
    return results

if __name__ == "__main__":
    asyncio.run(main())