import sys
import json
from urllib.parse import urlparse

domains = set()
urls = {}
with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' and e['_resourceType'] == 'image':
            if e['response']['status'] == 200 and e['response']['content']['size'] < 1000:
                    req_dom = urlparse(e['request']['url']).netloc
                    if req_dom not in domains:
                        domains.add(req_dom)
                        urls[req_dom] = []
                    urls[req_dom].append(e['request']['url'])

                    
data = []  
for s in domains:
    data.append({"domain:":s, "urls":urls[s]})

json_object = json.dumps(data, indent = 4)

with open(sys.argv[2], "w+") as outfile:
    outfile.write(json_object)
