from flask import Flask, render_template_string
import time, os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>POCKET SOC V2.3.1</title>
<style>
body { background: #000; color: #00FF41; font-family: 'Courier New'; margin: 10px; text-shadow: 0 0 3px #00FF41; }
.header { text-align: center; font-size: 18px; border-bottom: 2px solid #00FF41; padding-bottom: 5px; }
.card { border: 1px solid #00FF41; padding: 10px; margin: 10px 0; border-radius: 8px; }
.bar { background: #00FF41; height: 20px; margin: 5px 0; border-radius: 4px; }
.alert { font-size: 12px; border-bottom: 1px dashed #00FF41; padding: 3px 0; }
</style>
</head>
<body>
<div class="header">POCKET SOC V2.3.1 [LIVE] - GEOIP</div>

<div class="card">
<b>STATS</b><br>
Total: {{total}} | Blocked: {{blocked}}
</div>

<div class="card">
<b>TOP ATTACKER COUNTRIES</b><br>
{% for country, count in countries.items() %}
{{country}}<br>
<div class="bar" style="width:{{count*10}}%"></div>
{% endfor %}
</div>

<div class="card">
<b>RECENT ALERTS</b><br>
{% for alert in alerts %}
<div class="alert">{{alert}}</div>
{% endfor %}
</div>
</body>
</html>
"""

def read_logs():
    alerts = []
    countries = {}
    if os.path.exists(os.path.expanduser("~/pocketsoc/alerts.log")):
        with open(os.path.expanduser("~/pocketsoc/alerts.log")) as f:
            alerts = f.readlines()[-10:]
    if os.path.exists(os.path.expanduser("~/pocketsoc/geo_hits.log")):
        with open(os.path.expanduser("~/pocketsoc/geo_hits.log")) as f:
            for line in f:
                c = line.strip()
                countries[c] = countries.get(c, 0) + 1
    blocked = len(open(os.path.expanduser("~/pocketsoc/blocked_ips.log")).readlines()) if os.path.exists(os.path.expanduser("~/pocketsoc/blocked_ips.log")) else 0
    return alerts, countries, blocked

@app.route('/')
def home():
    alerts, countries, blocked = read_logs()
    return render_template_string(HTML, alerts=alerts, countries=countries, total=sum(countries.values()), blocked=blocked)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
