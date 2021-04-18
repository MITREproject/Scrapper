import requests
import json
from elasticsearch import Elasticsearch
es = Elasticsearch()
es.indices.create(index='mitre123', ignore=400)

url = 'http://localhost:9200/mitre123/_settings'
body = {"index.mapping.total_fields.limit": 2000}
headers = {'content-type': 'application/json'}

r = requests.put(url, data=json.dumps(body), headers=headers)
print(r)
