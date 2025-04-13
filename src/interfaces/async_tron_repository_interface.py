from abc import ABC, abstractmethod
from decimal import Decimal


class AsyncTronRepositoryInterface(ABC):
    """Асинхронный репозиторий для работы с Tron"""

    @abstractmethod
    async def get_account_balance(self, address: str) -> Decimal:
        """Получить информацию об балансе аккаунта в TRX"""
        pass

    @abstractmethod
    async def get_bandwidth(self, address: str) -> int:
        """Получить информацию о bandwidth аккаунта"""
        pass

    @abstractmethod
    async def get_account_energy_limit(self, address: str) -> int:
        """Получить информацию о максимальной энергии аккаунта"""
        pass
