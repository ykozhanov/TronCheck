from src.interfaces import AsyncTronInfoRepositoryInterface
from tronpy import AsyncTron
from src.schemas import TronAccountInfoSchema, TronResourceInfoSchema


class AsyncTronpyTronInfoRepository(AsyncTronInfoRepositoryInterface):

    def __init__(self, client: AsyncTron):
        self.client = client

    async def get_account_info(self, address: str) -> TronAccountInfoSchema:
        async with self.client as client:
            account = await client.get_account_balance(address)
        return TronAccountInfoSchema(**account)

    async def get_account_resource(self, address: str) -> TronResourceInfoSchema:
        async with self.client as client:
            resources = await client.get_bandwidth(address)
        return TronResourceInfoSchema(**resources)
