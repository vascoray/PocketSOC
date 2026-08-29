import pathlib
BASE=pathlib.Path.home()/"pocketsoc/logs/blocked_ips.log"
print("POCKET SOC v3.2 | KING VASCO - GeoIP World Map")
print("-"*50)
try:
    data=open(BASE).read().strip().splitlines()
    if not data:
        print("No blocked IPs yet - run 1) Start Engine first")
    else:
        for line in data[-20:]:
            parts=line.split()
            ip=parts[1] if len(parts)>1 else parts[0]
            if ip.startswith("192.168."): loc="Ghana Local 🇬🇭"
            elif ip.startswith("41."): loc="Ghana/Africa"
            elif ip.startswith("8.8."): loc="USA - Google DNS"
            elif ip.startswith("10."): loc="Private Network"
            else: loc="Unknown - Offline DB"
            print(f" {ip} -> {loc}")
except:
    print("No blocked IPs yet - file empty")
input("\nPress ENTER to return...")
