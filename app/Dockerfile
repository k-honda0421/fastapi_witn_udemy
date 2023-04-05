FROM python:3.9.1
USER root

RUN mkdir app

WORKDIR /root/app/

RUN apt-get update
COPY . .

RUN apt-get install -y vim less
RUN apt-get install -y sqlite3
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["uvicorn", "sql_app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
