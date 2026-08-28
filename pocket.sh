#!/bin/bash
mkdir -p ~/pocketsoc/results
SUBNET=$(ip route | grep -o "192.168.[0-9]*.[0-9]*/[0-9]*" | head -1)
SUBNET=${SUBNET:-192.168.1.0/24}

# Cleanup old live files - keep last 10
ls -t ~/pocketsoc/results/live_*.xml 2>/dev/null | tail -n +10 | xargs rm -f 2>/dev/null

while true; do
  TS=$(date +%H-%M-%S)
  OUT=~/pocketsoc/results/live_${TS}.xml
  
  nmap -sV --open $SUBNET -oX $OUT --host-timeout 30s -T4
  
  [ -f ~/pocketsoc/merge.py ] && python3 ~/pocketsoc/merge.py --input "$OUT"
  
  sleep 60
done
