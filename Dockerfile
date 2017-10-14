FROM debian:jessie

MAINTAINER librescan@gmail.com

ADD ./ /app

WORKDIR /app

RUN apt-get update && \
    apt-get -y install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libjpeg-dev libssl-dev libffi-dev libturbojpeg1-dev libyaml-dev && \
    sh misc/Dependencies.sh && \
    pip3 install -r src/requirements.txt

WORKDIR src/

RUN python3 setup.py

ENV LS_DEV_MODE=False

VOLUME /root/LibreScanProjects

EXPOSE 8080

CMD ["python3", "main.py", "web"]
