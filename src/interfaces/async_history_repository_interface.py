from abc import ABC, abstractmethod
from typing import List

from src.models import TronAddressInfo


class AsyncHistoryRepositoryInterface(ABC):
    """Асинхронный репозиторий для работы с историей запросов информации об адресах Tron"""

    @abstractmethod
    async def add_tron_address_info(self, tron_address_info: TronAddressInfo) -> TronAddressInfo:
        """Добавить информацию о запросе информации об адресе Tron в историю"""
        pass

    @abstractmethod
    async def get_all_tron_address_info(self) -> List[TronAddressInfo]:
        """Получить историю всех запросов"""
        pass