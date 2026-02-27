import time
import csv
from colorama import Fore, Style, init

init(autoreset=True)

def log_event(message, log_file, severity="INFO"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Console colors
    if severity == "CRITICAL":
        print(Fore.RED + f"[{severity}] {message}")
    elif severity == "WARNING":
        print(Fore.YELLOW + f"[{severity}] {message}")
    else:
        print(Fore.GREEN + f"[{severity}] {message}")

    # Log to text file
    with open(log_file, "a") as f:
        f.write(f"{timestamp},{severity},{message}\n")

    # Log to CSV (SIEM style)
    with open("security_logs.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, severity, message])
