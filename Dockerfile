# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt requirements_gui.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements_gui.txt

# Copy application files
COPY foreplay_gui.py .
COPY foreplay_client.py .
COPY config.py .

# Expose Streamlit default port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "foreplay_gui.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true", "--browser.serverAddress=0.0.0.0"]

