"""
Statistics reporting utilities for crawl metrics and performance tracking.
"""

from typing import Dict, Any, List
from datetime import datetime
import json
from pathlib import Path


class StatisticsReporter:
    """Utility class for collecting and reporting crawl statistics."""
    
    def __init__(self):
        """Initialize the statistics reporter."""
        self.start_time = datetime.now()
        self.pages_crawled = 0
        self.pages_failed = 0
        self.domains_discovered = set()
        self.domains_crawled = set()
        self.domains_with_sitemap = set()
        self.pages_per_domain = {}
        self.errors_by_type = {}
        self.total_bytes = 0
    
    def add_page_crawled(self, domain: str, success: bool = True, size_bytes: int = 0) -> None:
        """
        Record a page crawl.
        
        Args:
            domain: The domain of the page
            success: Whether the crawl was successful
            size_bytes: Size of the page in bytes
        """
        if success:
            self.pages_crawled += 1
            self.total_bytes += size_bytes
        else:
            self.pages_failed += 1
        
        # Track pages per domain
        if domain not in self.pages_per_domain:
            self.pages_per_domain[domain] = {'success': 0, 'failed': 0}
        
        if success:
            self.pages_per_domain[domain]['success'] += 1
        else:
            self.pages_per_domain[domain]['failed'] += 1
    
    def add_domain_discovered(self, domain: str) -> None:
        """Record discovery of a new domain/subdomain."""
        self.domains_discovered.add(domain)
    
    def add_domain_crawled(self, domain: str) -> None:
        """Record that a domain has been crawled."""
        self.domains_crawled.add(domain)
    
    def add_error(self, error_type: str, domain: str = None) -> None:
        """
        Record an error occurrence.
        
        Args:
            error_type: Type/class of the error
            domain: Optional domain where error occurred
        """
        if error_type not in self.errors_by_type:
            self.errors_by_type[error_type] = []
        
        self.errors_by_type[error_type].append({
            'timestamp': datetime.now().isoformat(),
            'domain': domain
        })
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive statistics summary.
        
        Returns:
            Dictionary containing all statistics
        """
        elapsed = (datetime.now() - self.start_time).total_seconds()
        total_pages = self.pages_crawled + self.pages_failed
        
        summary = {
            'start_time': self.start_time.isoformat(),
            'end_time': datetime.now().isoformat(),
            'duration_seconds': elapsed,
            'total_pages': total_pages,
            'successful_pages': self.pages_crawled,
            'failed_pages': self.pages_failed,
            'domains_discovered': len(self.domains_discovered),
            'domains_crawled': len(self.domains_crawled),
            'domains_with_sitemap': list(self.domains_with_sitemap),
            'success_rate': self.pages_crawled / total_pages if total_pages > 0 else 0,
            'pages_per_second': total_pages / elapsed if elapsed > 0 else 0,
            'average_page_size_kb': (self.total_bytes / 1024 / self.pages_crawled) 
                                   if self.pages_crawled > 0 else 0,
            'pages_per_domain': self._summarize_pages_per_domain(),
            'error_summary': self._summarize_errors()
        }
        
        return summary
    
    def _summarize_pages_per_domain(self) -> Dict[str, int]:
        """Create simplified pages per domain summary."""
        return {
            domain: stats['success'] + stats['failed']
            for domain, stats in self.pages_per_domain.items()
        }
    
    def _summarize_errors(self) -> Dict[str, int]:
        """Create error summary by type."""
        return {
            error_type: len(occurrences)
            for error_type, occurrences in self.errors_by_type.items()
        }
    
    def save_to_file(self, filepath: Path) -> None:
        """
        Save statistics to a JSON file.
        
        Args:
            filepath: Path to save the statistics file
        """
        summary = self.get_summary()
        
        # Convert sets to lists for JSON serialization
        summary['domains_discovered'] = list(self.domains_discovered)
        summary['domains_crawled'] = list(self.domains_crawled)
        
        with open(filepath, 'w') as f:
            json.dump(summary, f, indent=2, default=str)
    
    def print_summary(self) -> None:
        """Print a formatted summary to console."""
        from utils.result_formatter import ResultFormatter
        
        summary = self.get_summary()
        ResultFormatter.print_crawl_results(summary)
        ResultFormatter.print_domain_stats(summary)
        
        # Print error summary if there were errors
        if self.errors_by_type:
            print("\nError Summary:")
            for error_type, count in summary['error_summary'].items():
                print(f"  {error_type}: {count} occurrences")
    
    @classmethod
    def merge_statistics(cls, stats_list: List['StatisticsReporter']) -> 'StatisticsReporter':
        """
        Merge multiple statistics reporters into one.
        
        Args:
            stats_list: List of StatisticsReporter instances to merge
            
        Returns:
            New StatisticsReporter with merged statistics
        """
        merged = cls()
        
        for stats in stats_list:
            merged.pages_crawled += stats.pages_crawled
            merged.pages_failed += stats.pages_failed
            merged.domains_discovered.update(stats.domains_discovered)
            merged.domains_crawled.update(stats.domains_crawled)
            merged.domains_with_sitemap.update(stats.domains_with_sitemap)
            merged.total_bytes += stats.total_bytes
            
            # Merge pages per domain
            for domain, counts in stats.pages_per_domain.items():
                if domain not in merged.pages_per_domain:
                    merged.pages_per_domain[domain] = {'success': 0, 'failed': 0}
                merged.pages_per_domain[domain]['success'] += counts['success']
                merged.pages_per_domain[domain]['failed'] += counts['failed']
            
            # Merge errors
            for error_type, occurrences in stats.errors_by_type.items():
                if error_type not in merged.errors_by_type:
                    merged.errors_by_type[error_type] = []
                merged.errors_by_type[error_type].extend(occurrences)
        
        # Use earliest start time and latest end time
        if stats_list:
            merged.start_time = min(s.start_time for s in stats_list)
        
        return merged