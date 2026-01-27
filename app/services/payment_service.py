from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.vehicle import Vehicle
from app.models.payment_rate import PaymentRate


async def resolve_payment_amount(db: AsyncSession, vehicle_id: int) -> float:
    vehicle_result = await db.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
    vehicle = vehicle_result.scalar_one_or_none()
    if not vehicle:
        raise ValueError("Vehicle not found")

    rate_result = await db.execute(select(PaymentRate).where(PaymentRate.vehicle_type == vehicle.vehicle_type))
    rate = rate_result.scalar_one_or_none()
    if not rate:
        raise ValueError("Payment rate not configured")

    return float(rate.amount)
