# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /PYTHON-SCRIPT

# Copy the local code to the container image
COPY . .

# Install any dependencies your Python script needs
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your Python script
CMD ["python", "index.py"]
