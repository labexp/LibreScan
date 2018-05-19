FROM labexperimental/debian:jessie

MAINTAINER LabExperimental <librescan@gmail.com>

VOLUME /root/LibreScanProjects

VOLUME /root/.librescan

VOLUME /dev/bus/usb

EXPOSE 8080

ADD ./ /librescan

WORKDIR /tmp

RUN python3 -m venv ~/.virtualenvs/librescan && \
    /bin/bash -c "source ~/.virtualenvs/librescan/bin/activate" && \
    chmod +x /librescan/misc/chdkptp_dependency.sh && \
    chmod +x /librescan/misc/docker-entry.sh && \
    sh /librescan/misc/chdkptp_dependency.sh

WORKDIR /librescan/src

RUN pip install -r requirements.txt && \
    python setup.py

ENV LS_DEV_MODE=False

ENTRYPOINT ["../misc/docker-entry.sh"]