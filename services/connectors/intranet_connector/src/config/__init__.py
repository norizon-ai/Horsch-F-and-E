"""
Configuration module for the Intranet Connector.

Provides centralized configuration management with profile support.
"""

from config.settings import CrawlerSettings, settings
from config.crawl_config import CrawlConfig, CrawlMode

__all__ = ['CrawlerSettings', 'settings', 'CrawlConfig', 'CrawlMode']