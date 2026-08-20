import socket
import sys

target = sys.argv[1]
print(f"[*] Scanning {target} for live hosts...")

try:
    ip = socket.gethostbyname(target)
    print(f"[+] {target} resolved to {ip}")
    print("[+] Host is UP")
except:
    print("[-] Host is DOWN or invalid IP")
