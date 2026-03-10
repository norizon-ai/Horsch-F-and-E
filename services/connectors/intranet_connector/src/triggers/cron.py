"""
Cron trigger for scheduled crawling.

This trigger executes crawls based on cron schedules.
"""

import asyncio
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
from croniter import croniter

from triggers.base import TriggerBase
from publishers.base import PublisherBase
from publishers.factory import PublisherFactory
from config.settings import CrawlerSettings

logger = logging.getLogger(__name__)


class CronJob:
    """Represents a scheduled crawl job."""
    
    def __init__(self, name: str, schedule: str, config: Dict[str, Any]):
        """
        Initialize a cron job.
        
        Args:
            name: Job name for identification
            schedule: Cron expression (e.g., "0 2 * * *" for 2 AM daily)
            config: Crawl configuration
        """
        self.name = name
        self.schedule = schedule
        self.config = config
        self.cron = croniter(schedule, datetime.now())
        self.next_run = self.cron.get_next(datetime)
        
    def should_run(self) -> bool:
        """Check if job should run now."""
        return datetime.now() >= self.next_run
    
    def update_next_run(self):
        """Update next run time after execution."""
        self.next_run = self.cron.get_next(datetime)


class CronTrigger(TriggerBase):
    """
    Cron-based trigger for scheduled crawl execution.
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None,
                 jobs: Optional[List[Dict[str, Any]]] = None):
        """
        Initialize cron trigger.
        
        Args:
            settings: Crawler settings
            jobs: List of cron job configurations, each containing:
                - name: Job identifier
                - schedule: Cron expression
                - config: Crawl configuration
        """
        super().__init__(settings)
        self.jobs: List[CronJob] = []
        
        # Load jobs from configuration or parameter
        if jobs:
            for job_config in jobs:
                self.add_job(
                    job_config['name'],
                    job_config['schedule'],
                    job_config['config']
                )
        else:
            # Load from settings if available
            self._load_jobs_from_settings()
    
    def add_job(self, name: str, schedule: str, config: Dict[str, Any]) -> None:
        """
        Add a cron job.
        
        Args:
            name: Job name
            schedule: Cron expression
            config: Crawl configuration
        """
        try:
            job = CronJob(name, schedule, config)
            self.jobs.append(job)
            logger.info(f"Added cron job '{name}' with schedule '{schedule}'")
            logger.info(f"Next run: {job.next_run}")
        except Exception as e:
            logger.error(f"Failed to add cron job '{name}': {e}")
            raise
    
    async def start(self) -> None:
        """Start the cron scheduler."""
        if not self.jobs:
            logger.warning("No cron jobs configured")
            return
        
        logger.info(f"Starting cron trigger with {len(self.jobs)} jobs")
        self.is_running = True
        
        # Print job schedule
        print("\n" + "=" * 60)
        print("CRON JOBS SCHEDULED")
        print("=" * 60)
        for job in self.jobs:
            print(f"Job: {job.name}")
            print(f"  Schedule: {job.schedule}")
            print(f"  Next run: {job.next_run}")
            print(f"  URL: {job.config.get('url')}")
        print("=" * 60 + "\n")
        
        try:
            while self.is_running:
                # Check each job
                for job in self.jobs:
                    if job.should_run():
                        await self._execute_job(job)
                
                # Sleep for a short interval before checking again
                await asyncio.sleep(30)  # Check every 30 seconds
                
        except asyncio.CancelledError:
            logger.info("Cron trigger cancelled")
        except Exception as e:
            logger.error(f"Cron trigger error: {e}")
            raise
        finally:
            await self.stop()
    
    async def stop(self) -> None:
        """Stop the cron trigger."""
        logger.info("Stopping cron trigger")
        self.is_running = False
    
    def get_publisher(self) -> PublisherBase:
        """Get publisher for cron jobs."""
        # Use configured publisher type
        return PublisherFactory.create_publisher(self.settings)
    
    async def _execute_job(self, job: CronJob) -> None:
        """
        Execute a cron job.
        
        Args:
            job: CronJob to execute
        """
        try:
            logger.info(f"Executing cron job '{job.name}'")
            print(f"\n[{datetime.now()}] Running scheduled job: {job.name}")
            
            # Validate configuration
            self.validate_config(job.config)
            
            # Execute crawl
            start_time = datetime.now()
            results = await self.execute_crawl(job.config)
            elapsed = (datetime.now() - start_time).total_seconds()
            
            # Log results
            logger.info(f"Job '{job.name}' completed in {elapsed:.1f}s: {results}")
            print(f"Job '{job.name}' completed:")
            print(f"  Pages crawled: {results.get('published_count', 0)}")
            print(f"  Failed: {results.get('failed_count', 0)}")
            print(f"  Duration: {elapsed:.1f} seconds")
            
            # Update next run time
            job.update_next_run()
            print(f"  Next run: {job.next_run}")
            
        except Exception as e:
            logger.error(f"Error executing job '{job.name}': {e}")
            print(f"ERROR: Job '{job.name}' failed: {e}")
            
            # Still update next run time
            job.update_next_run()
    
    def _load_jobs_from_settings(self) -> None:
        """Load cron jobs from settings/environment."""
        # Check for CRON_JOBS in settings
        if hasattr(self.settings, 'CRON_JOBS'):
            for job_config in self.settings.CRON_JOBS:
                self.add_job(
                    job_config['name'],
                    job_config['schedule'],
                    job_config['config']
                )
        
        # Also check environment for simple single job
        import os
        if os.getenv('CRON_SCHEDULE') and os.getenv('CRON_URL'):
            self.add_job(
                "default",
                os.getenv('CRON_SCHEDULE'),
                {
                    "url": os.getenv('CRON_URL'),
                    "max_pages": int(os.getenv('CRON_MAX_PAGES', '100')),
                    "use_sitemap": os.getenv('CRON_USE_SITEMAP', 'true').lower() == 'true'
                }
            )


# Example usage configuration
EXAMPLE_CRON_JOBS = [
    {
        "name": "daily_fau_crawl",
        "schedule": "0 2 * * *",  # 2 AM daily
        "config": {
            "url": "https://www.fau.de",
            "allowed_domains": ["fau.de", "www.fau.de"],
            "max_pages": 500,
            "use_sitemap": True
        }
    },
    {
        "name": "weekly_full_crawl", 
        "schedule": "0 3 * * 0",  # 3 AM Sunday
        "config": {
            "url": "https://www.fau.de",
            "allowed_domains": ["fau.de", "www.fau.de"],
            "max_pages": 5000,
            "use_sitemap": True,
            "include_subdomains": True
        }
    }
]