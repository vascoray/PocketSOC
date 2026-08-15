#!/bin/bash
if [ -z "$1" ]
then
  echo "Usage: ./dns-recon.sh target.com"
  exit 1
fi

echo "================================="
echo "[*] POCKETSOC DNS RECON: $1"
echo "================================="

echo ""
echo "[+] A Records - IP Addresses:"
dig +short $1 A

echo ""
echo "[+] MX Records - Mail Servers:"
dig +short $1 MX

echo ""
echo "[+] NS Records - Nameservers:"
dig +short $1 NS

echo ""
echo "[+] TXT Records - SPF/DKIM/Verification:"
dig +short $1 TXT

echo ""
echo "[+] WHOIS - Domain Owner Info:"
whois $1 | grep -E "Registrar|Creation Date|Registrant|OrgName"

echo ""
echo "[+] Quick Port Scan:"
for port in 80 443 22 21 25 53
do
  nc -zv -w 1 $1 $port 2>&1 | grep -o "succeeded" && echo "Port $port OPEN"
done

echo ""
echo "[*] Recon Complete"
echo "[*] To save: ./dns-recon.sh $1 | tee $1-recon.txt"
