# Scrapy settings for mitre project

BOT_NAME = 'mitre'

SPIDER_MODULES = ['mitre.spiders']
NEWSPIDER_MODULE = 'mitre.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   #'mitre.pipelines.MitrePipeline': 800,
   'mitre.pipelines.JsonWriterPipeline': 300,
    #'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 300
}

# ELASTICSEARCH_SERVER = 'localhost' 
# ELASTICSEARCH_PORT = 9200 
# ELASTICSEARCH_INDEX = 'mitre'
# ELASTICSEARCH_TYPE = 'tactics'
#ELASTICSEARCH_UNIQ_KEY = 'ID'
#SCRAPYES_ENABLED = True
