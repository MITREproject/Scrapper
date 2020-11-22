import scrapy
from scrapy.http import Request


class SanetSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['sanet.st']
    start_urls = ['https://attack.mitre.org/']

    def parse(self, response):
        
        yield {
            # Do something.
             "id":  response.xpath('//span[@h5 card-title]/text()').extract_first().strip(),
                # "synopsis": tr_sel.css("div.pt4::text").extract_first(),
                # "type_": tr_sel.css('td:nth-child(3)::text').extract_first().strip(),
                # "episodes": tr_sel.css('td:nth-child(4)::text').extract_first().strip(), 
                # "rating": tr_sel.css('td:nth-child(5)::text').extract_first().strip(),
            
        }

        # next_page = /page-{}/ where {} number of page.
        next_page = response.xpath('//div[@class="technique-cell supertechniquecell"]/@href').extract_first()

        # next_page = https://sanet.st/page-{}/ where {} number of page.
        next_page = response.urljoin(next_page)

        # If next_page have value
        if next_page:
            # Recall parse with url https://sanet.st/page-{}/ where {} number of page.
            yield scrapy.Request(url=next_page, callback=self.parse)