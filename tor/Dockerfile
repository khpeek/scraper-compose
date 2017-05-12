FROM alpine:latest
EXPOSE 9050 9051
RUN apk --update add tor
COPY torrc /etc/tor/torrc
ARG password
RUN echo "HashedControlPassword $(tor --quiet --hash-password $password)" >> /etc/tor/torrc
CMD ["tor"]