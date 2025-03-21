import asyncio
from customers.consumer import resive_message as resive_message_customers


if __name__ == "__main__":
    asyncio.run(resive_message_customers())
