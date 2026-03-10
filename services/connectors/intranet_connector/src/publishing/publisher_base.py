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
        Establishes a connection to the message broker.
        """
        pass

    @abstractmethod
    async def publish_message(self, message: RawArticle) -> None:
        """
        Publishes a message.

        Args:
            message (RawArticle): The message to be published.
        """
        pass

    @abstractmethod
    async def close(self) -> None:
        """
        Closes the connection to the message broker.
        """
        pass
