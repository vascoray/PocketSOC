import subprocess,re,time,pathlib
BASE=pathlib.Path.home()/"pocketsoc"
LOG=BASE/"logs/auth.log"
BLOCK=BASE/"logs/blocked_ips.log"
EVD=BASE/"evidence"
EVD.mkdir(exist_ok=True)
print(f"POCKET SOC v3.2 OFFLINE | KING VASCO - Watching {LOG}")
print("Engine running... CTRL+C to stop")
try:
    p=subprocess.Popen(["tail","-F",str(LOG)],stdout=subprocess.PIPE,text=True,bufsize=1)
    cnt={}
    for line in p.stdout:
        if "Failed" in line:
            m=re.search(r"from (\d+\.\d+\.\d+\.\d+)",line)
            if not m: continue
            ip=m.group(1)
            cnt[ip]=cnt.get(ip,0)+1
            print(f"[{cnt[ip]}] {ip}")
            if cnt[ip]>=3:
                ts=time.strftime("%Y-%m-%d_%H-%M-%S")
                open(BLOCK,"a").write(f"{ts} {ip} BLOCKED\n")
                open(EVD/f"{ts}_{ip}.log","w").write(line)
                print(f"[BLOCKED] {ip}")
                cnt[ip]=0
except KeyboardInterrupt:
    print("STOPPED clean")
