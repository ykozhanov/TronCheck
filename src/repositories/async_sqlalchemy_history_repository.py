from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.interfaces import AsyncHistoryRepositoryInterface
from src.models import TronAddressInfo
from src.schemas import TronAddressInfoSchema, TronAddressInfoResponseSchema


class AsyncSQLAlchemyHistoryRepository(AsyncHistoryRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_tron_address_info(
        self, tron_address_info: TronAddressInfoSchema
    ) -> TronAddressInfoResponseSchema:
        new_tron_address_info = TronAddressInfo(
            address=tron_address_info.address,
            balance_trx=tron_address_info.balance_trx,
            bandwidth=tron_address_info.bandwidth,
            energy_limit=tron_address_info.energy_limit,
        )
        self.session.add(new_tron_address_info)
        await self.session.commit()
        return TronAddressInfoResponseSchema.model_validate(new_tron_address_info)

    async def get_all_tron_address_info(self) -> List[TronAddressInfoResponseSchema]:
        all_tron_address_info_sqlalchemy = await self.session.execute(
            select(TronAddressInfo)
        )
        all_tron_address_info = [
            TronAddressInfoResponseSchema.model_validate(a)
            for a in all_tron_address_info_sqlalchemy.scalars().all()
        ]
        return all_tron_address_info
