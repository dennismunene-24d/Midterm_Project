# Use official Python 3.13 slim image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (leverage Docker cache)
COPY requirements.txt .

# Install system dependencies for Python packages
# Remove unnecessary packages like libxml2-dev, libxslt1-dev, etc. unless needed
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libffi-dev \
        libssl-dev \
        wget \
        curl \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY predict.py train.py final_dt_model.bin ./
# Optionally copy notebooks if needed
COPY *.ipynb ./

# Expose API port
EXPOSE 9696

# Default command to run the API
CMD ["python", "predict.py"]
