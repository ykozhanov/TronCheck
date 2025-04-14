from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.interfaces import AsyncHistoryRepositoryInterface
from src.models import TronInfo
from src.schemas import (
    TronInfoResponseSchema,
    TronInfoCreateSchema,
    HistoryResponseSchema,
    PaginatorHistorySchema,
)


class AsyncSQLAlchemyHistoryRepository(AsyncHistoryRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tron_info: TronInfoCreateSchema) -> TronInfoResponseSchema:
        new_tron_info = TronInfo(
            address=tron_info.address,
            balance_trx=tron_info.balance_trx,
            bandwidth=tron_info.bandwidth,
            energy_free=tron_info.energy_free,
        )
        self.session.add(new_tron_info)
        await self.session.commit()
        return TronInfoResponseSchema.model_validate(new_tron_info)

    async def get_all(
        self, offset: int = 0, limit: Optional[int] = None
    ) -> HistoryResponseSchema:
        total_query = await self.session.execute(select(func.count()).select_from(TronInfo))
        total = total_query.scalar()

        query = select(TronInfo).offset(offset)

        if limit is not None:
            query = query.limit(limit)

        all_tron_address_info = await self.session.execute(query)

        paginator = PaginatorHistorySchema(
            offset=offset,
            limit=limit,
            total=total,
        )

        return HistoryResponseSchema(
            history=list(all_tron_address_info.scalars().all()),
            paginator=paginator,
        )
