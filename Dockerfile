FROM python:3.11
WORKDIR /
COPY / /
CMD apt update && apt install -y nano
CMD pip install -r /requirements.txt
