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
# Prediction Input Schema
# -------------------------------------------------------
class PredictionInput(BaseModel):
    loan_amount: float
    income: float
    age: float
    employment_length: float
    credit_score: float
    loan_purpose: str
    dti: float


# -------------------------------------------------------
# Prediction Result Schema
# -------------------------------------------------------
class PredictionResult(BaseModel):
    prediction: int
    probability: float
    model_version: Optional[str] = None


# -------------------------------------------------------
# Prediction DB Schema
# -------------------------------------------------------
class PredictionInDB(BaseModel):
    id: Optional[PyObjectId] = None
    user_id: str
    input_data: Dict[str, Any]
    prediction: int
    probability: float
    model_version: Optional[str] = None
    created_at: datetime = datetime.utcnow()

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True


# -------------------------------------------------------
# API Response Schema
# -------------------------------------------------------
class PredictionResponse(BaseModel):
    id: str
    prediction: int
    probability: float
    model_version: Optional[str]
    created_at: datetime
