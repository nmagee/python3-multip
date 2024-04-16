FROM python:3.11
WORKDIR /
COPY / /
CMD pip install -r /requirements.txt
