from pydantic import BaseModel
from typing import Optional

class InstructorCreate(BaseModel):
    name: str
    bio: Optional[str] = None

class InstructorUpdate(BaseModel):
    name: Optional[str]
    bio: Optional[str]

class InstructorOut(BaseModel):
    id: str
    name: str
    bio: Optional[str] = None