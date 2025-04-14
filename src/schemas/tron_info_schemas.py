from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TronAccountInfoSchema(BaseModel):
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


class TronInfoSchema(BaseModel):
    address: str
    balance_trx: Decimal    # Баланс в TRX
    bandwidth: int          # (freeNetLimit - freeNetUsed) + (NetLimit - NetUsed)
    energy_free: int        # energy_limit - energy_used


class TronInfoResponseSchema(TronInfoSchema):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


# TODO Посчитать энергию и пропускную способность
# (freeNetLimit - freeNetUsed) + (NetLimit - NetUsed)
# result = {
#     "balance": balance_trx,
#     "bandwidth": {
#         "used": bandwidth_used,
#         "limit": bandwidth_limit,
#         "free": max(bandwidth_limit - bandwidth_used, 0)
#     },
#     "energy": {
#         "used": energy_used,
#         "limit": energy_limit,
#         "free": max(energy_limit - energy_used, 0)
#     }
# }

# TODO Посчитать баланс
# Баланс в сунгах (1 TRX = 1_000_000 сунгов)  Decimal(info.get("balance", 0)) / 1_000_000
