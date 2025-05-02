from sqlalchemy import Column, Date, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    username = Column(String(20), primary_key=True, index=True)  # Match column name exactly
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    semester = Column(Integer, nullable=False)
    department = Column(String(50), nullable=False)
    batch = Column(String(20))
    phone = Column(String(15), unique=True)

class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), ForeignKey("students.username"), nullable=False, index=True)
    subject_id = Column(String(20), ForeignKey("subjects.subject_id"), nullable=False)
    date = Column(Date, nullable=False)
    period_id = Column(Integer, nullable=False)
    hours_present = Column(Integer, nullable=False)
    total_hours = Column(Integer, nullable=False)

    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum("student", "teacher", "parent"), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)


class Teacher(Base):
    __tablename__ = "teachers"

    username = Column(String(20), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    designation = Column(Enum("Faculty", "HOD", "Registrar", "Director", "Admin"), nullable=False)


class ExamGrades(Base):
    __tablename__ = "exam_grades"

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), ForeignKey("students.username"), nullable=False, index=True)
    subject_id = Column(String(20), ForeignKey("subjects.subject_id"), nullable=False, index=True)
    marks_obt = Column(Integer, nullable=False)
    total_marks = Column(Integer, nullable=False)
    exam_type = Column(Enum("MST1", "MST2", "MST3", "End_Sem"), nullable=False)

    student = relationship("Student", backref="exam_grades")