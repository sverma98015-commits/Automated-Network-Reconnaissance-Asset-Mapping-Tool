# 🔍 Automated Network Reconnaissance & Asset Mapping Tool

> **Python-based utility for automated local network reconnaissance, asset discovery, and security auditing.**

---

## 📖 Overview

This tool performs **active ARP-based network discovery** across a local subnet to identify active hosts and map network assets in real time.

It provides detailed visibility into:

- Active devices on the network
- Hardware asset identification via MAC addresses
- Open service ports
- Risk assessment indicators
- Historical audit logging

All collected data is exported to a persistent **CSV audit log**, enabling long-term asset tracking and change detection.

---

## ⚙️ Technical Stack

| Component | Technology |
|-----------|------------|
| Network Discovery | `scapy` |
| Concurrency | `concurrent.futures` |
| Data Logging | `csv` |
| Reporting | `tabulate` |
| Language | `Python 3` |

---

## 🚀 Key Features

### 🖥️ MAC-Based Asset Tracking
Track devices using their unique hardware (MAC) addresses rather than IP addresses, ensuring accurate identification even when DHCP assignments change.

### 🔎 Automated Host Discovery
Performs active ARP scanning to rapidly discover live hosts across the target subnet.

### ⚡ Multi-Threaded Port Analysis
Utilizes `ThreadPoolExecutor` for concurrent scanning, significantly improving performance on larger networks.

### 🛡️ Vulnerability Detection
Automatically identifies potentially risky services and ports, including:

- FTP (Port 21)
- SMB (Ports 139 / 445)

These services are flagged for further security review.

### 📊 Historical Change Detection
Maintains a master audit log, allowing administrators to:

- Detect newly connected devices
- Identify unknown assets
- Monitor network growth
- Track infrastructure changes over time

### 📁 Persistent Audit Logging
Every scan result is automatically appended to a centralized CSV database for compliance and auditing purposes.

---

## 📂 Project Structure

```text
project/
│
├── z.py
├── known_devices.txt
├── master_log.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### Clone Repository

```bash
git clone <repository-url>
cd project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Execution

Run the scanner with administrative privileges to enable raw packet capture and ARP operations.

```bash
python z.py
```

> ⚠️ Administrator/root privileges may be required depending on your operating system.

---

## 📝 Asset Inventory Management

Maintain a local inventory of trusted devices using:

```text
known_devices.txt
```

Add one MAC address per line:

```text
aa:bb:cc:dd:ee:ff
11:22:33:44:55:66
```

Requirements:

- Lowercase format
- One address per line
- No additional comments or spaces

---

## 📈 Audit & Compliance

After each scan, the tool automatically generates:

```text
master_log.csv
```

This file serves as a historical audit database and should be preserved for:

- Security assessments
- Asset management
- Compliance reporting
- Unauthorized device detection
- Network change tracking

---

## 🎯 Use Cases

- Network Asset Inventory
- Security Auditing
- Internal Network Monitoring
- Unauthorized Device Detection
- Small Office Infrastructure Management
- Home Lab Security Assessment

---

## 🔒 Security Note

This utility is intended for **authorized network environments only**. Ensure you have permission to scan and monitor any network before use.

---

## 📜 License

This project is provided for educational, research, and authorized security assessment purposes.

---

### 👨‍💻 Developed for Network Visibility, Asset Management & Security Auditing
