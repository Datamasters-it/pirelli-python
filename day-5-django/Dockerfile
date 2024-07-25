# Use the official Python image from the Docker Hub
FROM python

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# RUN python manage.py migrate

# Run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
