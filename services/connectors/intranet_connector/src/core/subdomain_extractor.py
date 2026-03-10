"""
Subdomain extraction from crawled page content.

This module provides functionality to discover subdomains by analyzing
the content of crawled pages, including HTML links, JavaScript, and meta tags.
"""

import re
from typing import Set, List, Optional, Any
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)


class SubdomainExtractor:
    """
    Extracts subdomain references from page content.
    
    Discovers subdomains by analyzing:
    - HTML links (href attributes)
    - JavaScript code (API endpoints, configurations)
    - Meta tags (canonical URLs, og:url, etc.)
    - Text content (subdomain mentions)
    """
    
    def __init__(self, base_domain: str):
        """
        Initialize the subdomain extractor.
        
        Args:
            base_domain: The base domain to find subdomains for (e.g., 'fau.de')
        """
        # Clean base domain (remove www. prefix if present)
        self.base_domain = base_domain.replace('www.', '')
        self.discovered_subdomains = set()
        
        # Compile regex patterns for efficiency
        self._compile_patterns()
        
    def _compile_patterns(self):
        """Compile regex patterns for subdomain extraction."""
        # Pattern for finding subdomains in URLs
        # Matches: https://subdomain.fau.de or //subdomain.fau.de
        escaped_domain = re.escape(self.base_domain)
        
        self.url_pattern = re.compile(
            rf'(?:https?:)?//([a-zA-Z0-9](?:[a-zA-Z0-9\-]{{0,61}}[a-zA-Z0-9])?)\.{escaped_domain}',
            re.IGNORECASE
        )
        
        # Pattern for finding subdomains in JavaScript strings
        self.js_pattern = re.compile(
            rf'["\'](?:https?:)?//([a-zA-Z0-9](?:[a-zA-Z0-9\-]{{0,61}}[a-zA-Z0-9])?)\.{escaped_domain}',
            re.IGNORECASE
        )
        
        # Pattern for email addresses (can reveal subdomains)
        self.email_pattern = re.compile(
            rf'@([a-zA-Z0-9](?:[a-zA-Z0-9\-]{{0,61}}[a-zA-Z0-9])?)\.{escaped_domain}',
            re.IGNORECASE
        )
    
    def extract_from_crawl4ai_links(self, links_data: Any) -> Set[str]:
        """
        Extract subdomains from crawl4ai's extracted links.
        
        Args:
            links_data: Links dictionary from crawl4ai containing internal and external links
            
        Returns:
            Set of discovered subdomain names (without base domain)
        """
        new_subdomains = set()
        
        try:
            # Handle dictionary format (crawl4ai returns dict)
            if isinstance(links_data, dict):
                # Process internal links
                if 'internal' in links_data and links_data['internal']:
                    for link in links_data['internal']:
                        if isinstance(link, dict) and 'href' in link:
                            matches = self.url_pattern.findall(link['href'])
                            new_subdomains.update(matches)
                
                # Process external links (might contain subdomains)
                if 'external' in links_data and links_data['external']:
                    for link in links_data['external']:
                        if isinstance(link, dict) and 'href' in link:
                            # Check if it's actually a subdomain of our base domain
                            matches = self.url_pattern.findall(link['href'])
                            new_subdomains.update(matches)
            
            # Handle object format (in case crawl4ai changes)
            elif hasattr(links_data, 'internal'):
                # Process internal links
                if links_data.internal:
                    for link in links_data.internal:
                        href = link.href if hasattr(link, 'href') else link.get('href') if isinstance(link, dict) else None
                        if href:
                            matches = self.url_pattern.findall(href)
                            new_subdomains.update(matches)
            
            # Filter out common non-subdomains
            new_subdomains = self._filter_subdomains(new_subdomains)
            
            # Update global discovered set
            self.discovered_subdomains.update(new_subdomains)
            
        except Exception as e:
            logger.error(f"Error extracting subdomains from links: {e}")
        
        return new_subdomains
    
    def extract_from_page(self, page_content: str, page_url: str, links_data: Optional[Any] = None) -> Set[str]:
        """
        Extract all subdomain references from a page.
        
        Args:
            page_content: HTML content of the page
            page_url: URL of the page (for context)
            links_data: Optional Links object from crawl4ai with pre-extracted links
            
        Returns:
            Set of discovered subdomain names (without base domain)
        """
        new_subdomains = set()
        
        # First, use crawl4ai's extracted links if available (most efficient)
        if links_data:
            new_subdomains.update(self.extract_from_crawl4ai_links(links_data))
            logger.info(f"Found {len(new_subdomains)} subdomains from crawl4ai links in {page_url}")
            return new_subdomains
        
        # Fallback to HTML parsing if no links data provided
        try:
            # Parse HTML
            soup = BeautifulSoup(page_content, 'html.parser')
            
            # 1. Extract from HTML links
            link_subdomains = self._extract_from_links(soup)
            new_subdomains.update(link_subdomains)
            
            # 2. Extract from JavaScript
            js_subdomains = self._extract_from_javascript(soup)
            new_subdomains.update(js_subdomains)
            
            # 3. Extract from meta tags
            meta_subdomains = self._extract_from_meta(soup)
            new_subdomains.update(meta_subdomains)
            
            # 4. Extract from text content using regex
            text_subdomains = self._extract_from_text(page_content)
            new_subdomains.update(text_subdomains)
            
            # Filter out common non-subdomains
            new_subdomains = self._filter_subdomains(new_subdomains)
            
            # Log discoveries
            if new_subdomains:
                logger.info(f"Found {len(new_subdomains)} subdomains in {page_url}")
                for subdomain in new_subdomains:
                    if subdomain not in self.discovered_subdomains:
                        logger.debug(f"  New subdomain: {subdomain}.{self.base_domain}")
            
            # Update global discovered set
            self.discovered_subdomains.update(new_subdomains)
            
        except Exception as e:
            logger.error(f"Error extracting subdomains from {page_url}: {e}")
        
        return new_subdomains
    
    def _extract_from_links(self, soup: BeautifulSoup) -> Set[str]:
        """Extract subdomains from HTML link elements."""
        subdomains = set()
        
        # Check all elements with href attribute
        for element in soup.find_all(href=True):
            href = element['href']
            matches = self.url_pattern.findall(href)
            subdomains.update(matches)
        
        # Check all elements with src attribute (scripts, images, etc.)
        for element in soup.find_all(src=True):
            src = element['src']
            matches = self.url_pattern.findall(src)
            subdomains.update(matches)
        
        # Check action attributes in forms
        for form in soup.find_all('form', action=True):
            action = form['action']
            matches = self.url_pattern.findall(action)
            subdomains.update(matches)
        
        return subdomains
    
    def _extract_from_javascript(self, soup: BeautifulSoup) -> Set[str]:
        """Extract subdomains from JavaScript code."""
        subdomains = set()
        
        # Find all script tags
        for script in soup.find_all('script'):
            if script.string:
                # Look for subdomain patterns in JavaScript
                matches = self.js_pattern.findall(script.string)
                subdomains.update(matches)
                
                # Also look for API configurations
                # Pattern: apiUrl: "https://api.fau.de"
                # Pattern: endpoint: '//services.fau.de'
                api_patterns = [
                    rf'(?:api|endpoint|url|host|domain|server)["\s:]+["\'](?:https?:)?//([a-zA-Z0-9\-]+)\.{re.escape(self.base_domain)}',
                    rf'["\'](?:https?:)?//([a-zA-Z0-9\-]+)\.{re.escape(self.base_domain)}["\']'
                ]
                
                for pattern in api_patterns:
                    regex = re.compile(pattern, re.IGNORECASE)
                    matches = regex.findall(script.string)
                    subdomains.update(matches)
        
        # Check inline JavaScript in onclick, onload, etc.
        for element in soup.find_all(True):
            for attr in ['onclick', 'onload', 'onchange', 'onsubmit']:
                if element.has_attr(attr):
                    js_code = element[attr]
                    matches = self.js_pattern.findall(js_code)
                    subdomains.update(matches)
        
        return subdomains
    
    def _extract_from_meta(self, soup: BeautifulSoup) -> Set[str]:
        """Extract subdomains from meta tags."""
        subdomains = set()
        
        # Check various meta tags that might contain URLs
        meta_properties = [
            'og:url',           # Open Graph URL
            'og:image',         # Open Graph Image
            'og:video',         # Open Graph Video
            'twitter:url',      # Twitter Card URL
            'twitter:image',    # Twitter Card Image
            'canonical',        # Canonical URL
        ]
        
        for prop in meta_properties:
            # Try property attribute
            meta = soup.find('meta', property=prop)
            if not meta:
                # Try name attribute
                meta = soup.find('meta', {'name': prop})
            if not meta:
                # Try rel attribute for canonical
                if prop == 'canonical':
                    link = soup.find('link', rel='canonical')
                    if link and link.has_attr('href'):
                        matches = self.url_pattern.findall(link['href'])
                        subdomains.update(matches)
            
            if meta and meta.has_attr('content'):
                matches = self.url_pattern.findall(meta['content'])
                subdomains.update(matches)
        
        # Check CSP (Content Security Policy) for allowed domains
        csp_meta = soup.find('meta', {'http-equiv': 'Content-Security-Policy'})
        if csp_meta and csp_meta.has_attr('content'):
            matches = self.url_pattern.findall(csp_meta['content'])
            subdomains.update(matches)
        
        return subdomains
    
    def _extract_from_text(self, content: str) -> Set[str]:
        """Extract subdomains from text content using regex."""
        subdomains = set()
        
        # Find all URL patterns
        url_matches = self.url_pattern.findall(content)
        subdomains.update(url_matches)
        
        # Find email addresses that might reveal subdomains
        email_matches = self.email_pattern.findall(content)
        subdomains.update(email_matches)
        
        return subdomains
    
    def _filter_subdomains(self, subdomains: Set[str]) -> Set[str]:
        """
        Filter out invalid or unwanted subdomains.
        
        Args:
            subdomains: Set of potential subdomain names
            
        Returns:
            Filtered set of valid subdomains
        """
        filtered = set()
        
        # Common CDN/static subdomains to potentially exclude
        # (can be made configurable)
        exclude_patterns = [
            r'^(www|ftp|mail|smtp|pop|imap)$',  # Common service subdomains
            r'^(ns\d+|dns\d+)$',                 # DNS servers
            r'^(static|cdn|assets|media)$',      # Static content (optional)
        ]
        
        for subdomain in subdomains:
            # Skip empty or invalid
            if not subdomain or subdomain == 'www':
                continue
            
            # Skip if matches exclude pattern (optional)
            # skip_subdomain = False
            # for pattern in exclude_patterns:
            #     if re.match(pattern, subdomain, re.IGNORECASE):
            #         skip_subdomain = True
            #         break
            # if skip_subdomain:
            #     continue
            
            # Validate subdomain format
            if self._is_valid_subdomain(subdomain):
                filtered.add(subdomain.lower())
        
        return filtered
    
    def _is_valid_subdomain(self, subdomain: str) -> bool:
        """
        Check if a string is a valid subdomain.
        
        Args:
            subdomain: Potential subdomain string
            
        Returns:
            True if valid subdomain format
        """
        # Check length (max 63 characters per label)
        if len(subdomain) > 63 or len(subdomain) < 1:
            return False
        
        # Check format (alphanumeric and hyphens, not starting/ending with hyphen)
        if not re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$', subdomain):
            return False
        
        return True
    
    def get_all_discovered(self) -> Set[str]:
        """
        Get all discovered subdomains.
        
        Returns:
            Set of all discovered subdomain names
        """
        return self.discovered_subdomains.copy()
    
    def get_full_domains(self) -> List[str]:
        """
        Get full domain names for all discovered subdomains.
        
        Returns:
            List of full domain names (subdomain.base_domain)
        """
        return [f"{subdomain}.{self.base_domain}" for subdomain in self.discovered_subdomains]