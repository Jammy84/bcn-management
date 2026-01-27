from pydantic import BaseModel, ConfigDict


class PaymentCreate(BaseModel):
    vehicle_id: int
    amount: float | None = None


class PaymentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vehicle_id: int
    amount: float
