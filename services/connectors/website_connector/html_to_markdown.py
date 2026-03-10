#!/usr/bin/env python3
"""
Convert downloaded HTML files to Markdown with configurable content cleaning.
Uses pandoc for fast conversion and multiprocessing for parallel processing.
"""

import os
import sys
import subprocess
import hashlib
import json
import warnings
import yaml
from pathlib import Path
from multiprocessing import Pool, cpu_count
from typing import Dict, List, Optional
from datetime import datetime
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from tqdm import tqdm
import logging

# Suppress XML parsing warnings (some files are RSS/sitemaps, not HTML)
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_config_env():
    """Load configuration from config.env file if it exists"""
    config_paths = [
        Path("./config.env"),
        Path.home() / ".website-connector" / "config.env",
        Path("/app/config.env")
    ]

    for config_path in config_paths:
        if config_path.exists():
            logger.info(f"Loading configuration from: {config_path}")
            with open(config_path) as f:
                for line in f:
                    line = line.strip()
                    # Skip comments and empty lines
                    if line and not line.startswith('#'):
                        # Remove inline comments
                        if '#' in line:
                            line = line.split('#')[0].strip()
                        # Parse KEY=VALUE
                        if '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip().strip('"').strip("'")
                            # Only set if not already in environment
                            if key not in os.environ:
                                os.environ[key] = value
            return True

    logger.warning("No config.env found. Using environment variables or defaults.")
    return False


# Load config.env on module import
load_config_env()


