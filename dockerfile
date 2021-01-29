# Select base image
FROM python:latest

# Create working directory
WORKDIR /app

# Install dependecies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Source code
COPY /src .

# Start program
CMD [ "python", "main.py" ]