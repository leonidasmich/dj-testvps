FROM python:3.11-slim 

WORKDIR /code  # Match this with the volume mapping in docker-compose.yml

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "hello_world_project.wsgi:application", "--bind", "0.0.0.0:8000"]