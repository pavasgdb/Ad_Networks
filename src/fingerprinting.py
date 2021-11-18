import sys
import json

tags = [ 'HTMLCanvasElement','CanvasRenderingContext2D','RTCPeerConnection','createDataChannel',
'createOffer','AudioContext','OscillatorNode']
found = [False]*len(tags)
name = sys.argv[1][:-5]

import os
for f in os.listdir(name+"_files"):
    if f.endswith(".txt") or f.endswith(".html") or f.endswith(".json") or f.endswith(".download"):
        f = os.path.join(name+"_files", f)
        f1 = open(f, "r", encoding='utf-8')
        try:
            s = f1.read()
            for i in range(len(tags)):
                if tags[i] in s:
                    found[i]=True
        except:
            pass

data = []
for i in range(len(tags)):
    if found[i]:
        data.append(tags[i])

json_object = json.dumps({"tags_found":data}, indent = 4)

with open(sys.argv[2], "w+") as outfile:
    outfile.write(json_object)