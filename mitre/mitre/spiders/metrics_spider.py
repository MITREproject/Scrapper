import scrapy
import re
import string 
from ..items import MitreItem

class MetricsSpider(scrapy.Spider):
	name = 'metrics'  #name of the spider
	start_urls = [
		#'https://attack.mitre.org/techniques/T1529/'  #url which we want to scrap
		'https://attack.mitre.org'
	]

	def parse(self, response):
		url = response.css('table.techniques-table a::attr(href)').extract()
		for item in url:
			yield response.follow(item, callback = self.parse_dir_contents)

	def parse_dir_contents(self, response):

		TechniqueData = {} #to be used as dynamic item

		keys = response.xpath("//span[@class = 'h5 card-title']")
		values = response.xpath("//div[@class = 'col-md-11 pl-0']")
		
		print(len(keys), len(values))

		for i in range(len(keys)):
			key = keys[i].xpath('text()').extract()
			key[0] = key[0].replace("\xa0", "")
			value = values[i].xpath('text()' + "|" + "a/text()").extract()
			temp_val = []
			for j in range(len(value)):
				value[j] = value[j].strip()
				if not "\n" in value[j] and len(value[j]) > 1:
					temp_val.append(value[j])
			TechniqueData[key[0]] = temp_val

		TechniqueData['Detection'] = "".join(response.xpath("//div[@class = 'container-fluid']/div/p/text()").extract())
		TechniqueData['Description'] = "".join(response.xpath("//div[@class = 'description-body']/p/a/text()" + "|" 
			+ "//div[@class = 'description-body']/p/text()").extract())	

		Mitigations = {}
		ProcedureExamples = {}		    

		tables = response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']")

		for i in range(len(tables)):
			type = tables[i].xpath('thead/tr/th/text()').extract()[1]
			for row in tables[i].xpath('tbody/tr'):
				keys = row.xpath('td/a/text()')[0].extract() 
				mid_values = row.xpath('td/a/text()')[1].extract()
				values = row.xpath("td/p/text()" + "|" + "td/p/a/text()").extract()
				values = "".join(values)
				keys=''.join(e for e in keys if e.isalnum())
				if type == "Name":
					ProcedureExamples[keys.strip().lower()] = mid_values + " : " + values
				elif type == "Mitigation":
					Mitigations[keys.strip().lower()] = mid_values + " : " + values

		if Mitigations:
			TechniqueData['mitigations'] = Mitigations
		if ProcedureExamples:
			TechniqueData['procedureexamples'] = ProcedureExamples
			if not Mitigations:
				Mitigations['mitigations'] = response.xpath("//div[@class = 'container-fluid']/p[not(@scite-citeref-number)]/text()").extract()[0].strip() 
				TechniqueData['mitigations']= Mitigations

		#returning the created dictionary
		yield MitreItem( **TechniqueData )




		
