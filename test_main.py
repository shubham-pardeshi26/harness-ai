from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "server" in response.json()


def test_train_model():
    response = client.post("/train")
    assert response.status_code == 200
    assert response.json()["message"] == "Model trained successfully"


def test_predict():
    client.post("/train")  # Ensure model is trained before prediction
    response = client.get("/predict")
    assert response.status_code == 200
    assert "prediction" in response.json()
