import scrapy
from lxml import html

class CaptionSpider(scrapy.Spider):
    name = "Caption"
    start_urls = ['https://imgflip.com/meme/Mocking-Spongebob']

    def parse(self, response):
        if not response:
            self.log("Failed to fetch page")
            return None
        self.log(response.text)
        parser = html.fromstring(response.text)
        search_results = parser.xpath("//li[@class='component_property-card js-component_property-card js-quick-view ']")
        self.log(parser)
        self.log('test')
        self.log(searchresults)