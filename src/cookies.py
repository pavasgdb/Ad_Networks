import sys
import json
from urllib.parse import urlparse
from requests import request

url = "https://api.domaintools.com/v1/domaintools.com"

domains = set()
with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' and len(e['request']['cookies']) > 0:
                req_dom = urlparse(e['request']['url']).netloc
                domains.add(req_dom)

data_out = []              
for s in domains:
    data_out.append({"domain":s})  

json_object = json.dumps(data_out, indent = 4)

with open(sys.argv[2], "w+") as outfile:
    outfile.write(json_object)
