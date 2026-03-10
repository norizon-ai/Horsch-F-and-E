"""
Factory for creating crawler instances based on configuration.
"""

from typing import Dict, Any

from config.settings import CrawlerSettings


class CrawlerFactory:
    """
    Factory class for creating appropriate crawler instances.
    """
    
    @staticmethod
    def create_crawler(settings: CrawlerSettings, config: Dict[str, Any]):
        """
        Create a crawler instance based on configuration.
        
        Args:
            settings: Crawler settings
            config: Crawl configuration
            
        Returns:
            Crawler instance (IntranetCrawler or SitemapCrawler)
        """
        # Import here to avoid circular dependencies
        from core.crawler import IntranetCrawler
        from core.sitemap_crawler import SitemapCrawler
        
        # Determine crawler type
        if config.get('use_sitemap', settings.USE_SITEMAP):
            return SitemapCrawler(settings)
        else:
            return IntranetCrawler(settings)