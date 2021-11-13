import sys
import json
from urllib.parse import urlparse

domains = set()
with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' and len(e['request']['cookies']) > 0:
                req_dom = urlparse(e['request']['url']).netloc
                domains.add(req_dom)
                
for s in domains:
    print(s)  
