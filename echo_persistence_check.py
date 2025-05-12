import json
from datetime import datetime

def load_echo_data(path="Echo_Shell_Symmetry_Log.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("[ERROR] Echo log not found.")
        return []

def analyze_echo_lifespan(echo_data):
    results = []
    for entry in echo_data:
        try:
            anchor_id = entry["anchor_id"]
            timestamps = entry["echo_timestamps"]  # Expecting a list
            if len(timestamps) >= 2:
                t_start = timestamps[0]
                t_end = timestamps[-1]
                lifespan = t_end - t_start
                results.append({
                    "anchor_id": anchor_id,
                    "lifespan": lifespan,
                    "timestamp": datetime.utcnow().isoformat()
                })
        except KeyError:
            continue
    return results

def save_lifespan_results(results, output_path="echo_lifespan_log.csv"):
    with open(output_path, "a") as f:
        for r in results:
            f.write(f"{r['timestamp']},{r['anchor_id']},{r['lifespan']}\n")

if __name__ == "__main__":
    echo_data = load_echo_data()
    if echo_data:
        lifespan_results = analyze_echo_lifespan(echo_data)
        save_lifespan_results(lifespan_results)
        print(f"[INFO] Logged {len(lifespan_results)} echo lifespan entries.")
    else:
        print("[INFO] No echo data to process.")
        2025-05-12T17:13:02Z,M_104,18.24
