from fastapi import APIRouter, HTTPException
from models.student import StudentCreate, StudentOut, StudentUpdate
import crud.student as crud

router = APIRouter(prefix="/student", tags=["student"])

@router.get("/student/", response_model=list[StudentOut])
def list_instructors():
    return crud.list_instructors()

@router.post("", response_model=StudentOut)
def create_student(inp: StudentCreate):
    _id = crud.create_student(inp.model_dump())
    return {"id": _id}

@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: str):
    doc = crud.get_student(student_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc

@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: str, inp: StudentUpdate):
    doc = crud.update_student(student_id, {k: v for k, v in inp.model_dump().items() if v is not None})
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc

@router.delete("/{student_id}")
def delete_student(student_id: str):
    deleted = crud.delete_student(student_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"deleted": True}