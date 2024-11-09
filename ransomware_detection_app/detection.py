import os
import time


def monitor_directory(path):
    before = set(os.listdir(path))
    while True:
        time.sleep(10)  # Check every 10 seconds
        after = set(os.listdir(path))
        added = after - before
        if added:
            return f"New files added: {added}"
        before = after
