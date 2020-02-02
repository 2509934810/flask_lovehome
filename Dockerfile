FROM python:3.7

COPY ./* /workspace/lovehome/flask_demo_1/

WORKDIR /workspace/lovehome/flask_demo_1/

RUN cd /workspace/lovehome/flask_demo_1/ && pip3 install -r requirements.txt

EXPOSE 5000

CMD ["/bin/bash", "python3 setup.py"]