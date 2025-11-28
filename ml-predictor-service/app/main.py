from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from app.preprocess import preprocess_input
import os

app = FastAPI(
    title="ML Predictor Service",
    version="1.0.0",
    description="Loads trained loan default model and serves predictions."
)

# -------------------------------------------------------
# Load Model at Startup
# -------------------------------------------------------
MODEL_PATH = "/app/model/model.pkl"
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")

try:
    model = joblib.load(MODEL_PATH)
    print(f"Loaded model from {MODEL_PATH}")
except Exception as e:
    print("Model load failed:", str(e))
    model = None


@app.get("/")
def root():
    return {"message": "ML Predictor Service Running", "model_version": MODEL_VERSION}


# -------------------------------------------------------
# Prediction Endpoint
# -------------------------------------------------------
@app.post("/predict")
def predict(payload: dict):
    """
    Accepts raw JSON from Backend API.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Preprocess the input
    try:
        x = preprocess_input(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Run prediction
    pred = model.predict(x)[0]
    probability = model.predict_proba(x)[0][1]

    return {
        "prediction": int(pred),
        "probability": float(probability),
        "model_version": MODEL_VERSION
    }
