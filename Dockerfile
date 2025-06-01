# Base image with Geo libraries and Python
FROM kartoza/geopandas:latest

# Set workdir
WORKDIR /app

# Copy code
COPY . .

# Install additional Python packages if needed
RUN pip install --no-cache-dir -r requirements.txt

# Expose Dash app port
EXPOSE 8050

# Run the app
CMD ["python", "main.py"]
