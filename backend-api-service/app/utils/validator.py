import re
from fastapi import HTTPException, status


# -------------------------------------------------------
# Email Validator
# -------------------------------------------------------
def validate_email(email: str):
    """
    Validate email format.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format"
        )


# -------------------------------------------------------
# Required Field Validator
# -------------------------------------------------------
def validate_required(field: str, field_name: str):
    """
    Ensure a required field is not empty.
    """
    if field is None or field == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} is required"
        )


# -------------------------------------------------------
# Number Validator
# -------------------------------------------------------
def validate_number(value, field_name: str):
    """
    Ensure input is a valid number.
    """
    try:
        float(value)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must be a valid number"
        )


# -------------------------------------------------------
# Prediction Input Validator
# -------------------------------------------------------
def validate_prediction_input(data: dict):
    """
    Validate prediction form fields.
    """
    required_fields = [
        "loan_amount",
        "income",
        "age",
        "employment_length",
        "credit_score",
        "loan_purpose",
        "dti"
    ]

    for field in required_fields:
        if field not in data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Missing field: {field}"
            )

        # Numeric fields
        if field in ["loan_amount", "income", "age", "employment_length", "credit_score", "dti"]:
            validate_number(data[field], field)

    return True
