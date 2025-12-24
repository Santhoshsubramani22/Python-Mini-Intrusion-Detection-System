
# 🛡️ Python Mini Intrusion Detection System (Mini IDS)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![Security](https://img.shields.io/badge/Security-Intrusion%20Detection-green)
![License](https://img.shields.io/badge/License-Educational-orange)

---

## 📘 Project Overview

The **Python Mini Intrusion Detection System (Mini IDS)** is a **log-based, read-only IDS** designed to monitor **local Linux authentication logs** for suspicious activity.

It simulates how real-world IDS tools work by detecting:
- Multiple failed login attempts (possible brute-force attacks)
- Root login sessions

This project is built strictly for **educational, ethical, and lab-based learning**, making it ideal for cybersecurity students and portfolio projects.

---

## ⚠️ Legal & Ethical Disclaimer

> This tool must only be used on systems you own.

- Reads system logs only (no modification)
- No configuration changes are made
- No exploitation techniques are used
- Unauthorized use on other systems is illegal and unethical

The author is not responsible for misuse.

---

## ✨ Key Features

- 🚨 Detects multiple failed login attempts
- 🔐 Detects root login sessions
- 📝 Appends alerts to a persistent report file
- 📂 Uses local authentication logs only:
  - `/var/log/auth.log`
  - `/var/log/secure`
- 🧩 Lightweight and dependency-free
- 🛡️ Safe for labs and learning environments

---

## 🛠️ System Requirements

- **Operating System:** Linux
- **Python Version:** 3.8 or higher
- **Dependencies:** None (Python standard library only)

Verify Python installation:
```bash
python3 --version
````

---

## 📂 Project Structure

```
mini_ids/
├── mini_ids.py        # Main IDS script
├── ids_alerts.txt     # Alert report file
└── README.md          # Documentation
```

---

## ▶️ Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/mini-ids.git
cd mini-ids
```

### 2️⃣ Run the IDS

```bash
python3 mini_ids.py
```

### 3️⃣ View Alerts

```text
ids_alerts.txt
```

---

## 📄 Example Output

```
============================================================
MINI INTRUSION DETECTION SYSTEM (LOG-BASED)
Analysis Time: 2025-12-22 19:00:12
============================================================
[ALERT] Multiple failed login attempts detected from IP 192.168.1.50 (7 times)
[ALERT] Root login session detected
============================================================
Total Alerts: 2
```

### Alert Explanation

* **Multiple failed login attempts** → Possible brute-force activity
* **Root login detected** → Root account access occurred
* **Total Alerts** → Number of suspicious events found in this run

---

## 🔍 How It Works

1. Reads local authentication logs
2. Searches for suspicious patterns:

   * Failed password attempts
   * Root login sessions
3. Generates alerts for detected events
4. Appends results to a report file for historical analysis

---

## 🔐 Safety & Legality Summary

| Feature                    | Status |
| -------------------------- | ------ |
| Read-only log access       | ✅      |
| No system modification     | ✅      |
| No network activity        | ✅      |
| Local system only          | ✅      |
| Safe for students and labs | ✅      |

---

## 🚀 Learning Outcomes

* Intrusion detection fundamentals
* Linux authentication log analysis
* Pattern recognition in Python
* Ethical security monitoring practices
* Logging and alert reporting techniques

---

## 🔜 Future Enhancements

* Severity levels (LOW / MEDIUM / HIGH)
* Time-based correlation analysis
* Email alerts (lab environments)
* Integration with SIEM-style log analyzers
* Dashboard or visualization support

---

## 📜 License

This project is released **for educational purposes only**.
Use responsibly on systems you own. Unauthorized use is prohibited.

---

- 📁 Align all projects into **one master cybersecurity repo**
- 📄 Make this **resume-ready**
- 📊 Add screenshots & diagrams
- 🔐 Turn it into a **full IDS mini-suite**
```
