FROM python:3.9.1
USER root

RUN mkdir streamlit

WORKDIR /root/streamlit/

RUN apt-get update
COPY . .

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install streamlit

CMD ["streamlit", "run", "app.py"]
