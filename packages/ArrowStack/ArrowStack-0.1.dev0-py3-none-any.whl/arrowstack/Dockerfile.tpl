FROM ubuntu:18.04

RUN apt-get update && apt-get install -y

WORKDIR /opt/lib
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.6 get-pip.py

COPY . /opt/{{ app_name }}

WORKDIR /opt/{{ app_name }}

CMD python3.6 app.py
