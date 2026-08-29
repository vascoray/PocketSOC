import time, pathlib, re
BASE=pathlib.Path.home()/"pocketsoc"
LOG=BASE/"logs/auth.log"

print("POCKET SOC v3.2 | KING VASCO - PACKET SNIFFER")
print("-"*45)
target = input("Enter IP to sniff (or press ENTER for all): ").strip()

print(f"\n[SNIFFING] Watching {LOG}")
if target:
    print(f"Filter: {target}\n")
else:
    print("Filter: ALL traffic\n")

print("Press CTRL+C to stop\n")

try:
    with open(LOG, "r") as f:
        f.seek(0,2) # go to end
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            if target and target not in line:
                continue
            # Highlight
            if "Failed" in line or "BLOCKED" in line:
                print(f"[ALERT] {line.strip()}")
            else:
                print(f"[PACKET] {line.strip()}")
except KeyboardInterrupt:
    print("\n[STOPPED] Sniffer stopped clean")
    input("Press ENTER to return...")
except FileNotFoundError:
    print(f"Log not found: {LOG}")
    print("Creating dummy log for demo...")
    LOG.parent.mkdir(exist_ok=True)
    LOG.touch()
    print("Now run: 1) Start Engine, then try sniffer again")
    input("Press ENTER...")
