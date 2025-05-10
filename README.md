# 🏫 Student Attendance Management System

A full-stack web application for managing student attendance and academic records with **role-based login authentication**. Designed for use in schools, colleges, and institutions to simplify attendance tracking and academic monitoring for both **students and teachers**.

---

## 🚀 Features

### 🔐 Authentication & Role-based Access
- **Secure Login**:
  - Students log in using their **Student ID (Username)**.
  - Teachers log in using their **Employee ID (Username)**.
- Role validation using **JWT tokens** for secure access.


📷 **Preview Placeholder:**  
<!-- Embed YouTube video -->
<p align="center">
  <a href="https://youtu.be/9S7n6OdoDL0" target="_blank">
    <img src="https://img.youtu.be/9S7n6OdoDL0/0.jpg" alt="Watch Video" width="600"/>
  </a>
</p>


---

### 👨‍🎓 Student Module

- ✅ View personal profile (name, email, semester, department, batch, phone).
- 📊 View attendance per subject with period-wise breakdown.
- 📄 View exam grades for MSTs and End-Sem.
- 🔐 Access only their own data after login.

📷 **Screenshot Placeholder:**  
<p align="center">
  <a href="https://youtu.be/xCHHfWhJO4w" target="_blank">
    <img src="https://img.youtu.be/xCHHfWhJO4w/0.jpg" alt="Watch Video" width="600"/>
  </a>
</p>
---

### 👨‍🏫 Teacher Module

- 📋 Take attendance for any student in their subject(s).
- 📅 View attendance records of students by subject and date.
- 📈 Access and manage student grades (MST1, MST2, MST3, End-Sem).
- 👁️ View full list of students and their respective records.
- 🔐 Access only authorized teacher operations after login.

📷 **Screenshot Placeholder:**  
<p align="center">
  <a href="https://youtu.be/0VBIIY0sSDE" target="_blank">
    <img src="https://img.youtube.com/vi/9S7n6OdoDL0/0.jpg" alt="Watch Video" width="600"/>
  </a>
</p>

---

### 🧱 Tech Stack

- **Backend:** FastAPI, SQLAlchemy
- **Database:** MySQL
- **Authentication:** JWT (JSON Web Tokens)
- **ORM:** SQLAlchemy
- **Frontend:** (Optional) Can be extended using React/Vue/HTML Templates

---

## 🗂️ Database Schema Overview

### 📄 Students Table
- `username`, `name`, `email`, `semester`, `department`, `batch`, `phone`

### 📄 Attendance Table
- `attendance_id`, `username`, `subject_id`, `date`, `period_id`, `hours_present`, `total_hours`

### 📄 Exam Grades Table
- `grade_id`, `username`, `subject_id`, `marks_obt`, `total_marks`, `exam_type` (MST1, MST2, MST3, End_Sem)

### 📄 Users Table (for auth)
- `id`, `username`, `password_hash`, `role` (student/teacher/parent)

---

## 📷 Screenshots

> Place your screenshots in a `screenshots/` folder and reference them below.

### 🔐 Login Page
`![Login Page](screenshots/login.png)`

### 👨‍🎓 Student Dashboard
`![Student Dashboard](screenshots/student_dashboard.png)`

### 📋 Teacher Attendance Panel
`![Teacher Attendance Panel](screenshots/teacher_attendance.png)`

### 📈 Grades View
`![Grades](screenshots/grades_view.png)`

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yashordK/student-attendance-management.git

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure MySQL database and .env file

# 5. Start the FastAPI server
uvicorn main:app --reload
