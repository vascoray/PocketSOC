import socket, sys
print("POCKET SOC v3.2 | KING VASCO - MANUAL IP SCANNER")
print("-" * 45)
ip = input("Enter target IP (e.g. 192.168.1.1 or 8.8.8.8): ").strip()
if not ip:
    ip = "127.0.0.1"
    print(f"No IP entered, scanning {ip}")

ports = [21,22,23,25,53,80,110,135,139,443,445,3306,8080,8000]
open_ports = []

print(f"\n[SCANNING] {ip} -> {len(ports)} ports...\n")

for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.8)
    try:
        res = s.connect_ex((ip, p))
        if res == 0:
            print(f"  [+] Port {p} OPEN")
            open_ports.append(p)
        else:
            print(f"  [-] Port {p} closed")
    except Exception as e:
        print(f"  [?] Port {p} error: {e}")
    s.close()

print("\n" + "="*45)
if open_ports:
    print(f"RESULT: {ip} has {len(open_ports)} open ports: {open_ports}")
    with open(f"{socket.gethostname() if False else ''}", "a") as f: pass
    open(f"{__import__('pathlib').Path.home()}/pocketsoc/logs/blocked_ips.log","a").write(f"SCAN {ip} OPEN {open_ports}\n")
else:
    print(f"RESULT: {ip} - No open ports found (or filtered)")
print("="*45)
input("\nPress ENTER to return to menu...")
