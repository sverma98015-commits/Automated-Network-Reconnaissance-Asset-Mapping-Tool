Markdown
# Network Asset Auditor

A Python-based utility for automated local network reconnaissance and hardware asset mapping.

---

## 📋 Overview
This tool performs active ARP discovery on a local subnet to identify active hosts. It provides real-time mapping of device status, open ports, and risk metrics, outputting data to a persistent CSV log for historical audit trails.

## 🛠 Technical Stack
* **Discovery:** `scapy` (ARP protocol manipulation)
* **Concurrency:** `concurrent.futures` (ThreadPoolExecutor for optimized scanning)
* **Logging:** `csv` (automated master log generation)
* **Reporting:** `tabulate` (CLI formatting)

## 🚀 Key Features
* **MAC-Based Asset Tracking:** Persistent identification using hardware addresses, bypassing dynamic IP changes.
* **Vulnerability Detection:** Automated checks for high-risk ports (FTP/SMB) to flag potential attack vectors.
* **Change Detection:** Historical logging facilitates the identification of unauthorized or "Unknown" assets appearing on the network over time.

## ⚡ Quick Start

### 1. Dependencies
Install the required libraries:
```bash
pip install -r requirements.txt
2. Execution
Run the script with administrative privileges to enable raw packet capture:

Bash
python z.py
3. Asset Inventory
Maintain your local known_devices.txt file by adding the MAC addresses of trusted hardware (one per line, lowercase).

📊 Audit & Compliance
The tool generates master_log.csv upon each scan completion. For security auditing, ensure this file is preserved to track network evolution and device behavior over time.
