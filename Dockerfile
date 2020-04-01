FROM python:3.6.9

# COPY .ssh/* /root/.ssh/

# RUN git clone git@github.com:2509934810/flask_demo_1.git && cd flask_demo_1/ && pip3 install -r requirements.txt

# RUN rm -rf /root/.ssh/

# WORKDIR /workspace/lovehome/flask_demo_1/

COPY ./sources.list /etc/apt

WORKDIR /workspace/lovehome/

RUN apt update && pip3 install pipenv -i https://mirrors.aliyun.com/pypi/simple

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --dev

COPY . .

ENTRYPOINT [ "flask" ]

EXPOSE 5000
EXPOSE 5001
EXPOSE 80
CMD ["--help"]