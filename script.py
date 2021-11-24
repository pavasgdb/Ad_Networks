from src.cookie_sync_whois import *
from src.cookies_whois import *
from src.pixel_track_whois import *
import json
import sys
import os

import os

news = sys.argv[1]
indir = os.path.join("processed", news)
outdir = os.path.join("processed_whois", news)

mapping = {
    'adsrvr.org': 'The Trade Desk',
    'smartadserver.com': 'Smartadserver',
    'yahoo.com': 'Verizon Media Inc.',
    'google-analytics.com': 'Google LLC', 
    'scorecardresearch.com': 'TMRG, Inc',
    'imrworldwide.com': 'The Nielsen Company',
    'spotxchange.com': 'SpotX, Inc',
    'taboola.com':'Taboola', 
    'mfadsrvr.com': 'Media Force Ltd.', 
    'turn.com': 'Perfect Privacy, LLC',
    'inmobi.com':'InMobi Pte Ltd',
    'adswizz.com': 'Adswizz Inc.',
    'bidswitch.net':'BidSwitch', 
    'creativecdn.com': 'RTB House S.A.',
    'linkedin.com': 'LinkedIn Corporation', 
    'facebook.com': 'Facebook, Inc.',
    'adtelligent.com': 'Vertamedia,LLC', 
    'clarity.ms': 'Microsoft Corporation',
    'tribalfusion.com': 'Exponential', 
    'crwdcntrl.net': 'Lotame Solutions Inc.', 
    'advertising.com': 'Verizon Media Inc.', 
    'izooto.com':'iZooto',
    'outbrain.com': 'Outbrain',
    'audrte.com': 'AudienceRate Ltd',
    'pubmatic.com': 'PubMatic, Inc.',
    'rubiconproject.com': 'The Rubicon Project, Inc.',
    'tappx.com': 'Tappcelerator Media, S.L.',
    'eyeota.net': 'Eyeota Pte Ltd',
    'doubleclick.net': 'Google LLC',
    'google.com': 'Google LLC',
    'google.co.in': 'Google LLC',
    'amazon-adsystem.com': 'Amazon Technologies, Inc.',
    'adnxs.com': 'AppNexus Inc',
    'admanmedia.com': 'Perfect Privacy, LLC',
    'openx.net': 'OpenX',
    '3lift.com': 'TripleLift',
    'dotomi.com': 'Conversant LLC',
    'tapad.com': 'Tapad, Inc.',
    'sitescout.com': 'Centro Media, Inc',
    'ipredictive.com': 'Adelphic, Inc.',
    'stackadapt.com': 'Collective Roll',
    'amgdgt.com': 'Amobee Inc',
    'id5-sync.com': 'ID5 Technology Ltd',
    'rlcdn.com': 'TowerData',
    'bidr.io': 'Beeswax',
    'sharethrough.com': 'Sharethrough',
    'casalemedia.com': 'Index Exchange Inc.',
    'richaudience.com': 'Rich Audience',
    'zeotap.com': 'Zeotap',
    'adform.net': 'Adform',
    'admixer.net': 'Admixer',
    'e-volution.ai': 'Evolution AI',
    'bluekai.com': 'Oracle Corporation',
    'mathtag.com': 'MediaMath',
    'ladsp.jp': 'F@N Communications',
    'ladsp.com': 'F@N Communications',
    'extend.tv': 'ZypMedia',
    'advertising.com': 'AOL',
    'betweendigital.com': 'Between Digital',
    'unrulymedia.com': 'Unruly Group Ltd',
    '1rx.io': 'RhythmOne',
    'servenobid.com': 'Servenobid',
    '33across.com': '33Across',
    'tynt.com': 'Tynt',
    'quantserve.com': 'Quantcast',
    'adpushup.com': 'AdPushup',
    'bttrack.com': 'Bidtellect',
    'feedify.net': 'Feedify',
    'adrta.com': 'Pixalate',
    'zemanta.com': 'Outbrain',
    'kargo.com': 'Kargo',
    'affinity.com':'Hostway',
    'criteo.com': 'Criteo',
    '360yield.com': 'Advanced Ag Solutions',

    }


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