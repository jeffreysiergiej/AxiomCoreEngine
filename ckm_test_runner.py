import json
from ckm_engine import analyze_ckm_event

def load_ckm_data(filepath='data/sample_ckm.json'):
    with open(filepath, 'r') as f:
        return json.load(f)

def run_ckm_test():
    data = load_ckm_data()
    for event in data:
        result = analyze_ckm_event(
            position=event["position"],
            energy=event["energy"],
            phase=event["phase"]
        )
        print(f"{event['id']} => {result}")

if __name__ == "__main__":
    run_ckm_test()
