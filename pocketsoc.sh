#!/data/data/com.termux/files/usr/bin/bash
clear

echo "=============================================="
echo "POCKET SOC MOBILE v2.2b 👑 DEMO MODE"
echo "Built in Ghana GH"
echo "King Vasco"
echo "=============================================="
echo "1) Start Demo NIDS"
echo "2) Stop Demo NIDS" 
echo "3) View Live Alerts"
echo "4) Threat Intel + Geo"
echo "5) Port Scanner"
echo "6) Dashboard Stats"
echo "7) View Blocked IPs"
echo "8) Clear Logs"
echo "9) GeoIP World Map - See attacker locations"
echo "10) Exit"
echo "=============================================="

read -p "Select option: " opt

case $opt in
1)
    echo "[+] Starting Demo NIDS..."
    pkill -f "demo_sniffer.py"
    python3 ~/pocketsoc/demo_sniffer.py &
    echo "NIDS running in DEMO MODE. Check dashboard at localhost:8080"
    ;;
2)
    echo "[+] Stopping Demo NIDS..."
    pkill -f "demo_sniffer.py"
    ;;
3)
    echo "[+] Live Alerts:"
    tail -f ~/pocketsoc/alerts.log
    ;;
4)
    echo "[+] Threat Intel + Geo Lookup"
    pkg install jq -y
    read -p "Enter IP to investigate: " ip
    curl -s http://ip-api.com/json/$ip | jq .
    ;;
5)
    echo "[+] Port Scanner"
    pkg install nmap -y
    read -p "Enter target IP: " target
    nmap -sV $target
    ;;
6)
    echo "[+] Starting Dashboard v2.2..."
    echo "Open browser to: http://localhost:8080"
    python3 ~/pocketsoc/dashboard.py
    ;;
7)
    echo "[+] Blocked IPs:"
    cat ~/pocketsoc/blocked_ips.log 2>/dev/null || echo "No IPs blocked yet"
    ;;
8)
    echo "[+] Clearing logs..."
    > ~/pocketsoc/alerts.log
    > ~/pocketsoc/blocked_ips.log
    > ~/pocketsoc/geo_hits.log
    echo "Logs cleared"
    ;;
9)
    echo "[+] Scanning alerts for GeoIP data..."
    python3 ~/pocketsoc/geoip_lookup.py
    ;;
10)
    echo "Exiting PocketSOC. Stay secure king."
    exit
    ;;
*)
    echo "Invalid option"
    ;;
esac
