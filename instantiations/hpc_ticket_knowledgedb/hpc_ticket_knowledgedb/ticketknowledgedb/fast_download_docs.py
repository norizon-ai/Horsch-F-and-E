#!/usr/bin/env python3
"""
Fast documentation scraper that uses wget to download all HTML files first,
then processes them locally to convert to markdown.
"""

import os
import re
import json
import hashlib
import subprocess
from pathlib import Path
from typing import List, Dict
from bs4 import BeautifulSoup
import html2text
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FastDocScraper:
    def __init__(self, base_url: str = "https://doc.nhr.fau.de", output_dir: str = "docsmd"):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.html_dir = Path("temp_html")
        
        # HTML to Markdown converter
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0  # Don't wrap lines
        
        # Create output directories
        self.output_dir.mkdir(exist_ok=True)
        self.html_dir.mkdir(exist_ok=True)
        
        # JSONL output file
        self.jsonl_file = self.output_dir / "docs_data.jsonl"
    
    def download_with_wget(self):
        """Use wget to download the entire website"""
        logger.info("Starting wget download...")
        
        # wget command to mirror the website
        wget_cmd = [
            "wget",
            "--recursive",           # Download recursively
            "--no-clobber",         # Don't overwrite existing files
            "--page-requisites",    # Download all page requisites (CSS, images, etc.)
            "--html-extension",     # Save HTML files with .html extension
            "--convert-links",      # Convert links for local viewing
            "--restrict-file-names=windows",  # Use safe filenames
            "--domains", "doc.nhr.fau.de",    # Stay within domain
            "--no-parent",          # Don't go up in directory structure
            "--reject", "*.pdf,*.zip,*.tar.gz,*.exe,*.dmg",  # Skip binary files
            "--directory-prefix", str(self.html_dir),
            "--user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            self.base_url
        ]
        
        try:
            # Run wget
            result = subprocess.run(wget_cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("wget download completed successfully")
            else:
                logger.warning(f"wget completed with return code {result.returncode}")
                if result.stderr:
                    logger.warning(f"wget stderr: {result.stderr}")
            
            return True
            
        except subprocess.TimeoutExpired:
            logger.error("wget download timed out after 5 minutes")
            return False
        except FileNotFoundError:
            logger.error("wget not found. Please install wget: brew install wget")
            return False
        except Exception as e:
            logger.error(f"Error running wget: {e}")
            return False
    
    def url_to_filename(self, url: str) -> str:
        """Convert URL to safe filename"""
        filename = url.replace('https://', 'https___').replace('http://', 'http___')
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = filename.replace('/', '_')
        
        if not filename.endswith('.md'):
            filename += '.md'
        
        return filename
    
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
    
    def html_file_to_url(self, html_file: Path) -> str:
        """Convert local HTML file path back to original URL"""
        # Get relative path from the domain directory
        domain_dir = self.html_dir / "doc.nhr.fau.de"
        
        try:
            rel_path = html_file.relative_to(domain_dir)
            # Convert back to URL
            url_path = str(rel_path).replace('\\', '/')
            
            # Remove .html extension if it was added by wget
            if url_path.endswith('.html') and not url_path.endswith('index.html'):
                url_path = url_path[:-5]  # Remove .html
            
            # Construct full URL
            if url_path == 'index.html' or url_path == '':
                return self.base_url
            else:
                return f"{self.base_url}/{url_path}"
                
        except ValueError:
            # Fallback: use the file path
            return f"{self.base_url}/{html_file.name}"
    
    def process_html_file(self, html_file: Path) -> Dict:
        """Process a single HTML file and convert to markdown"""
        try:
            # Read HTML file
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse HTML
            soup = BeautifulSoup(content, 'html.parser')
            
            # Clean the content
            soup = self.clean_html_content(soup)
            
            # Extract title
            title_tag = soup.find('title')
            title = title_tag.get_text().strip() if title_tag else html_file.name
            
            # Extract headings
            headings = self.extract_headings(soup)
            
            # Convert to markdown
            markdown_content = self.h.handle(str(soup))
            
            # Clean up markdown
            markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
            
            # Get original URL
            original_url = self.html_file_to_url(html_file)
            
            # Generate filename
            filename = self.url_to_filename(original_url)
            
            # Save markdown file
            md_path = self.output_dir / filename
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {original_url}\n\n")
                f.write(markdown_content)
            
            # Generate unique ID
            page_id = hashlib.md5(original_url.encode()).hexdigest()
            
            # Prepare JSONL entry
            jsonl_entry = {
                "id": page_id,
                "url": original_url,
                "title": title,
                "titles": headings,
                "text": markdown_content,
                "filename": filename
            }
            
            return jsonl_entry
            
        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
            return None
    
    def process_all_html_files(self):
        """Process all downloaded HTML files"""
        logger.info("Processing HTML files...")
        
        # Clear JSONL file
        if self.jsonl_file.exists():
            self.jsonl_file.unlink()
        
        # Find all HTML files
        html_files = []
        for pattern in ['**/*.html', '**/*.htm']:
            html_files.extend(self.html_dir.glob(pattern))
        
        logger.info(f"Found {len(html_files)} HTML files to process")
        
        processed_count = 0
        
        for html_file in html_files:
            # Skip if it's not from our target domain
            if 'doc.nhr.fau.de' not in str(html_file):
                continue
                
            jsonl_entry = self.process_html_file(html_file)
            
            if jsonl_entry:
                # Append to JSONL file
                with open(self.jsonl_file, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(jsonl_entry, ensure_ascii=False) + '\n')
                
                processed_count += 1
                
                if processed_count % 10 == 0:
                    logger.info(f"Processed {processed_count} files...")
        
        logger.info(f"Processing completed. Converted {processed_count} HTML files to markdown.")
    
    def cleanup_temp_files(self):
        """Remove temporary HTML files"""
        import shutil
        if self.html_dir.exists():
            shutil.rmtree(self.html_dir)
            logger.info("Cleaned up temporary HTML files")
    
    def run_fast_scrape(self, cleanup: bool = True):
        """Run the complete fast scraping process"""
        try:
            # Step 1: Download with wget
            if not self.download_with_wget():
                logger.error("Failed to download with wget")
                return False
            
            # Step 2: Process all HTML files
            self.process_all_html_files()
            
            # Step 3: Cleanup (optional)
            if cleanup:
                self.cleanup_temp_files()
            
            return True
            
        except Exception as e:
            logger.error(f"Error during fast scraping: {e}")
            return False

def main():
    """Main function to run the fast scraper"""
    scraper = FastDocScraper()
    
    try:
        logger.info("Starting fast documentation scraping...")
        
        success = scraper.run_fast_scrape(cleanup=True)
        
        if success:
            # Print summary
            md_files = list(scraper.output_dir.glob("*.md"))
            print(f"\n=== Fast Scraping Summary ===")
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
        else:
            print("Fast scraping failed. Check the logs for details.")
    
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == "__main__":
    main()
