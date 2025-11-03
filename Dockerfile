# Use a lightweight official Python image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies first (for better caching)
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./app /app

# Expose the port Gunicorn will run on (5000 is default for Flask)
EXPOSE 5000

# Command to run the application using Gunicorn (production web server)
# The format is: gunicorn -b <bind address:port> <module_name>:<callable_name>
# We bind to 0.0.0.0 to listen on all interfaces inside the container.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]