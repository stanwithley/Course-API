from fastapi import APIRouter, HTTPException
from models.course import CourseCreate, CourseOut, CourseUpdate
import crud.course as crud

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/courses/", response_model=list[CourseOut])
def list_courses():
    return crud.list_courses()

@router.post("/courses/", response_model=dict)
def create_course(inp: CourseCreate):
    _id = crud.create_course(inp.model_dump())
    return {"id": _id}

@router.get("/courses/{course_id}", response_model=CourseOut)
def get_course(course_id: str):
    doc = crud.get_course(course_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Course not found")
    return doc

@router.put("/courses/{course_id}", response_model=CourseOut)
def update_course(course_id: str, inp: CourseUpdate):
    doc = crud.update_course(course_id, {k: v for k, v in inp.model_dump().items() if v is not None})
    if not doc:
        raise HTTPException(status_code=404, detail="Course not found")
    return doc

@router.delete("/courses/{course_id}")
def delete_course(course_id: str):
    deleted = crud.delete_course(course_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"deleted": True}

@router.get("/instructors/{course_id}/courses", response_model=list[CourseOut])
def list_instructors(course_id: str):
    return crud.list_courses_by_instructor(course_id)