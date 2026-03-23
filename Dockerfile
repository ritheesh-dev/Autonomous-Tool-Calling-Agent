RUN useradd -m appuser
USER appuser

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD ["python", "src/main.py"]



