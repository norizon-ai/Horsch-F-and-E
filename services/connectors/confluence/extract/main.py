#!/usr/bin/env python3

import argparse
import sys
import json
from pathlib import Path
from confluence_scraper import ConfluenceScraper, ScraperConfig


def main():
    parser = argparse.ArgumentParser(
        description="Confluence Data Scraper - Extract all data from Confluence instance"
    )
    
    parser.add_argument(
        "--base-url",
        help="Base URL of the Confluence instance (e.g., https://company.atlassian.net/wiki)"
    )
    
    parser.add_argument(
        "--token",
        help="Bearer token for authentication"
    )
    
    parser.add_argument(
        "--output-dir",
        default="confluence_export",
        help="Output directory for exported data (default: confluence_export)"
    )
    
    parser.add_argument(
        "--max-workers",
        type=int,
        default=5,
        help="Maximum number of concurrent workers (default: 5)"
    )
    
    parser.add_argument(
        "--page-size",
        type=int,
        default=50,
        help="Number of items to fetch per API request (default: 50, max: 250)"
    )
    
    parser.add_argument(
        "--no-attachments",
        action="store_true",
        help="Skip downloading attachments"
    )
    
    parser.add_argument(
        "--config-file",
        help="Load configuration from JSON file"
    )
    
    parser.add_argument(
        "--save-config",
        help="Save current configuration to JSON file"
    )
    
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Start fresh scrape, ignoring any existing checkpoint"
    )
    
    parser.add_argument(
        "--test-connection",
        action="store_true",
        help="Test connection to Confluence API and exit"
    )
    
    args = parser.parse_args()
    
    if args.config_file:
        config = ScraperConfig.from_file(args.config_file)
        print(f"Loaded configuration from {args.config_file}")
    else:
        if not args.base_url or not args.token:
            parser.error("--base-url and --token are required when not using --config-file")
        config = ScraperConfig(
            base_url=args.base_url,
            bearer_token=args.token,
            output_dir=args.output_dir,
            max_workers=args.max_workers,
            page_size=min(args.page_size, 250),
            download_attachments=not args.no_attachments
        )
    
    if args.save_config:
        config.save_to_file(args.save_config)
        print(f"Configuration saved to {args.save_config}")
    
    scraper = ConfluenceScraper(config)
    
    if args.test_connection:
        if scraper.test_connection():
            print("✓ Successfully connected to Confluence API")
            sys.exit(0)
        else:
            print("✗ Failed to connect to Confluence API")
            sys.exit(1)
    
    print("\n" + "="*60)
    print("CONFLUENCE DATA SCRAPER")
    print("="*60)
    print(f"Base URL: {config.base_url}")
    print(f"Output Directory: {config.output_dir}")
    print(f"Max Workers: {config.max_workers}")
    print(f"Page Size: {config.page_size}")
    print(f"Download Attachments: {config.download_attachments}")
    print(f"Resume Mode: {not args.no_resume}")
    print("="*60 + "\n")
    
    try:
        success = scraper.scrape_all(resume=not args.no_resume)
        
        if success:
            print("\n✓ Scraping completed successfully!")
            print(f"Data exported to: {config.output_dir}")
            print(f"Check export_report.json for detailed statistics")
            sys.exit(0)
        else:
            print("\n✗ Scraping failed. Check logs for details.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nScraping interrupted by user.")
        print("Progress has been saved. Run again to resume.")
        sys.exit(130)
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()