class HTMLToMarkdownConverter:
    """Convert HTML files to Markdown with configurable cleaning"""

    def __init__(self):
        """Initialize converter with configuration from environment variables"""
        # Input/Output directories
        self.html_dir = Path(os.getenv("HTML_INPUT_DIR", "fau_temp_html_eu_de"))
        self.output_dir = Path(os.getenv("MARKDOWN_OUTPUT_DIR", "fau_docsmd"))
        self.cleanup_html = os.getenv("CLEANUP_HTML", "false").lower() == "true"

        # Content cleaning configuration
        self.remove_elements = os.getenv("REMOVE_ELEMENTS", "nav,footer,header,script,style").split(",")
        self.remove_selectors = os.getenv(
            "REMOVE_SELECTORS",
            ".navigation,.nav,.sidebar,.footer,#navigation,#nav,#sidebar,#footer"
        ).split(",")

        # Parallel processing
        self.parallel_workers = int(
            os.getenv("PARALLEL_WORKERS", str(max(1, cpu_count() - 1)))
        )

        # Domains for URL reconstruction
        self.domains = os.getenv("DOMAINS", "fau.de,fau.eu").split(",")
        self.primary_domain = self.domains[0]

        # Create output directory
        self.output_dir.mkdir(exist_ok=True, parents=True)

        # JSONL output (optional)
        self.generate_jsonl = os.getenv("GENERATE_JSONL", "false").lower() == "true"
        self.jsonl_file = self.output_dir / "docs_data.jsonl" if self.generate_jsonl else None

        # Timestamp for metadata
        self.scraped_at = datetime.utcnow().isoformat() + "Z"

        # Check for pandoc
        self._check_pandoc()

    def _check_pandoc(self):
        """Check if pandoc is installed"""
        try:
            subprocess.run(
                ["pandoc", "--version"],
                capture_output=True,
                check=True,
                timeout=5
            )
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            logger.error(
                "Pandoc not found! Install with: brew install pandoc (macOS) "
                "or sudo apt install pandoc (Linux)"
            )
            sys.exit(1)

    def clean_html_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Remove navigation, footer, and other non-content elements"""
        # For malformed HTML, extract() instead of decompose() is safer
        # Remove specified HTML elements
        for element_tag in self.remove_elements:
            element_tag = element_tag.strip()
            if element_tag:
                for element in soup.find_all(element_tag):
                    element.extract()  # Use extract instead of decompose

        # Remove elements matching CSS selectors
        for selector in self.remove_selectors:
            selector = selector.strip()
            if selector:
                try:
                    for element in soup.select(selector):
                        element.extract()  # Use extract instead of decompose
                except Exception as e:
                    logger.warning(f"Invalid CSS selector '{selector}': {e}")

        return soup

    def extract_headings(self, soup: BeautifulSoup) -> List[str]:
        """Extract all headings from the page"""
        headings = []
        for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            text = heading.get_text().strip()
            if text:
                headings.append(text)
        return headings

    def html_file_to_url(self, html_file: Path) -> str:
        """Convert local HTML file path back to original URL"""
        # Try to find which domain this file belongs to
        domain_name = None
        domain_dir = None

        # Check if file is under html_dir/domain/...
        try:
            rel_to_html_dir = html_file.relative_to(self.html_dir)
            # First part of path should be the domain
            potential_domain = rel_to_html_dir.parts[0] if rel_to_html_dir.parts else None

            if potential_domain and '.' in potential_domain:
                # This looks like a domain (has dots)
                domain_name = potential_domain
                domain_dir = self.html_dir / domain_name
        except ValueError:
            pass

        # Fallback: try configured domains
        if not domain_dir:
            for domain in self.domains:
                potential_dir = self.html_dir / domain
                if potential_dir.exists() and potential_dir in html_file.parents:
                    domain_name = domain
                    domain_dir = potential_dir
                    break

        # Final fallback
        if not domain_dir or not domain_name:
            domain_name = self.primary_domain
            domain_dir = self.html_dir / self.primary_domain

        try:
            rel_path = html_file.relative_to(domain_dir)
            # Convert back to URL
            url_path = str(rel_path).replace("\\", "/")

            # Remove .html extension if it was added by wget
            if url_path.endswith(".html") and not url_path.endswith("index.html"):
                url_path = url_path[:-5]

            # Construct full URL
            if url_path == "index.html" or url_path == "":
                return f"https://{domain_name}"
            else:
                return f"https://{domain_name}/{url_path}"

        except ValueError:
            # Fallback: use the file path
            return f"https://{domain_name}/{html_file.name}"

    def url_to_filename(self, url: str) -> str:
        """Convert URL to safe filename with length limits"""
        import re

        # Replace protocol
        filename = url.replace("https://", "https___").replace("http://", "http___")

        # Replace unsafe characters
        filename = re.sub(r'[<>:"/\\|?*]', "_", filename)
        filename = filename.replace("/", "_")

        # Remove .md extension if present for length calculation
        if filename.endswith(".md"):
            filename = filename[:-3]

        # Max filename length (most filesystems support 255, leave room for .md)
        MAX_LENGTH = 250

        if len(filename) > MAX_LENGTH:
            # Use hash for uniqueness when truncating
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]

            # Keep the beginning and add hash
            truncated_length = MAX_LENGTH - len(url_hash) - 1  # -1 for underscore
            filename = f"{filename[:truncated_length]}_{url_hash}"

        return filename + ".md"

    def convert_with_pandoc(self, html_content: str) -> str:
        """Convert HTML to Markdown using pandoc"""
        try:
            result = subprocess.run(
                ["pandoc", "-f", "html", "-t", "markdown", "--wrap=none"],
                input=html_content,
                capture_output=True,
                text=True,
                timeout=30,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Pandoc conversion failed: {e.stderr}")
            return ""
        except subprocess.TimeoutExpired:
            logger.error("Pandoc conversion timed out")
            return ""

    def process_html_file(self, html_file: Path) -> Optional[Dict]:
        """Process a single HTML file and convert to markdown"""
        try:
            # Read HTML file
            with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if not content or len(content) < 100:
                logger.warning(f"Empty or too small HTML file: {html_file}")
                return None

            # Parse HTML with lxml (much better for malformed HTML than html.parser)
            soup = BeautifulSoup(content, "lxml")

            # Extract title before cleaning
            title_tag = soup.find("title")
            title = title_tag.get_text().strip() if title_tag else html_file.name

            # Extract headings before cleaning
            headings = self.extract_headings(soup)

            # Clean the content
            soup = self.clean_html_content(soup)

            # Get cleaned HTML
            cleaned_html = str(soup)

            # Debug: check if cleaned HTML is empty
            if len(cleaned_html.strip()) < 50:
                logger.warning(f"Cleaned HTML too short for {html_file}: {len(cleaned_html)} chars")
                logger.debug(f"Cleaned HTML: {cleaned_html[:200]}")
                return None

            # Convert cleaned HTML to markdown using pandoc
            markdown_content = self.convert_with_pandoc(cleaned_html)

            if not markdown_content:
                logger.warning(f"Empty markdown for {html_file}")
                return None

            # Get original URL
            original_url = self.html_file_to_url(html_file)

            # Generate unique ID
            page_id = hashlib.md5(original_url.encode()).hexdigest()

            # Generate filename
            filename = self.url_to_filename(original_url)

            # Prepare frontmatter metadata
            frontmatter = {
                'url': original_url,
                'title': title,
                'id': page_id,
                'headings': headings,
                'scraped_at': self.scraped_at
            }

            # Save markdown file with YAML frontmatter
            md_path = self.output_dir / filename
            with open(md_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(yaml.dump(frontmatter, allow_unicode=True, sort_keys=False))
                f.write("---\n\n")
                f.write(f"# {title}\n\n")
                f.write(f"Source: {original_url}\n\n")
                f.write(markdown_content)

            # Prepare JSONL entry (only if enabled)
            if self.generate_jsonl:
                jsonl_entry = {
                    "id": page_id,
                    "url": original_url,
                    "title": title,
                    "titles": headings,
                    "text": markdown_content,
                    "filename": filename,
                }
                return jsonl_entry
            else:
                # Return minimal info for progress tracking
                return {"id": page_id, "url": original_url}

        except Exception as e:
            logger.error(f"Error processing {html_file}: {e}")
            return None

    def find_html_files(self) -> List[Path]:
        """Find all HTML files in the input directory"""
        html_files = []
        for pattern in ["**/*.html", "**/*.htm"]:
            html_files.extend(self.html_dir.glob(pattern))

        # Filter out files not in our domains
        filtered_files = []
        for html_file in html_files:
            for domain in self.domains:
                if domain.replace(".", "_") in str(html_file) or domain in str(html_file):
                    filtered_files.append(html_file)
                    break

        return filtered_files

    def process_all_files(self):
        """Process all HTML files in parallel"""
        logger.info("Finding HTML files...")
        html_files = self.find_html_files()

        if not html_files:
            logger.error(f"No HTML files found in {self.html_dir}")
            return

        logger.info(f"Found {len(html_files)} HTML files to process")
        logger.info(f"Using {self.parallel_workers} parallel workers")
        if self.generate_jsonl:
            logger.info(f"JSONL generation enabled: {self.jsonl_file}")
        else:
            logger.info("JSONL generation disabled (using frontmatter only)")

        # Clear JSONL file if enabled
        if self.generate_jsonl and self.jsonl_file.exists():
            self.jsonl_file.unlink()

        # Process files in parallel with progress bar
        processed_count = 0
        with Pool(processes=self.parallel_workers) as pool:
            results = list(
                tqdm(
                    pool.imap(self.process_html_file, html_files),
                    total=len(html_files),
                    desc="Converting to Markdown",
                    unit="file"
                )
            )

        # Write results to JSONL (if enabled)
        if self.generate_jsonl:
            with open(self.jsonl_file, "w", encoding="utf-8") as f:
                for jsonl_entry in results:
                    if jsonl_entry:
                        # Only write full entries (not minimal ones)
                        if "text" in jsonl_entry:
                            f.write(json.dumps(jsonl_entry, ensure_ascii=False) + "\n")
                            processed_count += 1
        else:
            # Count successful conversions
            processed_count = sum(1 for r in results if r is not None)

        logger.info(f"Successfully converted {processed_count}/{len(html_files)} files")
        logger.info(f"Markdown files: {self.output_dir}")
        if self.generate_jsonl:
            logger.info(f"JSONL file: {self.jsonl_file}")
        else:
            logger.info("JSONL file: Not generated (disabled in config)")

        # Cleanup HTML files if requested
        if self.cleanup_html:
            logger.info("Cleaning up HTML files...")
            import shutil
            if self.html_dir.exists():
                shutil.rmtree(self.html_dir)
                logger.info(f"Removed {self.html_dir}")


def main():
    """Main function"""
    print("=" * 70)
    print("HTML to Markdown Converter")
    print("=" * 70)

    # Load configuration
    converter = HTMLToMarkdownConverter()

    print(f"Input directory:     {converter.html_dir}")
    print(f"Output directory:    {converter.output_dir}")
    print(f"Parallel workers:    {converter.parallel_workers}")
    print(f"Remove elements:     {', '.join(converter.remove_elements)}")
    print(f"Remove selectors:    {', '.join(converter.remove_selectors[:3])}...")
    print(f"Cleanup HTML:        {converter.cleanup_html}")
    print("=" * 70)
    print()

    # Check if input directory exists
    if not converter.html_dir.exists():
        logger.error(f"Input directory not found: {converter.html_dir}")
        logger.error("Run ./scrape_all.sh first to download HTML files")
        sys.exit(1)

    # Process all files
    try:
        converter.process_all_files()
        print("\n" + "=" * 70)
        print("Conversion completed successfully!")
        print("=" * 70)

    except KeyboardInterrupt:
        print("\nConversion interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
