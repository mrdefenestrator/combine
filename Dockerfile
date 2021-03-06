# Container for CLI
FROM alpine:latest
WORKDIR /app
RUN apk add --no-cache \
    python3 \
    py3-pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY combine.py ./
ENTRYPOINT [ "./combine.py" ]
