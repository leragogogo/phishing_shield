# Dockerfile

# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run your app
CMD ["python", "main.py"]
