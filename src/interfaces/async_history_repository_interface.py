from abc import ABC, abstractmethod
from typing import List, Optional

from src.schemas import TronAddressInfoSchema, TronAddressInfoResponseSchema


class AsyncHistoryRepositoryInterface(ABC):
    """Асинхронный репозиторий для работы с историей запросов информации об адресах Tron"""

    @abstractmethod
    async def add_tron_address_info(self, tron_address_info: TronAddressInfoSchema) -> TronAddressInfoResponseSchema:
        """Добавить информацию о запросе информации об адресе Tron в историю"""
        pass

    @abstractmethod
    async def get_all_tron_address_info(self, offset: Optional[int] = 0, limit: Optional[int] = None) -> List[TronAddressInfoResponseSchema]:
        """Получить историю всех запросов"""
        pass