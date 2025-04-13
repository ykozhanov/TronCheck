from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from src.core.db import Base


class TronAddressInfoSQLAlchemy(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    balance_trx: Mapped[Decimal]
    bandwidth: Mapped[int]
    energy_limit: Mapped[int]
