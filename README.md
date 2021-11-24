# Ad_Networks

A parser to extract information about a website regarding its cookies involved, pixel tracking, cookie synchronization, code fingerprinting

# Execution
### Module 1 - Extracting relevant domains
Add the input data in the following structure

Input Directory -> website(folder) -> website files(website.har, website.har)

(example input -> input/ndtv.com -> input/ndtv.com/ndtv.com.har, input/ndtv.com/ndtv.com.html)

Now execute the command 
```
./run.sh ndtv.com
```

### Module 3 - Extracting companies ownership (whois)

Input Directory -> processed -> website (folder) -> jsons (cookies.json, cookie_sync.json, pixel_track.json)

Output -> processed_whois -> website (folder) -> jsons (cookies_whois.json, cookie_sync_whois.json, pixel_track_whois.json)

Excution
```
python script.py ndtv.com
```
