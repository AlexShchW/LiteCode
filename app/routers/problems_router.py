from typing import Optional
from fastapi import APIRouter
from sqlalchemy import select

from app.database.database_access import async_session_maker
from app.database.problems_model import Problems


router = APIRouter(
    prefix="/problems",
    tags=["Problems"],
)

@router.get("")
async def get_problems(
    difficulty: Optional[str] = None,
    category: Optional[str] = None):
    async with async_session_maker() as session:
        query = select(Problems)
        result = await session.execute(query)
        return result.scalars().all()