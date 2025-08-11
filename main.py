from fastapi import FastAPI
from routers import instructor, course, student, enrollment
from database import client

app = FastAPI(title="Course Selling API")

app.include_router(instructor.router)
app.include_router(course.router)
app.include_router(student.router)
app.include_router(enrollment.router)


@app.get("/")
def root():
    try:
        client.server_info()
        mongo_status = "Connected"
    except Exception as e:
        mongo_status = f"Error: {str(e)}"
    return {
        "message": "Course Selling API is running",
        "mongo_status": mongo_status
    }