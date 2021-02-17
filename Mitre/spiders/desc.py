import scrapy
import re
import string 
from ..items import MitreItem


class MitreDesc(scrapy.Spider):
    name='desc'
    start_urls = [
		'https://attack.mitre.org/'  #url which we want to scrap
	]

    def parse(self, response):
	    url = response.css('table.techniques-table a::attr(href)').extract()
	    for item in url:
		    yield response.follow(item, callback = self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        technique_name = response.css('h1::text').extract()
        detection=response.xpath("//div[@class = 'container-fluid']/div/p/text()").extract()
        description=response.xpath("//div[@class = 'description-body']/p/text()").extract()
        mitigation=response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']//a/text()").extract()
        miti_descri=response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']//p/text()").extract()
        proc_example=response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']//td/p/text()").extract()
        dict1={}
        

        dict1['Technique']=technique_name
        dict1['Description']=description
        dict1['Mitigation']=mitigation
        dict1['Detection']=detection
        dict1['Mitigation_Description']=miti_descri
        dict1['proc_example']=proc_example
        yield MitreItem(**dict1)
