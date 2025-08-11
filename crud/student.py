from database import obj_id_to_str, students_col
from bson import ObjectId


def create_student(data: dict):
    result = students_col.insert_one(data)
    return str(result.inserted_id)

def get_student(student_id: str):
    doc = students_col.find_one({"_id": ObjectId(student_id)})
    return obj_id_to_str(doc)

def update_student(student_id: str, data: dict):
    students_col.update_one({"_id": ObjectId(student_id)}, {"$set": data})
    return get_student(student_id)

def delete_student(student_id: str):
    res = students_col.delete_one({"_id": ObjectId(student_id)})
    return res.deleted_count

def list_instructors():
    return [obj_id_to_str(d) for d in students_col.find()]