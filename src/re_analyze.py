import pathlib, subprocess, re, time, sys
print("POCKET SOC v3.2 | KING VASCO - RE Analyze Binary [r2] entry0")
print("-"*55)
path=input("Enter binary path (/bin/ls or evidence file): ").strip()
if not path:
    print("No path"); input("ENTER..."); sys.exit(0)
p=pathlib.Path(path).expanduser()
if not p.exists():
    print(f"[X] Not found: {p}")
    print("Tip: ls ~/pocketsoc/evidence/")
    input("ENTER..."); sys.exit(0)
print(f"\n[FILE] {p} - {p.stat().st_size} bytes")
print(f"[TYPE] {subprocess.getoutput(f'file \"{p}\"')}")
has_r2="r2" in subprocess.getoutput("which r2")
if has_r2:
    print("\n[r2] Found - disasm entry0:")
    print(subprocess.getoutput(f"r2 -AA -q -c 'ie; pd 20 @ entry0' '{p}' 2>&1 | head -n 40"))
else:
    print("\n[r2] Not installed (pkg install radare2) - using Python engine")
try:
    data=open(p,'rb').read()
    entry=0
    if data[:4]==b'\x7fELF':
        entry=int.from_bytes(data[24:28],'little') if data[4]==1 else int.from_bytes(data[32:40],'little')
        print(f"\n[ELF] entry0 = 0x{entry:x}")
    strs=re.findall(b"[ -~]{4,}", data)
    hits=[s.decode() for s in strs if any(k in s.lower() for k in [b'pass',b'flag',b'/bin/sh',b'http',b'key'])]
    print(f"\n[STRINGS] {len(strs)} total")
    for s in hits[:25]:
        print(f" - {s}")
    if b'/bin/sh' in data:
        print("\n[!] SHELL SPAWN DETECTED")
    rep=pathlib.Path.home()/f"pocketsoc/evidence/RE_{p.name}_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    open(rep,'w').write(f"File {p}\nEntry0 0x{entry:x}\n" + "\n".join([s.decode(errors='ignore') for s in strs[:200]]))
    print(f"\n[REPORT] Saved: {rep}")
except Exception as e:
    print(f"Error: {e}")
print("\n"+"="*55)
input("Press ENTER...")
