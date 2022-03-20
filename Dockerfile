FROM python:3.9.10-alpine3.15

RUN mkdir code
RUN pip install --upgrade pip
COPY ./django_hello_world /code/
WORKDIR /code
RUN pip install -r ./requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
