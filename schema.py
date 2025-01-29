from pydantic import BaseModel, Field, EmailStr

class EmployeeSchema(BaseModel):
    empid: int
    name: str
    email: EmailStr
    pword: str = Field(min_length=6, description="Password must be at least 6 characters long")
