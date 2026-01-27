from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.routes.auth import get_current_user
from app.models.payment import Payment
from app.models.user import User
from app.schemas.payment import PaymentCreate, PaymentOut
from app.services.payment_service import resolve_payment_amount

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/", response_model=PaymentOut)
async def create_payment(
    payment_in: PaymentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    amount = payment_in.amount
    if amount is None:
        try:
            amount = await resolve_payment_amount(db, payment_in.vehicle_id)
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    payment = Payment(vehicle_id=payment_in.vehicle_id, amount=amount, created_by=current_user.id)
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return payment


@router.get("/", response_model=list[PaymentOut])
async def list_payments(
    skip: int = 0,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Payment).order_by(Payment.paid_at.desc()).offset(skip).limit(limit))
    return result.scalars().all()
