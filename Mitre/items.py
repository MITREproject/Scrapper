# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MitreItem(scrapy.Item):
    #item which has dynamic fields
    #creating dynamic pipeline
    def __setitem__(self, key, value):
        self._values[key] = value
        self.fields[key] = {}
