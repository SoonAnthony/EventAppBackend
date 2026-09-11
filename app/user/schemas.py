from pydantic import BaseModel, EmailStr, Field, ConfigDict
from uuid import UUID
from typing import Optional
from app.user.models import UserRole

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    home_city: Optional[str] = None

class UserRead(BaseModel):
    id: UUID
    role: UserRole
    full_name: str
    email: EmailStr 
    phone_number: Optional[str] = None
    home_city: Optional[str] = None
    is_verified: bool
    preferred_radius_km: float

    model_config = ConfigDict(from_attributes=True)

class AdminUpdate(BaseModel):
    role: Optional[UserRole] = None
    is_verified: Optional[bool] = None
    stripe_customer_id: Optional[str] = None
