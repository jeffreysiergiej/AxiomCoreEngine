import time
import psutil
import platform
import json
import socket

def gather_health_metrics():
    return {
        "timestamp": int(time.time()),
        "hostname": socket.gethostname(),
        "platform": f"{platform.system()} {platform.release()}",
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "net_io_sent_MB": round(psutil.net_io_counters().bytes_sent / 1_000_000, 2),
        "net_io_recv_MB": round(psutil.net_io_counters().bytes_recv / 1_000_000, 2),
        "uptime_seconds": int(time.time() - psutil.boot_time())
    }

def log_system_health(output_path=None, as_json=True):
    metrics = gather_health_metrics()
    if as_json:
        output = json.dumps(metrics, indent=4)
    else:
        output = "\n".join([f"{k}: {v}" for k, v in metrics.items()])
    
    print("=== SYSTEM HEALTH REPORT ===")
    print(output)

    if output_path:
        with open(output_path, 'a') as f:
            f.write(output + "\n")

# Optional interval-based daemon for background logging
def run_health_daemon(interval=300):
    while True:
        log_system_health(output_path="system_health.log", as_json=True)
        time.sleep(interval)
import psutil
import datetime

def log_system_health():
    stats = {
        "timestamp": datetime.datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent
    }
    print("System Health:", stats)
    return stats
