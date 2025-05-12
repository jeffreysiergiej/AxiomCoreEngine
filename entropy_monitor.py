import random
import time
from datetime import datetime

LOG_PATH = "entropy_monitor.log"

def generate_entropy_signal():
    # Simulate an entropy level from 0.0 to 1.0
    return round(random.uniform(0.0, 1.0), 4)

def log_entropy_signal(path=LOG_PATH):
    entropy = generate_entropy_signal()
    timestamp = datetime.utcnow().isoformat()
    with open(path, "a") as f:
        f.write(f"{timestamp}, {entropy}\n")
    print(f"[LOGGED] {timestamp} | entropy={entropy}")

if __name__ == "__main__":
    print("=== Entropy Monitor Running ===")
    try:
        while True:
            log_entropy_signal()
            time.sleep(30)  # Log every 30 seconds
    except KeyboardInterrupt:
        print("\n[INFO] Entropy monitor stopped.")
