from abc import ABC, abstractmethod
from typing import Optional

from src.schemas import TronInfoSchema, TronInfoResponseSchema, HistoryResponseSchema


class AsyncHistoryRepositoryInterface(ABC):
    """Асинхронный репозиторий для работы с историей запросов информации об адресах Tron"""

    @abstractmethod
    async def create(self, tron_info: TronInfoSchema) -> TronInfoResponseSchema:
        """Добавить информацию о запросе информации об адресе Tron в историю"""
        pass

    @abstractmethod
    async def get_all(self, offset: Optional[int] = None, limit: Optional[int] = None) -> HistoryResponseSchema:
        """Получить историю всех запросов"""
        pass