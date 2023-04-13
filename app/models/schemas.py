from pydantic import BaseModel, EmailStr, validator
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

class JournalElement(BaseModel):

    type: str
    element_data: Dict

    @validator('element_data')
    def must_be_valid_journal_element(cls, element_data, values):
        
        type = None
        if 'type' in values:
            type = values['type']

        if type == "write":
            JournalElement.WriteElement(**element_data)
            return element_data

        elif type == "reflection":
            JournalElement.ReflectionElement(**element_data)
            return element_data
        
        elif type == "thanks":
            JournalElement.ThanksElement(**element_data)
            return element_data

        elif type == "thoughts":
            JournalElement.ThoughtsElement(**element_data)
            return element_data

        elif type == "prompt":
            JournalElement.PromptElement(**element_data)
            return element_data

        else:
            raise ValueError(f"{type} is not a valid journal element type")

    class WriteElement(BaseModel):
        text: str

    class ReflectionElement(BaseModel):
        event: str
        reflection: str

    class ThanksElement(BaseModel):
        thankful_for: str
        why: str

    class ThoughtsElement(BaseModel):
        thoughts: List[str]

    class PromptElement(BaseModel):
        prompt_id: int
        prompt: str
        response: str

class CompletedExercise(BaseModel):
    exercise_name: str
    completed: bool

    @validator('exercise_name')
    def must_be_a_valid_exercise(cls, exercise_name):
        exercises = ["breathing", "journaling", "stretching", "meditating"]
        if exercise_name not in exercises:
            raise ValueError(f"'{exercise_name}' is not a valid exercise")
        else:
            return exercise_name

class UserData:

    #schema for a user
    class UserBase(BaseModel):
        email: EmailStr
        username: str
        phone_number: Optional[str]

    #schema response for a user
    class UserOut(UserBase):
        id: int
        created_at: datetime

        class Config:
            orm_mode = True

    class UserCreate(UserBase):
        password: str

    #schema for updating a user
    class UserUpdate(UserBase):
        pass

    #schema for completed exercise
    class CompletedExerciseInfo(BaseModel):
        completed_exercises: List[CompletedExercise]
        completion_date: datetime

    class JournalEntry:
        #schema for journal entries
        class JournalEntryBase(BaseModel):
            title: str
            type: str
            tags: List[str]
            elements: List[JournalElement]

        #schema for journal entry response
        class JournalEntryOut(JournalEntryBase):
            id: str
            created_at: datetime


class Token:

    #Schema for a token response 
    class TokenOut(BaseModel):
        access_token: str
        token_type: str
            
        @validator('token_type')
        def must_be_correct_token_type(cls, token_type):
            if token_type != 'bearer':
                raise ValueError(f'{token_type} is not a valid token type')
            else:
                return token_type

    #Schema for the token payload data
    class TokenData(BaseModel):
        user_id: int
        admin: bool

class Extras:

    class LoadAll(BaseModel):

        exercises: List[Exercise.ExerciseOut]
        resources: List[Resource.ResourceOut]
        prompts: List[Prompt.PromptOut]
        completed_exercise_info: UserData.CompletedExerciseInfo
        journal_entries: List[UserData.JournalEntry.JournalEntryOut]