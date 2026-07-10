# FIXED: Upgraded from buster to bookworm to fix the broken apt repositories
FROM python:3.10-slim-bookworm

WORKDIR /app
COPY . /app

# FIXED: Combined updates, installations, and pip into a single layer for better Docker caching
RUN apt-get update -y && \
    apt-get install awscli -y && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]