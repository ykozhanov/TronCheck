from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.interfaces import AsyncHistoryRepositoryInterface
from src.models import TronAddressInfo, TronAddressInfoSQLAlchemy


class AsyncSQLAlchemyHistoryRepository(AsyncHistoryRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_tron_address_info(
        self, tron_address_info: TronAddressInfo
    ) -> TronAddressInfo:
        new_tron_address_info = TronAddressInfoSQLAlchemy(
            address=tron_address_info.address,
            balance_trx=tron_address_info.balance_trx,
            bandwidth=tron_address_info.bandwidth,
            energy_limit=tron_address_info.energy_limit,
        )
        self.session.add(new_tron_address_info)
        await self.session.commit()
        return TronAddressInfo(
            id=new_tron_address_info.id,
            address=new_tron_address_info.address,
            balance_trx=new_tron_address_info.balance_trx,
            bandwidth=new_tron_address_info.bandwidth,
            energy_limit=new_tron_address_info.energy_limit,
        )

    async def get_all_tron_address_info(self) -> List[TronAddressInfo]:
        all_tron_address_info_sqlalchemy = await self.session.execute(
            select(TronAddressInfoSQLAlchemy)
        )
        all_tron_address_info = [
            TronAddressInfo(
                id=a.id,
                address=a.address,
                balance_trx=a.balance_trx,
                bandwidth=a.bandwidth,
                energy_limit=a.energy_limit,
            )
            for a in all_tron_address_info_sqlalchemy.scalars().all()
        ]
        return all_tron_address_info
