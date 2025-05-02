from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentCreate(BaseModel):
    username: str
    name: str
    email: EmailStr
    semester: int
    department: str
    batch: Optional[str] = None
    phone: Optional[str] = None

class StudentResponse(StudentCreate):
    class Config:
        orm_mode = True
