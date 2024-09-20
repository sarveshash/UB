FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y python3 python3-pip openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/Sophia

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Sophia"]
