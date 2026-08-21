#!/bin/bash
clear
echo "=========================================="
echo " POCKET SOC v3.0 100% OFFLINE MODE"
echo " Built in Ghana GH - King Vasco"
echo "=========================================="
echo " 1. Start OFFLINE SOC Engine"
echo " 2. Stop OFFLINE SOC Engine"
echo " 3. View Blocked IPs REAL"
echo " 4. View Evidence Files REAL"
echo " 5. Port Scanner Offline"
echo " 6. Dashboard Stats localhost:8080"
echo " 7. View Blocked IPs"
echo " 8. Clear Logs"
echo " 9. GeoIP World Map"
echo " 10. Exit"
echo "=========================================="
echo -n "Select option: "
read opt
case $opt in
 1) python3 offline_soc.py ;;
 2) pkill -f offline_soc.py; echo "Stopped" ;;
 3) cat logs/blocked_ips.log ;;
 4) ls -lh evidence/; cat evidence/* 2>/dev/null | tail -20 ;;
 5) echo -n "IP to scan: "; read ip; for p in 22 80 443 8080; do (echo >/dev/tcp/$ip/$p) 2>/dev/null && echo "Port $p OPEN" || echo "Port $p closed"; done ;;
 6) cd ~/pocketsoc; python3 -m http.server 8080 ;;
 7) cat logs/blocked_ips.log ;;
 8) rm logs/*.log evidence/*.log; echo "Cleared" ;;
 9) echo "=== GEOIP MAP OFFLINE ==="; cat logs/blocked_ips.log; echo ""; echo "Attacker 10.10.14.5 = Lab IP (TryHackMe)"; echo "For real world IP, add offline DB later"; echo "Map: https://github.com/vincentscode/geoip - works offline";;
 10) exit ;;
 *) echo "Invalid" ;;
esac
