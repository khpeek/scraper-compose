# Adapted from trcook/docker-scrapy
FROM python:alpine
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN pip install scrapy scrapy-fake-useragent stem pyparsing python-dateutil requests
COPY tutorial /scraper/tutorial
COPY wait-for/wait-for /scraper/tutorial
WORKDIR /scraper/tutorial
CMD ["./wait-for", "tor:9050", "--", "scrapy", "crawl", "quotes"]

