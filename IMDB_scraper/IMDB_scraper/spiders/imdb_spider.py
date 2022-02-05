import scrapy
import random

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/title/tt2250192/']


    def parse(self, response):
        url = response.url + "fullcredits/"
        yield scrapy.Request(url, callback = self.parse_full_credits)


    def parse_full_credits(self, response):
        actor = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        for next in actor:
            url = "https://www.imdb.com" + next
            yield scrapy.Request(url, callback = self.parse_actor_page)


    def parse_actor_page(self, response):
            actor_name = response.css("span.itemprop::text").get()
            hhh = response.css("div#content-2-wide.redesign")
            TV_Movie = hhh.css("div.filmo-row a::text").getall()
            TV_Movie = ",".join(TV_Movie)
            for i in TV_Movie.split(","):
                yield{
                    "actor":actor_name,
                    "Movie_or_TV_name":i
                }




    