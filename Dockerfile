FROM python:3.11
WORKDIR /
COPY / /
CMD apt update && apt install -y nano && chmod 755 pi && pip install -r /requirements.txt
