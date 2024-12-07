from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
import os
from dotenv import load_dotenv  # Import to load the .env file

# Load environment variables from the .env file
load_dotenv()

# Get the DATABASE_URL from the environment variable, with a fallback for local development
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')  # Fallback for local development

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base class
Base = declarative_base()

# Define the Rabbit model
class RabbitModel(Base):
    __tablename__ = 'rabbits'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    health_status = Column(String)
    last_vaccination = Column(Date)

# Function to provide a session to interact with the database
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
