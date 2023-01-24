from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#schema for a user
class UserBase(BaseModel):
    email: EmailStr
    password: str

#schema response for a user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

