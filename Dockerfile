FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY .env .env

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]


