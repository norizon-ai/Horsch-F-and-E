#!/usr/bin/env python3
"""
Main entry point for the Intranet Connector service.

This module provides a unified interface for running the connector
with different triggers (CLI, Queue, Cron, API) and publishers (File, Queue, Mock).

Usage:
    # CLI mode (default)
    python main.py crawl https://example.com
    
    # Queue listener mode
    CRAWLER_TRIGGER_TYPE=queue python main.py
    
    # Cron scheduler mode
    CRAWLER_TRIGGER_TYPE=cron python main.py
    
    # With specific profile
    CRAWLER_PROFILE=prod python main.py
"""

import asyncio
import logging
import signal
import sys
import os
from typing import Optional

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import CrawlerSettings, settings
from triggers import CLITrigger, QueueTrigger, CronTrigger

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format=settings.LOG_FORMAT
)
logger = logging.getLogger(__name__)


class IntranetConnectorService:
    """
    Main service class that orchestrates triggers and publishers.
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None):
        """
        Initialize the service.
        
        Args:
            settings: Configuration settings
        """
        self.settings = settings or CrawlerSettings()
        self.trigger = None
        self.shutdown_event = asyncio.Event()
        
    async def start(self) -> None:
        """Start the service with configured trigger."""
        logger.info(f"Starting Intranet Connector Service")
        logger.info(f"Profile: {os.getenv('CRAWLER_PROFILE', 'default')}")
        logger.info(f"Trigger: {self.settings.TRIGGER_TYPE}")
        logger.info(f"Publisher: {self.settings.PUBLISHER_TYPE}")
        
        try:
            # Create trigger based on configuration
            self.trigger = self._create_trigger()
            
            # Set up signal handlers
            self._setup_signal_handlers()
            
            # Start the trigger
            await self.trigger.start()
            
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt")
        except Exception as e:
            logger.error(f"Service error: {e}")
            raise
        finally:
            await self.stop()
    
    async def stop(self) -> None:
        """Stop the service gracefully."""
        logger.info("Stopping Intranet Connector Service")
        
        if self.trigger:
            await self.trigger.stop()
        
        self.shutdown_event.set()
        logger.info("Service stopped")
    
    def _create_trigger(self):
        """
        Create trigger based on configuration.
        
        Returns:
            Trigger instance
        """
        trigger_type = self.settings.TRIGGER_TYPE.lower()
        
        if trigger_type == "cli":
            return CLITrigger(self.settings)
        elif trigger_type == "queue":
            return QueueTrigger(self.settings)
        elif trigger_type == "cron":
            # Load cron jobs from settings or environment
            cron_jobs = self._load_cron_jobs()
            return CronTrigger(self.settings, cron_jobs)
        elif trigger_type == "api":
            # API trigger to be implemented
            raise NotImplementedError("API trigger not yet implemented")
        else:
            raise ValueError(f"Unknown trigger type: {trigger_type}")
    
    def _load_cron_jobs(self):
        """
        Load cron jobs from configuration.
        
        Returns:
            List of cron job configurations
        """
        # First check settings
        if self.settings.CRON_JOBS:
            return self.settings.CRON_JOBS
        
        # Check environment for simple configuration
        if os.getenv("CRON_SCHEDULE") and os.getenv("CRON_URL"):
            return [{
                "name": "default",
                "schedule": os.getenv("CRON_SCHEDULE"),
                "config": {
                    "url": os.getenv("CRON_URL"),
                    "max_pages": int(os.getenv("CRON_MAX_PAGES", "100")),
                    "use_sitemap": os.getenv("CRON_USE_SITEMAP", "true").lower() == "true"
                }
            }]
        
        # Default example jobs for testing
        return [{
            "name": "test_crawl",
            "schedule": "*/5 * * * *",  # Every 5 minutes
            "config": {
                "url": "https://example.com",
                "max_pages": 10,
                "use_sitemap": False
            }
        }]
    
    def _setup_signal_handlers(self):
        """Set up signal handlers for graceful shutdown."""
        def signal_handler(signum, frame):
            logger.info(f"Received signal {signum}")
            asyncio.create_task(self.stop())
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


async def main():
    """Main entry point."""
    # Print banner
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           INTRANET CONNECTOR SERVICE                     ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # Load configuration
    profile = os.getenv("CRAWLER_PROFILE")
    if profile:
        logger.info(f"Loading profile: {profile}")
        service_settings = CrawlerSettings.from_profile(profile)
    else:
        service_settings = settings
    
    # Create and start service
    service = IntranetConnectorService(service_settings)
    
    try:
        await service.start()
    except Exception as e:
        logger.error(f"Service failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the service
    asyncio.run(main())