FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "hello_world_project.wsgi:application", "--bind", "0.0.0.0:8000"]