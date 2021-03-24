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
        dict1={}
        idx=0
        capec=[]
        other=response.xpath("//div[@class = 'card-data']/text()").extract()
        key=response.xpath("//span[@class = 'h5 card-title']/text()").extract()
        sub_technique=response.xpath("//div[@class = 'card-data']//a/text()").extract()
        technique_name = response.css('h1::text').extract()
        processed=[]
        
        detection=response.xpath("//div[@class = 'container-fluid']/div/p/text()").extract()
        description=response.xpath("//div[@class = 'description-body']/p[not(@scite-citeref-number)]/text()").extract()
        count=len(response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']").extract())
        if(count==2):
            # proc_example=scrapy.Request(response.url,callback=self.Process,meta="proc1")
            
            for r in response.xpath("//table[@class = 'table table-bordered table-alternate mt-2'][1]//p[not(@scite-citeref-number)]"):
                process = [p.strip() for p in r.xpath('.//text()').extract() if p.strip()]
                processed.append("".join(process))
            proc_example=processed

            # response.xpath("//table[@class = 'table table-bordered table-alternate mt-2'][1]//a/text()"+"|"+"//table[@class = 'table table-bordered table-alternate mt-2'][1]//p/text()").extract()
            mitigation=response.xpath("//table[@class = 'table table-bordered table-alternate mt-2'][2]//a/text()"+"|"+"//table[@class = 'table table-bordered table-alternate mt-2'][2]//p[not(@scite-citeref-number)]/text()").extract()
            dict1['proc_example']=proc_example
            dict1['Mitigation']=mitigation
        elif(count==1):
            h21=response.xpath("//div[@class = 'container-fluid']/h2/text()").extract_first()
            
            if(h21=="Mitigations"):
                mitigation=response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']//a/text()"+"|"+"//table[@class = 'table table-bordered table-alternate mt-2']//p[not(@scite-citeref-number)]/text()").extract()
                dict1['Mitigation']=mitigation
            elif(h21=="Procedure Examples"):
                processed.clear()
                for r in response.xpath("//table[@class = 'table table-bordered table-alternate mt-2']//p[not(@scite-citeref-number)]"):
                    process = [p.strip() for p in r.xpath('.//text()').extract() if p.strip()]
                    processed.append("".join(process))
                proc_example=processed
                # proc_example=scrapy.Request(response.url,callback=self.Process,meta="proc2")
                # description=response.xpath("//div[@class = 'description-body']/p[not(@scite-citeref-number)]/text()").extract()
                mitigation=response.xpath("//div[@class = 'container-fluid']/p[not(@scite-citeref-number)]/text()").extract()
                dict1['Mitigation']=mitigation
                dict1['proc_example']=proc_example
        technique_name = "".join(technique_name)
        technique_name = technique_name.strip()
        technique_name = technique_name.replace("\n", "")
        
        

        dict1['Technique']=technique_name
        dict1['Description']=description
        dict1['count']=count
        
        dict1['Detection']=detection
        # dict1['Mitigation_Description']=miti_descri
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

        yield MitreItem(**dict1)

    
        

# elasticsearch_loader --index index_name --type type_name json filename.json