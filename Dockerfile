# Use official Python slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies for GeoPandas and shapely
RUN apt-get update && apt-get install -y \
    build-essential \
    gdal-bin \
    libgdal-dev \
    python3-dev \
    libspatialindex-dev \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip packages
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose Dash port
EXPOSE 8050

# Start the app
CMD ["python", "main.py"]
