# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install Django
RUN pip install --upgrade pip
RUN pip install django

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server bound to 0.0.0.0 on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

