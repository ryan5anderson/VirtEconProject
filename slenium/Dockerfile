# Use an official Python image as base
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script files into the container
COPY . .

# Set the default command
CMD ["python", "scraper.py"]

