import time

def log_event(message, log_file):
    with open(log_file, "a") as f:
        f.write(f"{time.ctime()} - {message}\n")
    print(message)
