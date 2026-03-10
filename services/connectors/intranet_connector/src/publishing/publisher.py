from publishing.publisher_base import PublisherBase
from models.articles import RawArticle
import aio_pika
import json

class DataPublisher(PublisherBase):
    """
    A class to handle publishing messages to a RabbitMQ queue.
    """

    def __init__(self, amqp_url: str, queue_name: str):
        """
        Initializes the DataPublisher with RabbitMQ connection parameters.
        Args:
            amqp_url (str): The connection URL for RabbitMQ.
            queue_name (str): The name of the queue to publish to.
        """
        self.amqp_url = amqp_url
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    async def connect(self) -> None:
        """
        Establishes a connection to RabbitMQ and declares the queue.
        """
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()
        await self.channel.declare_queue(self.queue_name, durable=True)

    async def publish_message(self, message: RawArticle) -> None:
        """
        Publishes a message to the configured RabbitMQ queue.
        Args:
            message (RawArticle): The message to be published.
        """
        if not self.channel:
            raise ConnectionError("Publisher is not connected. Call connect() first.")

        # Serialize the Pydantic model to a JSON string
        message_body = message.model_dump_json().encode()

        await self.channel.default_exchange.publish(
            aio_pika.Message(body=message_body),
            routing_key=self.queue_name,
        )

    async def close(self) -> None:
        """
        Closes the connection to RabbitMQ.
        """
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()
