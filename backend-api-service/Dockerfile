# ==============================
# Stage 1: Base Image
# ==============================
FROM python:3.10-slim as base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

COPY app/ ./app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ==============================
# Stage 2: Runtime Image
# ==============================
FROM python:3.10-slim

WORKDIR /app

COPY --from=base /usr/local /usr/local
COPY --from=base /app /app

EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
