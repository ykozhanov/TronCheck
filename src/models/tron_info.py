from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from src.core.db import Base


class TronInfo(Base):
    __tablename__ = "tron_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    balance_trx: Mapped[Decimal]
    bandwidth: Mapped[int]
    energy_free: Mapped[int]
