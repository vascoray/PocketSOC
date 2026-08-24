#!/data/data/com.termux/files/usr/bin/bash
while true; do
clear
echo "========================================="
echo "POCKET SOC v3.2 100% OFFLINE MODE"
echo "Built in Ghana GH - King Vasco"
echo "Alias: pocketsoc"
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
echo "10. RE Analyze Binary [r2] entry0"
echo "11. Exit"
echo "========================================="
read -p "Select option: " opt
case $opt in
10) read -p "Binary [/bin/ls]: " b; b=${b:-/bin/ls}; r2 -e bin.relocs.apply=true -AA -q -c 'afl~entry; pdf @ entry0' "$b"; read -p "Enter";;
11) exit;;
*) echo "opt $opt"; sleep 1;;
esac
done
