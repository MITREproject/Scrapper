import scrapy
import re
import string 
from ..items import MitreItem

class MetricsSpider(scrapy.Spider):
	name = 'metrics'  #name of the spider
	start_urls = [
		#'https://attack.mitre.org/techniques/T1595/'  #url which we want to scrap
		'https://attack.mitre.org'
	]

	def parse(self, response):
		url = response.css('table.techniques-table a::attr(href)').extract()
		for item in url:
			yield response.follow(item, callback = self.parse_dir_contents)

	def parse_dir_contents(self, response):

		cardValues = response.xpath("//div[@class = 'card-data']/text()").extract() #holds values of card details
		cardKeys = response.xpath("//span[@class = 'h5 card-title']/text()").extract() #holds keys of card details
		subTechnique = response.xpath("//div[@class = 'card-data']//a/text()").extract() #holds sub-technique id's and CAPEC id's
		techniqueName = response.css('h1::text').extract() #holds technique names
		capec = [] #seperate CAPEC id's from sub_technique
		TechniqueData = {} #to be used as dynamic item
		idx = 0 #position of tag 'CAPEC ID' in key

		detection = response.xpath("//div[@class = 'container-fluid']/div/p/text()").extract() 
		description = response.xpath("//div[@class = 'description-body']/p/a/text()" + "|" 
			+ "//div[@class = 'description-body']/p/text()").extract()	
		description = "".join(description)
		detection = "".join(detection)
		Mitigations = {}
		ProcedureExamples = {}		    

		tables = response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']")

		for i in range(len(tables)):
			type = tables[i].xpath('thead/tr/th/text()').extract_first()
			for row in tables[i].xpath('tbody/tr'):
				keys = row.xpath('td/a/text()')[0].extract()
				values = row.xpath("td/p/text()" + "|" + "td/p/a/text()").extract()
				values = "".join(values)
				if type == "Name":
					ProcedureExamples[keys.strip()] = values
				elif type == "Mitigation":
					Mitigations[keys.strip()] = values

		TechniqueData['Detection'] = detection
		TechniqueData['Description'] = description
		if Mitigations:
			TechniqueData['Mitigations'] = Mitigations
		if ProcedureExamples:
			TechniqueData['Procedure Examples'] = ProcedureExamples
			if not Mitigations:
				TechniqueData['Mitigations']=response.xpath("//div[@class = 'container-fluid']/p[not(@scite-citeref-number)]/text()").extract()

		#remove leading and trailing spaces from technique name and remove unwanted symbols
		techniqueName = "".join(techniqueName).strip().replace("\n", "")

		#initializing technique name
		TechniqueData['TechniqueName'] = techniqueName

		#formatting the keys. Removing trailing spaces and colon
		for i in range(len(cardKeys)):
			cardKeys[i] = cardKeys[i].strip()
			cardKeys[i] = cardKeys[i][:-1]
			if cardKeys[i] == 'CAPEC ID':
				idx = i

		#formatting the values.Removing unwanted elements
		for i in range(len(cardValues)):
			cardValues[i] = cardValues[i].strip()
			if "\n" in cardValues[i]:
				cardValues.remove(cardValues[i])

		#eliminating blank elements in values
		for elem in cardValues[:]:
			if len(elem) <= 1:
				cardValues.remove(elem)

		#seperating CAPEC id's from sub-technique id's
		for elem in subTechnique[:]:
			if "CAPEC" in elem:
				capec.append(elem)
				subTechnique.remove(elem)

		#initializing sub-technique id's
		if len(subTechnique) == 1:
			cardValues.insert(1, subTechnique[0])
		if len(subTechnique) > 1:
			cardValues.insert(1, subTechnique)

		#initializing capec id's
		if len(capec) == 1:
			cardValues.insert(idx, capec[0])
		if idx != 0 and len(capec) > 1: 
			cardValues.insert(idx, capec) 

		#initializing other attributes
		for i in range(len(cardKeys)):
			cardKeys[i]=''.join(e for e in cardKeys[i] if e.isalnum())
			TechniqueData[cardKeys[i]] = cardValues[i] 

		#returning the created dictionary
		yield MitreItem( **TechniqueData )




		