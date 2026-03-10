"""
CLI trigger with unified crawl command.

Provides a single, flexible crawl command with clear mode options
instead of multiple overlapping commands.
"""

import argparse
import logging
from typing import Optional
from datetime import datetime

from triggers.base import TriggerBase
from publishers.factory import PublisherFactory
from config.settings import CrawlerSettings
from config.crawl_config import CrawlConfig, CrawlMode
from core.orchestrator import CrawlOrchestrator
from utils.domain_parser import DomainParser
from utils.result_formatter import ResultFormatter
from utils.statistics_reporter import StatisticsReporter

logger = logging.getLogger(__name__)


class CLITrigger(TriggerBase):
    """
    Command-line interface with unified crawl command.
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None):
        """Initialize CLI trigger."""
        super().__init__(settings)
        self.parser = self._create_parser()
        self.domain_parser = DomainParser()
        self.formatter = ResultFormatter()
        
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create simplified argument parser for CLI."""
        parser = argparse.ArgumentParser(
            description="Intranet Connector - Unified Web Crawling Service",
            epilog="Examples:\n"
                   "  %(prog)s crawl https://example.com                    # Basic crawl\n"
                   "  %(prog)s crawl https://example.com --discover         # Discover and crawl subdomains\n"
                   "  %(prog)s crawl https://example.com --max-pages 100    # Limited crawl\n"
                   "  %(prog)s crawl https://example.com --resume           # Resume previous crawl\n",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Command to run")
        
        # Unified crawl command
        crawl_parser = subparsers.add_parser(
            "crawl", 
            help="Crawl a website or domain",
            description="Flexible crawling with multiple modes and options"
        )
        
        # Required arguments
        crawl_parser.add_argument("url", help="Starting URL to crawl")
        
        # Crawl mode options
        mode_group = crawl_parser.add_argument_group("Crawl Mode")
        mode_group.add_argument(
            "--discover-subdomains", "-d", 
            action="store_true",
            help="Discover and crawl subdomains dynamically"
        )
        mode_group.add_argument(
            "--include-subdomains", "-i",
            action="store_true", 
            help="Include known subdomains in crawl scope"
        )
        
        # Scope limits
        scope_group = crawl_parser.add_argument_group("Scope Limits")
        scope_group.add_argument(
            "--max-pages", 
            type=int,
            help="Maximum pages to crawl (default: unlimited with --discover)"
        )
        scope_group.add_argument(
            "--max-depth",
            type=int,
            help=f"Maximum crawl depth (default: {self.settings.MAX_DEPTH if self.settings else 5})"
        )
        scope_group.add_argument(
            "--max-subdomains",
            type=int,
            help="Maximum subdomains to discover and crawl"
        )
        scope_group.add_argument(
            "--unlimited",
            action="store_true",
            help="Remove all limits (use with caution)"
        )
        
        # Crawl strategy
        strategy_group = crawl_parser.add_argument_group("Crawl Strategy")
        strategy_group.add_argument(
            "--deep",
            action="store_true",
            help="Use deep crawling without sitemap"
        )
        strategy_group.add_argument(
            "--domains",
            nargs="+",
            help="Explicit list of allowed domains"
        )
        
        # Resume and recrawl
        state_group = crawl_parser.add_argument_group("State Management")
        state_group.add_argument(
            "--resume",
            action="store_true",
            help="Resume from previous crawl state"
        )
        state_group.add_argument(
            "--force-recrawl",
            action="store_true",
            help="Force recrawl of already visited URLs"
        )
        
        # Output options
        output_group = crawl_parser.add_argument_group("Output Options")
        output_group.add_argument(
            "--output", "-o",
            choices=["file", "queue", "mock"],
            default="file",
            help="Output publisher type (default: file)"
        )
        output_group.add_argument(
            "--verbose", "-v",
            action="store_true",
            help="Enable verbose output"
        )
        
        # Utility commands (kept simple)
        subparsers.add_parser("list", help="List previous crawl sessions")
        
        estimate_parser = subparsers.add_parser("estimate", help="Estimate crawl scope")
        estimate_parser.add_argument("url", help="URL to analyze")
        
        return parser
    
    async def start(self) -> None:
        """Parse arguments and execute command."""
        args = self.parser.parse_args()
        
        if not args.command:
            self.parser.print_help()
            return
        
        self.is_running = True
        
        try:
            if args.command == "crawl":
                await self._handle_unified_crawl(args)
            elif args.command == "list":
                await self._handle_list(args)
            elif args.command == "estimate":
                await self._handle_estimate(args)
            else:
                self.parser.print_help()
        finally:
            self.is_running = False
    
    async def _handle_unified_crawl(self, args) -> None:
        """
        Handle the unified crawl command.
        
        This replaces both _handle_crawl and _handle_comprehensive with
        a single, cleaner implementation.
        """
        # Create crawl configuration from arguments, using settings for defaults
        config = CrawlConfig.from_args(args, self.settings)
        
        # Parse domains if not explicitly provided
        if not config.allowed_domains:
            config.allowed_domains = self.domain_parser.parse_allowed_domains(
                config.url, 
                args.domains
            )
        
        # Extract base domain for orchestrator (used in subdomain display)
        # base_domain = self.domain_parser.extract_base_domain(config.url)
        
        # Print configuration
        self.formatter.print_crawl_config(config.to_dict())
        
        # Get publisher
        publisher = PublisherFactory.create_publisher(self.settings, config.output_type)
        
        # Create orchestrator
        orchestrator = CrawlOrchestrator(self.settings, config.url)
        
        # Track timing
        start_time = datetime.now()
        
        # Execute crawl based on mode
        if config.mode == CrawlMode.DISCOVER or config.discover_subdomains:
            # Use comprehensive crawl for subdomain discovery
            stats = await orchestrator.orchestrate_comprehensive_crawl(
                publisher=publisher,
                max_subdomains=config.max_subdomains,
                resume=config.resume,
                force_recrawl=config.force_recrawl
            )
            
            # Display discovered subdomains
            discovered = orchestrator.get_discovered_subdomains()
            if discovered:
                print("\n📍 Discovered Subdomains:")
                for subdomain in sorted(discovered):
                    print(f"  • {subdomain}")
        else:
            # Simple crawl without subdomain discovery
            from core.crawler import IntranetCrawler
            from core.sitemap_crawler import SitemapCrawler
            
            # Update settings with config values for the crawl
            crawl_settings = self.settings.model_copy()
            if config.max_pages:
                crawl_settings.MAX_PAGES = config.max_pages
            if config.max_depth:
                crawl_settings.MAX_DEPTH = config.max_depth
            
            # Connect publisher first
            await publisher.connect()
            
            try:
                # Choose crawler based on sitemap preference
                if config.use_sitemap:
                    has_sitemap = await self._check_for_sitemap(config.url)
                    if has_sitemap:
                        print("📄 Using sitemap-based crawling")
                        # For sitemap crawler, we need to use the appropriate method
                        crawler = SitemapCrawler(crawl_settings)
                        stats = await crawler.crawl_from_sitemap(
                            config.url,
                            publisher,
                            include_subdomains=config.include_subdomains,
                            max_urls=config.max_pages
                        )
                    else:
                        crawler = IntranetCrawler(crawl_settings)
                        print("🔍 Using deep crawling (no sitemap found)")
                        stats = await crawler.crawl_and_publish(
                            config.url,
                            config.allowed_domains,
                            publisher
                        )
                else:
                    crawler = IntranetCrawler(crawl_settings)
                    print("🔍 Using deep crawling")
                    stats = await crawler.crawl_and_publish(
                        config.url,
                        config.allowed_domains,
                        publisher
                    )
            finally:
                await publisher.close()
        
        # Calculate elapsed time
        elapsed = (datetime.now() - start_time).total_seconds()
        
        # Print results
        self.formatter.print_crawl_results(stats, elapsed)
        
        print(f"\n✅ Crawl complete!")
    
    async def _check_for_sitemap(self, url: str) -> bool:
        """Check if a domain has a sitemap."""
        try:
            from core.sitemap_crawler import SitemapParser
            parser = SitemapParser(url)
            sitemaps = await parser.find_sitemaps()
            return len(sitemaps) > 0
        except Exception:
            return False
    
    async def _handle_list(self, _args) -> None:
        """Handle list sessions command."""
        from pathlib import Path
        import json
        
        storage_path = Path(self.settings.STORAGE_PATH)
        
        if not storage_path.exists():
            print(f"No crawl data found at {storage_path}")
            return
        
        sessions = []
        for session_dir in storage_path.iterdir():
            if session_dir.is_dir():
                stats_file = session_dir / "statistics.json"
                if stats_file.exists():
                    with open(stats_file, "r") as f:
                        stats = json.load(f)
                    sessions.append({
                        "id": session_dir.name,
                        "articles": stats.get("total_articles", 0),
                        "pages": stats.get("total_pages", 0),
                        "start": stats.get("session_start", session_dir.name)
                    })
        
        if not sessions:
            print("No crawl sessions found")
            return
        
        sessions.sort(key=lambda x: x["start"], reverse=True)
        
        self.formatter.print_header("CRAWL SESSIONS")
        print(f"{'Session ID':<25} {'Pages':<10} {'Articles':<10} {'Start Time':<30}")
        print("-" * 80)
        for session in sessions[:20]:
            print(f"{session['id']:<25} {session['pages']:<10} {session['articles']:<10} {session['start']:<30}")
    
    async def _handle_estimate(self, args) -> None:
        """Handle estimate command."""
        from utils.estimators import CrawlEstimator
        
        domains = self.domain_parser.parse_allowed_domains(args.url)
        
        estimator = CrawlEstimator(self.settings)
        await estimator.estimate(args.url, domains)
    
    async def stop(self) -> None:
        """Stop the CLI trigger."""
        self.is_running = False
        logger.info("CLI trigger stopped")
    
    def get_publisher(self):
        """Get publisher based on configuration."""
        publisher_type = getattr(self, '_publisher_type', self.settings.PUBLISHER_TYPE)
        return PublisherFactory.create_publisher(self.settings, publisher_type)