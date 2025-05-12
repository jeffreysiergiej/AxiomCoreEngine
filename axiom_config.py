# axiom_config.py
# Core runtime config and control flags for AxiomCoreEngine

import os
from datetime import datetime

# Project reference
PROJECT_NAME = "AxiomCoreEngine"
AUTHOR = "Jeffrey Siergiej"
VERSION = "v1.0.0"
HOUSE_SYSTEM_DOI = "https://doi.org/10.6084/m9.figshare.28690268.v2"

# File paths
ENTROPY_LOG = "entropy_monitor.log"
TICK_LOG = "clu_tick_log.csv"
SPAWN_LOG = "genesis_spawn_log.csv"
MACRO_LOG = "voice_macro_log.csv"
SYNC_LOG = "autosync_log.csv"
HOUSE_SYSTEM_FILE = "house_scaling_system.py"

# AI Activation Flags
AI_ENABLED = {
    "genesis": True,
    "entropy_monitor": True,
    "ckm_classifier": True,
    "voice_macros": True,
    "autosync_daemon": True,
    "tick_clock": True
}

# System Toggles
USE_CLOUD_SYNC = True
ALLOW_OFFLINE_MODE = True
DEBUG_MODE = True
LOG_INTERVAL_SECONDS = 60

# Timestamped startup ID
SESSION_ID = f"{PROJECT_NAME}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"

def print_config():
    print("=== AxiomCoreEngine Config ===")
    print(f"Project: {PROJECT_NAME} | Author: {AUTHOR} | Session: {SESSION_ID}")
    print(f"Version: {VERSION} | DOI: {HOUSE_SYSTEM_DOI}")
    print("Active Modules:")
    for agent, state in AI_ENABLED.items():
        status = "ON" if state else "OFF"
        print(f" - {agent.upper():<20} : {status}")

if __name__ == "__main__":
    print_config()
