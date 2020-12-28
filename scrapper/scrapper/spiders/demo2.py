import scrapy
import re
import string 
from ..items import ScrapperItem

class MetricsSpider(scrapy.Spider):
	name = 'demo2'  #name of the spider
	start_urls = [
		'https://attack.mitre.org/'  #url which we want to scrap
	]

	def parse(self, response):
		#title = response.css('title::text').extract()
		#yield {'titletext' : title}
		# items = MitreItem() #creating object of MitreItem class
		# tactics = response.xpath("//td[@class = 'tactic name']").css('a::text').extract()
		# #yield {'Tactics' : tactics}
		# items['tactic_name'] = tactics
		# yield items

		url = response.css('div.technique-cell a::attr(href)').extract()
		for item in url:
			yield response.follow(item, callback = self.parse_dir_contents)

	def parse_dir_contents(self, response):
	    other = response.xpath("//div[@class = 'card-data']/text()").extract()
	    id = response.css('[id="card-id"]::text').extract()
	    sub_technique = response.xpath("//div[@class = 'card-data']//a/text()").extract()
	    tactic = response.css('[id="card-tactics"]::text').extract()
	    platform = response.css('[id="card-platforms"]::text').extract()
	    technique_name = response.css('h1::text').extract()

	    tactic = "".join(tactic)
	    # tactic = tactic.replace(" ", "")
	    tactic = tactic.replace("\n", "")
	    technique_name = "".join(technique_name)
	    technique_name = technique_name.replace(" ", "")
	    technique_name = technique_name.replace("\n", "")

	    items = ScrapperItem() #creating object of MitreItem class
	    items['id'] = "".join(id[0])
	    items['sub_technique'] = sub_technique
	    items['tactic'] = tactic
	    items['platform'] = "".join(platform[0])
	    items['technique_name'] = technique_name
	    items['data_sources'] = other[-4]
	    items['version'] = other[-3]
	    items['created'] = other[-2]
	    items['last_modified'] = other[-1]
	    yield items