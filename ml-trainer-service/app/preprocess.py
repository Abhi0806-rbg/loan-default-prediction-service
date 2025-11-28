import pandas as pd
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

def preprocess_data(df):
    """
    Clean, encode, and prepare dataset for training.
    """
    df = df.copy()

    # Encode categorical column
    df["loan_purpose"] = label_encoder.fit_transform(df["loan_purpose"])

    # Features
    X = df.drop("default", axis=1)
    y = df["default"]

    return X, y, label_encoder
