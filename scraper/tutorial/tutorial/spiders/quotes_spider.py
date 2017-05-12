import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/page/{n}/'.format(n=n) for n in range(1, 3)]

    custom_settings = {
                       'TOR_RENEW_IDENTITY_ENABLED': True,
                       'TOR_ITEMS_TO_SCRAPE_PER_IDENTITY': 5
                       }


    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('small.author::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item