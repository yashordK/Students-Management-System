from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
import models
from datetime import date

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# Pydantic Schema for Attendance
class AttendanceBase(BaseModel):
    username: str
    subject_id: str
    date: date
    period_id: int
    hours_present: int
    total_hours: int

# Create a new attendance record
@router.post("/")
def create_attendance(attendance: AttendanceBase, db: Session = Depends(get_db)):
    db_attendance = models.Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# Get all attendance records
@router.get("/")
def get_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()

# Get attendance records by roll number
@router.get("/student/{username}")
def get_student_attendance(username: str, db: Session = Depends(get_db)):
    attendance_records = db.query(models.Attendance).filter(models.Attendance.roll_no == username).all()
    if not attendance_records:
        raise HTTPException(status_code=404, detail="No attendance records found for this student")
    return attendance_records

# Update an attendance record
@router.put("/{attendance_id}")
def update_attendance(attendance_id: int, attendance: AttendanceBase, db: Session = Depends(get_db)):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.attendance_id == attendance_id).first()
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    for key, value in attendance.dict().items():
        setattr(db_attendance, key, value)
    
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# Delete an attendance record
@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.attendance_id == attendance_id).first()
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    db.delete(db_attendance)
    db.commit()
    return {"message": "Attendance record deleted successfully"}
