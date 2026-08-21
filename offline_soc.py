import subprocess, time, os
from collections import defaultdict

LOG="/data/data/com.termux/files/home/pocketsoc/logs/auth.log"
EVD="/data/data/com.termux/files/home/pocketsoc/evidence"
os.makedirs(EVD, exist_ok=True)
open(LOG,'a').close()

print("POCKET SOC v3.0 ANDROID - OFFLINE MODE")
print(f"Watching {LOG}")
print("No internet needed. All features local.")

hits=defaultdict(list)
p=subprocess.Popen(['tail','-F',LOG],stdout=subprocess.PIPE,text=True)

for line in p.stdout:
 if "from" not in line: continue
 try: ip=line.split()[line.split().index("from")+1]
 except: continue
 hits[ip].append(time.time())
 hits[ip]=[t for t in hits[ip] if time.time()-t<60]
 if len(hits[ip])>=3:
  ts=time.strftime("%Y-%m-%d_%H-%M-%S")
  open(f"{EVD}/{ts}_{ip}.log","w").write(line)
  # Android: no iptables without root, so we log block
  open(os.path.expanduser("~/pocketsoc/logs/blocked_ips.log"),"a").write(f"{ts} {ip} BLOCKED\n")
  subprocess.run(['termux-vibrate','-d','500'])
  print(f"[OFFLINE BLOCK] {ip} - Evidence saved - {ts}")
