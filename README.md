# Course Selling API  
**FastAPI + MongoDB (PyMongo)**



## 🚀 ویژگی‌ها
✅ مدیریت **مدرس‌ها** (CRUD)  
✅ مدیریت **دوره‌ها** و ارتباط با مدرس (CRUD)  
✅ مدیریت **دانشجوها** (CRUD)  
✅ ثبت‌نام دانشجوها در دوره‌ها (Many-to-Many)  
✅ مستندات خودکار API با **Swagger** و **ReDoc**

---

## 📦 پیش‌نیازها
- Python 3.10+
- MongoDB (لوکال یا Atlas)
- pip و ترجیحاً محیط مجازی venv

course_api/
│
├── main.py
├── database.py
├── requirements.txt
│
├── models/
│   ├── instructor.py
│   ├── course.py
│   ├── student.py
│   └── enrollment.py
│
├── crud/
│   ├── instructor.py
│   ├── course.py
│   ├── student.py
│   └── enrollment.py
│
└── routers/
    ├── instructor.py
    ├── course.py
    ├── student.py
    └── enrollment.py


| موجودیت    | متد    | مسیر                      | توضیح                   |
| ---------- | ------ | ------------------------- | ----------------------- |
| Instructor | GET    | `/instructors/`           | لیست همه مدرس‌ها        |
| Instructor | POST   | `/instructors/`           | ساخت مدرس جدید          |
| Instructor | GET    | `/instructors/{id}`       | دریافت جزئیات یک مدرس   |
| Instructor | PUT    | `/instructors/{id}`       | ویرایش مدرس             |
| Instructor | DELETE | `/instructors/{id}`       | حذف مدرس                |
| Course     | GET    | `/courses/`               | لیست همه دوره‌ها        |
| Course     | POST   | `/courses/`               | ساخت دوره جدید          |
| Course     | GET    | `/courses/{id}`           | دریافت جزئیات یک دوره   |
| Course     | PUT    | `/courses/{id}`           | ویرایش دوره             |
| Course     | DELETE | `/courses/{id}`           | حذف دوره                |
| Student    | GET    | `/students/`              | لیست همه دانشجوها       |
| Student    | POST   | `/students/`              | ساخت دانشجو             |
| Enrollment | POST   | `/enrollments/`           | ثبت‌نام دانشجو در دوره  |
| Enrollment | GET    | `/students/{id}/courses/` | لیست دوره‌های یک دانشجو |
| Enrollment | GET    | `/courses/{id}/students/` | لیست دانشجوهای یک دوره  |

