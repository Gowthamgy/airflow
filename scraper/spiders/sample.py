
import scrapy

class SampleSpider(scrapy.Spider):
    name = 'sample'
    start_urls = ['https://httpbin.org/html']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'email': 'john@example.com',
            'name': 'Gowtham'
        }
