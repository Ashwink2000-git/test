# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the calculator.py file and templates folder into the container at /app
COPY calculator.py .
COPY templates/ templates/

# Expose port 1000 for the application
EXPOSE 1000

# Set the command to run the calculator app
CMD ["python", "calculator.py"]

