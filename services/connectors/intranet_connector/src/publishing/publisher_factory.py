"""
Factory for creating the appropriate publisher based on configuration.
"""

from typing import Optional
from config import CrawlerSettings
from publishing.publisher_base import PublisherBase
from publishing.publisher import DataPublisher
from publishing.file_storage_publisher import FileStoragePublisher, ParquetStoragePublisher
from testing.mock_publisher import MockPublisher


class PublisherFactory:
    """
    Factory class for creating publishers based on configuration.
    """
    
    @staticmethod
    def create_publisher(settings: Optional[CrawlerSettings] = None) -> PublisherBase:
        """
        Create a publisher based on the configured storage mode.
        
        Args:
            settings: Crawler settings (uses defaults if not provided)
            
        Returns:
            Publisher instance based on configuration
        """
        if settings is None:
            from config import settings
        
        storage_mode = settings.STORAGE_MODE.lower()
        
        if storage_mode == "rabbitmq":
            # Use the regular RabbitMQ publisher
            return DataPublisher(
                settings.RABBITMQ_URL,
                settings.OUTPUT_QUEUE
            )
        
        elif storage_mode == "file":
            # Use file-based storage
            return FileStoragePublisher(
                storage_path=settings.STORAGE_PATH,
                batch_size=settings.BATCH_SIZE
            )
        
        elif storage_mode == "parquet":
            # Use Parquet storage for better compression
            return ParquetStoragePublisher(
                storage_path=settings.STORAGE_PATH,
                batch_size=settings.BATCH_SIZE
            )
        
        elif storage_mode == "mock":
            # Use mock publisher for testing
            return MockPublisher(
                settings.RABBITMQ_URL,
                settings.OUTPUT_QUEUE
            )
        
        else:
            raise ValueError(
                f"Unknown storage mode: {storage_mode}. "
                f"Valid options: rabbitmq, file, parquet, mock"
            )
    
    @staticmethod
    def get_publisher_info(settings: Optional[CrawlerSettings] = None) -> dict:
        """
        Get information about the configured publisher.
        
        Args:
            settings: Crawler settings
            
        Returns:
            Dictionary with publisher information
        """
        if settings is None:
            from config import settings
        
        storage_mode = settings.STORAGE_MODE.lower()
        
        info = {
            "storage_mode": storage_mode,
            "description": ""
        }
        
        if storage_mode == "rabbitmq":
            info["description"] = f"RabbitMQ publisher to queue '{settings.OUTPUT_QUEUE}'"
            info["rabbitmq_url"] = settings.RABBITMQ_URL
            info["queue"] = settings.OUTPUT_QUEUE
        
        elif storage_mode in ["file", "parquet"]:
            format_name = "JSON" if storage_mode == "file" else "Parquet"
            info["description"] = f"{format_name} file storage at '{settings.STORAGE_PATH}'"
            info["storage_path"] = settings.STORAGE_PATH
            info["batch_size"] = settings.BATCH_SIZE
            info["format"] = format_name
        
        elif storage_mode == "mock":
            info["description"] = "Mock publisher (in-memory storage for testing)"
        
        return info