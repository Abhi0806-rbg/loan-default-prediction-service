from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserRegisterRequest, UserLoginRequest, UserResponse
from app.utils.validator import validate_email
from app.utils.hash import hash_password, verify_password
from app.utils.jwt import create_access_token, get_current_user
from app.utils.db import get_user_collection, serialize_doc
from app.core.config import settings
from datetime import datetime

router = APIRouter()

# -------------------------------------------------------
# Register New User
# -------------------------------------------------------
@router.post("/register", response_model=UserResponse)
async def register_user(payload: UserRegisterRequest):
    validate_email(payload.email)

    users = get_user_collection()

    # Check if email already registered
    existing = await users.find_one({"email": payload.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    user_doc = {
        "email": payload.email,
        "password_hash": hash_password(payload.password),
        "created_at": datetime.utcnow()
    }

    result = await users.insert_one(user_doc)
    user_doc["_id"] = result.inserted_id

    return serialize_doc(user_doc)


# -------------------------------------------------------
# Login
# -------------------------------------------------------
@router.post("/login")
async def login(payload: UserLoginRequest):
    validate_email(payload.email)

    users = get_user_collection()

    user = await users.find_one({"email": payload.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT token
    token = create_access_token({"user_id": str(user["_id"])})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(user["_id"]),
            "email": user["email"]
        }
    }


# -------------------------------------------------------
# Get Current User
# -------------------------------------------------------
@router.get("/me", response_model=UserResponse)
async def get_me(current_user = Depends(get_current_user)):
    users = get_user_collection()
    user = await users.find_one({"_id": current_user["user_id"]})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return serialize_doc(user)
