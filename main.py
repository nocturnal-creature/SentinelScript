import json
from sentinel.baseline import generate_baseline
from sentinel.monitor import start_monitoring

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()

    directory = config["monitor_directory"]
    baseline_file = config["baseline_file"]
    log_file = config["log_file"]

    print("1. Generate Baseline")
    print("2. Start Monitoring")
    choice = input("Choose option: ")

    if choice == "1":
        generate_baseline(directory, baseline_file)
    elif choice == "2":
        start_monitoring(directory, baseline_file, log_file)
