from decimal import Decimal

from src.interfaces import AsyncTronInfoRepositoryInterface
from src.schemas import TronInfoSchema, TronResourceInfoSchema


class AsyncTronInfoService:

    def __init__(self, tron_info_repo: AsyncTronInfoRepositoryInterface):
        self.tron_info_repo = tron_info_repo

    @staticmethod
    def _get_trx_from_sun(balance_sun: Decimal) -> Decimal:
        return balance_sun / 1_000_000

    @staticmethod
    def _get_bandwidth(acc_res: TronResourceInfoSchema) -> int:
        return (acc_res.free_net_limit - acc_res.free_net_used) + (
            acc_res.net_limit - acc_res.net_used
        )

    @staticmethod
    def _get_energy_free(acc_res: TronResourceInfoSchema) -> int:
        return acc_res.energy_limit - acc_res.energy_used

    async def get_base_info(self, address: str) -> TronInfoSchema:
        acc_info = await self.tron_info_repo.get_account_info(address)
        acc_res = await self.tron_info_repo.get_account_resource(address)

        balance_trx = self._get_trx_from_sun(acc_info.balance_sun)
        bandwidth = self._get_bandwidth(acc_res)
        energy_free = self._get_energy_free(acc_res)

        return TronInfoSchema(
            address=address,
            balance_trx=balance_trx,
            bandwidth=bandwidth,
            energy_free=energy_free,
        )
