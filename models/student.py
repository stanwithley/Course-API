from typing import Optional
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]

class StudentOut(BaseModel):
    id: str
    name: str
    email: str