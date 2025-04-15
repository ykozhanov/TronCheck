from sqlalchemy import select

from src.models import TronInfo
from src.repositories import AsyncSQLAlchemyHistoryRepository


async def test_create_tron_info(setup_db, session, tron_data):
    repo = AsyncSQLAlchemyHistoryRepository(session)
    created = await repo.create(tron_data)

    assert created.address == tron_data.address
    assert created.balance_trx == tron_data.balance_trx
    assert created.bandwidth == tron_data.bandwidth
    assert created.energy_free == tron_data.energy_free

    result = await session.execute(
        select(TronInfo).where(TronInfo.address == tron_data.address)
    )
    db_item = result.scalar_one_or_none()

    assert db_item is not None
    assert db_item.address == tron_data.address
