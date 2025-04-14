from tronpy import AsyncTron
from tronpy.exceptions import BadAddress, AddressNotFound

from src.interfaces import AsyncTronInfoRepositoryInterface
from src.schemas import TronAccountInfoSchema, TronResourceInfoSchema
from src.exceptions import AddressNotFoundException, BadRequestException


class AsyncTronpyTronInfoRepository(AsyncTronInfoRepositoryInterface):

    def __init__(self, client: AsyncTron):
        self.client = client

    async def get_account_info(self, address: str) -> TronAccountInfoSchema:
        try:
            async with self.client as client:
                account = await client.get_account_balance(address)
            return TronAccountInfoSchema(**account)
        except BadAddress:
            raise BadRequestException(address=address)
        except AddressNotFound:
            raise AddressNotFoundException(address=address)

    async def get_account_resource(self, address: str) -> TronResourceInfoSchema:
        try:
            async with self.client as client:
                resources = await client.get_bandwidth(address)
            return TronResourceInfoSchema(**resources)
        except BadAddress:
            raise BadRequestException(address=address)
        except AddressNotFound:
            raise AddressNotFoundException(address=address)
