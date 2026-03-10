#!/usr/bin/env python3
"""
Test subdomain discovery in sitemap mode.
"""

import asyncio
from core.orchestrator import CrawlOrchestrator
from config.settings import CrawlerSettings
from publishing.file_storage_publisher import FileStoragePublisher

async def test_sitemap_subdomain_discovery():
    """Test that subdomains are discovered when crawling via sitemap."""
    
    print("\n" + "=" * 60)
    print("TESTING SUBDOMAIN DISCOVERY IN SITEMAP MODE")
    print("=" * 60)
    
    # Configure for limited sitemap crawl
    settings = CrawlerSettings(
        USE_SITEMAP=True,
        MAX_PAGES=5,  # Only crawl 5 pages to test quickly
        STORAGE_PATH="./test_sitemap_subdomains",
        USE_STREAMING=False  # Disable streaming for simpler testing
    )
    
    # Create orchestrator
    orchestrator = CrawlOrchestrator(settings, "https://www.fau.de")
    
    # Create publisher
    publisher = FileStoragePublisher(settings.STORAGE_PATH, batch_size=5)
    
    # Run limited crawl
    print("\nStarting crawl (limited to 5 pages from sitemap)...")
    stats = await orchestrator.orchestrate_comprehensive_crawl(
        publisher=publisher,
        max_subdomains=0  # Don't crawl discovered subdomains, just discover them
    )
    
    # Show discovered subdomains
    discovered = orchestrator.get_discovered_subdomains()
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Pages crawled: {stats['total_pages']}")
    print(f"Subdomains discovered: {len(discovered)}")
    
    if discovered:
        print("\nDiscovered subdomains:")
        for subdomain in sorted(discovered):
            print(f"  • {subdomain}")
    else:
        print("\n❌ No subdomains discovered!")
        print("This indicates the subdomain extraction is not working in sitemap mode.")
    
    # Check if we're getting links data
    print("\n" + "-" * 40)
    print("Debug: Checking if links are being extracted...")
    
    # Try crawling one page directly to see what we get
    from core.sitemap_crawler import SitemapCrawler
    crawler = SitemapCrawler(settings)
    
    test_urls = [{'loc': 'https://www.fau.de'}]
    print(f"Crawling {test_urls[0]['loc']} directly...")
    
    async for result in crawler.crawl_urls(test_urls, ['www.fau.de']):
        if result.get('success'):
            print(f"  ✓ Page crawled successfully")
            print(f"  • Has HTML: {bool(result.get('html'))}")
            print(f"  • Has links: {bool(result.get('links'))}")
            if result.get('links'):
                links = result['links']
                if isinstance(links, dict):
                    print(f"  • Internal links: {len(links.get('internal', []))}")
                    print(f"  • External links: {len(links.get('external', []))}")
                    
                    # Check for subdomains in links
                    from core.subdomain_extractor import SubdomainExtractor
                    extractor = SubdomainExtractor('fau.de')
                    subdomains = extractor.extract_from_crawl4ai_links(links)
                    print(f"  • Subdomains in links: {len(subdomains)}")
                    if subdomains:
                        for s in sorted(subdomains)[:5]:
                            print(f"    - {s}.fau.de")
        else:
            print(f"  ❌ Failed to crawl: {result.get('error')}")

if __name__ == "__main__":
    asyncio.run(test_sitemap_subdomain_discovery())