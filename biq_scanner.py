# Biq Scanner v2 - by Biq Chalet
# Ethical use only: scanme.nmap.org or sites you own

import socket
import requests
import sys
from datetime import datetime

target = sys.argv[1] if len(sys.argv) > 1 else "scanme.nmap.org"
print(f"\n[+] Biq Scanner v2 - Scanning: {target}")
print(f"[+] Time: {datetime.now()} \n")

open_ports = []
found_dirs = []

# 1. PORT SCAN
print("[*] Checking common ports...")
ports = [21,22,23,25,53,80,110,135,139,443,445,993,995,9929,8080,8443,31337]
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((target, port))
        print(f" [OPEN] Port {port}")
        open_ports.append(port)
        s.close()
    except:
        pass

# 2. DIR SCAN
print(f"\n[*] Checking hidden folders on http://{target}")
paths = ["images","shared","admin","login","images/","css","js","index","backup","config","api","uploads","dashboard","server-status",".git"]
for p in paths:
    url = f"http://{target}/{p}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code in [200,403,301,302]:
            print(f" [FOUND] {url} - CODE {r.status_code} - SIZE {len(r.text)}")
            found_dirs.append(f"{url} - CODE {r.status_code}")
    except:
        pass

# 3. SAVE REPORT
with open("report.txt","w") as f:
    f.write(f"Biq Scanner v2 Report for {target}\n")
    f.write(f"Time: {datetime.now()}\n\n")
    f.write(f"Open Ports: {open_ports}\n")
    f.write(f"Found Dirs:\n")
    for d in found_dirs:
        f.write(d+"\n")

print("\n[Done] Scan finished - Saved to report.txt - Biq Scanner v2")

