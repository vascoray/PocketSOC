import sys, datetime, os, re
from collections import defaultdict

os.makedirs(os.path.expanduser("~/pocketsoc"), exist_ok=True)
ips = defaultdict(int)
ip_regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

print("Sniffer started. Waiting for packets...")
for line in sys.stdin:
    found_ips = ip_regex.findall(line)
    for ip in found_ips:
        if ip!= "127.0.0.1":
            ips[ip] += 1
            if ips[ip] == 4:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg = f"{timestamp} - High - SSH/HTTP Brute Force from {ip} - BLOCKED\n"
                with open(os.path.expanduser("~/pocketsoc/alerts.log"), "a") as f:
                    f.write(msg)
                with open(os.path.expanduser("~/pocketsoc/blocked_ips.log"), "a") as f:
                    f.write(f"{ip}\n")
                print(f"[ALERT] {ip} BLOCKED")
