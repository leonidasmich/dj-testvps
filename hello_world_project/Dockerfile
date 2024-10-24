# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Command to run your application
CMD ["gunicorn", "hello_world_project.wsgi:application", "--bind", "0.0.0.0:8000"]
