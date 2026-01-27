from datetime import datetime, timedelta
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.payment import Payment
from app.models.vehicle import Vehicle
from app.models.enums import VehicleType


async def get_dashboard_metrics(db: AsyncSession) -> dict:
    now = datetime.utcnow()
    day_start = now - timedelta(days=1)
    week_start = now - timedelta(days=7)
    month_start = now - timedelta(days=24)

    total_day = await db.execute(select(func.coalesce(func.sum(Payment.amount), 0)).where(Payment.paid_at >= day_start))
    total_week = await db.execute(select(func.coalesce(func.sum(Payment.amount), 0)).where(Payment.paid_at >= week_start))
    total_month = await db.execute(select(func.coalesce(func.sum(Payment.amount), 0)).where(Payment.paid_at >= month_start))

    taxi_count = await db.execute(select(func.count(Vehicle.id)).where(Vehicle.vehicle_type == VehicleType.TAXI))
    taxi_bus_count = await db.execute(select(func.count(Vehicle.id)).where(Vehicle.vehicle_type == VehicleType.TAXI_BUS))

    total_day_val = float(total_day.scalar_one())
    total_week_val = float(total_week.scalar_one())
    total_month_val = float(total_month.scalar_one())
    company_share = total_month_val * 0.12

    return {
        "total_day": total_day_val,
        "total_week": total_week_val,
        "total_month": total_month_val,
        "taxi_count": taxi_count.scalar_one(),
        "taxi_bus_count": taxi_bus_count.scalar_one(),
        "company_share": company_share,
    }
