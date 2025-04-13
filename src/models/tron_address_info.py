from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class TronAddressInfo:
    address: str
    balance_trx: Decimal
    bandwidth: int
    energy_limit: int
    id: Optional[int] = None
