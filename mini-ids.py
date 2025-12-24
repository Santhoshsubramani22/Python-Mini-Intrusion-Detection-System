from datetime import datetime
import os
import re

# ===============================
# CONFIGURATION
# ===============================
LOG_FILES = [
    "/var/log/auth.log",      # Debian / Ubuntu
    "/var/log/secure"         # RHEL / CentOS
]

FAILED_LIMIT = 5
OUTPUT_FILE = "ids_alerts.txt"

# ===============================
# Read Log File Safely
# ===============================
def read_log_file(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", errors="ignore") as file:
            return file.readlines()
    except Exception:
        return []

# ===============================
# Detect Failed Login Attempts
# ===============================
def detect_failed_logins(lines):
    failed = {}
    alerts = []

    for line in lines:
        if "Failed password" in line:
            match = re.search(r"from ([\d\.]+)", line)
            if match:
                ip = match.group(1)
                failed[ip] = failed.get(ip, 0) + 1

    for ip, count in failed.items():
        if count >= FAILED_LIMIT:
            alerts.append(
                f"Multiple failed login attempts detected from IP {ip} ({count} times)"
            )

    return alerts

# ===============================
# Detect Root Login Attempts
# ===============================
def detect_root_login(lines):
    alerts = []
    for line in lines:
        if "session opened for user root" in line.lower():
            alerts.append("Root login session detected")
    return alerts

# ===============================
# Run IDS Analysis
# ===============================
def run_ids():
    all_lines = []

    for log in LOG_FILES:
        all_lines.extend(read_log_file(log))

    with open(OUTPUT_FILE, "a") as file:
        header = (
            "\n" + "=" * 60 + "\n"
            "MINI INTRUSION DETECTION SYSTEM (LOG-BASED)\n"
            f"Analysis Time: {datetime.now()}\n"
            + "=" * 60 + "\n"
        )

        print(header)
        file.write(header)

        alerts = []
        alerts.extend(detect_failed_logins(all_lines))
        alerts.extend(detect_root_login(all_lines))

        if not alerts:
            line = "No suspicious activity detected\n"
            print(line.strip())
            file.write(line)
        else:
            for alert in alerts:
                line = f"[ALERT] {alert}\n"
                print(line.strip())
                file.write(line)

        footer = (
            "=" * 60 + "\n"
            f"Total Alerts: {len(alerts)}\n"
        )

        print(footer)
        file.write(footer)

# ===============================
# Entry Point
# ===============================
if __name__ == "__main__":
    run_ids()
