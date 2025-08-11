from database import obj_id_to_str, enrollments_col
from bson import ObjectId
from datetime import datetime, timezone


def create_enrollment(data: dict):
    data["enrolled_at"] = datetime.now(timezone.utc).isoformat()
    result = enrollments_col.insert_one(data)
    return str(result.inserted_id)

def delete_enrollment(enrollment_id: str):
    res = enrollments_col.delete_one({"_id": ObjectId(enrollment_id)})
    return res.deleted_count

def get_enrollments_by_student(student_id: str):
    docs = list(enrollments_col.find({"student_id": student_id}))
    return [obj_id_to_str(d) for d in docs]

def get_enrollments_by_course(course_id: str):
    docs = list(enrollments_col.find({"course_id": course_id}))
    return [obj_id_to_str(d) for d in docs]

def list_enrollments():
    return [obj_id_to_str(d) for d in enrollments_col.find()]