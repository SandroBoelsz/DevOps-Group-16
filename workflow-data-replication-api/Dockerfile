FROM alpine:latest

# Add Rclone to the container
RUN apk add rclone

# Install Python, pip, and bash
RUN apk add --no-cache python3 py3-pip bash

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Create a virtual environment and install dependencies inside it
RUN python3 -m venv venv \
    && /usr/src/app/venv/bin/pip install --upgrade pip \
    && /usr/src/app/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && /usr/src/app/venv/bin/pip install --no-cache-dir gunicorn

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set environment variables for Rclone
ENV UVA_MINIO_API=test
ENV SPAIN_MINIO_API=test
ENV MINIO_ACCESS_KEY_ID=test
ENV MINIO_ACCESS_KEY=test
ENV MINIO_REGION=test

# Run the application with Gunicorn
CMD ["/usr/src/app/venv/bin/python", "-m", "gunicorn", "--reload", "--bind", "0.0.0.0:5000", "run:app"]
