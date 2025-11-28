from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import Optional

from app.utils.jwt import get_current_user
from app.utils.db import get_metadata_collection, serialize_doc
from app.schemas.prediction_schema import PredictionResult

router = APIRouter()


# -------------------------------------------------------
# GET /metadata/model — Get latest model metadata
# -------------------------------------------------------
@router.get("/model")
async def get_model_metadata(current_user=Depends(get_current_user)):

    metadata = get_metadata_collection()
    doc = await metadata.find_one(sort=[("trained_at", -1)])

    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model metadata not found"
        )

    return serialize_doc(doc)


# -------------------------------------------------------
# POST /metadata/model — Update model metadata
# Used by ML-Trainer service after training a new model
# -------------------------------------------------------
@router.post("/model")
async def update_model_metadata(
    payload: dict,
):

    metadata = get_metadata_collection()

    doc = {
        "version": payload.get("version"),
        "accuracy": payload.get("accuracy"),
        "metrics": payload.get("metrics"),
        "trained_at": datetime.utcnow()
    }

    result = await metadata.insert_one(doc)
    doc["_id"] = result.inserted_id

    return {
        "message": "Model metadata updated successfully",
        "data": serialize_doc(doc)
    }
