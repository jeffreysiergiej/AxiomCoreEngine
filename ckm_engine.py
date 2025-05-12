"""
CKM Engine Module – AxiomCoreEngine
Simulates Collapse Knot Manifold field behavior.
"""

import csv
import json
from datetime import datetime

LOG_FILE = "ckm_log.json"

def load_ckm_data(filepath="CKM_Registry.csv"):
    data = []
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        print(f"[CKM] Loaded {len(data)} knots from {filepath}")
    except Exception as e:
        print(f"[CKM] Error loading file: {e}")
    return data

def evaluate_knot_stability(knot):
    try:
        frequency = float(knot.get("frequency", 0))
        amplitude = float(knot.get("amplitude", 0))
        stability = round(frequency * amplitude, 3)
        result = {
            "knot_id": knot.get("id", "unknown"),
            "frequency": frequency,
            "amplitude": amplitude,
            "stability": stability,
            "timestamp": datetime.utcnow().isoformat()
        }
        return result
    except Exception as e:
        return {"error": str(e)}

def log_ckm_result(result):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(result) + "\n")
    except Exception as e:
        print(f"[CKM] Logging error: {e}")

def run_ckm_sim():
    knots = load_ckm_data()
    for knot in knots:
        result = evaluate_knot_stability(knot)
        print(f"[CKM] Knot {result['knot_id']} stability: {result.get('stability', '?')}")
        log_ckm_result(result)

# Direct test
if __name__ == "__main__":
    run_ckm_sim()
