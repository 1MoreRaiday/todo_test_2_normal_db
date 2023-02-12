import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from todo_test_2_normal_db import config

engine = create_async_engine(config.db_url)
Base = declarative_base()
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Task(Base):
    __tablename__ = 'tasks'

    id = sa.Column(sa.Integer, primary_key=True)

    title = sa.Column(sa.String, nullable=False)
    isDone = sa.Column(sa.Boolean, nullable=False)


__all__ = ['engine', 'Base', 'async_session', 'Task']
