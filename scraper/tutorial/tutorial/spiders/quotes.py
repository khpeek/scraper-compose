# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/page/{n}/'.format(n=n) for n in range(1, 3)]

    custom_settings = {
                       }

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('small.author::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
