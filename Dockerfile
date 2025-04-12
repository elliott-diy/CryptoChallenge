FROM python:3.5-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libffi-dev build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY encrypt.py .

CMD ["python", "encrypt.py"]
