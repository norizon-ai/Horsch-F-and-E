"""
Crawl state management module.

Handles crawl state persistence and recovery for resume functionality.
"""

import json
import logging
from pathlib import Path
from typing import Set, Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class CrawlStateManager:
    """
    Manages crawl state for persistence and resume functionality.
    
    This class extracts the state management logic from the monolithic
    orchestrator, providing a clean interface for state operations.
    """
    
    def __init__(self, base_domain: str):
        """
        Initialize the state manager.
        
        Args:
            base_domain: The base domain being crawled
        """
        self.base_domain = base_domain
        self.discovered_subdomains: Set[str] = set()
        self.crawled_subdomains: Set[str] = set()
        self.pending_subdomains: Set[str] = set()
        self.failed_subdomains: Set[str] = set()
        self.crawled_urls: Set[str] = set()
        
    def initialize_from_url(self, start_url: str) -> None:
        """
        Initialize state from starting URL.
        
        Args:
            start_url: The initial crawl URL
        """
        from urllib.parse import urlparse
        from utils.domain_parser import DomainParser
        
        parser = DomainParser()
        parsed = urlparse(start_url)
        
        # Determine if we're starting from base domain or subdomain
        if parsed.netloc == self.base_domain or parsed.netloc == f"www.{self.base_domain}":
            # Starting from base domain
            self.pending_subdomains.add('__base__')
        else:
            # Starting from a subdomain
            subdomain = parser.extract_subdomain(parsed.netloc, self.base_domain)
            if subdomain != '__base__':
                self.discovered_subdomains.add(subdomain)
                self.pending_subdomains.add(subdomain)
            else:
                self.pending_subdomains.add('__base__')
    
    def load_from_publisher(self, publisher: Any) -> bool:
        """
        Load state from publisher if it supports state persistence.
        
        Args:
            publisher: Publisher instance that may have state persistence
            
        Returns:
            True if state was loaded, False otherwise
        """
        if not hasattr(publisher, 'get_subdomain_state'):
            return False
        
        try:
            prev_state = publisher.get_subdomain_state()
            if not prev_state or prev_state.get('base_domain') != self.base_domain:
                return False
            
            # Load discovered subdomains
            discovered = prev_state.get('discovered_subdomains', set())
            if isinstance(discovered, list):
                discovered = set(discovered)
            self.discovered_subdomains.update(discovered)
            
            # Load crawled subdomains
            crawled = prev_state.get('crawled_subdomains', set())
            if isinstance(crawled, list):
                crawled = set(crawled)
            self.crawled_subdomains.update(crawled)
            
            # Load failed subdomains
            failed = prev_state.get('failed_subdomains', set())
            if isinstance(failed, list):
                failed = set(failed)
            self.failed_subdomains.update(failed)
            
            # Rebuild pending set (discovered but not crawled or failed)
            for subdomain in discovered:
                if subdomain not in crawled and subdomain not in failed:
                    self.pending_subdomains.add(subdomain)
            
            logger.info(f"Loaded state: {len(discovered)} discovered, "
                       f"{len(crawled)} crawled, {len(self.pending_subdomains)} pending")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to load state from publisher: {e}")
            return False
    
    async def save_to_publisher(self, publisher: Any) -> bool:
        """
        Save state to publisher if it supports state persistence.
        
        Args:
            publisher: Publisher instance that may have state persistence
            
        Returns:
            True if state was saved, False otherwise
        """
        if not hasattr(publisher, 'save_subdomain_state'):
            return False
        
        try:
            await publisher.save_subdomain_state(
                base_domain=self.base_domain,
                discovered=self.discovered_subdomains,
                crawled=self.crawled_subdomains,
                pending=self.pending_subdomains,
                failed=self.failed_subdomains
            )
            return True
        except Exception as e:
            logger.error(f"Failed to save state to publisher: {e}")
            return False
    
    def mark_subdomain_discovered(self, subdomain: str) -> bool:
        """
        Mark a subdomain as discovered.
        
        Args:
            subdomain: The subdomain to mark as discovered
            
        Returns:
            True if this is a newly discovered subdomain
        """
        if subdomain in self.discovered_subdomains:
            return False
        
        self.discovered_subdomains.add(subdomain)
        
        # Add to pending if not already crawled or failed
        if subdomain not in self.crawled_subdomains and subdomain not in self.failed_subdomains:
            self.pending_subdomains.add(subdomain)
        
        return True
    
    def mark_subdomain_crawled(self, subdomain: str) -> None:
        """
        Mark a subdomain as successfully crawled.
        
        Args:
            subdomain: The subdomain to mark as crawled
        """
        self.crawled_subdomains.add(subdomain)
        self.pending_subdomains.discard(subdomain)
        self.failed_subdomains.discard(subdomain)
    
    def mark_subdomain_failed(self, subdomain: str) -> None:
        """
        Mark a subdomain as failed.
        
        Args:
            subdomain: The subdomain to mark as failed
        """
        self.failed_subdomains.add(subdomain)
        self.pending_subdomains.discard(subdomain)
    
    def get_next_pending_batch(self, batch_size: int = 10) -> list:
        """
        Get the next batch of pending subdomains to crawl.
        
        Args:
            batch_size: Maximum number of subdomains to return
            
        Returns:
            List of pending subdomains (up to batch_size)
        """
        pending_list = list(self.pending_subdomains)
        return pending_list[:batch_size]
    
    def should_crawl_subdomain(self, subdomain: str, force_recrawl: bool = False) -> bool:
        """
        Check if a subdomain should be crawled.
        
        Args:
            subdomain: The subdomain to check
            force_recrawl: If True, allow recrawling of already crawled subdomains
            
        Returns:
            True if the subdomain should be crawled
        """
        if force_recrawl:
            return True
        
        return subdomain not in self.crawled_subdomains
    
    def add_crawled_url(self, url: str) -> None:
        """
        Track a crawled URL.
        
        Args:
            url: The URL that was crawled
        """
        self.crawled_urls.add(url)
    
    def is_url_crawled(self, url: str) -> bool:
        """
        Check if a URL has been crawled.
        
        Args:
            url: The URL to check
            
        Returns:
            True if the URL has been crawled
        """
        return url in self.crawled_urls
    
    def get_state_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current state.
        
        Returns:
            Dictionary with state statistics
        """
        return {
            'base_domain': self.base_domain,
            'discovered_count': len(self.discovered_subdomains),
            'crawled_count': len(self.crawled_subdomains),
            'pending_count': len(self.pending_subdomains),
            'failed_count': len(self.failed_subdomains),
            'urls_crawled': len(self.crawled_urls),
            'discovered_subdomains': sorted(self.discovered_subdomains),
            'crawled_subdomains': sorted(self.crawled_subdomains),
            'pending_subdomains': sorted(self.pending_subdomains),
            'failed_subdomains': sorted(self.failed_subdomains)
        }
    
    def export_to_file(self, filepath: Path) -> None:
        """
        Export state to a JSON file.
        
        Args:
            filepath: Path to save the state file
        """
        state = self.get_state_summary()
        state['exported_at'] = datetime.now().isoformat()
        
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)