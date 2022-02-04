import scrapy
import random

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/title/tt0106145/']


    def parse(self, response):
        url = response.url + "fullcredits/"
        yield scrapy.Request(url, callback = self.parse_full_credits)


    def parse_full_credits(self, response):
        actor = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        for next in actor:
            url = "https://www.imdb.com" + next
            yield scrapy.Request(url, callback = self.parse_actor_page)


    def parse_actor_page(self, response):
        for element in response.css("div#content-2-wide.redesign"):
            actor_name = element.css("span.itemprop::text").get()
            TV_Movie = element.css("div.filmo-row a::text").getall()
            TV_Movie = ",".join(TV_Movie)

            yield {"actor" : actor_name, "movie_or_TV_name" : TV_Movie}




    