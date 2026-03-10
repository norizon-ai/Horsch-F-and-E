"""
Subdomain queue management for crawl orchestration.

Handles the queue of subdomains to be discovered and crawled.
"""

import asyncio
import logging
from typing import Set, List, Optional, Tuple
from collections import deque

from utils.domain_parser import DomainParser

logger = logging.getLogger(__name__)


class SubdomainQueue:
    """
    Manages the queue of subdomains for discovery and crawling.
    
    This class extracts subdomain queue logic from the orchestrator,
    providing efficient queue management with priority handling.
    """
    
    def __init__(self, base_domain: str, max_subdomains: Optional[int] = None):
        """
        Initialize the subdomain queue.
        
        Args:
            base_domain: The base domain for subdomain resolution
            max_subdomains: Maximum number of subdomains to process
        """
        self.base_domain = base_domain
        self.max_subdomains = max_subdomains
        self.queue = deque()
        self.processing: Set[str] = set()
        self.completed: Set[str] = set()
        self.domain_parser = DomainParser()
        self._lock = asyncio.Lock()
        
    async def add(self, subdomain: str, priority: int = 0) -> bool:
        """
        Add a subdomain to the queue.
        
        Args:
            subdomain: The subdomain to add
            priority: Priority level (higher = processed sooner)
            
        Returns:
            True if added, False if already in queue or processed
        """
        async with self._lock:
            # Check if already processed or in queue
            if subdomain in self.completed or subdomain in self.processing:
                return False
            
            # Check if already in queue
            for item in self.queue:
                if item[0] == subdomain:
                    return False
            
            # Check subdomain limit
            if self.max_subdomains and len(self.completed) >= self.max_subdomains:
                logger.debug(f"Subdomain limit reached ({self.max_subdomains})")
                return False
            
            # Add to queue with priority
            if priority > 0:
                # High priority items go to the front
                self.queue.appendleft((subdomain, priority))
            else:
                # Normal priority items go to the back
                self.queue.append((subdomain, priority))
            
            logger.debug(f"Added {subdomain} to queue (priority: {priority})")
            return True
    
    async def add_batch(self, subdomains: List[str], priority: int = 0) -> int:
        """
        Add multiple subdomains to the queue.
        
        Args:
            subdomains: List of subdomains to add
            priority: Priority level for all subdomains
            
        Returns:
            Number of subdomains actually added
        """
        added = 0
        for subdomain in subdomains:
            if await self.add(subdomain, priority):
                added += 1
        return added
    
    async def get_next(self) -> Optional[str]:
        """
        Get the next subdomain to process.
        
        Returns:
            Next subdomain or None if queue is empty
        """
        async with self._lock:
            while self.queue:
                subdomain, _ = self.queue.popleft()
                
                # Skip if somehow already processed
                if subdomain in self.completed:
                    continue
                
                # Mark as processing
                self.processing.add(subdomain)
                return subdomain
            
            return None
    
    async def get_batch(self, batch_size: int = 5) -> List[str]:
        """
        Get a batch of subdomains to process.
        
        Args:
            batch_size: Maximum number of subdomains to return
            
        Returns:
            List of subdomains (may be less than batch_size)
        """
        batch = []
        for _ in range(batch_size):
            subdomain = await self.get_next()
            if subdomain is None:
                break
            batch.append(subdomain)
        return batch
    
    async def mark_completed(self, subdomain: str, success: bool = True) -> None:
        """
        Mark a subdomain as completed.
        
        Args:
            subdomain: The subdomain that was processed
            success: Whether processing was successful
        """
        async with self._lock:
            self.processing.discard(subdomain)
            if success:
                self.completed.add(subdomain)
            else:
                # Failed items could be re-queued with lower priority
                # For now, we just mark as completed to avoid infinite loops
                self.completed.add(subdomain)
                logger.debug(f"Marked {subdomain} as failed/completed")
    
    async def requeue_processing(self) -> int:
        """
        Re-queue all items currently being processed.
        
        This is useful for recovery after a crash or timeout.
        
        Returns:
            Number of items re-queued
        """
        async with self._lock:
            requeued = 0
            for subdomain in list(self.processing):
                self.queue.append((subdomain, -1))  # Lower priority for retries
                self.processing.remove(subdomain)
                requeued += 1
            return requeued
    
    def build_subdomain_url(self, subdomain: str) -> Tuple[str, str]:
        """
        Build URL and domain name for a subdomain.
        
        Args:
            subdomain: The subdomain (or '__base__' for base domain)
            
        Returns:
            Tuple of (url, domain_name)
        """
        return self.domain_parser.build_subdomain_url(subdomain, self.base_domain)
    
    @property
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.queue) == 0
    
    @property
    def size(self) -> int:
        """Get current queue size."""
        return len(self.queue)
    
    @property
    def total_processed(self) -> int:
        """Get total number of processed subdomains."""
        return len(self.completed)
    
    @property
    def is_at_limit(self) -> bool:
        """Check if subdomain limit has been reached."""
        return self.max_subdomains and self.total_processed >= self.max_subdomains
    
    def get_stats(self) -> dict:
        """
        Get queue statistics.
        
        Returns:
            Dictionary with queue statistics
        """
        return {
            'queued': self.size,
            'processing': len(self.processing),
            'completed': len(self.completed),
            'total': self.size + len(self.processing) + len(self.completed),
            'limit': self.max_subdomains,
            'at_limit': self.is_at_limit
        }
    
    def get_all_discovered(self) -> List[str]:
        """
        Get all discovered subdomains (queued, processing, and completed).
        
        Returns:
            List of all discovered subdomain names
        """
        all_subdomains = set()
        
        # Add from queue
        for subdomain, _ in self.queue:
            all_subdomains.add(subdomain)
        
        # Add processing and completed
        all_subdomains.update(self.processing)
        all_subdomains.update(self.completed)
        
        # Convert to full domain names
        result = []
        for subdomain in all_subdomains:
            if subdomain == '__base__':
                result.append(self.base_domain)
            else:
                result.append(f"{subdomain}.{self.base_domain}")
        
        return sorted(result)