import http.server
import socketserver
import os
import time
import re
from datetime import datetime

PORT = 8000
LOG_FILE = os.path.expanduser("~/PocketSOC/suricata/log/fast.log")

class SOCDashboard(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            alerts = []
            critical = high = medium = low = 0
            ip_count = {}
            
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r', errors='ignore') as f:
                    lines = f.readlines()[-100:]
                    for line in lines:
                        alerts.append(line.strip())
                        if 'Priority: 1' in line or 'Critical' in line:
                            critical += 1
                        elif 'Priority: 2' in line or 'High' in line:
                            high += 1
                        elif 'Priority: 3' in line:
                            medium += 1
                        else:
                            low += 1
                        
                        ips = re.findall(r'(\d+\.\d+\.\d+\.\d+):', line)
                        for ip in ips:
                            ip_count[ip] = ip_count.get(ip, 0) + 1
            
            top_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Pocket SOC Dashboard</title>
                <meta http-equiv="refresh" content="10">
                <style>
                    body {{ background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }}
                   .header {{ border-bottom: 2px solid #00ff00; padding-bottom: 10px; margin-bottom: 20px; }}
                   .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
                   .stat-box {{ border: 1px solid #00ff00; padding: 15px; flex: 1; }}
                   .critical {{ color: #ff0000; }}
                   .high {{ color: #ff6600; }}
                   .alert {{ background: #111; padding: 5px; margin: 2px 0; font-size: 12px; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>=== POCKET SOC v1.6.2 DASHBOARD ===</h1>
                    <p>Zero-Budget SOC | Built in Ghana | Auto-refresh 10s</p>
                </div>
                
                <div class="stats">
                    <div class="stat-box">
                        <h3>Total Last 100: {len(alerts)}</h3>
                        <p class="critical">Critical: {critical}</p>
                        <p class="high">High: {high}</p>
                        <p>Medium: {medium}</p>
                        <p>Low: {low}</p>
                    </div>
                    <div class="stat-box">
                        <h3>Top 5 Source IPs</h3>
                        {''.join([f'<p>{ip}: {count} hits</p>' for ip, count in top_ips])}
                    </div>
                </div>
                
                <h3>Recent Alerts</h3>
                <div>
                    {''.join([f'<div class="alert">{a}</div>' for a in alerts[-10:]])}
                </div>
                <p><small>Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small></p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), SOCDashboard) as httpd:
    print(f"Dashboard running at http://localhost:{PORT}")
    httpd.serve_forever()
