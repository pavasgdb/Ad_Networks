import sys
import json

with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)

    for e in data['log']['entries']:
        if e['request']['method'] == 'GET' :
            if e['response']['status'] == 302:
                if 'id' in str(e['response']) or 'id' in str(e['request']):
                    print()
                    print("Request URL :\t",e['request']['url'])
                    print("Response URL :\t",e['response']['redirectURL'])
                    
                
    
