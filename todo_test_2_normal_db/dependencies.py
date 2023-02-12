from sqlalchemy.ext.asyncio import AsyncSession
from todo_test_2_normal_db.models import async_session


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
