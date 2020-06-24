from scrapy import Request
from scrapy.spiders import Spider
from cat_movie.items import CatMovieItem
from scrapy.selector import Selector

class movie_spider(Spider):
    name = "cat"
    # allowed_domains = ['https://maoyan.com']
    # start_urls = ['https://maoyan.com/board']

    def start_requests(self):
        url = 'https://maoyan.com/board'
        yield Request(url)

    def parse(self, response):
        selector = Selector(response=response).xpath("//div[@class='movie-item-info']")
        for ones_selector in selector:
            name = ones_selector.xpath("p[@class='name']/a/text()").extract()[0]
            rel = ones_selector.xpath("p[@class='releasetime']/text()").extract_first()
            part_url = ones_selector.xpath("p[@class='name']/a/@href").extract_first()
            link = "https://maoyan.com" + part_url
            item = CatMovieItem()
            item['name'] = name
            item['rel'] = rel
            # item['type']= type
            yield Request(link,meta={"item":item},callback=self.parse_page)

    def parse_page(self,response):
        item = response.meta['item']
        type = response.xpath("//div[@class='movie-brief-container']/ul/li[@class='ellipsis']/a/text()").extract_first()
        item['type'] = type

        yield item
