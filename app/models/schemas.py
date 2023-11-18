from pydantic import BaseModel, EmailStr, validator
from typing import List, Dict, Optional
from datetime import datetime

class Exercise:
    """
    Schema for an exercise.

    Attributes:
        name (str): The name of the exercise.
        description (str): The description of the exercise.
        image_name (str): The name of the image associated with the exercise.
    """

    class ExerciseBase(BaseModel):
        name: str
        description: str
        image_name: str

    class ExerciseOut(ExerciseBase):
        """
        Schema for exercise response.

        Attributes:
            id (int): The unique identifier for an exercise.
        """
        id: int

        class Config:
            orm_mode = True

class Resource:
    """
    Schema for a resource.

    Attributes:
        name (str): The name of the resource.
        url (str): The URL associated with the resource.
        categories (List): List of categories associated with the resource.
        call (bool): A boolean indicating whether the resource supports calls.
        text (bool): A boolean indicating whether the resource supports text communication.
        online_chat (bool): A boolean indicating whether the resource supports online chat.
    """

    class ResourceBase(BaseModel):
        name: str
        url: str
        categories: List
        call: bool
        text: bool
        online_chat: bool

    class ResourceOut(ResourceBase):
        """
        Schema response for a resource.

        Attributes:
            id (int): The unique identifier for a resource.
        """
        id: int

        class Config:
            orm_mode = True


class Prompt:
    """
    Schema for a prompt.

    Attributes:
        prompt (str): The prompt text.
    """

    class PromptBase(BaseModel):
        prompt: str

    class PromptOut(PromptBase):
        """
        Schema for prompt response.

        Attributes:
            id (int): The unique identifier for a prompt.
        """
        id: int

        class Config:
            orm_mode = True

class JournalElement(BaseModel):
    """
    Schema for a journal element.

    Attributes:
        type (str): The type of the journal element.
        element_data (Dict): Data associated with the journal element.
    """

    type: str
    element_data: Dict

    @validator('element_data')
    def must_be_valid_journal_element(cls, element_data, values):
        """
        Validate that the journal element type matches the expected types and instantiate the corresponding subclass.

        Parameters:
          element_data (Dict): Data associated with the journal element.
          values: Values from the model that may be needed for validation.

        Returns:
          Dict: The validated and instantiated journal element data.
        """
        element_type = values.get('type', None)

        if element_type == "write":
            return JournalElement.WriteElement(**element_data).dict()

        elif element_type == "reflection":
            return JournalElement.ReflectionElement(**element_data).dict()

        elif element_type == "thanks":
            return JournalElement.ThanksElement(**element_data).dict()

        elif element_type == "thoughts":
            return JournalElement.ThoughtsElement(**element_data).dict()

        elif element_type == "prompt":
            return JournalElement.PromptElement(**element_data).dict()

        else:
            raise ValueError(f"{element_type} is not a valid journal element type")

    class WriteElement(BaseModel):
        """
        Schema for a 'write' journal element.

        Attributes:
            text (str): The text content of the 'write' element.
        """

        text: str

    class ReflectionElement(BaseModel):
        """
        Schema for a 'reflection' journal element.

        Attributes:
            event (str): The event associated with the reflection.
            reflection (str): The reflection text.
        """

        event: str
        reflection: str

    class ThanksElement(BaseModel):
        """
        Schema for a 'thanks' journal element.

        Attributes:
            thankful_for (str): What the user is thankful for.
            why (str): The reason behind the gratitude.
        """

        thankful_for: str
        why: str

    class ThoughtsElement(BaseModel):
        """
        Schema for a 'thoughts' journal element.

        Attributes:
            thoughts (List[str]): List of thoughts.
        """

        thoughts: List[str]

    class PromptElement(BaseModel):
        """
        Schema for a 'prompt' journal element.

        Attributes:
            prompt_id (int): The ID of the prompt.
            prompt (str): The prompt text.
            response (str): The user's response to the prompt.
        """

        prompt_id: int
        prompt: str
        response: str

class CompletedExercise(BaseModel):
    """
    Schema for a completed exercise.

    Attributes:
        exercise_name (str): The name of the completed exercise.
        completed (bool): Indicates whether the exercise is completed or not.
    """

    exercise_name: str
    completed: bool

    @validator('exercise_name')
    def must_be_a_valid_exercise(cls, exercise_name):
        """
        Validate that the completed exercise name is in the list of valid exercises.

        Parameters:
          exercise_name (str): The name of the completed exercise.

        Returns:
          str: The validated exercise name.
        """
        valid_exercises = ["breathing", "journaling", "stretching", "meditating"]

        if exercise_name not in valid_exercises:
            raise ValueError(f"'{exercise_name}' is not a valid exercise")
        else:
            return exercise_name

