from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


# -------------------------------------------------------
# Create Log Request
# -------------------------------------------------------
class LogCreateRequest(BaseModel):
    service_name: str
    level: str      # INFO / WARNING / ERROR
    message: str
    metadata: Optional[Dict[str, Any]] = None


# -------------------------------------------------------
# Log Response
# -------------------------------------------------------
class LogResponse(BaseModel):
    id: str
    service_name: str
    level: str
    message: str
    metadata: Optional[Dict[str, Any]] = None
    timestamp: datetime
