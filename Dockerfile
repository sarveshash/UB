FROM python:latest

WORKDIR /root/Sophia

COPY . .

RUN apt-get update && apt-get install -y openjdk-21 default-jre nodejs npm

RUN pip3 install --upgrade pip setuptools
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Sophia"]
