# Use an official Python runtime as the base image
FROM python:3.12.7-slim

# Set environment variables to prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port the Flask app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

# Command to run the application
CMD ["python", "wsgi.py"]
