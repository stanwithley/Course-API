from database import obj_id_to_str, courses_col
from bson import ObjectId


def create_course(data: dict):
    result = courses_col.insert_one(data)
    return str(result.inserted_id)

def get_course(course_id: str):
    doc = courses_col.find_one({"_id": ObjectId(course_id)})
    return obj_id_to_str(doc)

def update_course(course_id: str, data: dict):
    courses_col.update_one({"_id": ObjectId(course_id)}, {"$set": data})
    return get_course(course_id)

def delete_course(course_id: str):
    res = courses_col.delete_one({"_id": ObjectId(course_id)})
    return res.deleted_count

def list_courses_by_instructor(instructor_id: str):
    docs = list(courses_col.find({"instructor_id": instructor_id}))
    return [obj_id_to_str(d) for d in docs]

def list_course():
    return [obj_id_to_str(d) for d in courses_col.find()]