from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from ..database import Base
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

class User(Base):
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
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    categories = Column(ARRAY(String), nullable=False)
    call = Column(Boolean, nullable=False)
    text = Column(Boolean, nullable=False)
    online_chat = Column(Boolean, nullable=False)

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_name = Column(String, nullable=False)

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, nullable=False)
    prompt = Column(String, nullable=False)
    
