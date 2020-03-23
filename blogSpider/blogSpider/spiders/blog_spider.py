import scrapy
import json

class BlogSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        'https://www.design-seeds.com/blog/',
        ]

    def parse(self, response):
        yield {
            'url': response.css('.parker-featured-img>a>img::attr(src)').get(),
        }