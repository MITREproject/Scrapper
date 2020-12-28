import scrapy
from scrapy.http import Request
from scrapper.items import ScrapItem 

class Scrap1(scrapy.Spider):
    name='t1'
    start_urls = ['https://attack.mitre.org/#']

    def parse(self, response):

        id = response.xpath("//div[@class = 'technique-cell  supertechniquecell']").css('a::attr(title)').getall()+response.xpath("//div[@class = 'technique-cell  supertechniquecell']").css('a::text').getall()

        items=ScrapItem()
        items['id']=id
        yield items