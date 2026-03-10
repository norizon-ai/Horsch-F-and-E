"""
Domain parsing utilities for extracting and normalizing domain information.
"""

from typing import List, Tuple
from urllib.parse import urlparse


class DomainParser:
    """Utility class for parsing and extracting domain information from URLs."""
    
    @staticmethod
    def extract_base_domain(url: str) -> str:
        """
        Extract the base domain from a URL.
        
        Args:
            url: The URL to parse
            
        Returns:
            The base domain (e.g., 'example.com' from 'https://sub.example.com/path')
        """
        parsed = urlparse(url)
        domain = parsed.netloc
        
        # Remove www prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Extract base domain from subdomain
        parts = domain.split('.')
        if len(parts) > 2:
            # Assume last two parts are the base domain
            # This is a simplification - in production use publicsuffix library
            return '.'.join(parts[-2:])
        
        return domain
    
    @staticmethod
    def parse_allowed_domains(url: str, explicit_domains: List[str] = None) -> List[str]:
        """
        Parse allowed domains from URL and explicit list.
        
        Args:
            url: The starting URL
            explicit_domains: Explicitly provided domain list (optional)
            
        Returns:
            List of allowed domains including variations (with/without www)
        """
        if explicit_domains:
            return explicit_domains
        
        parsed = urlparse(url)
        domain = parsed.netloc
        allowed_domains = [domain]
        
        # Add www variation
        if not domain.startswith("www."):
            allowed_domains.append(f"www.{domain}")
        else:
            allowed_domains.append(domain[4:])  # Remove www.
        
        return allowed_domains
    
    @staticmethod
    def extract_subdomain(full_domain: str, base_domain: str) -> str:
        """
        Extract subdomain from a full domain.
        
        Args:
            full_domain: The full domain (e.g., 'api.example.com')
            base_domain: The base domain (e.g., 'example.com')
            
        Returns:
            The subdomain part (e.g., 'api') or '__base__' for base domain
        """
        # Remove www prefix for comparison
        full_domain = full_domain.replace('www.', '')
        base_domain = base_domain.replace('www.', '')
        
        if full_domain == base_domain:
            return '__base__'
        
        if full_domain.endswith(f'.{base_domain}'):
            subdomain = full_domain[:-len(f'.{base_domain}')]
            return subdomain
        
        return '__base__'
    
    @staticmethod
    def build_subdomain_url(subdomain: str, base_domain: str, scheme: str = 'https') -> Tuple[str, str]:
        """
        Build URL and domain name for a subdomain.
        
        Args:
            subdomain: The subdomain (or '__base__' for base domain)
            base_domain: The base domain
            scheme: The URL scheme (default: 'https')
            
        Returns:
            Tuple of (url, domain_name)
        """
        if subdomain == '__base__':
            url = f"{scheme}://{base_domain}"
            domain_name = base_domain
        else:
            url = f"{scheme}://{subdomain}.{base_domain}"
            domain_name = f"{subdomain}.{base_domain}"
        
        return url, domain_name