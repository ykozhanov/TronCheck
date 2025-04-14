from typing import Optional

from src.interfaces import AsyncHistoryRepositoryInterface
from src.schemas import TronInfoSchema, TronInfoResponseSchema, HistoryResponseSchema


class AsyncHistoryService:

    def __init__(self, history_repo: AsyncHistoryRepositoryInterface):
        self.history_repo = history_repo

    async def create(self, tron_info: TronInfoSchema) -> TronInfoResponseSchema:
        return await self.history_repo.create(tron_info)

    async def get_all(
        self, offset: Optional[int], limit: Optional[int]
    ) -> HistoryResponseSchema:
        return await self.history_repo.get_all(offset, limit)
