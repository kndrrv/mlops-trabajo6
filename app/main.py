from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.schemas import strokeinput, strokeoutput
from app import model as stroke_model

# ──────────────────────────────────────────
# lifespan: carga el modelo al iniciar la api
# se ejecuta una sola vez al arrancar
# ──────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    stroke_model.load_model()
    yield

# crear la aplicacion fastapi
app = FastAPI(
    title="api prediccion de stroke",
    description="modelo de machine learning para predecir riesgo de stroke",
    version="1.0",
    lifespan=lifespan
)

# ──────────────────────────────────────────
# endpoint raiz
# ──────────────────────────────────────────

@app.get("/", tags=["inicio"])
def root():
    return {
        "mensaje": "api de prediccion de stroke",
        "version": "1.0",
        "endpoints": {
            "prediccion": "/predict",
            "health": "/health",
            "docs": "/docs"
        }
    }

# ──────────────────────────────────────────
# health check: verifica que la api esta activa
# ──────────────────────────────────────────

@app.get("/health", tags=["inicio"])
def health():
    return {
        "estado": "activo",
        "modelo": "modelo_stroke.joblib",
        "version": "1.0"
    }

# ──────────────────────────────────────────
# endpoint de prediccion
# recibe los features y devuelve la prediccion
# ──────────────────────────────────────────

@app.post("/predict", response_model=strokeoutput, tags=["prediccion"])
def predict(data: strokeinput):
    try:
        # convertir el input a diccionario y predecir
        resultado = stroke_model.predict(data.model_dump())
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))