import os
import json
from .hashing import calculate_hash

def generate_baseline(directory, baseline_file):
    baseline = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            baseline[path] = calculate_hash(path)

    with open(baseline_file, "w") as f:
        json.dump(baseline, f, indent=4)

    print("Baseline generated successfully.")

def load_baseline(baseline_file):
    try:
        with open(baseline_file, "r") as f:
            return json.load(f)
    except:
        return {}
