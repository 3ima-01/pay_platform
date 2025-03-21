from aio_pika import IncomingMessage

from customers.dao import CustomersDAO
from customers.schemas import Customer


async def callback(message: IncomingMessage):
    body = message.body.decode("utf-8")
    print(body)
    user_data: Customer = Customer.model_validate_json(body)
    new_customer = await CustomersDAO.add(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone=user_data.phone,
        password=user_data.password,
    )
    print(new_customer)
    await message.ack()
