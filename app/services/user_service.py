from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.id_generator import generate_user_id


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    while True:
        candidate = generate_user_id()
        exists = await db.execute(select(User).where(User.user_id == candidate))
        if not exists.scalar_one_or_none():
            user_id = candidate
            break
    user = User(
        user_id=user_id,
        last_name=user_in.last_name,
        postnom=user_in.postnom,
        first_name=user_in.first_name,
        email=user_in.email,
        phone=user_in.phone,
        start_year=user_in.start_year,
        department=user_in.department,
        role=user_in.role,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
