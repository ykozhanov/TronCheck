from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TronInfoRequest(BaseModel):
    address: str


class TronAccountInfoSchema(TronInfoRequest):
    address: str
    balance_sun: Decimal = Field(
        ..., alias="balance"
    )  # Баланс в сунгах (1 TRX = 1_000_000 сунгов)


class TronResourceInfoSchema(BaseModel):
    free_net_used: int = Field(..., alias="freeNetUsed")
    free_net_limit: int = Field(..., alias="freeNetLimit")
    net_used: int = Field(..., alias="NetUsed")
    net_limit: int = Field(..., alias="NetLimit")
    energy_used: int = Field(..., alias="EnergyUsed")
    energy_limit: int = Field(..., alias="EnergyLimit")


class TronInfoCreateSchema(BaseModel):
    address: str
    balance_trx: Decimal    # Баланс в TRX
    bandwidth: int          # (freeNetLimit - freeNetUsed) + (NetLimit - NetUsed)
    energy_free: int        # energy_limit - energy_used


class TronInfoResponseSchema(TronInfoCreateSchema):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
