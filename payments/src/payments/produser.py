from aio_pika import Message, DeliveryMode
from src.config import settings


async def send_message(message):
    connection = await settings.RABBITMQ_CONNECTION
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("payments", durable=True)
        message_body = message
        await channel.default_exchange.publish(
            Message(
                body=message_body.encode(),
                delivery_mode=DeliveryMode.PERSISTENT,
            ),
            routing_key=queue.name,
        )
