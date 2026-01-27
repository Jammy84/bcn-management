from sqlalchemy import Integer, Date, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.enums import ReportType


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    report_type: Mapped[ReportType] = mapped_column(
        Enum(ReportType, native_enum=False, values_callable=lambda obj: [e.value for e in obj]),
        index=True,
    )
    period_start: Mapped[Date] = mapped_column(Date)
    period_end: Mapped[Date] = mapped_column(Date)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    pdf_path: Mapped[str] = mapped_column(String(255))
