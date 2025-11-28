import numpy as np


def preprocess_input(data: dict):
    """
    Convert JSON input into numpy array the model can understand.
    Add encoding or feature engineering here.
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
            raise ValueError(f"Missing field: {field}")

    # Categorical encoding for loan_purpose
    purpose_map = {
        "business": 0,
        "education": 1,
        "car": 2,
        "house": 3,
        "medical": 4,
        "other": 5
    }

    purpose_encoded = purpose_map.get(data["loan_purpose"].lower(), 5)

    x = np.array([
        [
            float(data["loan_amount"]),
            float(data["income"]),
            float(data["age"]),
            float(data["employment_length"]),
            float(data["credit_score"]),
            float(data["dti"]),
            purpose_encoded
        ]
    ])

    return x
