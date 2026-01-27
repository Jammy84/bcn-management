from sqlalchemy import String, Integer, DateTime, Enum, Boolean, Index
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.core.database import Base
from app.models.enums import Department, Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    last_name: Mapped[str] = mapped_column(String(100))
    postnom: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(50), unique=True)
    start_year: Mapped[int] = mapped_column(Integer)
    department: Mapped[Department] = mapped_column(
        Enum(Department, native_enum=False, values_callable=lambda obj: [e.value for e in obj])
    )
    role: Mapped[Role] = mapped_column(
        Enum(Role, native_enum=False, values_callable=lambda obj: [e.value for e in obj])
    )
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

