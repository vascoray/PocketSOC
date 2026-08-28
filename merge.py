import sys, xml.etree.ElementTree as ET, os, glob
from datetime import datetime

# Find latest input
inp = None
for i,a in enumerate(sys.argv):
    if a=="--input": inp=sys.argv[i+1]

if not inp:
    files = glob.glob(os.path.expanduser("~/pocketsoc/results/live_*.xml"))
    inp = max(files, key=os.path.getmtime) if files else None

if not inp or not os.path.exists(inp):
    sys.exit(0)

try:
    tree=ET.parse(inp)
    hosts=tree.findall(".//host")
    ports=len(tree.findall(".//port[state/@state='open']"))
    last=datetime.now().strftime("%H:%M:%S")

    html=f"""<html><head><meta http-equiv="refresh" content="10">
    <style>body{{font-family:monospace;background:#0a0a0a;color:#00ff88;padding:20px}}
    .live{{background:red;color:white;padding:2px 8px;border-radius:4px;animation:blink 1s infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
    </style></head><body>
    <h1>PocketSOC <span class="live">LIVE</span></h1>
    <p>Last Scan: {last} | Hosts: {len(hosts)} | Open Ports: {ports}</p>
    <p>File: {os.path.basename(inp)}</p><hr><pre>
    """
    for h in hosts[:20]:
        ip=h.findtext("address[@addrtype='ipv4']") or "?"
        html+=f"{ip}\n"
        for p in h.findall(".//port[state/@state='open']"):
            html+=f"  - {p.get('portid')}/{p.get('protocol')} {p.findtext('service/@name','')}\n"
    html+="</pre></body></html>"
    open(os.path.expanduser("~/pocketsoc/index.html"),"w").write(html)
    print(f"[{last}] {len(hosts)} hosts, {ports} open")
except Exception as e:
    print(f"merge err: {e}")
