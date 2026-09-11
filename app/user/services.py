from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
from app.user.models import User
from sqlalchemy import select
from app.user.exceptions import UserNotFoundError

async def get_user_by_email(session:AsyncSession, user_email:EmailStr)-> User:
    result = await session.execute(select(User).where(User.email == user_email))
    user = result.scalars().one_or_none()
    if user is None:
        raise UserNotFoundError(user_email)
    return user