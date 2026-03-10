import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from publishing.publisher_base import PublisherBase
from models.articles import RawArticle
from typing import List

class MockPublisher(PublisherBase):
    """
    A mock publisher for testing purposes.

    This class simulates the behavior of the DataPublisher without requiring a running
    RabbitMQ instance. It stores published messages in a list in memory, which can
    be inspected during tests.
    """

    def __init__(self, amqp_url: str, queue_name: str):
        """
        Initializes the MockPublisher.

        The parameters are kept for signature compatibility with the real DataPublisher,
        but they are not used in the mock implementation.

        Args:
            amqp_url (str): The connection URL for RabbitMQ (ignored).
            queue_name (str): The name of the queue to publish to (ignored).
        """
        self.messages: List[RawArticle] = []
        self.is_connected = False

    async def connect(self) -> None:
        """
        Simulates establishing a connection.
        """
        print("MockPublisher: Simulating connection.")
        self.is_connected = True

    async def publish_message(self, message: RawArticle) -> None:
        """
        Simulates publishing a message by appending it to an in-memory list.

        Args:
            message (RawArticle): The message to be "published".
        """
        if not self.is_connected:
            raise ConnectionError("Publisher is not connected. Call connect() first.")
        
        print(f"MockPublisher: Simulating publishing message to queue.")
        print("Received message: ", message, "...")
        self.messages.append(message)

    async def close(self) -> None:
        """
        Simulates closing the connection.
        """
        print("MockPublisher: Simulating connection close.")
        self.is_connected = False

    def get_published_messages(self) -> List[RawArticle]:
        """
        Returns the list of all messages that have been "published".

        This method is specific to the mock publisher and is used for test assertions.

        Returns:
            List[RawArticle]: A list of the published messages.
        """
        return self.messages

    def clear_messages(self) -> None:
        """
        Clears the in-memory list of published messages.

        This is useful for resetting the state between tests.
        """
        self.messages = []
