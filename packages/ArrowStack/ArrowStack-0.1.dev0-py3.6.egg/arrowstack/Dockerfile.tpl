FROM ubuntu:18.04

WORKDIR /opt/lib
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.6 get-pip.py
