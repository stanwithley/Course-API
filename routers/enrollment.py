from fastapi import APIRouter, HTTPException
from models.enrollment import EnrollmentCreate, EnrollmentOut
import crud.enrollment as crud
import crud.student as student_crud
import crud.course as course_crud

router = APIRouter(prefix="/enrollment", tags=["enrollment"])

@router.get("/enrollments/", response_model=list[EnrollmentOut])
def list_enrollments():
    return crud.list_enrollments()

@router.post("/enrollments/", response_model=dict)
def create_enrollment(inp: EnrollmentCreate):
    if not student_crud.get_student(inp.student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    if not course_crud.get_course(inp.course_id):
        raise HTTPException(status_code=404, detail="Course not found")

    _id = crud.create_enrollment(inp.model_dump())
    return {"id": _id}

@router.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: str):
    deleted = crud.delete_enrollment(enrollment_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"deleted": True}

@router.get("/students/{student_id}/courses/", response_model=list)
def student_courses(student_id: str):
    return crud.get_enrollments_by_student(student_id)

@router.get("/courses/{course_id}/students/", response_model=list)
def course_students(course_id: str):
    return crud.get_enrollments_by_course(course_id)