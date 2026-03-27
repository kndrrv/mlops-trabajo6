import joblib
import pandas as pd
from pathlib import Path

# ruta al modelo usando ruta absoluta desde la raiz del proyecto
MODEL_PATH = Path(__file__).parent.parent / "models" / "modelo_stroke.joblib"

model = None

def load_model():
    global model
    # verifica que el archivo existe antes de cargarlo
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"modelo no encontrado en: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    print(f"modelo cargado desde: {MODEL_PATH}")

def predict(data: dict) -> dict:
    df = pd.DataFrame([data])
    prediccion = int(model.predict(df)[0])
    probabilidad = float(model.predict_proba(df)[0][1])

    if prediccion == 1:
        mensaje = "alto riesgo de stroke, consulte a un medico"
    else:
        mensaje = "bajo riesgo de stroke"

    return {
        "prediccion": prediccion,
        "probabilidad": round(probabilidad, 4),
        "mensaje": mensaje
    }