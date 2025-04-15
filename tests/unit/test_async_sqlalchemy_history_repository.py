from sqlalchemy import select

from src.models import TronInfo
from src.repositories import AsyncSQLAlchemyHistoryRepository
from src.schemas import TronInfoCreateSchema


async def test_create_tron_info(setup_db, session, tron_data):
    tron_schema = TronInfoCreateSchema(**tron_data)
    repo = AsyncSQLAlchemyHistoryRepository(session)
    created = await repo.create(tron_schema)

    assert created.address == tron_schema.address
    assert created.balance_trx == tron_schema.balance_trx
    assert created.bandwidth == tron_schema.bandwidth
    assert created.energy_free == tron_schema.energy_free

    result = await session.execute(
        select(TronInfo).where(TronInfo.address == tron_schema.address)
    )
    db_item = result.scalar_one_or_none()

    assert db_item is not None
    assert db_item.address == tron_schema.address
