# Automated-Network-Reconnaissance-Asset-Mapping-Tool

A Python-based utility for automated local network reconnaissance and hardware asset mapping.

**Overview**
This tool performs active ARP discovery on a local subnet to identify active hosts. It provides real-time mapping of device status, open ports, and risk metrics, outputting data to a persistent CSV log for historical audit trails.

**Technical Stack**
Discovery: scapy (ARP protocol manipulation)

Concurrency: concurrent.futures (ThreadPoolExecutor for optimized scanning)

Logging: csv (automated master log generation)

Reporting: tabulate (CLI formatting)

**Key Features**
MAC-Based Asset Tracking: Persistent identification using hardware addresses, bypassing dynamic IP changes.

Vulnerability Detection: Automated checks for high-risk ports (FTP/SMB) to flag potential attack vectors.

Change Detection: Historical logging facilitates the identification of unauthorized or "Unknown" assets appearing on the network over time.

Quick Start
Dependencies:

**Bash**
pip install -r requirements.txt

**Execution:**

Bash
# Run with administrative privileges to enable raw packet capture
python z.py
Asset Inventory:
Maintain your local known_devices.txt file by adding MAC addresses of trusted hardware (one per line, lowercase).

Audit & Compliance
The tool generates master_log.csv upon each scan completion. For security auditing, ensure this file is preserved to track network evolution and device behavior over time.

Why this looks more "Human/Professional":
Concise Language: It cuts out the "I am happy to help" fluff and focuses strictly on the tool's utility.

Structural Hierarchy: It uses clean lists and code blocks, which is how senior software engineers write documentation.

No Over-Formatting: It avoids unnecessary bolding or italicizing, which makes the text look natural and deliberate rather than computer-generated.

Actionable Headers: It uses standard sections (Overview, Technical Stack, Quick Start) that hiring managers expect to see in a professional repository.
