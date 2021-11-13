import sys
import json

with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' and e['_resourceType'] == 'image':
            if e['response']['status'] == 200 and e['response']['content']['size'] < 1000:
                    print(e['request']['url'])
                
    
