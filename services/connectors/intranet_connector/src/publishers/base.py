"""
Base abstraction for all publisher types.

This module defines the interface that all publishers must implement.
"""

from abc import ABC, abstractmethod
from models.articles import RawArticle


class PublisherBase(ABC):
    """
    Abstract base class for data publishers.

    This class defines the interface that all publisher implementations (both real
    and mock) must adhere to, ensuring they are interchangeable.
    """

    @abstractmethod
    async def connect(self) -> None:
        """
        Establishes a connection to the output destination.
        
        This could be:
        - Opening file handles for file publishers
        - Connecting to message queue for queue publishers
        - Setting up database connections
        """
        pass

    @abstractmethod
    async def publish_message(self, message: RawArticle) -> None:
        """
        Publishes a message to the configured destination.

        Args:
            message (RawArticle): The message to be published.
        """
        pass

    @abstractmethod
    async def close(self) -> None:
        """
        Closes the connection and cleans up resources.
        """
        pass
    
    async def report_error(self, url: str, error: str) -> None:
        """
        Report a crawl error (optional implementation).
        
        Args:
            url: The URL that failed
            error: Error message
        """
        # Default implementation does nothing
        # Subclasses can override to provide error tracking
        pass