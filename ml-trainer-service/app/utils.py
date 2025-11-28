import httpx
from app.core.config import settings

def push_metadata(metadata):
    """
    Push model metadata to backend API.
    """
    try:
        url = f"{settings.BACKEND_URL}/metadata/model"
        httpx.post(url, json=metadata)
    except Exception as e:
        print("Failed to push metadata:", str(e))
