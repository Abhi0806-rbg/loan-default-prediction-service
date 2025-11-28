from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/auth/register", json={
        "email": "unit@test.com",
        "password": "pass123"
    })
    assert response.status_code in [200, 400]  # may already exist

def test_login():
    response = client.post("/auth/login", json={
        "email": "unit@test.com",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
