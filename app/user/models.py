from sqlmodel import SQLModel
from enum import Enum

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
