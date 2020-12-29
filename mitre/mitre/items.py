# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# triual fchnrejugjvmrfdijdiugh

import scrapy


class MitreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #tactic_name = scrapy.Field()
    id = scrapy.Field()
    sub_technique = scrapy.Field()
    tactic = scrapy.Field()
    platform = scrapy.Field()
    technique_name = scrapy.Field()
    data_sources = scrapy.Field()
    version = scrapy.Field()
    created = scrapy.Field()
    last_modified = scrapy.Field()


