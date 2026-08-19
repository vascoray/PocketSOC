import requests
import time
import subprocess
import json
import os
import re
from datetime import datetime

DASHBOARD_URL = "http://localhost:8080/api/logs"
BLOCKED_IPS = set()

def block_ip(ip):
    if ip not in BLOCKED_IPS:
        print(f"[BLOCKING] {ip}")
        # Requires root. Termux: pkg install tsu
        os.system(f"iptables -A INPUT -s {ip} -j DROP 2>/dev/null")
        BLOCKED_IPS.add(ip)
        return True
    return False

def check_auth_log():
    try:
        cmd = "tail -n 30 /data/data/com.termux/files/usr/var/log/auth.log"
        output = subprocess.getoutput(cmd)
        if "Failed password" in output:
            # Extract IP from "from 192.168.1.99 port"
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', output)
            if match:
                ip = match.group(1)
                was_blocked = block_ip(ip)
                status = "BLOCKED" if was_blocked else "ALREADY BLOCKED"
                return {
                    "severity": "High", 
                    "event": f"SSH Brute Force - {ip} {status}", 
                    "mitre": "T1110", 
                    "ip": ip
                }
    except Exception as e:
        print(f"[ERROR] {e}")
    return None

print("[POCKET.SOC AGENT v1.8] Starting... Auto-block ENABLED")
while True:
    alert = check_auth_log()
    if alert:
        alert["time"] = str(datetime.now())
        alert["source"] = "PHONE SENSOR"
        try:
            requests.post(DASHBOARD_URL, json=alert)
            print(f"[ALERT SENT] {alert['event']}")
        except:
            print("[WAITING] Dashboard not running")
    time.sleep(10)
