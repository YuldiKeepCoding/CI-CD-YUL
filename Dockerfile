# Establece la imagen base como Python 3.10
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

# Copia el contenido del directorio "app" al directorio de trabajo
COPY app .

# Comando que se ejecutará cuando se inicie el contenedor
CMD python3 main.py