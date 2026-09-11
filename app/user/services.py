from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
from app.user.models import User
from sqlalchemy import select
from uuid import UUID
from app.user.exceptions import UserNotFoundError, UserNotFoundByIdError

async def get_user_by_email(session:AsyncSession, user_email:EmailStr)-> User:
    result = await session.execute(select(User).where(User.email == user_email))
    user = result.scalars().one_or_none()
    if user is None:
        raise UserNotFoundError(user_email)
    return user

async def get_user_by_id(session:AsyncSession, user_id:UUID)->User:
    result = await session.execute(select(User).where(user_id == User.id))
    user = result.scalars().one_or_none()
    if user is None:
        raise UserNotFoundByIdError(user_id)
    return user