import sys
import json
from urllib.parse import urlparse
import requests

url = "https://zozor54-whois-lookup-v1.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "zozor54-whois-lookup-v1.p.rapidapi.com",
    'x-rapidapi-key': "9f1a548bd3msh9d854107242355ap1736efjsne3e7110bee95"
    }

with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' :
            if e['response']['status'] == 302:
                if 'id' in str(e['response']) or 'id' in str(e['request']):
                    print()
                    req_dom = urlparse(e['request']['url']).netloc
                    res_dom = urlparse(e['response']['redirectURL']).netloc
        
                    print("Request domain :\t",req_dom)
                    print("Redirect domain :\t",res_dom)
                    
                
    
