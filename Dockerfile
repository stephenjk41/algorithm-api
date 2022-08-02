FROM ubuntu:20.04 as ubuntu
RUN apt update && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install python3.9 python3-pip -y

RUN mkdir /home/root

COPY . /home/root/algorithm-api
WORKDIR /home/root/algorithm-api
RUN python3.9 -m pip install pipenv && \
    pipenv install --dev
RUN pip install -e .

CMD uvicorn algorithm_api.main:app --port 3000 --host 0.0.0.0