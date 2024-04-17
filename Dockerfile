FROM python:3.12.2-alpine3.19
WORKDIR /
COPY / /
RUN apk add nano && \
  chmod 755 /pi && \
  mv /pi /usr/bin/pi
CMD /usr/bin/pi
