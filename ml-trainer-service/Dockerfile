FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/
COPY training_data.csv /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

# Model storage volume
VOLUME ["/model-storage"]

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
