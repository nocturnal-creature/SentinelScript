# SentinelScript 🛡️

A real-time File Integrity Monitoring (FIM) system built in Python to detect unauthorized file modifications, deletions, and creations.

## 🔍 Why This Project?

File Integrity Monitoring is used in SOC environments to detect:
- Malware tampering
- Insider threats
- Unauthorized system changes
- Ransomware encryption activity

## ⚙️ Features

- SHA-256 hashing
- Baseline generation
- Real-time file monitoring using Watchdog
- Detects file creation, deletion, modification
- Event logging
- Modular architecture

## 🛠 Tech Stack

- Python
- Watchdog
- JSON
- SHA-256

## 🚀 How to Run

1. Install dependencies  
   pip install -r requirements.txt

2. Generate baseline  
   python main.py

3. Start monitoring  
   python main.py
