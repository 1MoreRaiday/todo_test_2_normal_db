from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from todo_test_2_normal_db.models import Task
from todo_test_2_normal_db.dependencies import get_session


router = APIRouter(prefix='/items')


@router.get('/')
async def get_all(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    return result.scalars().all()


class RegistrationRequest(BaseModel):
    title: str
    isDone: bool = False


@router.post('/create')
async def create(req: RegistrationRequest, session: AsyncSession = Depends(get_session)):
    task = Task(title=req.title, isDone=req.isDone)
    session.add(task)
    await session.commit()
    return task


class UpdateRequest(BaseModel):
    id: int
    title: Optional[str]
    isDone: Optional[bool]


@router.post('/update')
async def update(req: UpdateRequest, session: AsyncSession = Depends(get_session)):
    task = await session.execute(select(Task).where(Task.id == req.id))
    task = task.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail='not found')
    if req.title is not None:
        task.title = req.title
    if req.isDone is not None:
        task.isDone = req.isDone
    print(req)
    print(task.title, task.isDone)
    await session.commit()
    return task


class DeleteRequest(BaseModel):
    id: int


@router.post('/delete', status_code=204)
async def delete(req: DeleteRequest, session: AsyncSession = Depends(get_session)):
    task = await session.execute(select(Task).where(Task.id == req.id))
    task = task.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail='not found')
    await session.delete(task)
    await session.commit()
