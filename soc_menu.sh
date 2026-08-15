#!/bin/bash
while true; do
clear
echo "=== POCKET SOC v1.6.1 MENU ==="
echo "Built in Ghana 🇬🇭"
echo ""
echo "1) Start Suricata NIDS"
echo "2) Stop Suricata"
echo "3) View Live Alerts"
echo "4) Start Web Dashboard"
echo "5) Exit"
echo ""
read -p "Select option: " choice

case $choice in
 1)
    echo "Starting Suricata..."
    suricata -c ~/PocketSOC/suricata/suricata.yaml -i any
    ;;
 2)
    pkill suricata
    echo "Suricata stopped"
    sleep 2
    ;;
 3)
    tail -f ~/PocketSOC/suricata/log/fast.log
    ;;
 4)
    echo "Starting Dashboard at http://localhost:8000"
    cd ~/PocketSOC && python dashboard.py
    ;;
 5)
    exit
    ;;
 *)
    echo "Invalid option"
    sleep 1
    ;;
esac
done
