from fastapi import APIRouter, HTTPException
from models.instructor import InstructorCreate, InstructorOut, InstructorUpdate
import crud.instructor as crud

router = APIRouter(prefix="/instructor", tags=["instructor"])

@router.get("/instructors/", response_model=list[InstructorOut])
def list_instructors():
    return crud.list_instructors()

@router.post("/instructors/", response_model=dict)
def create_instructor(inp: InstructorCreate):
    _id = crud.create_instructor(inp.model_dump())
    return {"id": _id}

@router.get("/instructors/{instructor_id}", response_model=InstructorOut)
def get_instructor(instructor_id: str):
    doc = crud.get_instructor(instructor_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return doc

@router.put("/instructors/{instructor_id}", response_model=InstructorOut)
def update_instructor(instructor_id: str, inp: InstructorUpdate):
    doc = crud.update_instructor(instructor_id, {k: v for k, v in inp.model_dump().items() if v is not None})
    if not doc:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return doc

@router.delete("/instructors/{instructor_id}")
def delete_instructor(instructor_id: str):
    deleted = crud.delete_instructor(instructor_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return {"deleted": True}