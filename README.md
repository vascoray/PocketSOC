# POCKET SOC MOBILE V3.2 👑
SOC Dashboard + GeoIP World Map running on Termux Android
Built in Ghana GH by King Vasco

![Python](https://img.shields.io/badge/Python-3-blue) 
![Flask](https://img.shields.io/badge/Flask-WebDashboard-green)
![Termux](https://img.shields.io/badge/Platform-Termux-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

POCKET SOC v3.2 100% OFFLINE MODE
Built in Ghana GH - Accra - King Vasco

1. Start OFFLINE SOC Engine
2. Stop OFFLINE SOC Engine
3. View Blocked IPs REAL
4. View Evidence Files REAL
5. Port Scanner Offline + Online (8.8.8.8 / 127.0.0.1)
6. Dashboard Stats localhost:8080
7. View Blocked IPs
8. Clear Logs
9. GeoIP World Map
10. Exit

![Logo](Pocketsoc.jpg.jpg)

Pocket SOC Mobile Lab OS is a 9-module cybersecurity toolkit designed for African SMEs priced out of $20k SOC tools. 

![Dashboard](Dashboards.jpg.JPG)

![Dashboard](Dashboardss.jpg.JPG)

Runs 100% offline on Android.
5 Modules: Network Scan | Log Analysis | Detection Engine | Dashboard | Automation

![Menu](Menu.jpg.JPG)

Built around D.I.D.A.R: Detect → Investigate → Document → Automate → Reduce

![Logo](Pocket.png.PNG)

![Google Defined](https://img.shields.io/badge/Google_AI-Defines_as_%22mobile%20soc%20lab%22-4285F4)
![Creator](https://img.shields.io/badge/Creator-Vasco_Romeo_Yao_Akpobi_Ghana-black)
![Offline](https://img.shields.io/badge/100%25-OFFLINE-red)
![Version](https://img.shields.io/badge/VERSION-V3.3-red)
![Built In](https://img.shields.io/badge/BUILT_IN-GHANA_%F0%9F%87%AC%F0%9F%87%AD-yellow)
![License](https://img.shields.io/badge/LICENSE-MIT-yellow)
![Mode](https://img.shields.io/badge/MODE-100%25_OFFLINE-black)

## Run
git clone https://github.com/vascoray/pocketsoc.git
cd pocketsoc
pip install fastapi uvicorn -q
chmod +x *.py
python3 auto_block.py &
python3 live_server.py &
echo "Open: http://localhost:8080 and http://localhost:3003"
