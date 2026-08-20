#!/bin/bash
clear
echo "========================================"
echo "  POCKET SOC MOBILE LAB OS v1.8"
echo "  Auto-Block + Dashboard Edition"
echo "========================================"
echo ""
echo "1) Start Dashboard"
echo "2) Start Termux Agent - Auto Block"
echo "3) View Alerts"
echo "4) View Blocked IPs"
echo "5) Stop All"
echo "6) Exit"
echo ""
read -p "Select: " choice

case $choice in
 1) python dashboard.py ;;
 2) python termux_agent.py ;;
 3) cat alerts.json 2>/dev/null || echo "No alerts yet" ;;
  4) iptables -w -L INPUT -n | grep DROP ;;
 5) pkill -f dashboard.py; pkill -f termux_agent.py; echo "Stopped" ;;
 6) exit ;;
  *) echo "Invalid" ;;
esac
