# Etapa 1: build
FROM python:3.12-slim

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the code
COPY . .

# Run migrations automatically in the container
# ENTRYPOINT will be used to apply migrations before starting Gunicorn

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
# Port to expose
EXPOSE 8000
