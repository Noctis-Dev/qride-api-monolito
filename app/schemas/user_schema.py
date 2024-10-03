from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    full_name: str
    profile_picture: Optional[str] = None
    current_points: Optional[int] = None
    balance: Optional[float] = None
    phone_number: Optional[str] = None

class UserCreate(UserBase):
    password: str
    user_rol: int

class UserUpdate(UserBase):
    password: Optional[str] = None
    user_rol: Optional[int] = None

class UserInDBBase(UserBase):
    user_id: int
    user_uuid: str

    class Config:
        from_attributes = True

class UserInDB(UserInDBBase):
    hashed_password: str

class User(UserInDBBase):
    pass