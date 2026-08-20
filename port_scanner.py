import socket
import sys

target = sys.argv[1]
print(f"[*] Scanning {target} for open ports...")
print("")

# Most common ports hackers hit
ports = [21,22,23,25,53,80,443,445,8080,3389,5900]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} OPEN")
    s.close()
    
print("")
print("[*] Scan Complete")
