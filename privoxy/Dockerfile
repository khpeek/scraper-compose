FROM alpine:latest
EXPOSE 8118
RUN apk --update add privoxy
COPY config /etc/privoxy/config
CMD ["privoxy", "--no-daemon", "/etc/privoxy/config"]