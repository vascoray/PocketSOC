from collections import defaultdict
import os, time, subprocess

LOG=os.path.expanduser("~/pocketsoc/logs/auth.log")
EVD=os.path.expanduser("~/pocketsoc/evidence")
BLK=os.path.expanduser("~/pocketsoc/logs/blocked_ips.log")
LCK=os.path.expanduser("~/pocketsoc/logs/locked_ips.log")

os.makedirs(EVD, exist_ok=True)
os.makedirs(os.path.dirname(LOG), exist_ok=True)

print(f"POCKET SOC v3.2 - OFFLINE - Watching {LOG}")

hits=defaultdict(list)
p=subprocess.Popen(['tail','-F',LOG],stdout=subprocess.PIPE,text=True,bufsize=1)

for line in p.stdout:
    line=line.strip()
    if not line or "from" not in line:
        continue
    try:
        ip=line.split()[line.split().index("from")+1]
    except:
        continue
    now=time.time()
    hits[ip].append(now)
    hits[ip]=[t for t in hits[ip] if now-t < 60]
    if len(hits[ip]) >= 3:
        ts=time.strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"{EVD}/{ts}_{ip}.log","w") as f:
            f.write(line + "\n")
        with open(BLK,"a") as f:
            f.write(f"{ts} {ip} BLOCKED\n")
        with open(LCK,"a") as f:
            f.write(f"{ts} {ip} BLOCKED\n")
        subprocess.run(['termux-vibrate','-d','400'])
        print(f"[OFFLINE BLOCK] {ip} -> {ts}")
        hits[ip]=[]
