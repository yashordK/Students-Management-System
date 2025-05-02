from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
import models

router = APIRouter(prefix="/teachers", tags=["Teachers"])

# Pydantic Schema for Teacher
class TeacherBase(BaseModel):
    username: str
    name: str
    email: str
    password: str
    designation: str

# Create a new teacher
@router.post("/")
def create_teacher(teacher: TeacherBase, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# Get all teachers
@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

# Get a teacher by ID
@router.get("/{username}")
def get_teacher(username: str, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.username == username).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Update a teacher's details
@router.put("/{username}")
def update_teacher(username: str, teacher: TeacherBase, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.username == username).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    for key, value in teacher.dict().items():
        setattr(db_teacher, key, value)
    
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# Delete a teacher
@router.delete("/{username}")
def delete_teacher(username: str, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.username == username).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    db.delete(db_teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}
