import http.server, os
class H(http.server.SimpleHTTPRequestHandler):
 def do_GET(self):
  if 'dashboard' in self.path or self.path == '/':
   ips=open('logs/blocked_ips.log').read()[-3000:] if os.path.exists('logs/blocked_ips.log') else "No blocks yet - waiting for attacks..."
   raw=open('logs/auth.log').read()[-3000:] if os.path.exists('logs/auth.log') else "No attacks yet"
   ev="\n".join(os.listdir('evidence')) if os.path.exists('evidence') else "No evidence yet"
   html=f"<html><head><meta http-equiv='refresh' content='2'><meta name=viewport content='width=device-width'><style>body{{background:#000;color:#0f0;font-family:monospace;padding:10px}} .box{{border:2px solid #0f0;padding:10px;margin:10px 0}}</style></head><body><h1>POCKET SOC v3.0 - 100% OFFLINE LIVE</h1><p>Auto refresh 2s - LIVE READING FILES</p><div class=box><h2>Blocked IPs (LIVE AUTO)</h2><pre>{ips}</pre></div><div class=box><h2>Evidence Files - {len(ev.split())} files</h2><pre>{ev}</pre></div><div class=box><h2>Last Attack Raw (LIVE AUTO)</h2><pre>{raw}</pre></div></body></html>"
   self.send_response(200); self.send_header('Content-type','text/html'); self.end_headers(); self.wfile.write(html.encode())
  else:
   return super().do_GET()
print("Starting LIVE auto dashboard on 8080...")
http.server.test(HandlerClass=H, port=8080)
