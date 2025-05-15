FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

EXPOSE 5000

# Start
CMD ["python", "app.py"]