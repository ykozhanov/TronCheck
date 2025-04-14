# import os
# import sys
# from pathlib import Path
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

# # Добавляем путь к src в sys.path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
#
# # Устанавливаем переменную DEBUG
# os.environ["TESTING"] = "True"

# Подгружаем переменные из .env
load_dotenv()

from decimal import Decimal

import pytest
# from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from src.main import app
from src.core.db import Base, get_session
from src.models import TronInfo
from src.core.config import get_settings
from contextlib import asynccontextmanager

settings = get_settings()

engine = create_async_engine(
    settings.get_database_url(),
    echo=settings.DEBUG,
)

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# engine_test = create_async_engine(DATABASE_URL, echo=False)
# TestingSessionLocal = sessionmaker(
#     bind=engine_test, class_=AsyncSession, expire_on_commit=False
# )

# @pytest.fixture(scope="session", autouse=True)
# def app():
#     Base.metadata.create_all(engine)
#     yield _app
#     Base.metadata.drop_all(engine)
#     engine.dispose()

@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def override_get_session():
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
async def client(override_get_session):
    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c

@pytest.fixture
def item() -> TronInfo:
    return TronInfo(
        address="TR3MnVcj3APrAXx2wAY5M8H1tYYYYYYYYY",
        balance_trx=Decimal(100.500),
        bandwidth=100,
        energy_free=100,
    )

# @pytest.fixture
# async def new_tron_info(item) -> None:
#     async with AsyncSessionLocal() as session:
#         session.add(item)
#         await session.commit()
