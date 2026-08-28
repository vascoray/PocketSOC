#!/usr/bin/env python3
# POCKET SOC v3.0 - Termux to APK Bridge
# Built in Ghana GH - King Vasco
import http.server, socketserver, threading, os, time, webbrowser

PORT_DASHBOARD = 8080
PORT_ENGINE = 3003

print("="*50)
print("POCKET SOC v3.0 100% OFFLINE MODE")
print("Built in Ghana GH - King Vasco")
print("="*50)

# Start dashboard in background
def start_dashboard():
    os.system(f"python3 live_server.py 2>/dev/null &")
    os.system(f"python3 auto_block.py 2>/dev/null &")

start_dashboard()
time.sleep(2)

# Open in phone browser - this IS your APK view
print(f"\n[+] Dashboard: http://localhost:{PORT_DASHBOARD}")
print(f"[+] SOC Engine: http://localhost:{PORT_ENGINE}")
print("[+] Opening in browser...")

try:
    # Try termux-open
    os.system(f"termux-open http://localhost:{PORT_DASHBOARD}")
    print("[+] Opened in Chrome - Install as APK: Chrome > Menu > Add to Home Screen")
except:
    print("[+] Manual: Open Chrome and go to http://localhost:8080")

# Keep alive
print("\n[+] POCKET SOC RUNNING - Minimize Termux, use Chrome as APP")
print("[+] To make APK: Chrome > 3 dots > Add to Home Screen > PocketSOC")
while True:
    time.sleep(10)
    print(f"[LIVE] SOC Active - {time.strftime('%H:%M:%S')} Accra GH")
