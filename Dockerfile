FROM alpine:latest

RUN apk --update add redis
ADD entrypoint.sh entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
