"""
Centralized configuration settings for the Intranet Connector.

This module defines all configuration parameters and loads them from
environment variables or configuration files.
"""

from pydantic_settings import BaseSettings
from typing import List, Optional, Dict, Any
import os


class CrawlerSettings(BaseSettings):
    """
    Defines the configuration for the Intranet Connector.
    
    Settings are loaded from environment variables with the CRAWLER_ prefix.
    """
    
    # --- Trigger Configuration ---
    TRIGGER_TYPE: str = "cli"  # Options: "cli", "queue", "cron", "api"
    
    # --- Publisher Configuration ---
    PUBLISHER_TYPE: str = "file"  # Options: "file", "queue", "mock"
    STORAGE_MODE: str = "file"  # Deprecated, use PUBLISHER_TYPE
    
    # --- Crawler Engine ---
    USE_PLAYWRIGHT: bool = False
    USE_STREAMING: bool = True  # Stream results as they arrive
    
    # --- Crawler Behavior ---
    STRATEGY: str = "bfs"  # Options: "bfs", "dfs", "best_first"
    MAX_DEPTH: int = 5
    MAX_PAGES: int = 200
    
    # --- Content Filtering ---
    EXCLUDED_TAGS: List[str] = ['form', 'header', 'footer', 'nav']
    EXCLUDE_EXTERNAL_LINKS: bool = True
    EXCLUDE_SOCIAL_MEDIA_LINKS: bool = True
    
    # --- Storage Configuration ---
    STORAGE_PATH: str = "./crawled_data"
    BATCH_SIZE: int = 10
    
    # --- Sitemap Crawling ---
    USE_SITEMAP: bool = True
    CRAWL_DELAY: float = 1.0
    RANDOM_DELAY: bool = True
    INCLUDE_SUBDOMAINS: bool = True
    
    # --- Comprehensive Crawling ---
    UNLIMITED_CRAWL: bool = False  # Set True for no page/depth limits
    COMPREHENSIVE_CRAWL: bool = False  # Enable comprehensive subdomain discovery
    
    # --- Message Queue Configuration ---
    RABBITMQ_URL: str = "amqp://test_user:test_pass@localhost:5672/"
    INPUT_QUEUE: str = "crawl.requested"
    OUTPUT_QUEUE: str = "content.raw.received"
    
    # --- Cron Configuration ---
    CRON_JOBS: List[Dict[str, Any]] = []
    
    # --- API Configuration ---
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_KEY: Optional[str] = None
    
    # --- Secrets ---
    AUTH_TOKEN: Optional[str] = None
    
    # --- Logging ---
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        # This prefix makes all environment variables start with CRAWLER_
        env_prefix = "CRAWLER_"
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"  # Allow extra fields from profiles
        
    @classmethod
    def from_profile(cls, profile: str) -> "CrawlerSettings":
        """
        Load settings from a specific profile.
        
        Args:
            profile: Profile name (dev, prod, test)
            
        Returns:
            Settings instance with profile configuration
        """
        profile_module = f"config.profiles.{profile}"
        try:
            import importlib
            module = importlib.import_module(profile_module)
            
            # Get profile defaults
            profile_defaults = {}
            for key in dir(module):
                if key.isupper() and not key.startswith("_"):
                    # Only use profile value if env var is not set
                    env_key = f"CRAWLER_{key}"
                    if env_key not in os.environ:
                        profile_defaults[key] = getattr(module, key)
            
            # Create instance - env vars will override any profile defaults
            return cls(**profile_defaults)
            
        except ImportError:
            # Profile not found, use defaults
            return cls()


# Global settings instance
settings = CrawlerSettings()

# Check for profile override
profile = os.getenv("CRAWLER_PROFILE")
if profile:
    settings = CrawlerSettings.from_profile(profile)