from pydantic import BaseModel, EmailStr, validator, Field
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
    element_data: Dict[str, str]

    class WriteElement:

        class WriteElementBase(BaseModel):
            text: str

        class WriteElementOut(WriteElementBase):
            id: str
            
            class Config:
                orm_mode = True

    class ReflectionElement:

        class ReflectionElementBase(BaseModel):
            event: str
            reflection: str

        class ReflectionElementOut(ReflectionElementBase):
            class Config:
                orm_mode = True

    class ThanksElement:

        class ThanksElementBase(BaseModel):
            thankful_for: str
            why: str

        class ThanksElementOut(ThanksElementBase):
            
            class Config:
                orm_mode = True

    class ThoughtsElement:

        class ThoughtsElementBase(BaseModel):
            thoughts: List[str]

        class ThoughtsElementOut(ThoughtsElementBase):

            class Config:
                orm_mode = True

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

class UserData:

    #schema for a user
    class UserBase(BaseModel):
        email: EmailStr
        username: str
        password: str
        phone_number: Optional[str]

    #schema response for a user
    class UserOut(UserBase):
        id: int
        created_at: datetime
        password: str = Field(exclude=True)

        class Config:
            orm_mode = True

    class CompletedExerciseInfo:
        #schema for completed exercise
        class CompletedExerciseInfoBase(BaseModel):
            completed_exercises: Dict[str, bool]
            completion_date: datetime

        #schema for completed exercises response
        class CompletedExerciseInfoOut(CompletedExerciseInfoBase):
            class Config:
                orm_mode = True

    #schema for updating a user
    class UserUpdate(BaseModel):
        phone_number: Optional[str]
        username: str
        email: EmailStr

    class JournalEntries:
        #schema for journal entries
        class JournalEntryBase(BaseModel):
            title: str
            type: str
            tags: Optional[List[str]]
            elements: Optional[List[JournalElement]]

            @validator('elements', each_item=True)
            def must_be_journal_element_base(cls, element):
                type = element.type
                
                if type == "write":
                    JournalElement.WriteElement.WriteElementBase(**element.element_data) #validates incoming data
                    return element

                elif type == "reflection":
                    JournalElement.ReflectionElement.ReflectionElementBase(**element.element_data)
                    return element
                
                elif type == "thanks":
                    JournalElement.ThanksElement.ThanksElementBase(**element.element_data)

                elif type == "thoughts":
                    JournalElement.ThoughtsElement.ThoughtsElementBase(**element.element_data)

                elif type == "prompt":
                    JournalElement.PromptElement.PromptElementBase(**element.element_data)
    
                #left of here testing validaion
                #move to journal element class

                else:
                    raise ValueError(f"{element.type} is not a valid journal element")

        #schema for journal entry response
        class JournalEntryOut(JournalEntryBase):
            id: str
            created_at: datetime
        
            @validator('elements', each_item=True)
            def must_be_journal_element_out(cls, element):
                type = element.type
                print(type)
                if type == "write":
                    JournalElement.WriteElement.WriteElementOut(**element.element_data) #validates incoming data
                    return element

                elif type == "reflection":
                    JournalElement.ReflectionElement.ReflectionElementOut(**element.element_data)
                    return element
                
                elif type == "thanks":
                    JournalElement.ThanksElement.ThanksElementOut(**element.element_data)

                else:
                    raise ValueError(f"{element.type} is not a valid journal element")

            class Config:
                orm_mode = True
        
class Token:

    #Schema for a token response 
    class TokenOut(BaseModel):
        access_token: str
        token_type: str

    #Schema for the token payload data
    class TokenData(BaseModel):
        user_id: int
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