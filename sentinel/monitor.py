from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .hashing import calculate_hash
from .baseline import load_baseline
from .logger import log_event
import time

class SentinelHandler(FileSystemEventHandler):
    def __init__(self, baseline_file, log_file):
        self.baseline_file = baseline_file
        self.log_file = log_file

    def on_modified(self, event):
        if not event.is_directory:
            self.check_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            log_event(f"New file created: {event.src_path}", self.log_file, "WARNING")
    def on_deleted(self, event):
        if not event.is_directory:
            log_event(f"File deleted: {event.src_path}", self.log_file, "CRITICAL")

    def check_file(self, filepath):
        baseline = load_baseline(self.baseline_file)
        current_hash = calculate_hash(filepath)

        if filepath in baseline:
            if baseline[filepath] != current_hash:
                log_event(f"File modified: {filepath}", self.log_file, "CRITICAL")
        else:
            log_event(f"Unknown file detected: {filepath}", self.log_file, "WARNING")

def start_monitoring(directory, baseline_file, log_file):
    event_handler = SentinelHandler(baseline_file, log_file)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    print("Monitoring started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


