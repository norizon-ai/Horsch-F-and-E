#!/usr/bin/env python3
"""
Test subdomain discovery from deeper pages in sitemap.
"""

import asyncio
from core.sitemap_crawler import SitemapCrawler, SitemapParser
from core.subdomain_extractor import SubdomainExtractor
from config.settings import CrawlerSettings

async def test_deep_pages():
    """Test subdomain extraction from deeper pages in the sitemap."""
    
    print("\n" + "=" * 60)
    print("TESTING SUBDOMAIN DISCOVERY FROM DEEP PAGES")
    print("=" * 60)
    
    # Get some deeper URLs from the sitemap
    parser = SitemapParser("https://www.fau.de", include_subdomains=False)
    sitemap_data = await parser.parse_all_sitemaps()
    
    # Skip the first 100 URLs (usually main navigation pages) and take 5 deeper ones
    deep_urls = sitemap_data['urls'][100:105]
    
    print(f"\nTesting {len(deep_urls)} deeper pages from sitemap:")
    for i, url_data in enumerate(deep_urls, 1):
        print(f"  {i}. {url_data['loc'][:80]}...")
    
    # Create crawler and extractor
    settings = CrawlerSettings(USE_STREAMING=False)
    crawler = SitemapCrawler(settings)
    extractor = SubdomainExtractor('fau.de')
    
    # Track all discovered subdomains
    all_subdomains = set()
    
    print("\n" + "-" * 40)
    print("Crawling pages and extracting subdomains...")
    print("-" * 40)
    
    # Crawl each URL
    async for result in crawler.crawl_urls(deep_urls, ['www.fau.de']):
        if result.get('success'):
            url = result['url']
            print(f"\n📄 Page: {url[:80]}...")
            
            # Extract subdomains from links
            if result.get('links'):
                subdomains = extractor.extract_from_crawl4ai_links(result['links'])
                if subdomains:
                    print(f"  ✓ Found {len(subdomains)} subdomains:")
                    for subdomain in sorted(subdomains):
                        print(f"    • {subdomain}.fau.de")
                        all_subdomains.add(subdomain)
                else:
                    print(f"  - No subdomains found in links")
            else:
                print(f"  ⚠ No links data available")
                
            # Also check HTML as fallback
            if not result.get('links') and result.get('html'):
                subdomains = extractor.extract_from_page(result['html'], url)
                if subdomains:
                    print(f"  ✓ Found {len(subdomains)} subdomains via HTML parsing:")
                    for subdomain in sorted(subdomains):
                        print(f"    • {subdomain}.fau.de")
                        all_subdomains.add(subdomain)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total unique subdomains found: {len(all_subdomains)}")
    if all_subdomains:
        print("\nAll discovered subdomains:")
        for subdomain in sorted(all_subdomains):
            print(f"  • {subdomain}.fau.de")
    else:
        print("\n⚠ No subdomains found in deep pages")
        print("This is normal if the deep pages don't link to subdomains.")

if __name__ == "__main__":
    asyncio.run(test_deep_pages())