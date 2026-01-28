from datetime import date
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.core.database import get_db
from app.routes.auth import get_current_user
from app.models.user import User
from app.models.payment import Payment
from app.models.vehicle import Vehicle
from app.models.report import Report
from app.schemas.report import ReportCreate, ReportOut
from app.services.pdf_service import generate_report_pdf, upload_pdf_to_supabase

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/", response_model=ReportOut)
async def create_report(
    report_in: ReportCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    total_vehicles = await db.execute(select(func.count(Vehicle.id)))
    total_collected = await db.execute(select(func.coalesce(func.sum(Payment.amount), 0)).where(Payment.paid_at >= report_in.period_start, Payment.paid_at <= report_in.period_end))

    total_vehicles_val = total_vehicles.scalar_one()
    total_collected_val = float(total_collected.scalar_one())
    company_share = total_collected_val * 0.12

    report_name = f"{report_in.report_type.value}_{report_in.period_start}_{report_in.period_end}"
    pdf_path = generate_report_pdf(
        Path("reports"),
        report_name,
        report_in.period_start,
        report_in.period_end,
        total_vehicles_val,
        total_collected_val,
        company_share,
        f"{current_user.first_name} {current_user.last_name}",
        Path("static/images/logo.png"),
    )

    report_public_url = upload_pdf_to_supabase(pdf_path, report_name)
    report = Report(
        report_type=report_in.report_type,
        period_start=report_in.period_start,
        period_end=report_in.period_end,
        created_by=current_user.id,
        pdf_path=report_public_url or str(pdf_path),
    )
    db.add(report)
    await db.commit()
    await db.refresh(report)
    return report


@router.get("/", response_model=list[ReportOut])
async def list_reports(
    skip: int = 0,
    limit: int = 50,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Report).order_by(Report.period_end.desc()).offset(skip).limit(limit))
    return result.scalars().all()


@router.get("/{report_id}/download")
async def download_report(
    report_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Report).where(Report.id == report_id))
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    if report.pdf_path.startswith("http"):
        return RedirectResponse(report.pdf_path)
    return FileResponse(report.pdf_path, filename=Path(report.pdf_path).name)
