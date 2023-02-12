from fastapi import FastAPI
import asyncio

from todo_test_2_normal_db.models import *
from todo_test_2_normal_db import routes

app = FastAPI()
app.include_router(routes.router)
