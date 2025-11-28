from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime


# -------------------------------------------------------
# Prediction Input from Frontend
# -------------------------------------------------------
class PredictionRequest(BaseModel):
    loan_amount: float
    income: float
    age: float
    employment_length: float
    credit_score: float
    loan_purpose: str
    dti: float


# -------------------------------------------------------
# ML Predictor Response
# -------------------------------------------------------
class PredictionResult(BaseModel):
    prediction: int
    probability: float
    model_version: Optional[str] = None


# -------------------------------------------------------
# Stored Prediction Response
# -------------------------------------------------------
class PredictionResponse(BaseModel):
    id: str
    prediction: int
    probability: float
    model_version: Optional[str]
    created_at: datetime
