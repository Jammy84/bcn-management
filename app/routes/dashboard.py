from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.routes.auth import get_current_user
from app.services.dashboard_service import get_dashboard_metrics

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/metrics")
async def dashboard_metrics(db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await get_dashboard_metrics(db)
