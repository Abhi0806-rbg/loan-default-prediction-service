from fastapi import FastAPI, HTTPException
from app.training import train_models, load_metrics
from app.core.config import settings

app = FastAPI(
    title="ML Trainer Service",
    version="1.0.0",
    description="Trains ML models and updates model.pkl in shared storage."
)

@app.get("/")
def root():
    return {"message": "ML Trainer Service Running"}

@app.post("/train")
def train():
    try:
        metrics = train_models()
        return {
            "status": "success",
            "message": "Model trained successfully",
            "metrics": metrics
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
def get_metrics():
    return load_metrics()
