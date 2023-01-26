from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#schema for a user
class UserBase(BaseModel):
    email: EmailStr
    password: str
    phone_number: Optional[str]

#schema response for a user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    phone_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

#schema for updating a user
class UserUpdate(BaseModel):
    phone_number: Optional[str]
    email: str

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

#schema for an exrcise
class ExerciseBase(BaseModel):
    name: str
    description: str

#schema for exrcise response
class ExerciseOut(ExerciseBase):
    id: int

    class Config:
        orm_mode = True

#schema for prompt
class PromptBase(BaseModel):
    prompt: str

class PromptOut(PromptBase):
    id: int

    class Config:
        orm_mode = True  

#Schema for a token response 
class token(BaseModel):
    access_token: str
    token_type: str

#Schema for the token payload data
class tokenData(BaseModel):
    id: str
    admin: bool


