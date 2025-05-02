from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
import models, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(
        username=student.username,  # FIXED: Use roll_no instead of roll_number
        name=student.name,
        email=student.email,
        semester=student.semester,
        department=student.department,
        batch=student.batch,
        phone=student.phone
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/student/profile", response_model=schemas.StudentResponse)
def get_student_profile(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    student = db.query(models.Student).filter(models.Student.username == current_user["username"]).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.get("/student/grades")
def get_exam_grades(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    grades = db.query(models.ExamGrades).filter(models.ExamGrades.username == current_user["username"]).all()
    if not grades:
        raise HTTPException(status_code=404, detail="No grades found")
    return grades
