# ckm_loader.py

import json
import os

def load_ckm_data(file_path):
    """
    Load CKM data from a JSON file and return as a Python dict.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CKM data file not found: {file_path}")

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

def preview_ckm_sample(ckm_data, limit=3):
    """
    Preview first few CKM entries.
    """
    for i, entry in enumerate(ckm_data[:limit]):
        print(f"[{i}] {entry}")
