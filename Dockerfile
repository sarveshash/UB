FROM python:3.11-slim-bullseye

WORKDIR /root/Sophia

COPY . .

RUN pip3 install --upgrade pip setuptools
RUN apt install -y git
RUN pip3 install -U -r requirements.txt

CMD ["python3", "-m", "Sophia"]
