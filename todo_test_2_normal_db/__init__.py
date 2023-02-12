from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from todo_test_2_normal_db.models import *
from todo_test_2_normal_db import routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(routes.router)
