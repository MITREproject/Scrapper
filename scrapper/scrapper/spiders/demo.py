import scrapy
from scrapy.http import Request


class SanetSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['sanet.st']
    start_urls = ['https://attack.mitre.org/']
# tr/td/table/tbody/tr/td
    def parse(self, response):
        #for row in response.xpath('//[@class="matrix side"]//td//tr/table/tbody/'):
         for row in response.xpath('//[@class="matrix side"]//thead/tr/'):

            yield {
                # Do something.
                
               'tactic':row.xpath('td/a/text()').extract_first()
                
            }

        # # next_page = /page-{}/ where {} number of page.
        # next_page = response.xpath('//div[@class="technique-cell supertechniquecell"]/@href').extract_first()

        # # next_page = https://sanet.st/page-{}/ where {} number of page.
        # next_page = response.urljoin(next_page)

        # # If next_page have value
        # if next_page:
        #     # Recall parse with url https://sanet.st/page-{}/ where {} number of page.
        #     yield scrapy.Request(url=next_page, callback=self.parse)