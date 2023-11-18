from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from ..database import Base

class User(Base):
    """
    Class representing the 'users' table in the database.

    Attributes:
        id (int): The unique identifier for a user.
        admin (bool): A boolean indicating whether the user is an admin.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        created_at (datetime): The timestamp of when the user was created.
        phone_number (str): The phone number of the user (optional).
        completed_exercise_info (dict): Information about completed exercises in JSON format.
        journal_entries (list): List of journal entries in JSON format.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    admin = Column(Boolean, nullable=False, server_default=text('False'))
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=True)
    completed_exercise_info = Column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    journal_entries = Column(JSONB, nullable=True, server_default=text("'[]'::jsonb"))

class Resource(Base):
    """
    Class representing the 'resources' table in the database.

    Attributes:
        id (int): The unique identifier for a resource.
        name (str): The name of the resource.
        url (str): The URL associated with the resource.
        categories (list): List of categories associated with the resource.
        call (bool): A boolean indicating whether the resource supports calls.
        text (bool): A boolean indicating whether the resource supports text communication.
        online_chat (bool): A boolean indicating whether the resource supports online chat.
    """
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    categories = Column(ARRAY(String), nullable=False)
    call = Column(Boolean, nullable=False)
    text = Column(Boolean, nullable=False)
    online_chat = Column(Boolean, nullable=False)

class Exercise(Base):
    """
    Class representing the 'exercises' table in the database.

    Attributes:
        id (int): The unique identifier for an exercise.
        name (str): The name of the exercise.
        description (str): The description of the exercise.
        image_name (str): The name of the image associated with the exercise.
    """
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_name = Column(String, nullable=False)

class Prompt(Base):
    """
    Class representing the 'prompts' table in the database.

    Attributes:
        id (int): The unique identifier for a prompt.
        prompt (str): The prompt text.
    """
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, nullable=False)
    prompt = Column(String, nullable=False)

    
