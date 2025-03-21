from aio_pika import connect_robust
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # CUSTOMERS
    CUSTOMERS_URL: str

    # PAYADMIT
    PAYADMIT_URL: str
    PAYADMIT_KEY: str

    # RABBITMQ
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    @property
    async def RABBITMQ_CONNECTION(self):
        return await connect_robust(
            host=self.RABBITMQ_HOST,
            port=self.RABBITMQ_PORT,
            login=self.RABBITMQ_USER,
            password=self.RABBITMQ_PASS,
        )

    model_config = SettingsConfigDict(env_file="./.env")


settings = Settings()
