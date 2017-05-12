# Adapted from trcook/docker-scrapy
FROM python:alpine
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
COPY requirements.txt /scraper/requirements.txt
RUN pip install -r /scraper/requirements.txt
COPY tutorial /scraper/tutorial
COPY wait-for/wait-for /scraper/tutorial
WORKDIR /scraper/tutorial
CMD ["./wait-for", "tor:9050", "--", "scrapy", "crawl", "quotes"]

