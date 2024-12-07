from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal, RabbitModel
from models.rabbit import Rabbit

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new rabbit
@router.post("/rabbits/")
def create_rabbit(rabbit: Rabbit, db: Session = Depends(get_db)):
    db_rabbit = RabbitModel(**rabbit.dict())  # Convert Rabbit Pydantic model to SQLAlchemy model
    db.add(db_rabbit)
    db.commit()
    db.refresh(db_rabbit)
    return db_rabbit

# Route to get all rabbits
@router.get("/rabbits/")
def read_rabbits(db: Session = Depends(get_db)):
    return db.query(RabbitModel).all()
