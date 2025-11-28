import pickle
import json
from datetime import datetime

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from app.preprocess import preprocess_data
from app.core.config import settings
from app.utils import push_metadata

MODEL_PATH = "/model-storage/model.pkl"
METADATA_PATH = "/model-storage/metadata.json"


def train_models():
    # ---------------------------
    # Step 1 — Load training data
    # ---------------------------
    df = pd.read_csv("training_data.csv")

    # ---------------------------
    # Step 2 — Preprocess
    # ---------------------------
    X, y, encoder = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------------------------
    # Step 3 — Train Models
    # ---------------------------
    models = {
        "logistic_regression": LogisticRegression(max_iter=500),
        "random_forest": RandomForestClassifier(n_estimators=200),
        "xgboost": XGBClassifier(
            n_estimators=200,
            eval_metric="logloss",
            use_label_encoder=False
        )
    }

    trained_models = {}
    scores = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        scores[name] = accuracy_score(y_test, preds)
        trained_models[name] = model

    # ---------------------------
    # Step 4 — Pick best model
    # ---------------------------
    best_model_name = max(scores, key=scores.get)
    best_model = trained_models[best_model_name]
    best_score = scores[best_model_name]

    # ---------------------------
    # Step 5 — Save best model
    # ---------------------------
    with open(MODEL_PATH, "wb") as f:
        pickle.dump({
            "model": best_model,
            "encoder": encoder
        }, f)

    # ---------------------------
    # Step 6 — Save metadata
    # ---------------------------
    metadata = {
        "version": datetime.utcnow().isoformat(),
        "best_model": best_model_name,
        "accuracy": best_score,
        "trained_at": datetime.utcnow().isoformat(),
    }

    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f, indent=4)

    # ---------------------------
    # Step 7 — Notify Backend
    # ---------------------------
    push_metadata(metadata)

    return metadata


def load_metrics():
    """
    Return last saved model metadata.
    """
    with open(METADATA_PATH, "r") as f:
        return json.load(f)
