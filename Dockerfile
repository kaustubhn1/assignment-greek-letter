FROM ubuntu:18.04

RUN  apt-get update && apt-get -y install python3-pip \
        && python3 -m pip install pip --upgrade pip\
        && apt-get -y install python3-venv 
WORKDIR /test
ENV VIRTUAL_ENV=/myenv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/bin/bash", "start.sh"]