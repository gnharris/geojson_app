# Use a public geopandas image that includes shapely, fiona, pyproj, etc.
FROM geopandas/geopandas:latest

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Install additional Python packages
RUN pip install --no-cache-dir dash pandas

# Expose port for Dash
EXPOSE 8050

# Run the app
CMD ["python", "main.py"]
