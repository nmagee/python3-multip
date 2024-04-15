FROM python:3.11
WORKDIR /
COPY * *
RUN python3 -m pip install -r /requirements.txt
