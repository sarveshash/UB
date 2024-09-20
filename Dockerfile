FROM debian:bookworm

RUN apt-get update && \
    apt-get install -y python3 python3-pip openjdk-17-jdk python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/Sophia

COPY . .

RUN python3 -m venv venv

RUN . venv/bin/activate && \
    pip install --upgrade pip setuptools && \
    pip install -U -r requirements.txt

CMD ["venv/bin/python", "-m", "Sophia"]
