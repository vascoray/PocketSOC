# PocketSOC Cheatsheet: Mobile SOC = Enterprise SOC
`Termux commands that map 1:1 to Splunk + Wazuh`

Built in Ghana 🇬🇭 | Zero-Budget SOC

### 1. START / STOP SERVICES
| Action | PocketSOC | Splunk Enterprise | Wazuh |
| --- | --- | --- | --- |
| Start Everything | `bash soc_menu.sh` then `[2]` | `splunk start` | `systemctl start wazuh-manager wazuh-dashboard` |
| Start Dashboard Only | `python src/web/app.py` | `splunk start` | `systemctl start wazuh-dashboard` |
| Start Terminal Dashboard | `python dashboard.py` | N/A - Use CLI search | `wazuh-logtest` |
| Stop Everything | `pkill -f python` | `splunk stop` | `systemctl stop wazuh-manager` |
| Check Status | `ps aux \| grep python` | `splunk status` | `systemctl status wazuh-manager` |

### 2. VIEW & SEARCH LOGS
| Action | PocketSOC | Splunk SPL Query | Wazuh |
| --- | --- | --- | --- |
| Live Log Tail | `tail -f logs/suricata/eve.json` | `index=suricata \| tail` | `tail -f /var/ossec/logs/alerts/alerts.json` |
| View All Alerts | `cat data/alerts.json` | `index=* sourcetype=suricata` | `cat /var/ossec/logs/alerts/alerts.json` |
| Top Attacker IPs | Auto in Dashboard | `\| stats count by src_ip \| sort -count` | Dashboard > Agents > Top Sources |
| Severity Breakdown | Auto in Dashboard | `\| stats count by severity` | Dashboard > Rule.Level |

### 3. CONFIG & FILES
| Action | PocketSOC | Splunk | Wazuh |
| --- | --- | --- | --- |
| Main Config Folder | `./` | `$SPLUNK_HOME/etc/system/local/` | `/var/ossec/etc/` |
| Log Folder | `./logs/suricata/` | `$SPLUNK_HOME/var/log/splunk/` | `/var/ossec/logs/` |
| Alert Database | `./data/alerts.json` | Splunk Index | `/var/ossec/logs/alerts/` |
| Install Deps | `pip install -r requirements.txt` | N/A | `apt install wazuh-manager` |

### 4. EXTRA TOOLS
| Action | PocketSOC | Enterprise Equivalent |
| --- | --- | --- |
| Network Scan | Option 4 in `soc_menu.sh` | Splunk App for Nmap / Wazuh SCA |

---
### The PocketSOC Advantage
`RAM: 50MB` vs `Splunk: 4GB+` | `Wazuh: 2GB+`  
`Setup Time: 2 minutes` vs `2 hours`  
`Runs on: Any Android Phone`
