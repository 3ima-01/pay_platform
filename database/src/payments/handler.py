from aio_pika import IncomingMessage

from customers.dao import CustomersDAO
from customers.schemas import Customer


async def callback(message: IncomingMessage):
    body = message.body.decode("utf-8")

    await message.ack()
