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
