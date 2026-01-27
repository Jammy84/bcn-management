from pydantic import BaseModel, EmailStr, ConfigDict
from app.models.enums import Department, Role


class UserBase(BaseModel):
    last_name: str
    postnom: str
    first_name: str
    email: EmailStr
    phone: str
    start_year: int
    department: Department
    role: Role


class UserCreate(UserBase):
    password: str


class UserBootstrap(UserBase):
    password: str
    role: Role = Role.INGENIEUR_IT


class UserUpdate(BaseModel):
    last_name: str | None = None
    postnom: str | None = None
    first_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    start_year: int | None = None
    department: Department | None = None
    role: Role | None = None
    password: str | None = None


class UserOut(UserBase):
    model_config = ConfigDict(from_attributes=True)
    user_id: str
    is_active: bool
