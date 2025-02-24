from app.database_access import async_session_maker

from sqlalchemy import select, insert

from app.models.users_model import Users

class UsersDAO:
    
    @classmethod
    async def find_by_email(cls, email: str):
        async with async_session_maker() as session:
            query = select(Users).filter_by(email=email)
            result = await session.execute(query)
            return result.scalars().one_or_none()

    @classmethod
    async def find_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(Users).filter_by(id=id)
            result = await session.execute(query)
            return result.scalars().one_or_none()

    @classmethod
    async def create_user(cls, email: str, hashed_password: str):
        async with async_session_maker() as session:
            query = insert(Users).values(email=email, hashed_password=hashed_password)
            await session.execute(query)
            await session.commit()