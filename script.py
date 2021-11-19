from src.cookie_sync_whois import *
from src.cookies_whois import *
from src.pixel_track_whois import *
import json
import os

import os

news = "economictimes.indiatimes.com"
indir = os.path.join("processed", news)
outdir = os.path.join("processed_whois", news)

mapping = {'adsrvr.org': 'The Trade Desk', 'smartadserver.com': 'Smartadserver','yahoo.com': 'Verizon Media Inc.',
'google-analytics.com': 'Google LLC', 'scorecardresearch.com': 'TMRG, Inc','imrworldwide.com': 'The Nielsen Company',
'spotxchange.com': 'SpotX, Inc','taboola.com':'Taboola', 'mfadsrvr.com': 'Media Force Ltd.', 'turn.com': 'PERFECT PRIVACY, LLC',
'inmobi.com':'InMobi Pte Ltd','adswizz.com': 'Adswizz Inc.','bidswitch.net':'Domains By Proxy, LLC', 'creativecdn.com': 'RTB House S.A.',
'linkedin.com': 'LinkedIn Corporation', 'facebook.com': 'Facebook, Inc.','adtelligent.com': 'Vertamedia,LLC', 'clarity.ms': 'Microsoft Corporation',
'tribalfusion.com': 'Exponential', 'crwdcntrl.net': 'Lotame Solutions Inc.', 'advertising.com': 'Verizon Media Inc.', 'izooto.com':'iZooto',
'outbrain.com': 'Outbrain',}
mapping["audrte.com"] = "AudienceRate Ltd"
mapping["pubmatic.com"] = "PubMatic, Inc."
mapping["rubiconproject.com"] = "The Rubicon Project, Inc."
mapping["tappx.com"] = "Tappcelerator Media, S.L."
mapping["eyeota.net"] = "Eyeota Pte Ltd"
mapping["doubleclick.net"] = "Google Inc."
mapping["google.com"] = "Google LLC"
mapping["google.co.in"] = "Google LLC"
mapping["amazon-adsystem.com"] = "Amazon Technologies, Inc."
mapping["adnxs.com"] = "AppNexus Inc"
mapping["admanmedia.com"] = "PERFECT PRIVACY, LLC"

if not os.path.exists(outdir):
    os.makedirs(outdir)

print("Processing cookies:")
cookies_whois(os.path.join(indir, 'cookies.json'), os.path.join(outdir, 'cookies_whois.json'), mapping)
print("_____________________________________")

print("Processing cookie sync")
cookie_sync_whois(os.path.join(indir, 'cookie_sync.json'), os.path.join(outdir, 'cookie_sync_whois.json'), mapping)
print("______________________________________")

print("Processing pixel tracking")
pixel_track_whois(os.path.join(indir, 'pixel_track.json'), os.path.join(outdir, 'pixel_track_whois.json'), mapping)
print("______________________________________")