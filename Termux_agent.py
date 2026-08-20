import time
import subprocess
import os
import ipaddress
from datetime import datetime

LOG_FILE = "alerts.log"
CHECK_INTERVAL = 30

def is_local_ip(ip):
    """Block only external IPs. Never block local/private IPs"""
    try:
        ip_obj = ipaddress.ip_address(ip)
        # 192.168.x.x, 10.x, 172.16-31.x, 127.0.0.1 are all local
        return ip_obj.is_private or ip_obj.is_loopback
    except:
        return True # if bad IP, skip it

def block_ip(ip, reason):
    if is_local_ip(ip):
        print(f"[SKIPPED] {ip} is LOCAL NETWORK - SAFE")
        return
    
    print(f"[BLOCKING EXTERNAL] {ip} - {reason}")
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    with open("blocked_ips.txt", "a") as f:
        f.write(f"{datetime.now()} | {ip} | {reason}\n")

def run_scan():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        for line in lines[-10:]:
            if "THREAT_INTEL" in line or "HIGH" in line:
                parts = line.split("|")
                if len(parts) > 2:
                    ip = parts[2].strip()
                    reason = parts[1].strip()
                    block_ip(ip, reason)

print("[POCKET.SOC AGENT v2.1] Starting... LOCAL IPs AUTO-SKIPPED")
while True:
    run_scan()
    time.sleep(CHECK_INTERVAL)






















