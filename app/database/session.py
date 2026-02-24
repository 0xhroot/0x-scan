from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import declarative_base
import os

# 🔥 ADD THIS
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://reconuser:password@localhost:5432/recon"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
