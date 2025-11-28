from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# -------------------------------------------------------
# Generate JWT
# -------------------------------------------------------
def create_access_token(data: dict, expires_delta: Optional[int] = None):
    """
    Create JWT token with expiration.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=expires_delta if expires_delta else settings.JWT_EXPIRY_MINUTES
    )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


# -------------------------------------------------------
# Decode JWT
# -------------------------------------------------------
def verify_access_token(token: str):
    """
    Decode and validate the token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

        return {"user_id": user_id}

    except JWTError:
        raise credentials_exception


# -------------------------------------------------------
# FastAPI Dependency
# -------------------------------------------------------
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Used in routes to ensure user is authenticated.
    """
    return verify_access_token(token)
