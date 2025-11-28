from pydantic import BaseModel, EmailStr
from datetime import datetime


# -------------------------------------------------------
# User Register Request
# -------------------------------------------------------
class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str


# -------------------------------------------------------
# User Login Request
# -------------------------------------------------------
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


# -------------------------------------------------------
# User Response
# -------------------------------------------------------
class UserResponse(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
