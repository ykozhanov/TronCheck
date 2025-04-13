from decimal import Decimal

from src.interfaces import AsyncTronRepositoryInterface
from tronpy import AsyncTron
from tronpy.exceptions import AddressNotFound
from src.exceptions import TronAddressNotFoundException


class AsyncTronRepository(AsyncTronRepositoryInterface):

    def __init__(self, client: AsyncTron):
        self.client = client

    async def get_account_balance(self, address: str) -> Decimal:
        async with self.client as client:
            return await client.get_account_balance(address)

    async def get_bandwidth(self, address: str) -> int:
        try:
            async with self.client as client:
                return await client.get_bandwidth(address)
        except AddressNotFound:
            raise TronAddressNotFoundException()

    async  def get_account_energy_limit(self, address: str) -> int:
        try:
            async with self.client as client:
                resource = await client.get_account_resource(address)
            return resource.get("energy_limit", 0)
        except AddressNotFound:
            raise TronAddressNotFoundException()
