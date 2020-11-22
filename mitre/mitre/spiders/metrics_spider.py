import scrapy
from ..items import MitreItem

class MetricsSpider(scrapy.Spider):
	name = 'metrics'
	start_urls = [
		'https://attack.mitre.org/'
	]

	def parse(self, response):
		# title = response.css('title::text').extract()
		# yield {'titletext' : title}
		items = MitreItem()
		tactics = response.xpath("//td[@class = 'tactic name']").css('a::text').extract()
		#yield {'Tactics' : tactics}
		items['tactic_name'] = tactics
		yield items