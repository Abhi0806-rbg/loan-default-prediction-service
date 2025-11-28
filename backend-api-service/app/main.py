from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, predict, logs, metadata
from app.core.config import settings

app = FastAPI(
    title="Loan Default Prediction - API Gateway Service",
    version="1.0.0",
    description="Handles authentication, logging, prediction routing, and API gateway functionality."
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
def root():
    return {"message": "Backend API Gateway Running"}

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(metadata.router, prefix="/metadata", tags=["Model Metadata"])
