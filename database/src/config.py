from aio_pika import connect_robust
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # POSTGRESQL
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

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

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
