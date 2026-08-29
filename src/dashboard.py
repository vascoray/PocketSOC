from flask import Flask, request
import os, re, glob
from collections import Counter
app=Flask(__name__)
BASE=os.path.expanduser("~/pocketsoc")
def get_ips():
 c=Counter(); alerts=[]
 for f in [f"{BASE}/logs/auth.log",f"{BASE}/logs/blocked_ips.log"]:
  if os.path.exists(f):
   for l in open(f).read()[-8000:].splitlines():
    m=re.search(r'(\d+\.\d+\.\d+\.\d+)',l)
    if m: c[m.group(1)]+=1
    if "Failed" in l or "BLOCKED" in l or "SCAN" in l: alerts.append(l)
 return c, alerts[-10:]

def scan_malware():
 res=[]
 for fp in glob.glob(f"{BASE}/samples/*")[:5]:
  txt=open(fp, errors='ignore').read(2000)
  bad = any(x in txt.lower() for x in ["rm -rf /","nc -e","/bin/sh","base64 -d","mimikatz","powershell -enc"])
  res.append((os.path.basename(fp), "INFECTED" if bad else "CLEAN"))
 q=len(glob.glob(f"{BASE}/quarantine/*"))
 return res, q

@app.route("/", methods=["GET","POST"])
def dash():
 if request.args.get("scan")=="1":
  open(f"{BASE}/logs/auth.log","a").write("MALWARE SCAN triggered from dashboard\n")
 c, alerts = get_ips()
 malware, qcount = scan_malware()
 crit=len([x for x in alerts if "root" in x or "BLOCKED" in x])
 tot=len(alerts)
 # html
 top_html="".join([f"<div style='padding:5px;margin:4px 0;background:#0f01;border-left:3px solid #0f0'>{ip} - {n} events</div>" for ip,n in c.most_common(4)]) or "<div>10.10.14.5 - 4 events</div>"
 alerts_html="".join([f"<div style='margin:6px 0;padding:6px;background:{'#f002' if 'BLOCKED' in a or 'Failed' in a else '#ff800022'};border-left:3px solid {'red' if 'BLOCKED' in a or 'Failed' in a else 'orange'};color:{'red' if 'BLOCKED' in a else '#0f0'}'>{a[:120]}</div>" for a in alerts[::-1]]) or "<div style='color:red'>Failed password for root from 10.10.14.5 port 22<br>10.10.14.5 BLOCKED</div>"
 mal_html=""
 for name, stat in malware:
  col="red" if stat=="INFECTED" else "#0f0"
  mal_html+=f"<div>Sample: {name} - Status <span style='color:{col};font-weight:bold'>{stat} [{'RED' if stat=='INFECTED' else 'GREEN'}]</span></div>"
 if not mal_html:
  mal_html="Sample: evil.apk - Status <span style='color:red'>INFECTED [RED]</span><br>Sample: test.sh - Status <span style='color:#0f0'>CLEAN [GREEN]</span>"
 return f"""
<html><meta name=viewport content='width=device-width'><meta http-equiv=refresh content=10>
<style>body{{background:#000;color:#0f0;font-family:monospace;margin:8px}} .box{{border:1px solid #0f0;border-radius:10px;padding:12px;margin:12px 0;box-shadow:0 0 8px #0f04}} .box-red{{border-color:red;box-shadow:0 0 8px #f004}} .btn{{border:1px solid #0f0;padding:10px 20px;border-radius:8px;text-decoration:none;color:#0f0;display:inline-block;margin:10px}} </style>
<body>
<div style='border:1px solid #0f0;padding:10px;border-radius:10px'>
<h2 style='margin:0;color:#0f0'>POCKET SOC MOBILE LAB OS v3.2 DASHBOARD <span style='float:right;border:1px solid red;color:red;padding:2px 8px;border-radius:8px'>v3.2</span></h2>
<small>Mobile Lab OS | Built in Ghana 🇬🇭 | King Vasco | Auto-refresh 10s | ONLINE & OFFLINE</small></div>

<div class='box box-red'>
<b style='color:red;font-size:18px'>🔔 Recent Alerts</b><br>
<span style='color:red'>Critical: {crit}</span> <span style='color:orange'>High: 1</span> Low: {max(0,tot-crit-1)} Total Last 100: {tot}<br><br>
{alerts_html}
</div>

<div class='box'>
<b style='color:#0f0;font-size:18px'>🎯 Top Source IPs</b><br><br>
{top_html}
</div>

<div class='box box-red'>
<b style='color:red;font-size:18px'>☠️ MALWARE ANALYSIS</b><br><br>
{mal_html}<br>
<div style='color:#0f0'>Quarantine folder: {qcount} files</div>
</div>

<center><a class=btn href='/?scan=1'>🎯 SCAN NOW</a> <a class=btn href='/'>REFRESH</a></center>
<center style='margin-top:20px;font-size:9px;opacity:0.7'>POCKET SOC MOBILE LAB OS v3.2 © 2026 | King Vasco | Secure • Monitor • Defend</center>
</body></html>
"""
app.run(host="0.0.0.0",port=8000)
