# imagen base liviana de python 3.11
FROM python:3.11-slim

# directorio de trabajo dentro del contenedor
WORKDIR /app

# copiar dependencias primero (aprovecha cache de docker)
COPY requirements.txt .

# instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# copiar el codigo de la aplicacion
COPY app/ ./app/

# copiar el modelo
COPY models/ ./models/

# puerto que expone la api
EXPOSE 8000

# comando para iniciar la api
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]