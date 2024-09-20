FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/Sophia

COPY . .

RUN pip install --upgrade pip setuptools

RUN pip install -U -r requirements.txt

CMD ["python", "-m", "Sophia"]
