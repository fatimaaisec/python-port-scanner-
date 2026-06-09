# 🛡️ Python Port Scanner

A lightweight, multithreaded port scanner built in Python for cybersecurity learning and network reconnaissance practice.

> ⚠️ Disclaimer: This tool is for **educational and ethical use only**. Scan only systems you own or have explicit permission to test.

---

## ⚡ Overview

This tool scans a target host and detects open ports along with common services. It is designed to simulate basic functionality similar to professional network scanners.

---

## 🔍 Features

* Fast multithreaded port scanning
* Common service detection (HTTP, SSH, FTP, etc.)
* IP resolution from domain names
* Real-time scan output
* Results saved to file
* Clean CLI-based interface

---

## 🧠 How It Works

The scanner:

1. Resolves domain → IP address
2. Scans ports (1–1024) using TCP connections
3. Uses multithreading for speed
4. Identifies open ports and associated services
5. Saves results to a report file

---

## 🧰 Tech Stack

* Python 3
* `socket` (network connections)
* `threading` (parallel scanning)
* `datetime` (logging)

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
cd python-port-scanner
python port_scanner.py
```

---

## ▶️ Usage

```bash
Enter target IP or website: scanme.nmap.org
```

Example output:

```txt
==================================================
Scanning Target: scanme.nmap.org
Started at: 2026-06-09 12:00:00
==================================================

[OPEN] Port 22 - SSH
[OPEN] Port 80 - HTTP
[OPEN] Port 443 - HTTPS

Scan completed.
Results saved to scan_results_scanme.nmap.org.txt
```

---

## 🧪 Example Use Cases

* Network security testing
* Learning port and protocol behavior
* Ethical hacking practice
* Cybersecurity labs
* Reconnaissance simulation

---

## ⚙️ Project Structure

```txt
python-port-scanner/
│── port_scanner.py
│── README.md
│── requirements.txt
│── examples/
```

---

## 🔐 Ethical Notice

This tool is intended for:

* Educational purposes
* Authorized penetration testing
* Cybersecurity research

Unauthorized scanning of systems you do not own is illegal.

---

## 📈 Future Improvements

* Banner grabbing (service version detection)
* JSON/CSV output support
* Async scanning (faster than threading)
* GUI dashboard
* Stealth scan modes
* Exportable reports

---

## 👨‍💻 Author

Cybersecurity student building real-world security tools with Python and AI.

Documenting my journey into ethical hacking, automation, and system security.
