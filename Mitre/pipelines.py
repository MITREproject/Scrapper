# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class MitrePipeline(object):
    def __init__(self):
	    self.conn = pymongo.MongoClient(
			'localhost',
			27017
		)
	    db = self.conn['mitre']
	    self.collection = db['tech_desc']

    def process_item(self, item, spider):
	    self.collection.insert(dict(item))
	    return item
