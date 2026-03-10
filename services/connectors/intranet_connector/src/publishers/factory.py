"""
Factory for creating publisher instances.
"""

from typing import Optional

from config.settings import CrawlerSettings
from publishers.base import PublisherBase


class PublisherFactory:
    """
    Factory class for creating publishers based on configuration.
    """
    
    @staticmethod
    def create_publisher(settings: Optional[CrawlerSettings] = None, 
                        publisher_type: Optional[str] = None) -> PublisherBase:
        """
        Create a publisher based on configuration.
        
        Args:
            settings: Crawler settings (uses defaults if not provided)
            publisher_type: Override publisher type (uses settings if not provided)
            
        Returns:
            Publisher instance based on configuration
        """
        if settings is None:
            from config.settings import settings as default_settings
            settings = default_settings
        
        # Determine publisher type
        if publisher_type is None:
            publisher_type = settings.PUBLISHER_TYPE or settings.STORAGE_MODE
        
        publisher_type = publisher_type.lower()
        
        if publisher_type == "queue" or publisher_type == "rabbitmq":
            # Use the regular RabbitMQ publisher
            from publishing.publisher import DataPublisher
            return DataPublisher(
                settings.RABBITMQ_URL,
                settings.OUTPUT_QUEUE
            )
        
        elif publisher_type == "file":
            # Use file-based storage
            from publishing.file_storage_publisher import FileStoragePublisher
            return FileStoragePublisher(
                storage_path=settings.STORAGE_PATH,
                batch_size=settings.BATCH_SIZE
            )
        
        elif publisher_type == "parquet":
            # Use Parquet storage for better compression
            from publishing.file_storage_publisher import ParquetStoragePublisher
            return ParquetStoragePublisher(
                storage_path=settings.STORAGE_PATH,
                batch_size=settings.BATCH_SIZE
            )
        
        elif publisher_type == "mock":
            # Use mock publisher for testing
            from testing.mock_publisher import MockPublisher
            return MockPublisher(
                settings.RABBITMQ_URL,
                settings.OUTPUT_QUEUE
            )
        
        else:
            raise ValueError(
                f"Unknown publisher type: {publisher_type}. "
                f"Valid options: queue, file, parquet, mock"
            )