# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    id = scrapy.Field()
    sub_technique = scrapy.Field()
    tactic = scrapy.Field()
    platform = scrapy.Field()
    technique_name = scrapy.Field()
    data_sources = scrapy.Field()
    version = scrapy.Field()
    created = scrapy.Field()
    last_modified = scrapy.Field()
#     tactic_name=scrapy.Field()
#     count=scrapy.Field()
#     technique_with_sub=scrapy.Field()
#    # technique_with_sub_id=scrapy.Field()
#     technique_sub=scrapy.Field()
#    # technique_sub_id=scrapy.Field()
#     technique_without_sub=scrapy.Field()
#     technique_without_sub_id=scrapy.Field()
#     tech_sub_count=scrapy.Field()
   # sub=scrapy.Field()

class ScrapItem(scrapy.Item):
     
    
    id = scrapy.Field()
    sub_technique = scrapy.Field()
    sub_technique_id=scrapy.Field()
    tactic = scrapy.Field()
    technique_name = scrapy.Field()
