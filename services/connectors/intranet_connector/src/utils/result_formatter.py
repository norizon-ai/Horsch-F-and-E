"""
Result formatting utilities for consistent output display.
"""

from typing import Dict, Any
from datetime import datetime


class ResultFormatter:
    """Utility class for formatting crawl results and output."""
    
    @staticmethod
    def print_header(title: str, width: int = 60) -> None:
        """Print a formatted header."""
        print("\n" + "=" * width)
        print(title)
        print("=" * width)
    
    @staticmethod
    def print_section(title: str, width: int = 40) -> None:
        """Print a formatted section header."""
        print(f"\n{title}")
        print("-" * width)
    
    @staticmethod
    def print_crawl_config(config: Dict[str, Any]) -> None:
        """
        Print crawl configuration in a formatted way.
        
        Args:
            config: Dictionary containing crawl configuration
        """
        ResultFormatter.print_header("CRAWL CONFIGURATION")
        
        # Format configuration items
        items = [
            ("URL", config.get('url', 'N/A')),
            ("Mode", config.get('mode', 'standard')),
            ("Max Pages", config.get('max_pages', 'unlimited')),
            ("Max Depth", config.get('max_depth', 'unlimited')),
            ("Include Subdomains", config.get('include_subdomains', False)),
            ("Use Sitemap", config.get('use_sitemap', True)),
        ]
        
        if config.get('allowed_domains'):
            items.append(("Allowed Domains", ', '.join(config['allowed_domains'])))
        
        for key, value in items:
            print(f"{key:.<20} {value}")
    
    @staticmethod
    def print_crawl_results(stats: Dict[str, Any], elapsed_seconds: float = None) -> None:
        """
        Print crawl results in a formatted way.
        
        Args:
            stats: Dictionary containing crawl statistics
            elapsed_seconds: Optional elapsed time in seconds
        """
        ResultFormatter.print_header("CRAWL COMPLETE")
        
        # Basic statistics
        print(f"Pages crawled: {stats.get('total_pages', 0)}")
        print(f"Successful: {stats.get('successful_pages', 0)}")
        print(f"Failed: {stats.get('failed_pages', 0)}")
        
        # Subdomains if present
        if 'domains_discovered' in stats:
            print(f"Domains discovered: {stats['domains_discovered']}")
        if 'domains_crawled' in stats:
            print(f"Domains crawled: {stats['domains_crawled']}")
        
        # Timing information
        if elapsed_seconds:
            print(f"Time elapsed: {elapsed_seconds:.1f} seconds")
            
            pages = stats.get('total_pages', 0)
            if pages > 0:
                avg_time = elapsed_seconds / pages
                print(f"Average time per page: {avg_time:.2f} seconds")
                print(f"Pages per second: {pages / elapsed_seconds:.2f}")
        elif 'duration_seconds' in stats:
            print(f"Duration: {stats['duration_seconds']:.1f} seconds")
            if 'pages_per_second' in stats:
                print(f"Average speed: {stats['pages_per_second']:.1f} pages/second")
        
        # Success rate
        if 'success_rate' in stats:
            print(f"Success rate: {stats['success_rate']*100:.1f}%")
        elif stats.get('total_pages'):
            success_rate = stats.get('successful_pages', 0) / stats['total_pages']
            print(f"Success rate: {success_rate*100:.1f}%")
    
    @staticmethod
    def print_domain_stats(stats: Dict[str, Any], limit: int = 10) -> None:
        """
        Print per-domain statistics.
        
        Args:
            stats: Dictionary containing statistics with 'pages_per_domain' key
            limit: Maximum number of domains to display
        """
        pages_per_domain = stats.get('pages_per_domain', {})
        if not pages_per_domain:
            return
        
        print("\nPages per domain:")
        sorted_domains = sorted(
            pages_per_domain.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:limit]
        
        for domain, count in sorted_domains:
            print(f"  {domain}: {count} pages")
    
    @staticmethod
    def print_progress(current: int, total: int, prefix: str = "Progress") -> None:
        """
        Print progress indicator.
        
        Args:
            current: Current count
            total: Total count
            prefix: Prefix for the progress message
        """
        if total > 0:
            percentage = (current / total) * 100
            print(f"  {prefix}: {current}/{total} ({percentage:.0f}%)")
        else:
            print(f"  {prefix}: {current}")
    
    @staticmethod
    def format_timestamp(dt: datetime = None) -> str:
        """
        Format a datetime object or current time as string.
        
        Args:
            dt: Datetime to format (uses current time if None)
            
        Returns:
            Formatted timestamp string
        """
        if dt is None:
            dt = datetime.now()
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        """
        Format duration in seconds to human-readable string.
        
        Args:
            seconds: Duration in seconds
            
        Returns:
            Formatted duration string (e.g., "2h 15m 30s")
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        if secs > 0 or not parts:
            parts.append(f"{secs}s")
        
        return " ".join(parts)