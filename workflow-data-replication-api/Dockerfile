FROM alpine:latest

# Install Python, pip, and bash
RUN apk add --no-cache python3 py3-pip bash

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Create a virtual environment and install Python dependencies including Gunicorn
RUN python3 -m venv venv \
    && . /usr/src/app/venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application with Gunicorn
CMD ["/bin/sh", "-c", ". /usr/src/app/venv/bin/activate && gunicorn --bind 0.0.0.0:5000 run:app"]