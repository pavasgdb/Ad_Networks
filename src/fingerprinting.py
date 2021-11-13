import sys

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


for i in range(len(tags)):
    if found[i]:
        print(tags[i])