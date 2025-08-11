from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str

class EnrollmentOut(BaseModel):
    id: str
    student_id: str
    course_id: str
    enrolled_at: str