# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tactic_name=scrapy.Field()
    count=scrapy.Field()
    technique_with_sub=scrapy.Field()
    technique_with_sub_id=scrapy.Field()
    technique_sub=scrapy.Field()
    technique_sub_id=scrapy.Field()
    technique_without_sub=scrapy.Field()
    technique_without_sub_id=scrapy.Field()
    tech_sub_count=scrapy.Field()
    
   # sub=scrapy.Field()

# class Scrapped(scrapy.Item):
    


