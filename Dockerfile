# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install necessary build tools
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the image
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Expose the port that the application will run on
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]
