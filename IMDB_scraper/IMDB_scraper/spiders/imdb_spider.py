import scrapy
import random

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/title/tt2250192/']


    def parse(self, response):
        '''The function has two variables one is self and another is response.
        The purpose of this function is to go to the next page we want.
        '''
        # strat from original URL and go to the next.
        url = response.url + "fullcredits/"
        # use request to go to next link and apply next function.
        yield scrapy.Request(url, callback = self.parse_full_credits)


    def parse_full_credits(self, response):
        '''The function has two variables one is self and another is response.
        The purpose of this function is scrap all the actor names, and go to their
        own pages.
        '''
        # this is the hint given by professor, we can get the next link.
        actor = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        # because there are many actors, so we would like to go to many next pages.
        for next in actor:
            # write a URL per itration. 
            url = "https://www.imdb.com" + next
            # then, went to the next link and apply next funtion.
            yield scrapy.Request(url, callback = self.parse_actor_page)


    def parse_actor_page(self, response):
        '''The function has two variables one is self and another is response.
        The purpose of this function is scrap the actor's name and TV or Moive he 
        has worked before.
        '''
        # extract actor's name
        actor_name = response.css("span.itemprop::text").get()
        # get TV or Movie shows which the actor has worked before.
        boxes = response.css("div#content-2-wide.redesign")
        TV_Movie = boxes.css("div.filmo-row b a::text").getall()
        TV_Movie = ",".join(TV_Movie)
        # use for loop, so what we can get one row which contains the actor name and one TV or Movie show.
        for i in TV_Movie.split(","):
            yield{
                "actor":actor_name,
                "Movie_or_TV_name":i
            }




    