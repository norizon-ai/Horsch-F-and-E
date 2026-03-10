"""
Message queue trigger for automated crawling.

This trigger listens to a RabbitMQ queue for crawl job requests.
"""

import asyncio
import json
import logging
from typing import Optional, Dict, Any

import aio_pika
from aio_pika.abc import AbstractIncomingMessage

from triggers.base import TriggerBase
from publishers.base import PublisherBase
from publishers.factory import PublisherFactory
from config.settings import CrawlerSettings
from models.communication import CrawlJob

logger = logging.getLogger(__name__)


class QueueTrigger(TriggerBase):
    """
    Message queue trigger that listens for crawl jobs from RabbitMQ.
    """
    
    def __init__(self, settings: Optional[CrawlerSettings] = None,
                 amqp_url: Optional[str] = None,
                 input_queue: Optional[str] = None):
        """
        Initialize queue trigger.
        
        Args:
            settings: Crawler settings
            amqp_url: RabbitMQ connection URL
            input_queue: Queue name to listen on
        """
        super().__init__(settings)
        self.amqp_url = amqp_url or settings.RABBITMQ_URL
        self.input_queue = input_queue or settings.INPUT_QUEUE
        self.connection = None
        self.channel = None
        self.queue = None
        
    async def start(self) -> None:
        """Start listening to the message queue."""
        logger.info(f"Starting queue trigger on {self.input_queue}")
        self.is_running = True
        
        try:
            # Connect to RabbitMQ
            self.connection = await aio_pika.connect_robust(self.amqp_url)
            self.channel = await self.connection.channel()
            
            # Declare queue
            self.queue = await self.channel.declare_queue(
                self.input_queue,
                durable=True
            )
            
            # Start consuming messages
            await self.queue.consume(self._process_message)
            
            logger.info(f"Queue trigger listening on {self.input_queue}")
            
            # Keep running until stopped
            while self.is_running:
                await asyncio.sleep(1)
                
        except Exception as e:
            logger.error(f"Queue trigger error: {e}")
            raise
        finally:
            await self.stop()
    
    async def stop(self) -> None:
        """Stop the queue trigger and close connections."""
        logger.info("Stopping queue trigger")
        self.is_running = False
        
        if self.connection and not self.connection.is_closed:
            await self.connection.close()
        
        logger.info("Queue trigger stopped")
    
    def get_publisher(self) -> PublisherBase:
        """Get publisher configured for queue output."""
        # Queue trigger typically uses queue publisher for output
        return PublisherFactory.create_publisher(self.settings, "queue")
    
    async def _process_message(self, message: AbstractIncomingMessage) -> None:
        """
        Process a message from the queue.
        
        Args:
            message: Incoming message from RabbitMQ
        """
        async with message.process():
            try:
                # Parse message
                body = message.body.decode('utf-8')
                logger.info(f"Received message: {body[:100]}...")
                
                # Parse as CrawlJob
                job_data = json.loads(body)
                job = CrawlJob(**job_data)
                
                # Convert to crawl configuration
                crawl_config = self._job_to_config(job)
                
                # Validate configuration
                self.validate_config(crawl_config)
                
                # Execute crawl
                logger.info(f"Processing crawl job: {job.job_id}")
                results = await self.execute_crawl(crawl_config)
                
                # Log results
                logger.info(f"Job {job.job_id} completed: {results}")
                
                # Optionally send completion message
                if hasattr(job, 'callback_queue') and job.callback_queue:
                    await self._send_completion(job, results)
                
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in message: {e}")
                await message.reject(requeue=False)
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                await message.reject(requeue=True)
    
    def _job_to_config(self, job: CrawlJob) -> Dict[str, Any]:
        """
        Convert a CrawlJob to crawl configuration.
        
        Args:
            job: CrawlJob from message queue
            
        Returns:
            Crawl configuration dictionary
        """
        config = {
            "url": job.target_url,
            "allowed_domains": job.allowed_domains or [],
            "max_pages": job.max_pages or self.settings.MAX_PAGES,
            "max_depth": job.max_depth or self.settings.MAX_DEPTH
        }
        
        # Add optional parameters
        if hasattr(job, 'use_sitemap'):
            config["use_sitemap"] = job.use_sitemap
        if hasattr(job, 'include_subdomains'):
            config["include_subdomains"] = job.include_subdomains
        if hasattr(job, 'crawl_delay'):
            config["crawl_delay"] = job.crawl_delay
        
        return config
    
    async def _send_completion(self, job: CrawlJob, results: Dict[str, Any]) -> None:
        """
        Send completion message for a job.
        
        Args:
            job: Original crawl job
            results: Crawl results
        """
        try:
            completion_message = {
                "job_id": job.job_id,
                "status": "completed",
                "results": results,
                "timestamp": datetime.now().isoformat()
            }
            
            # Publish to callback queue
            await self.channel.default_exchange.publish(
                aio_pika.Message(
                    body=json.dumps(completion_message).encode(),
                    content_type="application/json"
                ),
                routing_key=job.callback_queue
            )
            
            logger.info(f"Sent completion message for job {job.job_id}")
            
        except Exception as e:
            logger.error(f"Failed to send completion message: {e}")