FROM python:3.9.5

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app


ENV HOST 0.0.0.0
ENV PORT 5000
EXPOSE 5000
CMD ["python", "app.py"]