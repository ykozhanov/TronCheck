from dotenv import load_dotenv

# Подгружаем переменные из .env
load_dotenv()

from decimal import Decimal

import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app
from src.core.db import Base, engine, AsyncSessionLocal
from src.models import TronInfo
from src.schemas import TronInfoCreateSchema


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        yield c


@pytest.fixture
async def session():
    async with AsyncSessionLocal() as s:
        yield s


@pytest.fixture
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def tron_data() -> TronInfo:
    return TronInfo(
        address="TR3MnVcj3APrAXx2wAY5M8H1tYYYYYYYYY",
        balance_trx=Decimal(100.500),
        bandwidth=100,
        energy_free=100,
    )
