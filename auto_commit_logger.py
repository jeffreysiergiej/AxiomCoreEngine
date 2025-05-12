# File: auto_commit_logger.py
import os
import subprocess
from datetime import datetime

def auto_commit(repo_path="."):
    os.chdir(repo_path)
    subprocess.run(["git", "add", "system_health_log.txt"])
    commit_msg = f"Auto-log system health at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    auto_commit()
