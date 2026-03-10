#!/usr/bin/env python3
"""
Test script to compare subdomain extraction methods.

This script demonstrates the difference between:
1. Using crawl4ai's built-in link extraction
2. Parsing HTML with BeautifulSoup
"""

import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from core.subdomain_extractor import SubdomainExtractor
import time

async def test_link_extraction():
    """Test and compare link extraction methods."""
    
    test_url = "https://www.fau.de"
    
    print("\n" + "=" * 60)
    print("LINK EXTRACTION COMPARISON TEST")
    print("=" * 60)
    print(f"Test URL: {test_url}")
    print("-" * 60)
    
    # Create crawler
    config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=30000,
        stream=False
    )
    
    async with AsyncWebCrawler() as crawler:
        # Crawl the page
        print("\n📥 Crawling page...")
        start_time = time.time()
        result = await crawler.arun(test_url, config=config)
        crawl_time = time.time() - start_time
        print(f"  ✓ Crawled in {crawl_time:.2f} seconds")
        
        if not result.success:
            print(f"  ❌ Crawl failed: {result.error_message}")
            return
        
        # Create extractor
        extractor = SubdomainExtractor("fau.de")
        
        # Method 1: Using crawl4ai's extracted links
        print("\n🔗 Method 1: Using crawl4ai's extracted links")
        start_time = time.time()
        subdomains_from_links = extractor.extract_from_crawl4ai_links(result.links)
        links_time = time.time() - start_time
        
        print(f"  Time: {links_time:.4f} seconds")
        print(f"  Subdomains found: {len(subdomains_from_links)}")
        if subdomains_from_links:
            for subdomain in sorted(subdomains_from_links)[:10]:
                print(f"    • {subdomain}.fau.de")
        
        # Method 2: Parsing HTML with BeautifulSoup
        print("\n📄 Method 2: Parsing HTML with BeautifulSoup")
        extractor2 = SubdomainExtractor("fau.de")  # Fresh extractor
        start_time = time.time()
        subdomains_from_html = extractor2.extract_from_page(result.html, test_url, links_data=None)
        html_time = time.time() - start_time
        
        print(f"  Time: {html_time:.4f} seconds")
        print(f"  Subdomains found: {len(subdomains_from_html)}")
        if subdomains_from_html:
            for subdomain in sorted(subdomains_from_html)[:10]:
                print(f"    • {subdomain}.fau.de")
        
        # Comparison
        print("\n" + "=" * 60)
        print("COMPARISON RESULTS")
        print("=" * 60)
        
        print(f"crawl4ai links method:")
        print(f"  • Time: {links_time:.4f}s")
        print(f"  • Subdomains: {len(subdomains_from_links)}")
        
        print(f"\nHTML parsing method:")
        print(f"  • Time: {html_time:.4f}s")
        print(f"  • Subdomains: {len(subdomains_from_html)}")
        
        if links_time < html_time:
            speedup = html_time / links_time
            print(f"\n✨ crawl4ai method is {speedup:.1f}x faster!")
        
        # Check for differences
        only_in_links = subdomains_from_links - subdomains_from_html
        only_in_html = subdomains_from_html - subdomains_from_links
        
        if only_in_links:
            print(f"\nFound only by crawl4ai links ({len(only_in_links)}):")
            for subdomain in sorted(only_in_links)[:5]:
                print(f"  • {subdomain}.fau.de")
        
        if only_in_html:
            print(f"\nFound only by HTML parsing ({len(only_in_html)}):")
            for subdomain in sorted(only_in_html)[:5]:
                print(f"  • {subdomain}.fau.de")
        
        # Show link statistics from crawl4ai
        if result.links:
            print(f"\n📊 crawl4ai Link Statistics:")
            if hasattr(result.links, 'internal'):
                print(f"  • Internal links: {len(result.links.internal)}")
            if hasattr(result.links, 'external'):
                print(f"  • External links: {len(result.links.external)}")

if __name__ == "__main__":
    asyncio.run(test_link_extraction())