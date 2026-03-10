#!/usr/bin/env python3
"""
Quick site estimator - A faster, simpler tool to estimate crawl scope.
"""

import asyncio
import time
from typing import Dict, List, Set
from urllib.parse import urlparse, urljoin
import httpx
from bs4 import BeautifulSoup
import random

class QuickSiteEstimator:
    """
    Quickly estimates the size and crawl time of a website.
    """
    
    def __init__(self):
        self.timeout = 10  # Shorter timeout for quick analysis
        
    async def estimate(self, start_url: str, sample_size: int = 3) -> Dict:
        """
        Quickly estimate site size and crawl time.
        
        Args:
            start_url: The starting URL
            sample_size: Number of pages to sample for timing
            
        Returns:
            Dictionary with estimation results
        """
        print(f"\n🚀 Quick Site Estimation for: {start_url}\n")
        
        # Step 1: Get homepage and discover links
        print("1️⃣ Analyzing homepage...")
        homepage_links = await self._get_page_links(start_url)
        print(f"   Found {len(homepage_links)} unique links on homepage")
        
        # Step 2: Sample a few pages to get link density
        print("\n2️⃣ Sampling pages for link density...")
        total_links = len(homepage_links)
        pages_sampled = 1
        sample_times = []
        
        # Sample random pages
        sample_pages = random.sample(list(homepage_links), min(sample_size, len(homepage_links)))
        
        for page_url in sample_pages:
            start_time = time.time()
            page_links = await self._get_page_links(page_url)
            elapsed = time.time() - start_time
            
            if page_links is not None:
                total_links += len(page_links)
                pages_sampled += 1
                sample_times.append(elapsed)
                print(f"   Sampled: {page_url[:50]}... ({len(page_links)} links, {elapsed:.2f}s)")
        
        # Step 3: Estimate total pages
        avg_links_per_page = total_links / pages_sampled if pages_sampled > 0 else 0
        
        # Using a simplified model: total_pages ≈ links_found * dampening_factor
        # The dampening factor accounts for duplicate links and external links
        dampening_factor = 0.3  # Empirical value
        estimated_pages = int(total_links * dampening_factor)
        
        # Step 4: Estimate crawl time
        avg_crawl_time = sum(sample_times) / len(sample_times) if sample_times else 1.0
        estimated_total_time = estimated_pages * avg_crawl_time
        
        results = {
            "start_url": start_url,
            "homepage_links": len(homepage_links),
            "pages_sampled": pages_sampled,
            "average_links_per_page": avg_links_per_page,
            "estimated_total_pages": estimated_pages,
            "average_page_time": avg_crawl_time,
            "estimated_total_time_seconds": estimated_total_time,
            "estimated_total_time_formatted": self._format_time(estimated_total_time)
        }
        
        # Print results
        print("\n" + "="*50)
        print("📊 ESTIMATION RESULTS")
        print("="*50)
        print(f"• Estimated total pages: ~{estimated_pages:,}")
        print(f"• Average crawl time per page: {avg_crawl_time:.2f} seconds")
        print(f"• Estimated total crawl time: {results['estimated_total_time_formatted']}")
        print(f"• Average links per page: {avg_links_per_page:.1f}")
        
        # Recommendations
        print("\n💡 RECOMMENDATIONS:")
        if estimated_pages > 5000:
            print("• ⚠️ Very large site! Consider:")
            print("  - Setting MAX_PAGES limit (e.g., 1000-5000)")
            print("  - Using relevance-based crawling")
            print("  - Running in batches")
        elif estimated_pages > 1000:
            print("• 📚 Large site. Consider:")
            print("  - Setting MAX_PAGES to", min(estimated_pages, 2000))
            print("  - Using BFS strategy for broad coverage")
        else:
            print("• ✅ Manageable size for full crawl")
            print("  - Can use default settings")
        
        if avg_crawl_time > 3:
            print(f"• 🐌 Slow page loads ({avg_crawl_time:.1f}s). Consider increasing timeout")
        
        # Suggested config
        print("\n🔧 SUGGESTED CONFIG:")
        print(f"MAX_PAGES = {min(estimated_pages, 5000)}")
        print(f"MAX_DEPTH = {3 if estimated_pages > 1000 else 5}")
        print(f"STRATEGY = '{'bfs' if estimated_pages > 1000 else 'best_first'}'")
        if avg_crawl_time > 3:
            print(f"PAGE_TIMEOUT = {int((avg_crawl_time + 5) * 1000)}")
        
        return results
    
    async def _get_page_links(self, url: str) -> Set[str]:
        """
        Get all internal links from a page.
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, follow_redirects=True)
                if response.status_code != 200:
                    return set()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                base_domain = urlparse(url).netloc
                
                links = set()
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(url, link['href'])
                    parsed = urlparse(full_url)
                    
                    # Only internal links
                    if parsed.netloc == base_domain:
                        # Remove fragment and normalize
                        clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                        if parsed.query:
                            clean_url += f"?{parsed.query}"
                        links.add(clean_url)
                
                return links
        except Exception as e:
            print(f"   ⚠️ Error fetching {url[:50]}...: {str(e)[:50]}")
            return set()
    
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
    """Run the quick estimator."""
    import sys
    
    # Get URL from command line or use default
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://www.fau.de"
    
    estimator = QuickSiteEstimator()
    results = await estimator.estimate(url, sample_size=3)
    
    return results


if __name__ == "__main__":
    asyncio.run(main())