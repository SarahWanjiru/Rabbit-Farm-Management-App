from pydantic import BaseModel
from datetime import date

class Rabbit(BaseModel):
    name: str
    breed: str
    age: int
    weight: float
    health_status: str
    last_vaccination: date
