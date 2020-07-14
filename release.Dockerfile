FROM alpine:latest AS ci
WORKDIR /app
RUN apk add --no-cache \
    bash \
    nodejs \
    npm
COPY package.json package-lock.json ./
RUN npm ci
COPY combine release ./
CMD [ "./release" ]


node_modules/.bin/semantic-release \
    --repository-url "https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" 1>&2

jq -r ".version" < package.json
