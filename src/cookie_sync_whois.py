import whois
import json

def cookie_sync_whois(infile, outfile, mapping = {}):
    data = json.load(open(infile,))

    store = []

    for obj in data:
        dict = {}
        if "co.in" in obj['request_domain']:
            dict['request_domain'] = '.'.join(obj['request_domain'].split('.')[-3:])
        else:
            dict['request_domain'] = '.'.join(obj['request_domain'].split('.')[-2:])
        if "co.in" in obj['redirect_domain']:
            dict['redirect_domain'] = '.'.join(obj['redirect_domain'].split('.')[-3:])
        else:
            dict['redirect_domain'] = '.'.join(obj['redirect_domain'].split('.')[-2:])
        
        
        # print(f"request domain: {dict['request_domain']}")
        if dict['request_domain'] in mapping.keys():
            dict['request_whois'] = mapping[dict['request_domain']]
            print(f"whois request: {mapping[dict['request_domain']]}")
        else:
            w_request = whois.whois(dict['request_domain'])
            dict['request_whois'] = w_request.org
            print(f"whois request: {w_request.org}")
            mapping[dict['request_domain']] = w_request.org
        # print(f"redirect domain: {dict['redirect_domain']}")

        if dict['redirect_domain'] in mapping.keys():
            dict['redirect_whois'] = mapping[dict['redirect_domain']]
            print(f"whois redirect: {mapping[dict['redirect_domain']]}")
        else:
            w_redirect = whois.whois(dict['redirect_domain'])
            dict['redirect_whois'] = w_redirect.org
            print(f"whois redirect: {w_redirect.org}")
            mapping[dict['redirect_domain']] = w_redirect.org

        print()
        store.append(dict)

    print(mapping)

    with open(outfile, 'w') as outfile:
        json.dump(store, outfile, indent=4)

if __name__ == "__main__":
    news = "zeenews.india.com"
    cookie_sync_whois(f'processed\{news}\cookie_sync.json', f'processed_whois\{news}\cookie_sync_whois.json')