class UserData:
    """
    Schema for user-related data.

    Attributes:
        UserBase (BaseModel): Base schema for user data.
        UserOut (UserBase): Schema for the user response.
        UserCreate (UserBase): Schema for creating a new user.
        UserUpdate (UserBase): Schema for updating user data.
        CompletedExerciseInfo (BaseModel): Base schema for completed exercise information.
    """

    class UserBase(BaseModel):
        """
        Base schema for user data.

        Attributes:
            email (EmailStr): User's email address.
            username (str): User's username.
            phone_number (Optional[str]): User's phone number (optional).
        """

        email: EmailStr
        username: str
        phone_number: Optional[str]

    class UserCreate(UserBase):
        """
        Schema for creating a new user.

        Attributes:
            password (str): User's password.
        """

        password: str

    class UserUpdate(UserBase):
        """
        Schema for updating user data.

        Attributes:
            pass  # No additional attributes for user update.
        """

        pass

    class UserOut(UserBase):
        """
        Schema for the user response.

        Attributes:
            id (int): User's ID.
            created_at (datetime): User's creation timestamp.
        """

        id: int
        created_at: datetime

        class Config:
            orm_mode = True

    class CompletedExerciseInfo:
        """
        Schema for completed exercise information.

        Attributes:
            CompletedExerciseInfoBase (BaseModel): Base schema for completed exercise information.
            CompletedExerciseInfoOut (CompletedExerciseInfoBase): Schema for the completed exercise information response.
        """

        class CompletedExerciseInfoBase(BaseModel):
            """
            Base schema for completed exercise information.

            Attributes:
                completed_exercises (List[CompletedExercise]): List of completed exercises.

            Validation:
                must_have_all_exercises: Ensure that there are no missing exercises.
            """

            completed_exercises: List[CompletedExercise]

            @validator('completed_exercises')
            def must_have_all_exercises(cls, completed_exercises):
                """
                Validate that there are no missing exercises.

                Parameters:
                  completed_exercises (List[CompletedExercise]): List of completed exercises.

                Returns:
                  List[CompletedExercise]: The validated list of completed exercises.
                """
                if len(completed_exercises) < 4:
                    raise ValueError("There is a missing exercise")
                return completed_exercises

        class CompletedExerciseInfoOut(CompletedExerciseInfoBase):
            """
            Schema for the completed exercise information response.

            Attributes:
                completion_date (datetime): Date of completion.
            """

            completion_date: datetime

    class JournalEntry:
        """
        Schema for journal entries.

        Attributes:
            JournalEntryBase (BaseModel): Base schema for journal entries.
            JournalEntryOut (JournalEntryBase): Schema for the journal entry response.
        """

        class JournalEntryBase(BaseModel):
            """
            Base schema for journal entries.

            Attributes:
                title (str): Journal entry title.
                type (str): Journal entry type.
                tags (List[str]): List of tags associated with the entry.
                elements (List[JournalElement]): List of journal elements.

            """
            
            title: str
            type: str
            tags: List[str]
            elements: List[JournalElement]

        class JournalEntryOut(JournalEntryBase):
            """
            Schema for the journal entry response.

            Attributes:
                id (str): Journal entry ID.
                created_at (datetime): Journal entry creation timestamp.
            """

            id: str
            created_at: datetime


class Token:
    """
    Schema for a token.

    Attributes:
        TokenOut (BaseModel): Schema for the token response.
        TokenData (BaseModel): Schema for the token payload data.
    """

    class TokenOut(BaseModel):
        """
        Schema for the token response.

        Attributes:
            access_token (str): Access token.
            token_type (str): Token type.

        Validation:
            must_be_correct_token_type: Ensure that the token type is 'bearer'.
        """

        access_token: str
        token_type: str

        @validator('token_type')
        def must_be_correct_token_type(cls, token_type):
            """
            Validate that the token type is 'bearer'.

            Parameters:
              token_type (str): Token type.

            Returns:
              str: The validated token type.
            """
            if token_type != 'bearer':
                raise ValueError(f'{token_type} is not a valid token type')
            else:
                return token_type

    class TokenData(BaseModel):
        """
        Schema for the token payload data.

        Attributes:
            user_id (int): User ID.
            admin (bool): Admin status.
        """

        user_id: int
        admin: bool

class Extras:
    """
    Extra schema.

    Attributes:
        LoadAll (BaseModel): Schema for loading all data.
    """

    class LoadAll(BaseModel):
        """
        Schema for loading all data.

        Attributes:
            exercises (List[Exercise.ExerciseOut]): List of exercise data.
            resources (List[Resource.ResourceOut]): List of resource data.
            prompts (List[Prompt.PromptOut]): List of prompt data.
            completed_exercise_info (UserData.CompletedExerciseInfo.CompletedExerciseInfoOut): Completed exercise information.
            journal_entries (List[UserData.JournalEntry.JournalEntryOut]): List of journal entry data.
        """

        exercises: List[Exercise.ExerciseOut]
        resources: List[Resource.ResourceOut]
        prompts: List[Prompt.PromptOut]
        completed_exercise_info: UserData.CompletedExerciseInfo.CompletedExerciseInfoOut
        journal_entries: List[UserData.JournalEntry.JournalEntryOut]
