import http.server
import socketserver
import os
import json

PORT = 8080
LOG_FILE = os.path.expanduser("~/pocketsoc/data/alerts.json")

class SOCDashboard(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            alerts = []
            critical = high = medium = low = 0
            ip_count = {}
            
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, 'r') as f:
                    try:
                        alerts = json.load(f)
                    except:
                        alerts = []
            
            for alert in alerts:
                sev = alert.get('severity', 'Low').lower()
                if sev == 'critical': critical += 1
                elif sev == 'high': high += 1
                elif sev == 'medium': medium += 1
                else: low += 1
                
                ip = alert.get('src_ip', 'Unknown')
                ip_count[ip] = ip_count.get(ip, 0) + 1
            
            top_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:5]
            
            html = f"""<!DOCTYPE html>
<html><head><title>POCKET.SOC v1.6.2</title>
<meta http-equiv="refresh" content="10">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{ background:#000; color:#00ff00; font-family:monospace; padding:10px; }}
.box {{ border:1px solid #00ff00; padding:10px; margin:10px 0; }}
.critical {{ color:red; }}.high {{ color:orange; }}.medium {{ color:yellow; }}.low {{ color:cyan; }}
table {{ width:100%; border-collapse:collapse; }}
td, th {{ border:1px solid #00ff00; padding:5px; }}
.blink {{ animation: blinker 1s linear infinite; }}
@keyframes blinker {{ 50% {{ opacity: 0; }}
</style></head><body>
<h1>POCKET.SOC v1.6.2 DASHBOARD <span class="blink">[LIVE]</span></h1>
<div class="box"><b>Total:</b> {len(alerts)}<br>
<b>Severity:</b> <span class="critical">Critical: {critical}</span> | <span class="high">High: {high}</span> | <span class="medium">Medium: {medium}</span> | <span class="low">Low: {low}</span></div>
<div class="box"><b>Top IPs:</b><br>{''.join([f'{ip}: {count} hits<br>' for ip, count in top_ips])}</div>
<div class="box"><b>Recent Alerts:</b><br><table>
<tr><th>Time</th><th>Severity</th><th>Source</th><th>Rule</th></tr>
{''.join([f"<tr class='{a.get('severity','low').lower()}'><td>{a.get('timestamp','N/A')}</td><td>{a.get('severity','Low')}</td><td>{a.get('src_ip','N/A')}</td><td>{a.get('rule','N/A')}</td></tr>" for a in alerts[-10:]]) }
</table></div>
<div style="text-align:center; font-size:10px;">Auto-refresh: 10s | Last updated: {datetime.now().strftime('%H:%M:%S')}</div>
</body></html>"""
            self.wfile.write(html.encode())
        else:
            self.send_error(404)

from datetime import datetime
with socketserver.TCPServer(("", PORT), SOCDashboard) as httpd:
    print(f"Dashboard running on http://localhost:{PORT}")
    httpd.serve_forever()
