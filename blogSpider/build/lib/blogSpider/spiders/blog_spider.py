import scrapy
import json

class BlogSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        'https://www.design-seeds.com/blog/',
        ]

    def parse(self, response):
        data = {}
        data["url"] = response.css('.parker-featured-img>a>img::attr(src)').get()
        with open('./url.json', 'wb') as f:
            json.dump(data, f)
        #yield {
        #    'url': response.css('.parker-featured-img a::attr(href)').get(),
        #}