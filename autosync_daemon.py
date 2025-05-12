import os
import time
import shutil
from datetime import datetime

QUEUE_DIR = "autosync_queue"
SYNC_LOG = "autosync_log.csv"

def is_online():
    response = os.system("ping -c 1 github.com > /dev/null 2>&1")
    return response == 0

def queue_file(file_path):
    if not os.path.exists(QUEUE_DIR):
        os.makedirs(QUEUE_DIR)
    filename = os.path.basename(file_path)
    dest = os.path.join(QUEUE_DIR, filename)
    shutil.copy(file_path, dest)
    log_sync_event(filename, "queued")

def sync_queued_files():
    if not os.path.exists(QUEUE_DIR):
        return
    for file in os.listdir(QUEUE_DIR):
        full_path = os.path.join(QUEUE_DIR, file)
        # Placeholder for actual sync logic
        print(f"[SYNC] Uploading {file} to GitHub...")
        log_sync_event(file, "synced")
        os.remove(full_path)

def log_sync_event(file, status):
    with open(SYNC_LOG, "a") as f:
        timestamp = datetime.utcnow().isoformat()
        f.write(f"{timestamp},{file},{status}\n")

def autosync_loop():
    print("=== Autosync Daemon Running ===")
    try:
        while True:
            if is_online():
                sync_queued_files()
            else:
                print("[OFFLINE] Queuing files or waiting for signal...")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[STOP] Autosync Daemon stopped.")

if __name__ == "__main__":
    autosync_loop()
