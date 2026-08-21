from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import glob

app = FastAPI(title="PocketSOC FastAPI")

LOG_FILE = "logs/alerts.log"

@app.get("/", response_class=HTMLResponse)
def dashboard():
    html = """
    <html>
    <head><title>PocketSOC v3.0</title>
    <meta http-equiv="refresh" content="10">
    <style>
    body{background:#000;color:#0f0;font-family:monospace;padding:20px}
    h1{color:#0ff} .alert{border:1px solid #0f0;padding:10px;margin:5px}
    .critical{color:red;font-weight:bold}
    </style></head>
    <body>
    <h1>=== POCKET SOC v3.0 FASTAPI DASHBOARD ===</h1>
    <p>Zero-Budget SOC | Built in Ghana | Auto-refresh 10s</p>
    <h2>Recent Alerts</h2>
    """
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()[-20:]
            for line in lines:
                cls = "critical" if "CRITICAL" in line else ""
                html += f'<div class="alert {cls}">{line}</div>'
    
    html += "</body></html>"
    return html
