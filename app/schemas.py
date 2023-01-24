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

#schema for a resource
class ResourceBase(BaseModel):
    name: str
    url: str
    categories: list
    call: bool
    text: bool
    online_chat: bool

#schema response for a resource
class ResourceOut(ResourceBase):
    id: int

    class Config:
        orm_mode = True

#schema for creating a resource
class ResourceCreate(BaseModel):
    name: str
    url: str
    categories: list
    call: bool
    text: bool
    online_chat: bool

#schema for an exrcise
class ExerciseBase(BaseModel):
    name: str
    description: str

#schema for exrcise response
class ExerciseOut(ExerciseBase):
    id: int

    class Config:
        orm_mode = True
    



