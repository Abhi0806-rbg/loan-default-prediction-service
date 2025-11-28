from fastapi import APIRouter, Depends, HTTPException, Query, status
from datetime import datetime
from typing import Optional

from app.schemas.log_schema import LogCreateRequest, LogResponse
from app.utils.jwt import get_current_user
from app.utils.db import get_logs_collection, serialize_doc, serialize_list

router = APIRouter()


# -------------------------------------------------------
# POST /logs — Create a log entry
# -------------------------------------------------------
@router.post("/", response_model=LogResponse)
async def create_log(
    payload: LogCreateRequest,
    current_user=Depends(get_current_user)
):
    logs = get_logs_collection()

    log_doc = {
        "service_name": payload.service_name,
        "level": payload.level.upper(),
        "message": payload.message,
        "metadata": payload.metadata,
        "timestamp": datetime.utcnow()
    }

    result = await logs.insert_one(log_doc)
    log_doc["_id"] = result.inserted_id

    return serialize_doc(log_doc)


# -------------------------------------------------------
# GET /logs — Get all logs
# Optional filters:
#  - level=INFO|ERROR|WARNING
#  - service_name
# -------------------------------------------------------
@router.get("/", response_model=list[LogResponse])
async def get_logs(
    level: Optional[str] = Query(None),
    service_name: Optional[str] = Query(None),
    current_user=Depends(get_current_user)
):
    logs = get_logs_collection()

    query = {}
    if level:
        query["level"] = level.upper()
    if service_name:
        query["service_name"] = service_name

    cursor = logs.find(query).sort("timestamp", -1)
    docs = [doc async for doc in cursor]

    return serialize_list(docs)


# -------------------------------------------------------
# GET /logs/{service_name} — Get logs for a specific microservice
# -------------------------------------------------------
@router.get("/{service_name}", response_model=list[LogResponse])
async def get_logs_by_service(
    service_name: str,
    current_user=Depends(get_current_user)
):
    logs = get_logs_collection()

    cursor = logs.find({"service_name": service_name}).sort("timestamp", -1)
    docs = [doc async for doc in cursor]

    return serialize_list(docs)
