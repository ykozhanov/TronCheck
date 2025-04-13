from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class TronAddressInfoSchema(BaseModel):
    address: str
    balance_trx: Decimal
    bandwidth: int
    energy_limit: int


class TronAddressInfoResponseSchema(TronAddressInfoSchema):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
