import scrapy
import re
import string 
from ..items import MitreItem

class MetricsSpider(scrapy.Spider):
	name = 'metrics'  #name of the spider
	start_urls = [
		'https://attack.mitre.org/'  #url which we want to scrap
	]

	def parse(self, response):
		url = response.css('table.techniques-table a::attr(href)').extract()
		for item in url:
			yield response.follow(item, callback = self.parse_dir_contents)

	def parse_dir_contents(self, response):

	    other = response.xpath("//div[@class = 'card-data']/text()").extract() #holds values of card details
	    key = response.xpath("//span[@class = 'h5 card-title']/text()").extract() #holds keys of card details
	    sub_technique = response.xpath("//div[@class = 'card-data']//a/text()").extract() #holds sub-technique id's and CAPEC id's
	    technique_name = response.css('h1::text').extract() #holds technique names
	    capec = [] #seperate CAPEC id's from sub_technique
	    dict1 = {} #to be used as dynamic item
	    idx = 0 #position of tag 'CAPEC ID' in key
	    
	    #remove leading and trailing spaces from technique name and remove unwanted symbols
	    technique_name = "".join(technique_name)
	    technique_name = technique_name.strip()
	    technique_name = technique_name.replace("\n", "")

	    #initializing technique name
	    dict1['Technique Name'] = technique_name

	    #formatting the keys. Removing trailing spaces and colon
	    for i in range(len(key)):
	    	key[i] = key[i].strip()
	    	key[i] = key[i][:-1]
	    	if key[i] == 'CAPEC ID':
	    		idx = i

	    #formatting the values.Removing unwanted elements
	    for i in range(len(other)):
	    	other[i] = other[i].strip()
	    	if "\n" in other[i]:
	    		other.remove(other[i])

	    #eliminating blank elements in values
	    for elem in other[:]:
	    	if len(elem) <= 1:
	    		other.remove(elem)
	    
	    #seperating CAPEC id's from sub-technique id's
	    for elem in sub_technique[:]:
	    	if "CAPEC" in elem:
	    		capec.append(elem)
	    		sub_technique.remove(elem)

	    #initializing sub-technique id's
	    if len(sub_technique) == 1:
	    	other.insert(1, sub_technique[0])
	    if len(sub_technique) > 1:
	    	other.insert(1, sub_technique)

	    #initializing capec id's
	    if len(capec) == 1:
	    	other.insert(idx, capec[0])
	    if idx != 0 and len(capec) > 1: 
	    	other.insert(idx, capec) 

	    #initializing other attributes
	    for i in range(len(key)):
	    	dict1[key[i]] = other[i] 

	    #returning the created dictionary
	    yield MitreItem( **dict1 )




		