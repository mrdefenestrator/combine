# Container for lint and testing
FROM alpine:latest
WORKDIR /app
RUN apk add --no-cache \
    bash \
    python3 \
    py3-pip
COPY ci_requirements.txt ./
RUN pip3 install -r ci_requirements.txt
COPY *.py ci ./
CMD [ "./ci" ]
