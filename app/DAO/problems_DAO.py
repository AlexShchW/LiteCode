from app.database_access import async_session_maker

from sqlalchemy import select

from app.models.problems_model import Problems

class ProblemsDAO:

    @classmethod
    async def find_all(cls, **filters):
        async with async_session_maker() as session:
            query = select(Problems).filter_by(**filters)
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def find_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(Problems).filter_by(id=id)
            result = await session.execute(query)
            return result.scalars().one_or_none()
