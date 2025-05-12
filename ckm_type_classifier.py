import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from datetime import datetime

INPUT_FILE = "CKM_Knot_Topology_Comparison.csv"
OUTPUT_FILE = "ckm_knot_classification_log.csv"

def load_knot_data(path=INPUT_FILE):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load knot data: {e}")
        return pd.DataFrame()

def classify_knot_types(df):
    features = df[['dimensionality', 'symmetry_score', 'braid_count']]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(scaled)
    df['classification'] = labels

    label_map = {
        0: "Torus",
        1: "Trefoil",
        2: "Unknown"
    }

    df['knot_type'] = df['classification'].map(label_map)
    return df[['knot_id', 'knot_type']]

def save_results(df, path=OUTPUT_FILE):
    with open(path, "a") as f:
        for _, row in df.iterrows():
            f.write(f"{datetime.utcnow().isoformat()},{row['knot_id']},{row['knot_type']}\n")

def main():
    data = load_knot_data()
    if not data.empty:
        result = classify_knot_types(data)
        save_results(result)
        print(f"[INFO] Classified {len(result)} knots.")
    else:
        print("[INFO] No data to classify.")

if __name__ == "__main__":
    main()
