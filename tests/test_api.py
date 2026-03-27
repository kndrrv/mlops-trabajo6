from fastapi.testclient import TestClient
from app.main import app
from app import model as stroke_model

# cliente de prueba
client = TestClient(app)

# test 1: verificar que la api esta activa
def test_root():
    response = client.get("/")
    assert response.status_code == 200

# test 2: verificar el health check
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["estado"] == "activo"

# test 3: verificar que el endpoint predict responde
def test_predict():
    # cargar el modelo manualmente antes del test
    stroke_model.load_model()

    response = client.post("/predict", json={
        "age": 45.0,
        "avg_glucose_level": 85.0,
        "bmi": 25.0,
        "gender": "Male",
        "ever_married": "Yes",
        "work_type": "Private",
        "Residence_type": "Urban",
        "smoking_status": "never smoked",
        "hypertension": 0,
        "heart_disease": 0
    })
    assert response.status_code == 200
    assert "prediccion" in response.json()
    assert "probabilidad" in response.json()
    assert "mensaje" in response.json()