# Use Python3.12 as base image
## You can find your Python version by running `python --version` in your terminal
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Update apt (while building the image, not when running the container)
RUN apt update -y
RUN apt upgrade -y

# Upgrade pip (while building the image, not when running the container)
RUN pip install --no-cache-dir --upgrade pip

# Install the dependencies (while building the image, not when running the container)
RUN pip install --no-cache-dir -r requirements.txt

# Run the exercise.py script when the container has launched
CMD ["python", "-u", "main.py"]