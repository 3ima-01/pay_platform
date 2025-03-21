from config import settings
from customers.handler import callback


async def resive_message():
    connection = await settings.RABBITMQ_CONNECTION
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("customers", durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                await callback(message)
