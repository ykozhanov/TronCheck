from typing import Optional

from src.interfaces import AsyncHistoryRepositoryInterface
from src.schemas import TronInfoCreateSchema, TronInfoResponseSchema, HistoryResponseSchema


class AsyncHistoryService:
    """Асинхронный сервис работы с историей запросов информации Tron"""

    def __init__(self, history_repo: AsyncHistoryRepositoryInterface):
        self.history_repo = history_repo

    async def create(self, tron_info: TronInfoCreateSchema) -> TronInfoResponseSchema:
        """Добавить запись в историю"""
        return await self.history_repo.create(tron_info)

    async def get_all(
        self, offset: int = 0, limit: Optional[int] = None
    ) -> HistoryResponseSchema:
        """Получить историю запросов"""
        return await self.history_repo.get_all(offset, limit)
