from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
ALERTS = []
LOG_FILE = "alerts.json"

# Load old alerts if file exists
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        try:
            ALERTS = json.load(f)
        except:
            ALERTS = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>POCKET.SOC v1.7</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="10">
    <style>
        body { background: #000; color: #00ff00; font-family: 'Courier New'; padding: 10px; }
        .header { color: #00ff00; font-size: 20px; font-weight: bold; margin-bottom: 10px; }
        .box { border: 2px solid #00ff00; padding: 10px; margin: 10px 0; }
        .critical { color: red; font-weight: bold; }
        .high { color: orange; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; font-size: 12px; }
        th, td { border: 1px solid #00ff00; padding: 5px; text-align: left; }
        th { background: #001100; }
    </style>
</head>
<body>
    <div class="header">POCKET.SOC v1.7 DASHBOARD [LIVE]</div>
    
    <div class="box">
        <b>Total: {{total}}</b><br>
        Severity: <span class="critical">Critical: {{critical}}</span> | 
        <span class="high">High: {{high}}</span> | 
        Medium: {{medium}} | Low: {{low}}
    </div>

    <div class="box">
        <b>Recent Alerts:</b>
        <table>
            <tr><th>Time</th><th>Severity</th><th>Source</th><th>Event</th></tr>
            {% for a in alerts %}
            <tr>
                <td>{{a.time}}</td>
                <td class="{{a.severity.lower()}}">{{a.severity}}</td>
                <td>{{a.source}}</td>
                <td>{{a.event}} {% if a.mitre %}| {{a.mitre}}{% endif %}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
    <div style="text-align:center; font-size:10px;">Auto-refresh: 10s | Last updated: {{last_update}}</div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    critical = sum(1 for a in ALERTS if a['severity'] == 'Critical')
    high = sum(1 for a in ALERTS if a['severity'] == 'High')
    medium = sum(1 for a in ALERTS if a['severity'] == 'Medium')
    low = sum(1 for a in ALERTS if a['severity'] == 'Low')
    
    return render_template_string(HTML, 
        alerts=ALERTS[-10:], 
        total=len(ALERTS),
        critical=critical, high=high, medium=medium, low=low,
        last_update=datetime.now().strftime("%H:%M:%S"))

@app.route('/api/logs', methods=['POST'])
def add_log():
    data = request.json
    # v1.7 FIX: Accept 'source' from agent. Fallback to 'ip' for old data
    alert = {
        'time': data.get('time', str(datetime.now())),
        'severity': data.get('severity', 'Low'),
        'source': data.get('source', data.get('ip', 'UNKNOWN')),  # KEY LINE
        'event': data.get('event', 'Unknown'),
        'mitre': data.get('mitre', '')
    }
    ALERTS.append(alert)
    # Save to file
    with open(LOG_FILE, 'w') as f:
        json.dump(ALERTS, f)
    print(f"[+] New Alert: {alert['source']} - {alert['event']}")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
