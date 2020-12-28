import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapper.items import ScrapperItem

class SanetSpider(scrapy.Spider):
    name = 'demo'
   
    start_urls = ['https://attack.mitre.org/']
# tr/td/table/tbody/tr/td
    def parse(self, response):
       
       
        #  item=ScrapperItem()
        #  rows=Selector(response).xpath("//td[@class = 'tactic name']").css('a::text').extract()
        #  item['tactics']=rows
        #  yield item
        # rows=Selector(response).xpath('//*[@id="layouts-content"]/div[1]/div/div/div[2]/table/thead')
        # for row in rows:
        #     item=ScrapperItem()
        #     item['tactic_name']=row.xpath('tr/td[@class="tactic name"]/a/text()').extract()
        #     item['count']=row.xpath('tr/td[@class="tactic count"]/text()').extract()
        #     yield item
        
        # cols=Selector(response).xpath('//*[@id="layouts-content"]/div[1]/div/div/div[2]/table/tbody/tr/td[1]/table/tbody/tr[1]')
        # for col in cols:
        #     item=ScrapperItem()
        #     item['technique']=cols.xpath('td[1]/table/tbody/tr/td/div[@class="technique-cell supertechniquecell"]/a/text()').extract()
        #     yield item
        technique_with_sub
        technique_sub
        technique_without_sub
        tactic_name
        item=ScrapperItem()
        item['technique_with_sub']=response.xpath("//div[@class = 'technique-cell  supertechniquecell']").css('a::text').extract()
        item['technique_sub']=response.xpath("//div[@class='subtechnique']/div[@class = 'technique-cell ']").css('a::text').extract()
        # item['technique_sub_id']=Selector(response).xpath("//div[@class='subtechnique']/div[@class = 'technique-cell ']").css('a::title data-original-title').extract()
        item['technique_without_sub']=response.xpath("//tr[@class='technique-row']/td/div[@class = 'technique-cell ']").css('a::text').extract()
        item['tactic_name']=response.xpath("//td[@class = 'tactic name']").css('a::text').extract()
        item['count']=response.xpath("//td[@class = 'tactic count']/text()").extract()
        item['tech_sub_count']=response.xpath("//div[@class = 'technique-cell  supertechniquecell']/a").css('sub::text').extract()
        yield item


       