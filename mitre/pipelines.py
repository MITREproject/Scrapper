# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter   
#from pyes import ES
import json
import os

# class MitrePipeline:

# 	# def __init__(self):
# 	# 	self.es = ES(['localhost:9200'])

# 	def process_item(self, item, spider):
# 		# json_object = json.dumps(ItemAdapter(item).asdict(), indent = 4)  
# 		# self.es.index(json.loads(json_object), index = 'mitre123', doc_type = 'tactics123', op_type = 'create')
# 		#self.es.put_file('xxxy.json', "mitre123", "tactics123")
		
# 		return item

#Elasticsearch helpers.bulk() ERROR: ('288 document(s) failed to index.', [{'index': {'_index': 'mitre123', '_type': 'tactics123', '_id': '7wVr4HgBTmgpyY4Hja23', 'status': 400, 'error': {'type': 'illegal_argument_exception', 'reason': 'Limit of total fields [1000] in index [mitre123] has been exceeded'}

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('MitreData.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item


# class MitrePipeline:
# 	def __init__(self):
# 		self.conn = pymongo.MongoClient(
# 			'localhost',
# 			27017
# 		)
# 		db = self.conn['mitre123']
# 		self.collection = db['tactics123']

# 	def process_item(self, item, spider):
# 		self.collection.insert(dict(item))
# 		return item