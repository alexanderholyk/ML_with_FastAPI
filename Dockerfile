# use an official lightweight Python image as a parent image
FROM python:3.9-slim

# set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt to the container at /app
COPY requirements.txt /app/

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container at /app
COPY . /app

# make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run the application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
