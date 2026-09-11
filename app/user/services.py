from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
from app.user.models import User
from sqlalchemy import select
from fastapi import HTTPException



async def get_user_by_email(session:AsyncSession, user_email:EmailStr)-> User:
    result = await session.execute(select(User).where(User.email == user_email))
    user = result.scalars().one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="No user found!")
    else:
        return user