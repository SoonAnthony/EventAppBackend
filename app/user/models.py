from sqlmodel import SQLModel, Field
from enum import Enum
from uuid import uuid7, UUID
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, DateTime, func

class UserRole(str, Enum):
    ATTENDEE = "attendee"
    ORGANIZER = "organizer"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"

class InteractionType(str, Enum):
    VIEW = "view"
    LIKE = "like"
    SAVE = "save"
    ATTEND = "attend"


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid7, primary_key= True)
    email: str = Field(index=True, unique=True, max_length=100, nullable=False)
    hashed_password: str = Field (nullable = False)
    full_name: str = Field (nullable= False)
    phone_number: Optional[str] = Field (nullable=True)
    is_verified: bool = Field (default = False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now() , onupdate=func.now(), nullable=False))
    role: UserRole = Field (default=UserRole.ATTENDEE)
    last_known_lat: Optional[float] = Field (nullable=True)
    last_known_lng: Optional[float] = Field (nullable=True)
    last_location_updated_at: Optional[datetime] = Field(nullable=True)
    home_city: Optional[str] = Field(nullable=True)
    location_permission_granted:bool = Field(default=False)
    preferred_radius_km: float = Field(default=10.0)
    notification_opt_in: bool = Field(default=True)
    stripe_customer_id: Optional[str] = Field(nullable=True)

