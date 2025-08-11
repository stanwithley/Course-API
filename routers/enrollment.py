from fastapi import APIRouter, HTTPException
from models.enrollment import EnrollmentCreate, EnrollmentOut
import crud.enrollment as crud
import crud.student as student_crud
import crud.course as course_crud

router = APIRouter(prefix="/enrollment", tags=["enrollment"])

@router.get("/enrollment/", response_model=list[EnrollmentOut])
def list_enrollments():
    return crud.list_enrollments()

@router.post("", response_model=dict)
def create_enrollment(inp: EnrollmentCreate):
    s = student_crud.get_student(inp.student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")

    c = course_crud.get_course(inp.course_id)
    if not c:
        raise HTTPException(status_code=404, detail="Course not found")

    _id = crud.create_enrollment(inp.model_dump())
    return {"id": _id}

@router.delete("{enrollment_id}")
def delete_enrollment(enrollment_id: str):
    deleted = crud.delete_enrollment(enrollment_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"deleted": True}


