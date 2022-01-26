import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    
    start_urls = ['https://www.imdb.com/title/tt2250192/?ref_=nv_sr_srsg_0']

    def parse(self, response):
        filename = f"imdb.html"
        with open(filename, "wb") as f:
            f.write(response.body)

