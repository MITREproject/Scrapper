# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pyes import *

import pymongo

import json   

class MitrePipeline:
    def process_item(self, item, spider):
        return item

# class MitrePipeline:
# 	def __init__(self):
# 		self.conn = pymongo.MongoClient(
# 			'localhost',
# 			27017
# 		)
# 		db = self.conn['mitre_project']
# 		self.collection = db['tactics']

# 	def process_item(self, item, spider):
# 		self.collection.insert(dict(item))
# 		return item

# class ElasticSearchPipeline:	
# 	def process_item(self, item, spider):
# 		conn = ES('localhost:9200')
# 		data = {
# 			"name" : "Prajakta",
# 			"roll" : 31
# 		}  
# 		conn.create_index("mitre_project")
# 		conn.put_mapping("tactics", {'properties':item}, ["mitre_project"])
# 		conn.index(item, "mitre_project", "tactics", 1)
# 		return item

