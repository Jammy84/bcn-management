from pydantic import BaseModel, ConfigDict
from app.models.enums import VehicleType


class VehicleCreate(BaseModel):
    vehicle_type: VehicleType
    plate_number: str | None = None


class VehicleOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vehicle_type: VehicleType
    plate_number: str | None = None
    active: bool


class VehicleUpdate(BaseModel):
    vehicle_type: VehicleType | None = None
    plate_number: str | None = None
    active: bool | None = None
