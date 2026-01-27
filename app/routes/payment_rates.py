from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.routes.auth import get_current_user
from app.models.user import User
from app.models.enums import Role
from app.models.payment_rate import PaymentRate
from app.schemas.payment_rate import PaymentRateCreate, PaymentRateOut

router = APIRouter(prefix="/payment-rates", tags=["payment-rates"])


@router.post("/", response_model=PaymentRateOut)
async def upsert_rate(
    rate_in: PaymentRateCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != Role.INGENIEUR_IT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")

    existing = await db.execute(select(PaymentRate).where(PaymentRate.vehicle_type == rate_in.vehicle_type))
    rate = existing.scalar_one_or_none()
    if rate:
        rate.amount = rate_in.amount
    else:
        rate = PaymentRate(vehicle_type=rate_in.vehicle_type, amount=rate_in.amount)
        db.add(rate)

    await db.commit()
    await db.refresh(rate)
    return rate


@router.get("/", response_model=list[PaymentRateOut])
async def list_rates(
    skip: int = 0,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(PaymentRate).offset(skip).limit(limit))
    return result.scalars().all()
