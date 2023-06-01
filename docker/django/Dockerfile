# Base image
FROM python:3.12.0b1-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the port that Django runs on
EXPOSE 8000

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get install -y libpq-dev

# Copy only requirements.txt first to leverage Docker layer caching
COPY crystal/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the container
COPY crystal /app/crystal

# Set working directory
WORKDIR /app/crystal

# Sleep for 5 seconds before running migrate
CMD sleep 5 \
&& python manage.py migrate \
&& echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('tibia', '', 'clicky')" | python manage.py shell \
&& python manage.py runserver 0.0.0.0:8000
