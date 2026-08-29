#!/data/data/com.termux/files/usr/bin/bash
clear
echo "POCKET SOC v3.2 OFFLINE | KING VASCO - GHANA"
echo "============================================="
echo "1. Start OFFLINE SOC Engine"
echo "2. Stop OFFLINE SOC Engine"
echo "3. View Blocked IPs REAL"
echo "4. View Evidence Files REAL"
echo "5. Port Scanner Offline"
echo "6. Packet Sniffer"
echo "7. Dashboard Stats localhost:8000"
echo "8. Clear Logs"
echo "9. GeoIP World Map"
echo "10. RE Analyze Binary [r2] entry0"
echo "11. Exit"
echo "============================================="
read -p "Select option: " c
case $c in
 1) python3 ~/pocketsoc/src/offline_soc.py ;;
 2) pkill -f offline_soc; pkill -f "tail -F"; echo "[STOPPED] Engine killed"; sleep 1; bash ~/pocketsoc/pocketsoc.sh ;;
 3) echo "--- Blocked IPs REAL ---"; cat ~/pocketsoc/logs/blocked_ips.log 2>/dev/null || echo "No blocks yet"; echo ""; read -p "Press ENTER..."; bash ~/pocketsoc/pocketsoc.sh ;;
 4) echo "--- Evidence Files REAL ---"; ls -lh ~/pocketsoc/evidence/ 2>/dev/null || echo "No evidence yet"; echo ""; read -p "Press ENTER..."; bash ~/pocketsoc/pocketsoc.sh ;;
 5) python3 ~/pocketsoc/src/port_scanner.py; bash ~/pocketsoc/pocketsoc.sh ;;
 6) python3 ~/pocketsoc/src/packet_sniffer.py; bash ~/pocketsoc/pocketsoc.sh ;;
 7) echo "Opening Dashboard 8000... http://localhost:8000"; python3 ~/pocketsoc/src/dashboard.py ;;
 8) > ~/pocketsoc/logs/auth.log; > ~/pocketsoc/logs/blocked_ips.log; rm -rf ~/pocketsoc/evidence/*; echo "[CLEARED] All logs & evidence cleared"; sleep 1; bash ~/pocketsoc/pocketsoc.sh ;;
 9) python3 ~/pocketsoc/src/geoip.py; bash ~/pocketsoc/pocketsoc.sh ;;
 10) python3 ~/pocketsoc/src/re_analyze.py; bash ~/pocketsoc/pocketsoc.sh ;;
 11) exit 0 ;;
 *) echo "Invalid"; sleep 1; bash ~/pocketsoc/pocketsoc.sh ;;
esac
