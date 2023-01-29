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
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=True)

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

class JournalEntry(Base):
    __tablename__ = "journalEntries"
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    type = Column(String, nullable=False)
    created_at = Column(String, nullable=False, server_default=text('now()'))
    tags = Column(ARRAY(String), nullable=True)
    elements = Column(ARRAY(JSONB), nullable=True)

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, nullable=False)
    prompt = Column(String, nullable=False)

class PromptElement(Base):
    __tablename__ = "promptElements"
    id = Column(Integer, primary_key=True, nullable=False)
    prompt = Column(String, nullable=False)
    response = Column(String, nullable=False)
    
