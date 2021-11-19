import whois
import json

def pixel_track_whois(infile, outfile, mapping = {}):
    data = json.load(open(infile,))
    store = []

    for obj in data:
        dict = {}
        if "co.in" in obj['domain']:
            dict['domain'] = '.'.join(obj['domain'].split('.')[-3:]) 
        else:
            dict['domain'] = '.'.join(obj['domain'].split('.')[-2:]) 
        # print(f"domain: {dict['domain']}")
        if dict['domain'] in mapping.keys():
            print(f"whois: {mapping[dict['domain']]}")
            dict['whois'] = mapping[dict['domain']]
        else:
            w = whois.whois(dict['domain'])
            print(f"whois: {w.org}")
            dict['whois'] = w.org
            mapping[dict['domain']] = w.org
        print()
        store.append(dict)

    print(mapping)

    with open(outfile, 'w') as outfile:
        json.dump(store, outfile, indent=4)


if __name__ == "__main__":
    news = "timesofindia.indiatimes.com"
    pixel_track_whois(f'processed\{news}\pixel_track.json', f'processed_whois\{news}\pixel_track_whois.json')
