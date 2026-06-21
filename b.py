import socket
import os
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from scapy.all import ARP, Ether, srp
from tabulate import tabulate

# Configuration: Hard-coded paths for your project
KNOWN_FILE = "known_devices.txt"
MASTER_LOG = "master_log.csv"

def load_known_macs():
    """Reads known MAC addresses from text file. Does not auto-update."""
    if not os.path.exists(KNOWN_FILE): return set()
    with open(KNOWN_FILE, "r") as f:
        return set(line.strip().lower() for line in f if line.strip())

def get_network_range():
    """Auto-detects the local subnet."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ".".join(ip.split('.')[:-1]) + ".0/24"
    finally:
        s.close()

def scan_host(ip, known_macs):
    """Scans single host for MAC, Name, and Ports."""
    mac = "Unknown"
    # ARP Request to get MAC
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=1, verbose=False)
    if ans:
        mac = ans[0][1].hwsrc.lower()
    
    try: name = socket.gethostbyaddr(ip)[0]
    except: name = "N/A"
    
    # Port Scan
    open_ports = []
    for port in [21, 22, 80, 443, 445]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.05)
            if s.connect_ex((ip, port)) == 0: open_ports.append(str(port))
    
    # Matching Logic: Strict MAC check
    status = "Known" if mac in known_macs else "Unknown"
    risk = "CRITICAL" if any(p in ['21', '445'] for p in open_ports) else "Safe"
    
    return [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, mac, name, ",".join(open_ports), status, risk]

def run_recon():
    net = get_network_range()
    known_macs = load_known_macs()
    print(f"[*] Reconnaissance on {net}...")
    
    # Discovery
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=net), timeout=3, verbose=False)
    live_hosts = [r.psrc for s, r in ans]
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(lambda ip: scan_host(ip, known_macs), live_hosts))
    
    # Output to CLI
    print(tabulate(results, headers=["Time", "IP", "MAC", "Name", "Ports", "Status", "Risk"], tablefmt="grid"))
    
    # Auto-log to CSV
    file_exists = os.path.isfile(MASTER_LOG)
    with open(MASTER_LOG, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists or os.path.getsize(MASTER_LOG) == 0:
            writer.writerow(["Time", "IP", "MAC", "Name", "Ports", "Status", "Risk"])
        writer.writerows(results)
    print(f"[*] Audit complete. Results appended to {MASTER_LOG}")

if __name__ == "__main__":
    run_recon()