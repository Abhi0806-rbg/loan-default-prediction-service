from fastapi import APIRouter, Depends, HTTPException, status
import httpx
from datetime import datetime
from app.schemas.prediction_schema import PredictionRequest, PredictionResponse, PredictionResult
from app.utils.validator import validate_prediction_input
from app.utils.jwt import get_current_user
from app.utils.db import (
    get_prediction_collection,
    get_metadata_collection,
    serialize_doc
)
from app.core.config import settings

router = APIRouter()


# -------------------------------------------------------
# POST /predict — Main Prediction Endpoint
# -------------------------------------------------------
@router.post("/", response_model=PredictionResponse)
async def make_prediction(
    payload: PredictionRequest,
    current_user=Depends(get_current_user)
):
    # Validate input fields
    validate_prediction_input(payload.dict())

    # Prepare request for ML-Predictor microservice
    predictor_url = f"{settings.ML_PREDICTOR_URL}/predict"
    input_data = payload.dict()

    # ---------------------------------------------------
    # Send request to ML Predictor microservice
    # ---------------------------------------------------
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(predictor_url, json=input_data)

        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="ML Predictor Service Error"
            )

        ml_result = PredictionResult(**response.json())

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

    # ---------------------------------------------------
    # Store prediction in MongoDB
    # ---------------------------------------------------
    predictions = get_prediction_collection()

    doc = {
        "user_id": current_user["user_id"],
        "input_data": input_data,
        "prediction": ml_result.prediction,
        "probability": ml_result.probability,
        "model_version": ml_result.model_version,
        "created_at": datetime.utcnow()
    }

    result = await predictions.insert_one(doc)
    doc["_id"] = result.inserted_id

    # ---------------------------------------------------
    # Return standardized response to frontend
    # ---------------------------------------------------
    return serialize_doc(doc)
