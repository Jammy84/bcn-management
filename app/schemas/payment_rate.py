from pydantic import BaseModel, ConfigDict
from app.models.enums import VehicleType


class PaymentRateCreate(BaseModel):
    vehicle_type: VehicleType
    amount: float


class PaymentRateOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vehicle_type: VehicleType
    amount: float
