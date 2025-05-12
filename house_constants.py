# house_constants.py
# Derived from: Siergiej, Jeffrey (2025). 8.A+M[S] House System
# DOI: https://doi.org/10.6084/m9.figshare.28690268.v2

HOUSE_LEVELS = [
    "House 0 – Core Planck Node",
    "House 1 – Sub-Fractal Atoms",
    "House 2 – Prime Quantum Scaffold",
    "House 3 – Emergent Standard Model",
    "House 4 – Molecular Harmonic",
    "House 5 – Biological Lattice",
    "House 6 – Neurological Field",
    "House 7 – Organismal Shell",
    "House 8 – Planetary Entanglement",
    "House 9 – Stellar Lattice Mesh",
    "House 10 – Galactic Harmonic Chain",
    "House 11 – Universal Echo Layer"
]

EMERGENT_PARTICLES = [
    "Photon",
    "Electron",
    "Muon",
    "Tau",
    "Up Quark",
    "Down Quark",
    "Strange Quark",
    "Charm Quark",
    "Top Quark",
    "Bottom Quark",
    "Gluon",
    "Z Boson",
    "W Boson",
    "Higgs Boson",
    "Graviton (hypothetical)"
]

HOUSE_ENERGY_SCALE = {
    "House 0": "1.22e+19 GeV (Planck scale)",
    "House 1": "1.0e+16 GeV",
    "House 2": "1.0e+13 GeV",
    "House 3": "91–125 GeV (Z/Higgs boson range)",
    "House 4": "1–10 eV (molecular vibration)",
    "House 5": "10^(-2) to 10^2 eV (bioelectric)",
    "House 6": "~10^(-3) eV (neurological field)",
    "House 7": "~10^(-4) eV (organismal scale)",
    "House 8": "~10^(-9) eV (geomagnetic lattice)",
    "House 9": "~10^(-14) eV (stellar interference)",
    "House 10": "~10^(-18) eV (galactic coupling)",
    "House 11": "~10^(-21) eV (universal background)"
}

def print_house_constants():
    print("=== A+M[S] House System Constants ===")
    for i, house in enumerate(HOUSE_LEVELS):
        tag = f"House {i}"
        print(f"{house}\n  Energy Scale: {HOUSE_ENERGY_SCALE.get(tag, 'N/A')}\n")

if __name__ == "__main__":
    print_house_constants()
