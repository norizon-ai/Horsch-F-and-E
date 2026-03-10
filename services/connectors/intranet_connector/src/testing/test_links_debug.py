#!/usr/bin/env python3
"""Debug script to see what crawl4ai returns in result.links"""

import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
import json

async def debug_links():
    test_url = "https://www.fau.de"
    
    config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=30000,
        stream=False
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(test_url, config=config)
        
        if result.success:
            print("=" * 60)
            print("DEBUGGING result.links")
            print("=" * 60)
            
            # Check type
            print(f"\nType of result.links: {type(result.links)}")
            print(f"result.links is None: {result.links is None}")
            
            if result.links:
                # Check attributes
                print(f"\nAttributes of result.links:")
                for attr in dir(result.links):
                    if not attr.startswith('_'):
                        print(f"  • {attr}")
                
                # Try to access internal/external
                if hasattr(result.links, 'internal'):
                    print(f"\nInternal links count: {len(result.links.internal)}")
                    if result.links.internal:
                        print("First 3 internal links:")
                        for i, link in enumerate(result.links.internal[:3]):
                            print(f"  {i+1}. Type: {type(link)}")
                            if hasattr(link, 'href'):
                                print(f"     href: {link.href}")
                            if hasattr(link, 'text'):
                                print(f"     text: {link.text[:50] if link.text else 'None'}...")
                            # Show all attributes
                            print(f"     Attributes: {[a for a in dir(link) if not a.startswith('_')]}")
                
                if hasattr(result.links, 'external'):
                    print(f"\nExternal links count: {len(result.links.external)}")
                    if result.links.external:
                        print("First 3 external links:")
                        for i, link in enumerate(result.links.external[:3]):
                            print(f"  {i+1}. Type: {type(link)}")
                            if hasattr(link, 'href'):
                                print(f"     href: {link.href}")
                            
                # Try dictionary access
                try:
                    if isinstance(result.links, dict):
                        print("\nresult.links is a dictionary:")
                        print(f"Keys: {result.links.keys()}")
                        if 'internal' in result.links:
                            print(f"Internal links: {len(result.links['internal'])}")
                            if result.links['internal']:
                                print(f"Internal links: {result.links['internal']}")
                except:
                    pass

if __name__ == "__main__":
    asyncio.run(debug_links())