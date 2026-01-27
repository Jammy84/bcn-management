from sqlalchemy import Integer, Enum, Numeric, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.enums import VehicleType


class PaymentRate(Base):
    __tablename__ = "payment_rates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    vehicle_type: Mapped[VehicleType] = mapped_column(
        Enum(VehicleType, native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        unique=True,
    )
    amount: Mapped[float] = mapped_column(Numeric(10, 2))

