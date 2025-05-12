import time
from datetime import datetime

TICK_LOG = "clu_tick_log.csv"
TICK_INTERVAL_SECONDS = 0.00628  # 1 CLU tick duration
TICK_START_TIME = time.time()

def get_current_tick():
    now = time.time()
    elapsed = now - TICK_START_TIME
    return int(elapsed / TICK_INTERVAL_SECONDS)

def log_tick():
    tick = get_current_tick()
    timestamp = datetime.utcnow().isoformat()
    with open(TICK_LOG, "a") as f:
        f.write(f"{timestamp},{tick}\n")
    print(f"[TICK] {timestamp} | Tick: {tick}")

def tick_loop():
    print("=== CLU Tick Clock Started ===")
    try:
        while True:
            log_tick()
            time.sleep(TICK_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n[STOPPED] CLU Tick Clock halted.")

if __name__ == "__main__":
    tick_loop()
