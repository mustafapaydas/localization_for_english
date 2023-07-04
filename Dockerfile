FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

FROM python:3.8

WORKDIR /app
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

VOLUME /data

ENV DB_NAME=_db_name
ENV DB_USERNAME=_db_user_name
ENV DB_PASSWORD=_db_password
ENV DB_HOST=_db_host

CMD ["python", "main.py"]