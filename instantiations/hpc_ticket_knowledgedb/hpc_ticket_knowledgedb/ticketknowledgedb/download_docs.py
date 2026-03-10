#!/usr/bin/env python3
"""
Script to download all pages from https://doc.nhr.fau.de and convert them to markdown.
Saves each page as .md file and also creates a JSONL file with structured data.
"""

import os
import re
import json
import time
import hashlib
from urllib.parse import urljoin, urlparse, quote
from pathlib import Path
from typing import Set, List, Dict, Optional
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.robotparser import RobotFileParser
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocScraper:
    def __init__(self, base_url: str = "https://doc.nhr.fau.de", output_dir: str = "docsmd"):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.visited_urls: Set[str] = set()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # HTML to Markdown converter
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0  # Don't wrap lines
        
        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        
        # JSONL output file
        self.jsonl_file = self.output_dir / "docs_data.jsonl"
        
        # Check robots.txt
        self.check_robots_txt()
    
    def check_robots_txt(self):
        """Check robots.txt to ensure we're allowed to scrape"""
        try:
            rp = RobotFileParser()
            rp.set_url(urljoin(self.base_url, '/robots.txt'))
            rp.read()
            if not rp.can_fetch('*', self.base_url):
                logger.warning("robots.txt disallows scraping. Proceeding with caution.")
        except Exception as e:
            logger.info(f"Could not read robots.txt: {e}")
    
    def url_to_filename(self, url: str) -> str:
        """Convert URL to safe filename"""
        # Remove protocol and replace special characters
        filename = url.replace('https://', 'https___').replace('http://', 'http___')
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = filename.replace('/', '_')
        
        # Ensure it ends with .md
        if not filename.endswith('.md'):
            filename += '.md'
        
        return filename
    
    def extract_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extract all internal links from the page"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Convert relative URLs to absolute
            absolute_url = urljoin(current_url, href)
            
            # Only include links from the same domain
            if urlparse(absolute_url).netloc == urlparse(self.base_url).netloc:
                # Remove fragments and query parameters for consistency
                clean_url = absolute_url.split('#')[0].split('?')[0]
                if clean_url not in self.visited_urls:
                    links.append(clean_url)
        
        return links
    
    def extract_headings(self, soup: BeautifulSoup) -> List[str]:
        """Extract all headings from the page"""
        headings = []
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            text = heading.get_text().strip()
            if text:
                headings.append(text)
        return headings
    
    def clean_html_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Remove navigation, footer, and other non-content elements"""
        # Remove common navigation and footer elements
        for element in soup.find_all(['nav', 'footer', 'header']):
            element.decompose()
        
        # Remove elements with common navigation classes/ids
        for selector in ['.navigation', '.nav', '.sidebar', '.footer', '#navigation', '#nav', '#sidebar', '#footer']:
            for element in soup.select(selector):
                element.decompose()
        
        # Remove script and style elements
        for element in soup.find_all(['script', 'style']):
            element.decompose()
        
        return soup
    
    def download_page(self, url: str) -> Optional[Dict]:
        """Download and process a single page"""
        try:
            logger.info(f"Downloading: {url}")
            
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Clean the content
            soup = self.clean_html_content(soup)
            
            # Extract title
            title_tag = soup.find('title')
            title = title_tag.get_text().strip() if title_tag else url
            
            # Extract headings
            headings = self.extract_headings(soup)
            
            # Convert to markdown
            markdown_content = self.h.handle(str(soup))
            
            # Clean up markdown (remove excessive newlines)
            markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
            
            # Generate filename
            filename = self.url_to_filename(url)
            
            # Save markdown file
            md_path = self.output_dir / filename
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(markdown_content)
            
            # Generate unique ID
            page_id = hashlib.md5(url.encode()).hexdigest()
            
            # Prepare JSONL entry
            jsonl_entry = {
                "id": page_id,
                "url": url,
                "title": title,
                "titles": headings,
                "text": markdown_content,
                "filename": filename
            }
            
            # Append to JSONL file
            with open(self.jsonl_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(jsonl_entry, ensure_ascii=False) + '\n')
            
            logger.info(f"Saved: {filename}")
            
            # Extract links for further crawling
            links = self.extract_links(soup, url)
            
            return {
                "url": url,
                "links": links,
                "success": True
            }
            
        except Exception as e:
            logger.error(f"Error downloading {url}: {e}")
            return {
                "url": url,
                "links": [],
                "success": False,
                "error": str(e)
            }
    
    def crawl_website(self, start_url: Optional[str] = None, max_pages: int = 1000):
        """Crawl the entire website starting from the base URL"""
        if start_url is None:
            start_url = self.base_url
        
        # Initialize with start URL
        urls_to_visit = [start_url]
        pages_processed = 0
        
        # Clear JSONL file
        if self.jsonl_file.exists():
            self.jsonl_file.unlink()
        
        logger.info(f"Starting crawl from: {start_url}")
        logger.info(f"Output directory: {self.output_dir}")
        
        while urls_to_visit and pages_processed < max_pages:
            current_url = urls_to_visit.pop(0)
            
            if current_url in self.visited_urls:
                continue
            
            self.visited_urls.add(current_url)
            
            # Download and process the page
            result = self.download_page(current_url)
            
            if result and result["success"]:
                # Add new links to the queue
                for link in result["links"]:
                    if link not in self.visited_urls and link not in urls_to_visit:
                        urls_to_visit.append(link)
                
                pages_processed += 1
                
                # Be respectful - add a small delay
                time.sleep(1)
            
            # Progress update
            if pages_processed % 10 == 0:
                logger.info(f"Processed {pages_processed} pages, {len(urls_to_visit)} URLs in queue")
        
        logger.info(f"Crawling completed. Processed {pages_processed} pages.")
        logger.info(f"Markdown files saved in: {self.output_dir}")
        logger.info(f"JSONL data saved in: {self.jsonl_file}")

def main():
    """Main function to run the scraper"""
    scraper = DocScraper()
    
    try:
        # Start crawling
        scraper.crawl_website()
        
        # Print summary
        md_files = list(scraper.output_dir.glob("*.md"))
        print(f"\n=== Scraping Summary ===")
        print(f"Total pages downloaded: {len(md_files)}")
        print(f"Markdown files directory: {scraper.output_dir}")
        print(f"JSONL file: {scraper.jsonl_file}")
        
        # Show some example filenames
        if md_files:
            print(f"\nExample files:")
            for i, file in enumerate(md_files[:5]):
                print(f"  - {file.name}")
            if len(md_files) > 5:
                print(f"  ... and {len(md_files) - 5} more files")
    
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == "__main__":
    main()
