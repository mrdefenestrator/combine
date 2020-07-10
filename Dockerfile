FROM alpine:latest AS ci
WORKDIR /app
RUN apk add --no-cache \
    bash \
    python3 \
    py3-pip
COPY ci_requirements.txt ./
RUN pip3 install -r ci_requirements.txt
COPY lint test combine ./
RUN ./lint
RUN ./test

FROM alpine:latest AS build
WORKDIR /app
RUN apk add --no-cache \
    python3 \
    py3-pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY combine ./
ENTRYPOINT [ "./combine" ]
