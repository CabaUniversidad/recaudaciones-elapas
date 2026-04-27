FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# El directorio de trabajo será la raíz del proyecto dentro del contenedor
WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo (incluyendo la carpeta /app) al directorio /code
COPY . .

EXPOSE 10000

# IMPORTANTE: Llamamos a app.main:app porque main.py está dentro de la carpeta app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]