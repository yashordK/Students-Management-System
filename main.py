from fastapi import FastAPI
from auth import get_current_user  # Import authentication function
from routes import student, teacher, attendance  # Import API routes
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(teacher.router, prefix="/teachers", tags=["Teachers"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Attendance Management System!"}
