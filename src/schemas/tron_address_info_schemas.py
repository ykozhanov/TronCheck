from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class TronAddressInfoResponseSchema(BaseModel):
    id: int
    address: str
    balance_trx: Decimal
    bandwidth: int
    energy_limit: int

    model_config = ConfigDict(
        from_attributes=True,
    )
