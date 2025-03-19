# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Ensure main.py is executable (WSL may have permission issues)
RUN chmod +x main.py

# Define the command to run the application
CMD ["python", "main.py"]
