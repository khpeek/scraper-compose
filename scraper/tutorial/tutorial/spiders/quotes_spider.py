import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/page/{n}/'.format(n=n) for n in range(1, 3)]

    custom_settings = {
                       'TOR_RENEW_IDENTITY_ENABLED': True,
                       'TOR_ITEMS_TO_SCRAPE_PER_IDENTITY': 5
                       }

    download_delay = 2    # Wait 2 seconds (actually a random time between 1 and 3 seconds) between downloading pages


    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('small.author::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item