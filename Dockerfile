FROM python

WORKDIR /root/Sophia

COPY . .

FROM openjdk:21-jre-slim as openjdk

FROM node:latest as nodejs

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Sophia"]
