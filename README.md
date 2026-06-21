<p align="center">
  <img src="assets/screenshot.JPG" alt="Project Screenshot" width="1000">
</p>

<h1 align="center">Automated Network Reconnaissance & Asset Mapping Tool</h1>

<p align="center">
Python • Scapy • ARP Discovery • Asset Tracking • Security Auditing
</p>

---

## Overview

A Python-based utility for automated local network reconnaissance and hardware asset mapping.

The tool performs active ARP-based network discovery to identify hosts on a local subnet, classify known and unknown assets, enumerate common services, assess potential security risks, and maintain a historical audit trail through persistent CSV logging.

---

## Features

* Active ARP-based host discovery using Scapy
* Automatic local subnet detection
* MAC address-based asset identification
* Reverse DNS hostname resolution
* Multi-threaded host analysis using ThreadPoolExecutor
* Open port enumeration
* Known and Unknown asset classification
* Risk assessment for exposed FTP and SMB services
* Persistent CSV audit logging
* Historical asset tracking and change detection

---

## Technology Stack

| Component         | Technology         |
| ----------------- | ------------------ |
| Language          | Python 3           |
| Network Discovery | Scapy              |
| Concurrency       | concurrent.futures |
| Networking        | socket             |
| Logging           | csv                |
| Reporting         | tabulate           |

---

## Architecture

```text
┌─────────────────────┐
│ Local Network Scan  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ARP Host Discovery  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Host Enumeration    │
│ • MAC Address       │
│ • Hostname          │
│ • Open Ports        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Asset Classification│
│ Known / Unknown     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Risk Assessment     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ CSV Audit Logging   │
└─────────────────────┘
```

---

## Project Structure

```text
Automated-Network-Reconnaissance-Asset-Mapping-Tool/
│
├── assets/
│   └── screenshot.JPG
│
├── b.py
├── known_devices.txt
├── master_log.csv
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sverma98015-commits/Automated-Network-Reconnaissance-Asset-Mapping-Tool.git
cd Automated-Network-Reconnaissance-Asset-Mapping-Tool
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scanner with administrative privileges:

```bash
python b.py
```

Administrator or root privileges may be required for ARP scanning and raw packet operations.

---

## Asset Inventory Management

Trusted devices are maintained in:

```text
known_devices.txt
```

Add one MAC address per line:

```text
d8:b3:2f:07:aa:26
6e:61:4b:4e:c7:fa
8e:f1:76:57:06:32
```

Devices found in this list will be classified as Known during scanning.

---

## Risk Assessment

The tool checks common network services including:

| Port | Service |
| ---- | ------- |
| 21   | FTP     |
| 22   | SSH     |
| 80   | HTTP    |
| 443  | HTTPS   |
| 445  | SMB     |

Hosts exposing FTP or SMB services are flagged as CRITICAL for further review.

---

## Sample Output

```text
+---------------------+---------------+-------------------+-------------+-----------+---------+----------+
| Time                | IP            | MAC               | Name        | Ports     | Status  | Risk     |
+---------------------+---------------+-------------------+-------------+-----------+---------+----------+
| 2026-06-20 10:30:12 | 192.168.31.1  | xx:xx:xx:xx:xx:xx | Router      | 80,443    | Known   | Safe     |
| 2026-06-20 10:30:12 | 192.168.31.58 | xx:xx:xx:xx:xx:xx | N/A         | 22        | Unknown | Safe     |
| 2026-06-20 10:30:12 | 192.168.31.233| xx:xx:xx:xx:xx:xx | Device      | 21,445    | Known   | CRITICAL |
+---------------------+---------------+-------------------+-------------+-----------+---------+----------+
```

---

## Screenshot

<p align="center">
  <img src="assets/screenshot.JPG" alt="Network Reconnaissance Scan" width="1000">
</p>

The screenshot demonstrates live network asset discovery, MAC address identification, hostname resolution, service enumeration, asset classification, and risk assessment.

---

## Audit Logging

Each completed scan automatically appends results to:

```text
master_log.csv
```

The log serves as a historical audit trail for:

* Asset inventory management
* Unauthorized device detection
* Security auditing
* Network change tracking
* Compliance documentation

---

## Security Notice

This tool is intended solely for authorized network administration, security auditing, educational purposes, and asset inventory management.

Only scan networks and systems for which you have explicit permission.

---

## Author

Satyam Verma

---

## License

This project is provided for educational and authorized security assessment purposes.
