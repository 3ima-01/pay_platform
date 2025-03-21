from sqlalchemy import select, insert, delete

from database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        query = insert(cls.model).values(**data).returning(cls.model.uuid)
        async with async_session_maker() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
