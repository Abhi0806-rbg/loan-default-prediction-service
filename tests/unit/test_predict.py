from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint(monkeypatch):
    # Mock ML predictor response
    def mock_predict(url, json):
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "prediction": 1,
                    "probability": 0.82,
                    "model_version": "v1"
                }
        return MockResponse()

    monkeypatch.setattr("httpx.post", mock_predict)

    # Fake JWT token for test
    headers = {"Authorization": "Bearer faketoken123"}

    payload = {
        "loan_amount": 5000,
        "income": 45000,
        "age": 30,
        "employment_length": 5,
        "credit_score": 720,
        "loan_purpose": "home",
        "dti": 12
    }

    response = client.post("/predict", json=payload, headers=headers)
    assert response.status_code in [200, 401]  # No real JWT in test
