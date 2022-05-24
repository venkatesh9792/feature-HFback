FROM python:3.9.5

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
EXPOSE 5432
CMD ["python", "app.py"]