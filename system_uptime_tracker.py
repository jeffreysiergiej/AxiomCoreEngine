import time
import os

UPTIME_PATH = "system_uptime_tracker.txt"

def initialize_uptime():
    if not os.path.exists(UPTIME_PATH):
        with open(UPTIME_PATH, "w") as f:
            f.write(str(time.time()))
        print("[INIT] Uptime initialized.")

def get_uptime_seconds():
    try:
        with open(UPTIME_PATH, "r") as f:
            start_time = float(f.read().strip())
        return time.time() - start_time
    except Exception as e:
        print(f"[ERROR] Failed to read uptime: {e}")
        return 0

if __name__ == "__main__":
    initialize_uptime()
    uptime = get_uptime_seconds()
    print(f"[INFO] Current system uptime: {uptime:.2f} seconds")
