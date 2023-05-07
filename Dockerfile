FROM python:3.10

WORKDIR /app

copy requirements.txt requirements.txt

RUN pip install -r requirements.txt

copy . .

Expose 8000

CMD python manage.py runserver 0.0.0.0:8000