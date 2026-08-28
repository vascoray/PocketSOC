import time, re, os
from datetime import datetime
print("POCKET SOC v3.0 - AUTO BLOCKER LIVE")
print("Watching auth.log -> blocking -> dashboard\n")
seen=set()
while True:
    if os.path.exists("logs/auth.log"):
        for line in open("logs/auth.log").read().splitlines()[-20:]:
            m=re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if m:
                ip=m.group(1)
                if ip not in seen:
                    seen.add(ip)
                    block=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')} {ip} BLOCKED - LIVE ATTACK"
                    open("logs/blocked_ips.log","a").write(block+"\n")
                    print(f"🚨 BLOCKED {ip} -> {block}")
                    # create evidence
                    open(f"evidence/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{ip}.log","w").write(line)
    time.sleep(2)
