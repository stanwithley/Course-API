from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    instructor_id: str
    price: Optional[float] = 0.0

class CourseUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]

class CourseOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    instructor_id: object
    price: float