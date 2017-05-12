# scraper-compose
Example project of anonymized scraping with Tor. (The spider is based on the [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)).

## Basic usage
This multi-container application uses [Docker Compose](https://docs.docker.com/compose/). In the project directory run the command

```
docker-compose build
```

followed by

```
docker-compose up
```

This will start the Tor and Privoxy services and initiate crawling the spider.
