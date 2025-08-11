from database import obj_id_to_str, instructors_col
from bson import ObjectId


def create_instructor(data: dict):
    result = instructors_col.insert_one(data)
    return str(result.inserted_id)

def get_instructor(instructor_id: str):
    doc = instructors_col.find_one({"_id": ObjectId(instructor_id)})
    return obj_id_to_str(doc)

def update_instructor(instructor_id: str, data: dict):
    instructors_col.update_one({"_id": ObjectId(instructor_id)}, {"$set": data})
    return get_instructor(instructor_id)

def delete_instructor(instructor_id: str):
    res = instructors_col.delete_one({"_id": ObjectId(instructor_id)})
    return res.deleted_count

def list_instructors():
    return [obj_id_to_str(d) for d in instructors_col.find()]