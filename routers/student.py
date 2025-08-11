from fastapi import APIRouter, HTTPException
from models.student import StudentCreate, StudentOut, StudentUpdate
import crud.student as crud

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/students/", response_model=list[StudentOut])
def list_students():
    return crud.list_students()

@router.post("/students/", response_model=dict)
def create_student(inp: StudentCreate):
    _id = crud.create_student(inp.model_dump())
    return {"id": _id}

@router.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: str):
    doc = crud.get_student(student_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc

@router.put("/students/{student_id}", response_model=StudentOut)
def update_student(student_id: str, inp: StudentUpdate):
    doc = crud.update_student(student_id, {k: v for k, v in inp.model_dump().items() if v is not None})
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc

@router.delete("/students/{student_id}")
def delete_student(student_id: str):
    deleted = crud.delete_student(student_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"deleted": True}