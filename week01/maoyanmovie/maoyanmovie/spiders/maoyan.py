import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

n_lim = 10

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        n = 0
        for movie in movies:
            if n >= 10:
                break

            item = MaoyanmovieItem()
            item['name'] = movie.xpath('./div[1]/span[1]/text()').extract_first()
            item['mold'] = movie.xpath('./div[2]/text()').extract()[1].split('\n')[1].strip()
            item['release_time'] = movie.xpath('./div[4]/text()')[1].extract().split('\n')[1].strip()

            n += 1

            yield item
