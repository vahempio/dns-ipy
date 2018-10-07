FROM python:3.7-alpine

LABEL maintainer="vahempio@gmail.com"

RUN pip3 install --no-cache-dir dnslib

COPY dns-ipy.py /

CMD [ "python3", "/dns-ipy.py" ]
