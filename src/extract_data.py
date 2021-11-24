import json
import sys
import os
news = sys.argv[1]

def get_cookies(news):
    infile = os.path.join("processed_whois", news, "cookies_whois.json")
    data = json.load(open(infile,))
    companies_list = []
    for obj in data:
        companies_list.append(obj["whois"])

    final_list = list(set(companies_list))
    index = 1
    for c in final_list:
        if c != ("REDACTED FOR PRIVACY" or "Whois Privacy Service") and c is not None:
            print(f"{index}. {c}")
            index+=1

def get_pixel_track(news):
    infile = os.path.join("processed_whois", news, "pixel_track_whois.json")
    data = json.load(open(infile,))
    companies_list = []
    for obj in data:
        companies_list.append(obj["whois"])

    final_list = list(set(companies_list))
    index = 1
    for c in final_list:
        if c != ("REDACTED FOR PRIVACY" or "Whois Privacy Service") and c is not None:
            print(f"{index}. {c}")
            index+=1

def get_cookie_sync(news):
    infile = os.path.join("processed_whois", news, "cookie_sync_whois.json")
    data = json.load(open(infile,))
    companies_list = []
    for obj in data:
        companies_list.append((obj["request_whois"], obj["redirect_whois"]))

    final_list = list(set(companies_list))
    index = 1
    for c in final_list:
        if (c[0] != ("REDACTED FOR PRIVACY" or "Whois Privacy Service") and c[0] is not None) and \
            (c[1] != ("REDACTED FOR PRIVACY" or "Whois Privacy Service") and c[1] is not None):
            print(f"{index}. {c[0]}, {c[1]}")
            index+=1

def get_fingerprint(news):
    infile = os.path.join("processed", news, "fingerprinting.json")
    data = json.load(open(infile,))

    index = 1
    for tag in data["tags_found"]:
        print(f"{index}. {tag}")
        index+=1

if __name__ == "__main__":
    news = sys.argv[1]
    get_cookies(news)
    print("------------------------")
    get_cookie_sync(news)
    print("------------------------")
    get_pixel_track(news)
    print("------------------------")
    get_fingerprint(news)