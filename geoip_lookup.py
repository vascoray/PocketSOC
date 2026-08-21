import os
from collections import Counter

print("==============================================")
print("GEOIP WORLD MAP - ATTACKER LOCATIONS")
print("==============================================")

geo_file = os.path.expanduser("~/pocketsoc/geo_hits.log")

if not os.path.exists(geo_file):
    print("No geo data yet. Start Demo NIDS first - Option 1")
    exit()

with open(geo_file) as f:
    countries = [line.strip() for line in f if line.strip()]

counts = Counter(countries)

if not counts:
    print("No attacks logged yet")
else:
    total = sum(counts.values())
    print(f"Total Attacks Logged: {total}\n")
    for country, count in counts.most_common():
        bar = "█" * count
        print(f"{country}: {bar} {count}")

print("==============================================")
