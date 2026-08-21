import time
import datetime
import random
import os

# Fake attacker IPs from different countries
ips = [
    "185.220.101.47",   # Russia
    "45.142.212.61",    # Poland  
    "103.216.156.12",   # China
    "94.130.12.34",     # Germany
    "192.168.1.50",     # Local/Ghana
    "203.0.113.45",     # USA
    "198.51.100.23"     # Brazil
]

countries = [
    "RUSSIA",
    "POLAND", 
    "CHINA",
    "GERMANY",
    "GHANA",
    "USA",
    "BRAZIL"
]

attack_types = [
    "SSH Brute Force",
    "HTTP Scan",
    "Port Scan",
    "SQL Injection Attempt"
]

# Make sure folders exist
os.makedirs(os.path.expanduser("~/pocketsoc"), exist_ok=True)

print("==============================================")
print("Demo NIDS started. Generating fake attacks...")
print("Press CTRL+C to stop")
print("==============================================")

while True:
    ip = random.choice(ips)
    country = random.choice(countries)
    attack = random.choice(attack_types)
    severity = random.choice(["Medium", "High", "Critical"])
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write to alerts.log
    alert_msg = f"{timestamp} - {severity} - {attack} from {ip} - BLOCKED\n"
    with open(os.path.expanduser("~/pocketsoc/alerts.log"), "a") as f:
        f.write(alert_msg)
    
    # Write to blocked_ips.log
    with open(os.path.expanduser("~/pocketsoc/blocked_ips.log"), "a") as f:
        f.write(f"{ip}\n")
    
    # Write to geo_hits.log for world map
    with open(os.path.expanduser("~/pocketsoc/geo_hits.log"), "a") as f:
        f.write(f"{country}\n")
    
    print(f"[ALERT] {severity} - {attack} from {ip} [{country}] BLOCKED")
    time.sleep(4)  # New attack every 4 seconds
