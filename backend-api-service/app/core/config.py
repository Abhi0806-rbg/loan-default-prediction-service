import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # -----------------------------
    # MongoDB
    # -----------------------------
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://mongo:27017/lone1")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "lone1")

    # -----------------------------
    # JWT Authentication
    # -----------------------------
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_MINUTES: int = 60 * 24  # 24 hours

    # -----------------------------
    # ML Microservices URLs
    # -----------------------------
    ML_PREDICTOR_URL: str = os.getenv("ML_PREDICTOR_URL", "http://ml-predictor-service:8001")
    ML_TRAINER_URL: str = os.getenv("ML_TRAINER_URL", "http://ml-trainer-service:8002")

    # -----------------------------
    # Service Metadata
    # -----------------------------
    SERVICE_NAME: str = "backend-api-service"
    VERSION: str = "1.0.0"

settings = Settings()
