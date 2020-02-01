FROM ubuntu:18.04

RUN apt update && apt install -y python3 python3-pip git


COPY ./* /workspace/lovehome/

WORKDIR /workspace/lovehome

RUN git clone git@github.com:2509934810/flask_demo_1.git && cd /workspace/lovehome/flask_demo_1

RUN pipenv shell && pipenv install

EXPOSE 5000

CMD ["/bin/bash", "flask run"]
