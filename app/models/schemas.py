from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional
from datetime import datetime


class Exercise:
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

class Resource:
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


class Prompt:
    #schema for prompt
    class PromptBase(BaseModel):
        prompt: str

    class PromptOut(PromptBase):
        id: int

        class Config:
            orm_mode = True


class UserData:

    class CompletedExerciseInfo:
        #schema for completed exercise
        class CompletedExerciseInfoBase(BaseModel):
            completed_exercises: Dict[str, bool]
            completion_date: datetime

        #schema for completed exercises response
        class CompletedExerciseInfoOut(CompletedExerciseInfoBase):
            class Config:
                orm_mode = True

    #schema for a user
    class UserBase(BaseModel):
        email: EmailStr
        username: str
        password: str
        phone_number: Optional[str]

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

    class JournalEntries:
        #schema for journal entries
        class JournalEntryBase(BaseModel):
            title: str
            type: str
            tags: Optional[List[str]]
            elements: Optional[List[Dict[str, str]]]

        #schema for journal entry response
        class JournalEntryOut(JournalEntryBase):
            id: str
            created_at: datetime

            class Config:
                orm_mode = True

class JournalElements:

    class PromptElement:
        #schema for the prompt element
        class PromptElementBase(BaseModel):
            prompt: str
            response: str

        #schema for the element response
        class PromtElementOut(PromptElementBase):
            id: int

            class Config:
                orm_mode = True
        
class Token:

    #Schema for a token response 
    class TokenOut(BaseModel):
        access_token: str
        token_type: str

    #Schema for the token payload data
    class TokenData(BaseModel):
        id: str
        admin: bool

class Extras:

    class LoadAll(BaseModel):

        exercises: List[Exercise.ExerciseOut]
        resources: List[Resource.ResourceOut]
        prompts: List[Prompt.PromptOut]
        completed_exercise_info: UserData.CompletedExerciseInfo.CompletedExerciseInfoOut
        journal_entries: List[UserData.JournalEntries.JournalEntryOut]

    class Config:
        orm_mode = True