from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any
from bson import ObjectId


# -------------------------------------------------------
# MongoDB Helper ObjectId
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
# Base Log Schema
# -------------------------------------------------------
class LogBase(BaseModel):
    service_name: str
    level: str  # INFO, ERROR, WARNING
    message: str
    metadata: Optional[Dict[str, Any]] = None


# -------------------------------------------------------
# Log stored in MongoDB
# -------------------------------------------------------
class LogInDB(LogBase):
    id: Optional[PyObjectId] = None
    timestamp: datetime = datetime.utcnow()

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True


# -------------------------------------------------------
# API Response Schema
# -------------------------------------------------------
class LogResponse(BaseModel):
    id: str
    service_name: str
    level: str
    message: str
    metadata: Optional[Dict[str, Any]]
    timestamp: datetime
