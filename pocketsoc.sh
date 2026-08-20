#!/bin/bash
while true
do
clear
echo "================================="
echo "  POCKET SOC MOBILE LAB OS v2.2  "
echo "  Auto-Block + Dashboard Edition "
echo "================================="
echo ""
echo "1) Start Dashboard"
echo "2) Start Termux Agent - Auto Block"
echo "3) View Alerts"
echo "4) View Blocked IPs"
echo "5) Manual IP Scanner"
echo "6) Manual Port Scanner"
echo "7) Clear Alerts Log"
echo "8) Stop All"
echo "9) Exit"
echo ""

read -p "Choose option: " choice

case $choice in
    1)
        echo "[*] Starting Dashboard on http://localhost:8080"
        python dashboard.py
        ;;
    2)
        echo "[*] Starting Auto-Block Agent..."
        python Termux_agent.py
        ;;
    3)
        echo "[*] Recent Alerts:"
        tail -20 alerts.log
        read -p "Press Enter to continue..."
        ;;
    4)
        echo "[*] Blocked IPs:"
        cat blocked_ips.txt
        read -p "Press Enter to continue..."
        ;;
    5)
        echo "[*] Manual IP Scanner"
        read -p "Enter IP or Range: " ip
        python ip_scanner.py $ip
        read -p "Press Enter to continue..."
        ;;
    6)
        echo "[*] Manual Port Scanner"
        read -p "Enter Target IP: " target
        python port_scanner.py $target
        read -p "Press Enter to continue..."
        ;;
    7)
        echo "[*] Clearing alerts.log..."
        > alerts.log
        echo "Cleared!"
        sleep 2
        ;;
    8)
        echo "[*] Stopping all processes..."
        pkill -f "python"
        sleep 2
        ;;
    9)
        exit
        ;;
    *)
        echo "Invalid option"
        sleep 2
        ;;
esac
done
