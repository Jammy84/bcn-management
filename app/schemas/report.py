from datetime import date
from pydantic import BaseModel, ConfigDict
from app.models.enums import ReportType


class ReportCreate(BaseModel):
    report_type: ReportType
    period_start: date
    period_end: date


class ReportOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    report_type: ReportType
    period_start: date
    period_end: date
    pdf_path: str
