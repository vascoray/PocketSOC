#!/data/data/com.termux/files/usr/bin/bash
while true; do
clear
echo "========================================="
echo "POCKET SOC v3.1 100% OFFLINE MODE"
echo "Built in Ghana GH - King Vasco"
echo "========================================="
echo "1. Start OFFLINE SOC Engine"
echo "2. Stop OFFLINE SOC Engine"
echo "3. View Blocked IPs REAL"
echo "4. View Evidence Files REAL"
echo "5. Port Scanner Offline"
echo "6. Dashboard Stats localhost:8080"
echo "7. View Blocked IPs"
echo "8. Clear Logs"
echo "9. GeoIP World Map"
echo "10. RE Analyze Binary [r2]"
echo "11. Exit"
echo "========================================="
read -p "Select option: " opt
case $opt in
1) echo "[*] Starting..."; read -p "Press enter";;
3) cat blocked_ips.txt 2>/dev/null || echo "No IPs"; read -p "Press enter";;
4) ls -lh evidence/ 2>/dev/null || ls *.log; read -p "Press enter";;
10)
  read -p "Binary path (/bin/ls): " binpath
  binpath=${binpath:-/bin/ls}
  echo "[*] Analyzing $binpath"
  r2 -e bin.relocs.apply=true -AA -q -c 'afl~entry; pdf @ entry0' "$binpath"
  echo ""; echo "[*] Done"; read -p "Press enter"
  ;;
11) exit 0;;
*) echo "Invalid"; sleep 1;;
esac
done
