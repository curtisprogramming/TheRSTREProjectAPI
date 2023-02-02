from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List, Dict

#schema for a user
class UserBase(BaseModel):
    email: EmailStr
    username: str
    password: str
    phone_number: Optional[str]
    completed_exercises: dict

#schema response for a user
class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    phone_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

#schema for updating a user
class UserUpdate(BaseModel):
    phone_number: Optional[str]
    username: str
    email: str

#schema for a resource
class ResourceBase(BaseModel):
    name: str
    url: str
    categories: List
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
    image_name: str

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

#schema for the prompt element
class PromptElement(BaseModel):
    prompt: str
    response: str

#schema for the element response
class PromtElementOut(PromptElement):
    id: int

    class Config:
        orm_mode = True

#schema for journal entries
class JournalEntry(BaseModel):
    title: str
    type: str
    tags: Optional[list]
    elements: Optional[List[Dict[str, str]]]

#schema for journal entry response
class JournalEntryOut(JournalEntry):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True

#schema for completed exercise
class CompletedExercises(BaseModel):
    completed_exercises: Dict[str, bool]
    completion_date: datetime

#schema for completed exercises response
class CompletedExercisesOut(CompletedExercises):
    class Config:
        orm_mode = True

class LoadAll(BaseModel):
    
    exercises: List[ExerciseOut]
    resources: List[ResourceOut]
    prompts: List[PromptOut]
    completed_exercises: CompletedExercisesOut

    class Config:
        orm_mode = True

