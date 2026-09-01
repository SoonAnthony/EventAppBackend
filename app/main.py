from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from .core.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    print("DB connected")
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)