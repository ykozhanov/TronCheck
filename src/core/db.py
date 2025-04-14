from typing import AsyncGenerator, Dict
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from src.core.config import get_settings

settings = get_settings()


def get_connect_args(testing: bool = settings.TESTING) -> Dict:
    if testing:
        return {}
    return {
        "server_settings": {
            "timezone": "UTC",
        }
    }


engine = create_async_engine(
    settings.get_database_url(),
    echo=settings.DEBUG,
    connect_args=get_connect_args(),
)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
