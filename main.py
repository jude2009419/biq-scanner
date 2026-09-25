import socket
import qrcode
from datetime import datetime

print("=== Biq Scanner v1.0 ===")
print(f"Author: Biq Chalet | {datetime.now().year}\n")
print("1. Port Scanner")
print("2. Generate QR Code")
choice = input("Choose (1/2): ")

if choice == "1":
    target = input("Enter IP (e.g 8.8.8.8 or 192.168.1.1): ").strip()
    if not target:
        target = "8.8.8.8"
    print(f"\nScanning {target}...\n")
    for port in [21,22,53,80,443,3306,8080]:
        s = socket.socket()
        s.settimeout(0.6)
        if s.connect_ex((target, port)) == 0:
            print(f" [OPEN] {port}")
        else:
            print(f" [closed] {port}")
        s.close()
else:
    data = input("Enter text/link for QR: ").strip()
    if not data:
        data = "https://github.com/jude2009419/biq-scanner"
    img = qrcode.make(data)
    img.save("qr.png")
    print(f"\n✓ QR saved as qr.png in {__import__('os').getcwd()}")
    print("Open your file manager to see it!")
