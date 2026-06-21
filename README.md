Markdown
# 🛡️ Network Asset Auditor

A high-performance Python utility designed for automated local network reconnaissance, hardware asset mapping, and security auditing.

---

## 🔍 Project Philosophy
This tool was engineered to address the need for **persistent asset tracking** in dynamic network environments. By utilizing ARP-based discovery and MAC-address matching, it ensures reliable device identification regardless of DHCP-assigned IP address changes.

## ⚙️ Technical Architecture
* **Discovery Engine:** Uses `scapy` to craft and send raw Ethernet/ARP packets, ensuring deep visibility into the local subnet.
* **Concurrency:** Implemented via `concurrent.futures.ThreadPoolExecutor` to perform multi-threaded port scanning, significantly reducing audit time.
* **Security Intelligence:** Automatically flags high-risk services (FTP/SMB) to identify potential attack vectors.
* **Persistence:** Generates structured CSV logs for historical trend analysis and change detection.

---

## 🚀 Deployment Guide

### Prerequisites
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
Execution
Run the auditor with Administrative Privileges to allow the raw socket access required for packet injection:

Bash
python z.py
Asset Management
The system relies on your known_devices.txt as the Source of Truth.

Format: One MAC address per line, in lowercase (e.g., d8:b3:2f:07:aa:26).

Strict Control: The application strictly monitors this list and will never auto-modify it, ensuring your configuration remains immutable.

📊 Security Auditing
The generated master_log.csv serves as your primary security artifact. Use this for:

Change Detection: Compare historical MAC entries to identify unauthorized new hardware.

Vulnerability Assessment: Monitor for devices exposing sensitive ports.

Compliance Reporting: Maintain a chronological inventory of every device seen on the network.

📝 License & Attribution
Developed for educational security research. Use only on networks you own or have explicit authorization to audit.
