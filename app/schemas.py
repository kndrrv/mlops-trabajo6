from pydantic import BaseModel

# datos de entrada que recibe el endpoint /predict
class strokeinput(BaseModel):
    age: float
    avg_glucose_level: float
    bmi: float
    gender: str
    ever_married: str
    work_type: str
    Residence_type: str
    smoking_status: str
    hypertension: int
    heart_disease: int

    model_config = {
        "json_schema_extra": {
            "example": {
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
            }
        }
    }

# respuesta que devuelve el endpoint /predict
class strokeoutput(BaseModel):
    prediccion: int       # 0 = no stroke, 1 = stroke
    probabilidad: float   # probabilidad entre 0 y 1
    mensaje: str          # interpretacion en texto