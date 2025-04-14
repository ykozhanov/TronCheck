from abc import ABC, abstractmethod
from src.schemas import TronAccountInfoSchema, TronResourceInfoSchema


class AsyncTronInfoRepositoryInterface(ABC):
    """Асинхронный репозиторий для работы с Tron"""

    @abstractmethod
    async def get_account_info(self, address: str) -> TronAccountInfoSchema:
        """Получить информацию об аккаунте"""
        pass

    @abstractmethod
    async def get_account_resource(self, address: str) -> TronResourceInfoSchema:
        """Получить информацию о ресурсах"""
        pass
