import sys
import json
from urllib.parse import urlparse
import requests

data_out = []

with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' :
            if e['response']['status'] == 302:
                if 'id' in str(e['response']) or 'id' in str(e['request']):
                    req_dom = urlparse(e['request']['url']).netloc
                    res_dom = urlparse(e['response']['redirectURL']).netloc

                    data_out.append({
                        "request_domain": req_dom,
                        "redirect_domain": res_dom,
                        "request_url":e['request']['url'],
                        "redirect_url":e['response']['redirectURL']
                    })
                    

json_object = json.dumps(data_out, indent = 4)

with open(sys.argv[2], "w+") as outfile:
    outfile.write(json_object)
                
    
