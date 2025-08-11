from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["course_api_db"]

instructors_col = db["instructors"]
courses_col = db["courses"]
students_col = db["students"]
enrollments_col = db["enrollments"]

def obj_id_to_str(doc: dict):
    if not doc:
        return doc
    doc = dict(doc)
    if "_id" in doc:
        doc["id"] = str(doc.pop("_id"))
    return doc