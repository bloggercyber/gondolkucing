# Use an official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
RUN apt -y update
RUN apt install -y curl wget
# Set work directory in container
WORKDIR /app

# Copy requirements.txt (if available)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
