from flask import Flask, render_template_string, jsonify, request
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
    <title>PocketSOC v1.8</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #000; color: #00FF00; font-family: 'Courier New', monospace; margin: 0; padding: 10px; }
        h1 { color: #00FF00; text-align: center; text-shadow: 0 0 10px #00FF00; }
        .stats { border: 2px solid #00FF00; padding: 10px; margin: 10px 0; }
        .critical { color: red; }
        .high { color: orange; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #00FF00; padding: 8px; text-align: left; }
        th { background: #001100; }
    </style>
</head>
<body>
    <h1>POCKET.SOC v1.8 DASHBOARD [LIVE]</h1>
    
    <div class="stats">
        <h2>Total: {{ total }}</h2>
        <p>Severity: <span class="critical">Critical: {{ critical }}</span> | 
        <span class="high">High: {{ high }}</span> | 
        Medium: {{ medium }} | Low: {{ low }}</p>
    </div>

    <h2>Recent Alerts:</h2>
    <table>
        <tr>
            <th>Time</th>
            <th>Severity</th>
            <th>Source</th>
            <th>Event</th>
        </tr>
        {% for alert in alerts %}
        <tr>
            <td>{{ alert.timestamp }}</td>
            <td class="{{ alert.severity.lower() }}">{{ alert.severity }}</td>
            <td>{{ alert.source }}</td>
            <td>{{ alert.event }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def dashboard():
    global ALERTS
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            try:
                ALERTS = json.load(f)
            except:
                pass
    
    ALERTS.reverse()
    total = len(ALERTS)
    critical = len([a for a in ALERTS if a['severity'] == 'Critical'])
    high = len([a for a in ALERTS if a['severity'] == 'High'])
    medium = len([a for a in ALERTS if a['severity'] == 'Medium'])
    low = len([a for a in ALERTS if a['severity'] == 'Low'])
    
    return render_template_string(HTML, 
        alerts=ALERTS[:20], 
        total=total,
        critical=critical,
        high=high,
        medium=medium,
        low=low)

@app.route('/api/alerts', methods=['POST'])
def add_alert():
    alert = request.json
    alert['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    ALERTS.append(alert)
    with open(LOG_FILE, 'w') as f:
        json.dump(ALERTS, f, indent=2)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
