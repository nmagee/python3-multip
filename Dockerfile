FROM python:3.11
WORKDIR /
COPY / /
RUN apt update && \
  apt install -y nano && \
  rm -rf /var/lib/apt/lists/* && \
  chmod 755 /pi && \
  mv /pi /usr/bin/pi && \
  pip install -r /requirements.txt
CMD /usr/bin/pi
