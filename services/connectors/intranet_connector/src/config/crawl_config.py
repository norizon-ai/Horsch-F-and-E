"""
Unified crawl configuration model.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, List


class CrawlMode(Enum):
    """Crawl mode enumeration."""
    SINGLE_DOMAIN = "single"          # Crawl only the specified domain
    WITH_SUBDOMAINS = "subdomains"    # Include known subdomains
    DISCOVER = "discover"              # Discover and crawl subdomains dynamically
    

@dataclass
class CrawlConfig:
    """
    Unified configuration for all crawl types.
    
    This replaces the multiple overlapping configuration approaches
    with a single, clear configuration model.
    """
    # Required fields
    url: str
    mode: CrawlMode = CrawlMode.SINGLE_DOMAIN
    
    # Scope limits
    max_pages: Optional[int] = None      # None means unlimited
    max_depth: Optional[int] = None      # Maximum crawl depth
    max_subdomains: Optional[int] = None # Maximum subdomains to discover
    
    # Crawl behavior
    use_sitemap: bool = True             # Try sitemap first
    discover_subdomains: bool = False    # Discover new subdomains during crawl
    include_subdomains: bool = False     # Include subdomains in scope
    
    # Resume and recrawl
    resume: bool = False                 # Resume from previous state
    force_recrawl: bool = False          # Force recrawl of visited URLs
    
    # Performance
    crawl_delay: float = 1.0             # Delay between requests
    batch_size: int = 10                 # Batch size for concurrent requests
    timeout: int = 120                   # Request timeout in seconds
    
    # Domain filtering
    allowed_domains: Optional[List[str]] = None  # Explicit domain list
    
    # Output
    output_type: str = "file"            # Publisher type
    
    @property
    def is_unlimited(self) -> bool:
        """Check if crawl has unlimited scope."""
        return self.max_pages is None and self.max_depth is None
    
    @property
    def should_discover(self) -> bool:
        """Check if subdomain discovery is enabled."""
        return self.mode == CrawlMode.DISCOVER or self.discover_subdomains
    
    @classmethod
    def from_args(cls, args, settings=None) -> 'CrawlConfig':
        """
        Create CrawlConfig from CLI arguments.
        
        Args:
            args: Parsed command line arguments
            settings: Optional CrawlerSettings to use for defaults
            
        Returns:
            CrawlConfig instance
        """
        # Check if settings provide defaults for subdomains
        default_include_subdomains = settings.INCLUDE_SUBDOMAINS if settings else False
        
        # Check if the argument was explicitly provided on command line
        # Since it's action="store_true", it will be False if not provided
        # We need to check if the user explicitly passed --include-subdomains
        # If they didn't, we should use the settings default
        # Unfortunately with store_true, we can't distinguish between not provided and explicitly False
        # So we'll use the settings default only if the CLI value is False
        cli_include_subdomains = getattr(args, 'include_subdomains', False)
        
        # Use settings default if CLI didn't explicitly set it
        # This assumes users won't pass --no-include-subdomains (which doesn't exist)
        final_include_subdomains = cli_include_subdomains or default_include_subdomains
        
        # Determine mode based on flags and settings
        if getattr(args, 'discover_subdomains', False):
            mode = CrawlMode.DISCOVER
        elif final_include_subdomains:
            mode = CrawlMode.WITH_SUBDOMAINS
        else:
            mode = CrawlMode.SINGLE_DOMAIN
        
        # Use settings for defaults if available
        default_max_depth = settings.MAX_DEPTH if settings else 5
        default_max_pages = settings.MAX_PAGES if settings else None
        default_use_sitemap = settings.USE_SITEMAP if settings else True
        
        # Build config
        config = cls(
            url=args.url,
            mode=mode,
            max_pages=getattr(args, 'max_pages', None) or default_max_pages,
            max_depth=getattr(args, 'max_depth', None) or default_max_depth,
            max_subdomains=getattr(args, 'max_subdomains', None),
            use_sitemap=not getattr(args, 'deep', False) if hasattr(args, 'deep') else default_use_sitemap,
            discover_subdomains=getattr(args, 'discover_subdomains', False),
            include_subdomains=final_include_subdomains,
            resume=getattr(args, 'resume', False),
            force_recrawl=getattr(args, 'force_recrawl', False),
            output_type=getattr(args, 'output', 'file')
        )
        
        # Handle unlimited flag
        if getattr(args, 'unlimited', False):
            config.max_pages = None
            config.max_depth = None
        
        return config
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            'url': self.url,
            'mode': self.mode.value,
            'max_pages': self.max_pages,
            'max_depth': self.max_depth,
            'max_subdomains': self.max_subdomains,
            'use_sitemap': self.use_sitemap,
            'discover_subdomains': self.discover_subdomains,
            'include_subdomains': self.include_subdomains,
            'resume': self.resume,
            'force_recrawl': self.force_recrawl,
            'allowed_domains': self.allowed_domains,
            'output_type': self.output_type
        }