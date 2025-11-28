from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from bson import ObjectId


# -------------------------------------------------------
# MongoDB Helper: ObjectId -> String
# -------------------------------------------------------
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)


# -------------------------------------------------------
# Base User Schema
# -------------------------------------------------------
class UserBase(BaseModel):
    email: EmailStr


# -------------------------------------------------------
# User Creation
# -------------------------------------------------------
class UserCreate(UserBase):
    password: str


# -------------------------------------------------------
# User DB Schema
# -------------------------------------------------------
class UserInDB(UserBase):
    id: Optional[PyObjectId] = None
    password_hash: str
    created_at: datetime = datetime.utcnow()

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True


# -------------------------------------------------------
# Response Schema
# -------------------------------------------------------
class UserResponse(UserBase):
    id: str
    created_at: datetime
